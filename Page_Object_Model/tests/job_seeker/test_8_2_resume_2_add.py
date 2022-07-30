import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_add_page import ResumeAddPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.data_for_testing import TestData


@pytest.mark.job_seeker
class TestResume2Add:
    @pytest.mark.s_r_c
    def test_adding_resume_2(self, browser, language):  # добавление второго резюме
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(language, 2)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

        my_resume_page = MyResumePage(browser, browser.current_url)
        my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

        add_resume_page = ResumeAddPage(browser, browser.current_url)
        add_resume_page.filling_in_required_fields(TestData.job_title_resume_2)  # заполнение обязательных полей
        browser.execute_script("window.scrollBy(0, -4000);")
        add_resume_page.filling_in_optional_fields()  # заполнение не обязательных полей
        add_resume_page.percentage_check_of_resume_completion()  # проверка заполнения резюме в процентах
        add_resume_page.checking_status_level_filling_resume(language)  # проверка статуса уровня заполнения резюме
        add_resume_page.submitting_resume_for_publication()  # отправка резюме на публикацию

        my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
        my_resume_page.confirmation_of_opening_of_page_my_resumes(language)  # подтверждение открытия страницы 'Мои резюме'
        my_resume_page.checking_message_confirming_of_creation_of_resume(language)  # проверка сообщения о создании нового резюме
        my_resume_page.checking_number_of_resumes_to_create(2)  # проверка уменьшения количества резюме для создания

        admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу всех резюме

        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_2)  # поиск резюме по названию должности
        singleton = Singleton()
        singleton.id_resume.append(admin_resumes_page.getting_resume_id())  # получение id резюме
        admin_resumes_page.checking_that_resume_status_is_on_moderated()  # проверка что статус резюме 'На модерацию'

        url_resume_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{singleton.id_resume[1]}"
        resume_page = ResumePage(browser, url_resume_page)
        resume_page.open()
        resume_page.checking_opening_of_page_of_an_unpublished_resume(language)  # проверка открытия страницы не опубликованного резюме

        admin_page.open()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу всех резюме

        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_2)  # поиск резюме по названию должности
        admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме

        admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
        admin_resume_edit_page.change_resume_status_to_published()  # изменение статуса резюме на 'Опубликовано'

        admin_resumes_page.waiting_to_save_status_and_open_resume_page()  # ожидание сохранения статуса и открытия страницы всех рузюме

        url_resume_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{singleton.id_resume[1]}"
        resume_page = ResumePage(browser, url_resume_page)
        resume_page.open()
        resume_page.checking_opening_of_page_of_published_resume(TestData.job_title_resume_2)  # проверка открытия страницы опубликованного резюме
