import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.company_registration_page import CompanyRegistrationPage
from Page_Object_Model.pages.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage
import time



@pytest.mark.s_r_c
def test_company_registration_with_filling_in_all_fields(browser, language):  # регистрация работодателя с заполнением всех полей
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open(False)
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.go_to_company_registration_page()  # нажатие на кнопку для перехода на страницу регистрации работодателя

    company_registration_page = CompanyRegistrationPage(browser, browser.current_url)
    company_registration_page.filling_in_required_fields()  # заполнение обязательных полей
    company_registration_page.filling_in_optional_fields()  # заполнение не обязательных полей
    company_registration_page.browser.execute_script("window.scrollBy(0, 1300);")
    company_registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.checking_message_for_sending_registration_form()  # проверка сообщения о подтверждении отправки формы регистрации


def test_checking_creation_of_user_in_admin_panel(browser, language):  # проверка создания пользователя в админке
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.checking_that_newly_created_user_has_status_Disabled()  # проверка что новосозданный пользователь имеет статус "Отключено"

def test_changing_user_role_from_User_to_SuperAdmin(browser, language):  # изменение роли пользователя с "User" на "SuperAdmin"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.changing_role_from_User_to_SuperAdmin()  # изменение роли с "User" на "SuperAdmin"
    admin_page.saving_user_card()  # сохранение карточки пользователя


def test_authorization_of_user_in_Disabled_status(browser, language):  # авторизация пользователя в статусе "Отключен"
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
    page.info_text_for_authorization_in_user_status_Disabled()  # инфо текст при авторизации в статусе пользователя "Отключен"

@pytest.mark.s_r_c
def test_email_verification_after_company_registration(browser, language):  # верификация почты после регистрации работодателя
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email

    if language == "/ua":
        email_page.confirmation_of_company_registration_in_letter_ua()  # переход по ссылке для подтверждения регистрации работодателя в письме
    else:
        email_page.confirmation_of_company_registration_in_letter_ru()  # переход по ссылке для подтверждения регистрации работодателя в письме

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.checking_employer_email_confirmation_message_after_registration()  # проверка сообщения о подтверждении электронной почты работодателя после регистрации


def test_authorization_of_user_in_On_moderation_status(browser, language):  # авторизация пользователя в статусе "На модерации"
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
    page.info_text_for_authorization_in_user_status_On_moderation()  # инфо текст при авторизации в статусе пользователя "На модерации"

@pytest.mark.s_r_c
def test_change_of_employer_status_from_On_moderation_to_Aktivet_ua(browser, language):  # изменение статуса работодателя с "На модерации" на "Активен" ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.change_of_user_status_from_On_moderation_to_Active()  # изменение статуса пользователя с "На модерации" на "Активен"
    admin_page.check_that_user_has_status_Active()  # проверка что пользователь имеет статус "Активен"


# def test_authorization_of_user_in_Active_status(browser, language):  # авторизация пользователя в статусе "Активен"
#     url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
#     page = OllPage(browser, url_Page)
#     # browser.maximize_window()
#     page.open()
#     page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
#     page.user_authorization()  # авторизация пользователя
#     page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя


def test_checking_letter_after_first_moderation_ru(browser, language):  # проверка письма после первой модерации компании ru
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email

    if language == "/ua":
        email_page.letter_after_first_moderation_of_company_ua()  # письмо после первой модерации компании ua
    else:
        email_page.letter_after_first_moderation_of_company_ru()  # письмо после первой модерации компании ru
