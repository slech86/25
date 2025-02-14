import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_add_page import ResumeAddPage
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.tests import _resources_tests
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.data_for_testing import TestData

# pytest --reruns 1 --html=./reports/report.html -s tests/job_seeker/resume/draft/test_8_3_adding_resume_to_draft_and_deletion_it.py

user = 'job_seeker'
id_resume = [1267, 1268, 1269, 1358, 1561]


@pytest.mark.job_seeker
class TestAddingResumeToDraft:
    def test_precondition(self, browser):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
        admin_sql_page.open()
        admin_sql_page.sql_deleting_all_user_resume_except_these(users_variables[user]["id"], id_resume)  # удаление всех резюме пользователя кроме указанных

    def test_checking_adding_resume_to_draft(self, browser, language):  # проверка добавления резюме в черновик
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

        my_resume_page = MyResumePage(browser, browser.current_url)
        number_of_resumes_created = my_resume_page.obtaining_number_of_resumes_to_create()  # получение количества резюме для создания
        my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

        add_resume_page = ResumeAddPage(browser, browser.current_url)
        add_resume_page.hiding_opening_button_copy_to_other_languages()  # скрытие-открытие кнопки "Скопировать на другие языки"
        page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
        add_resume_page.filling_in_field_job_title_for_draft()  # заполнение поля "Название должности" для черновика
        add_resume_page.adding_resume_to_draft()  # добавление резюме в черновик

        my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
        my_resume_page.confirmation_of_opening_of_page_my_resumes(language)  # подтверждение открытия страницы 'Мои резюме'
        my_resume_page.checking_message_about_adding_resume_to_draft(language)  # проверка сообщения о добавлении резюме в черновик
        my_resume_page.checking_number_of_resumes_to_create(number_of_resumes_created + 1)  # проверка количества резюме для создания

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу резюме

        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_for_draft)  # поиск резюме по названию должности
        id_resume = admin_resumes_page.getting_resume_id()  # получение id резюме
        admin_resumes_page.checking_that_resume_status_is_draft()  # проверка что статус резюме 'Черновик'

        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/my"
        my_resume_page = MyResumePage(browser, url_page)
        my_resume_page.open()
        my_resume_page.opening_menu_of_first_resume_in_list()  # открытие меню резюме
        my_resume_page.deletion_resume_draft(id_resume)  # удаление черновика резюме
        my_resume_page.checking_message_after_deleting_resume(language)  # проверка сообщения после удаления резюме
        my_resume_page.checking_number_of_resumes_to_create(number_of_resumes_created)  # проверка количества резюме для создания

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/resume')
        admin_page.open()
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_for_draft)  # поиск резюме по названию должности
        admin_resumes_page.checking_that_resume_status_is_deleted()  # проверка что статус резюме 'Удалено'
