import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_add_page import ResumeAddPage
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.data_for_testing import TestData


@pytest.mark.job_seeker
class TestAddingResumeToDraft:
    @pytest.mark.s_r_c
    def test_checking_adding_resume_to_draft(self, browser, language):  # проверка добавления резюме в черновик
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.new_user_authorization(language, 2)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

        my_resume_page = MyResumePage(browser, browser.current_url)
        my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

        add_resume_page = ResumeAddPage(browser, browser.current_url)
        add_resume_page.adding_resume_to_draft()  # добавление резюме в черновик
        add_resume_page.checking_field_job_title_validation_message_about_need_to_fill_out(language)  # проверка сообщения валидации поля "Название должности" о необходимости его заполнения
        add_resume_page.filling_in_field_job_title_for_draft()  # заполнение поля "Название должности" для черновика
        add_resume_page.adding_resume_to_draft()  # добавление резюме в черновик

        my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
        my_resume_page.confirmation_of_opening_of_page_my_resumes(language)  # подтверждение открытия страницы 'Мои резюме'
        my_resume_page.checking_message_about_adding_resume_to_draft(language)  # проверка сообщения о добавлении резюме в черновик
        my_resume_page.checking_number_of_resumes_to_create(4)  # проверка уменьшения количества резюме для создания

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу резюме

        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_for_draft)  # поиск резюме по названию должности
        singleton = Singleton()
        singleton.id_resume.append(admin_resumes_page.getting_resume_id())  # получение id резюме
        admin_resumes_page.checking_that_resume_status_is_draft()  # проверка что статус резюме 'Черновик'

        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/my"
        my_resume_page = MyResumePage(browser, url_page)
        my_resume_page.open()
        my_resume_page.opening_resume_menu()  # открытие меню резюме
        my_resume_page.deletion_resume_draft(3)  # удаление черновика резюме
        my_resume_page.checking_message_after_deleting_resume(language)  # проверка сообщения после удаления резюме
        my_resume_page.checking_number_of_resumes_to_create(3)  # проверка количества резюме для создания

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/resume')
        admin_page.open()
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_for_draft)  # поиск резюме по названию должности
        admin_resumes_page.checking_that_resume_status_is_deleted()  # проверка что статус резюме 'Удалено'
