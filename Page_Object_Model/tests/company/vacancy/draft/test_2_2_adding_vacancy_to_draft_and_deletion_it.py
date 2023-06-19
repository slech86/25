import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_add_page import VacancyAddPage
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.tests import _resources_tests
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables

# pytest --reruns 1 --html=./reports/report.html tests/company/vacancy/draft/test_2_2_adding_vacancy_to_draft_and_deletion_it.py

user = 'employer'
id_vacancies = [1979, 3037, 3519]


class TestAddingVacancyToDraft:
    def test_precondition(self, browser):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
        admin_sql_page.open()
        admin_sql_page.sql_deleting_all_user_vacancies_except_these(users_variables[user]["id"], id_vacancies)  # удаление всех вакансий пользователя кроме указанных

    def test_checking_adding_vacancy_to_draft(self, browser, language):  # проверка добавления вакансии в черновик
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

        my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
        my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

        add_vacancy_page = VacancyAddPage(browser, browser.current_url)
        add_vacancy_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
        page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
        add_vacancy_page.filling_in_field_job_title_for_draft()  # заполнение поля "Название должности" для черновика
        add_vacancy_page.adding_vacancy_to_draft()  # добавление вакансии в черновик

        my_vacancies_page.waiting_for_my_vacancies_page_to_open(language)  # ожидание открытия страницы 'Мои вакансии'
        my_vacancies_page.confirmation_of_opening_of_page_my_vacancies(language)  # подтверждение открытия страницы 'Мои вакансии'
        my_vacancies_page.checking_message_about_adding_vacancy_to_draft(language)  # проверка сообщения о добавлении вакансии в черновик

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_vacancies_page()  # переход на страницу вакансий
        admin_page.vacancy_search_by_job_title(TestData.job_title_vacancy_for_draft)  # поиск вакансии по названию должности

        id_vacancies = admin_page.getting_vacancy_id()  # получение id вакансии
        admin_page.checking_that_vacancy_status_is_draft()  # проверка что статус вакансии 'Черновик'

        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/vacancy/my"
        my_vacancies_page = MyVacanciesPage(browser, url_page)
        my_vacancies_page.open()
        my_vacancies_page.opening_vacancy_menu(id_vacancies)  # открытие меню вакансии
        my_vacancies_page.deletion_vacancy_draft(id_vacancies)  # удаление черновика вакансии
        my_vacancies_page.checking_message_after_deleting_vacancy(language)  # проверка сообщения после удаления вакансии

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/vacancies')
        admin_page.open()
        admin_page.vacancy_search_by_job_title(TestData.job_title_vacancy_for_draft)  # поиск вакансии по названию должности
        admin_page.checking_that_vacancy_status_is_deleted()  # проверка что статус вакансии 'Удалено'
