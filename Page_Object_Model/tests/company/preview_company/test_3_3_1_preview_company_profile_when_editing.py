import pytest
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_edit_page import CompanyEditPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.company_preview_page import CompanyPreviewPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.tests import _resources_tests

# pytest --reruns 1 --html=./reports/report.html -s tests/company/preview_company/test_3_3_1_preview_company_profile_when_editing.py

user = 'employer'


def test_precondition(browser, language):
    _resources_tests.admin_authorization(browser)  # авторизация в админку
    _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[user]["id"])  # изменение языка уведомлений на email


def test_preview_company_profile_when_editing(browser, language):  # предпросмотр профиля компании при редактировании
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

    company_edit_page = CompanyEditPage(browser, browser.current_url)
    company_edit_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    company_edit_page.go_to_preview_page()  # переход на страницу предпросмотра

    company_preview_page = CompanyPreviewPage(browser, browser.current_url)
    company_preview_page.checking_for_preview_page_to_open(users_variables[user]['company_name'])  # проверка открытия страницы предпросмотра

