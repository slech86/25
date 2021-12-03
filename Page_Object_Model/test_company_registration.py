import pytest
from .pages.oll_page import OllPage
from .pages.registration_page import RegistrationPage
from .pages.main_page import MainPage
from .pages.email_page import EmailPage
from .data_for_testing import UrlStartPage, UrlPageAdmin
from .pages.admin_page import AdminPage
import time


@pytest.mark.parametrize('language', ["", "/ua"])
def test_employer_registration_with_filling_in_only_required_fields(browser, language):  # регистрация работодателя с заполнением только обязательных полей
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.go_to_registration_page()  # нажатие на кнопку для перехода на страницу регистрации работодателя

    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.filling_in_required_fields()  # заполнение обязательных полей
    registration_page.browser.execute_script("window.scrollBy(0, 1300);")
    registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.confirmation_message_for_sending_registration_form()  # проверка сообщения о подтверждении отправки формы регистрации работодателем


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


def test_email_verification_after_employer_registration_ru(browser):  # верификация почты после регистрации работодателя RU
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.confirmation_of_employer_registration_in_letter_ru()  # переход по ссылке для подтверждения регистрации работодателя в письме
    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.checking_employer_email_confirmation_message_after_registration()  # проверка сообщения о подтверждении электронной почты работодателя после регистрации
def test_email_verification_after_employer_registration_ua(browser):  # верификация почты после регистрации работодателя UA
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.confirmation_of_employer_registration_in_letter_ua()  # переход по ссылке для подтверждения регистрации работодателя в письме
    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.checking_employer_email_confirmation_message_after_registration()  # проверка сообщения о подтверждении электронной почты работодателя после регистрации


@pytest.mark.parametrize('language', ["", "/ua"])
def test_authorization_of_user_in_On_moderation_status(browser, language):  # авторизация пользователя в статусе "На модерации"
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.authorization_after_registration()  # авторизация
    page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
    page.info_text_for_authorization_in_user_status_On_moderation()  # инфо текст при авторизации в статусе пользователя "На модерации"


def test_change_of_employer_status_from_On_moderation_to_Aktivet_ua(browser):  # изменение статуса работодателя с "На модерации" на "Активет" ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    admin_page.change_of_user_status_from_On_moderation_to_Active()  # изменение статуса пользователя с "На модерации" на "Активет"
def test_change_of_employer_status_from_On_moderation_to_Aktivet_ru(browser):  # изменение статуса работодателя с "На модерации" на "Активет" ru
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
    admin_page.change_of_user_status_from_On_moderation_to_Active()  # изменение статуса пользователя с "На модерации" на "Активет"


@pytest.mark.parametrize('language', ["", "/ua"])
def test_authorization_of_user_in_Active_status(browser, language):  # авторизация пользователя в статусе "Активен"
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.authorization_after_registration()  # авторизация
    page.check_for_user_authorization()  # проверка на авторизацию пользователя


def test_checking_letter_after_first_moderation_ru(browser):  # проверка письма после первой модерации ru
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.letter_after_first_moderation_ru()  # письмо после первой модерации ru
def test_checking_letter_after_first_moderation_ua(browser):  # проверка письма после первой модерации ua
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.letter_after_first_moderation_ua()  # письмо после первой модерации ua


def test_delete_user_ru(browser):  # удаление пользователя ru
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
    admin_page.changing_user_status_to_Deleted()  # изменение статуса пользователя на "Удалено"
def test_delete_user_ua(browser):  # удаление пользователя ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    admin_page.changing_user_status_to_Deleted()  # изменение статуса пользователя на "Удалено"
