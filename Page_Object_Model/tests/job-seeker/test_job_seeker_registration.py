import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.job_seeker_registration_page import JobSeekerRegistrationPage
from Page_Object_Model.pages.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage
import time


@pytest.mark.parametrize('language', ["", "/ua"])
def test_job_seeker_registration_with_filling_in_all_fields(browser, language):  # регистрация соискателя с заполнением всех полей
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.go_to_job_seeker_registration_page()  # нажатие на кнопку для перехода на страницу регистрации соискателя

    job_seeker_registration_page = JobSeekerRegistrationPage(browser, browser.current_url)
    job_seeker_registration_page.filling_in_all_fields()  # заполнение всех полей
    job_seeker_registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.confirmation_message_for_sending_registration_form()  # проверка сообщения о подтверждении отправки формы регистрации

def test_checking_creation_of_user_in_admin_panel_ru(browser):  # проверка создания пользователя в админке ru
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
    admin_page.checking_that_newly_created_user_has_status_Disabled()  # проверка что новосозданный пользователь имеет статус "Отключено"
def test_checking_creation_of_user_in_admin_panel_ua(browser):  # проверка создания пользователя в админке ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    admin_page.checking_that_newly_created_user_has_status_Disabled()  # проверка что новосозданный пользователь имеет статус "Отключено"

@pytest.mark.parametrize('language', ["", "/ua"])
def test_authorization_of_user_in_Disabled_status(browser, language):  # авторизация пользователя в статусе "Отключен"
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.authorization_after_registration()  # авторизация
    page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
    page.info_text_for_authorization_in_user_status_Disabled()  # инфо текст при авторизации в статусе пользователя "Отключен"

# def test_change_field_Login_and_Email_ru(browser):  # изменение поля "Login" и "Электронный адрес" ru
#     admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
#     admin_page.open()
#     admin_page.admin_authorization()
#     admin_page.go_to_users_page()  # переход на страницу пользователей
#     admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
#     admin_page.go_to_user_page()  # переход на страницу пользователя
#     admin_page.adding_unique_values_to_Login_and_Email_fields()  # внескние в поля "Login" и "Электронный адрес" уникальные значения
