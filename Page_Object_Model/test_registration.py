import pytest
from .pages.oll_page import OllPage
from .pages.registration_page import RegistrationPage
from .pages.main_page import MainPage
from .pages.email_page import EmailPage
from .data_for_testing import UrlStartPage
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
    page.go_to_registration_page()  # нажатие на кнопку для перехона на страницу регистрации работодателя

    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.filling_in_required_fields()  # заполнение обязательных полей
    registration_page.browser.execute_script("window.scrollBy(0, 1300);")
    registration_page.submitting_form_for_registration()  # отправка формы на регистрацию
    time.sleep(12)

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.confirmation_message_for_sending_registration_form()  # проверка сообщения о подтверждении отправки формы регистрации работодателем


def test_checking_creation_of_user_in_admin_panel_ru(browser):  # проверка создания пользователя в админке ru
    url_admin_page = "http://admin-work.pw.preprod.pw/x"
    admin_page = AdminPage(browser, url_admin_page)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.checking_that_newly_created_user_has_status_Disabled_ru()
    time.sleep(3)

def test_checking_creation_of_user_in_admin_panel_ua(browser):  # проверка создания пользователя в админке ua
    url_admin_page = "http://admin-work.pw.preprod.pw/x"
    admin_page = AdminPage(browser, url_admin_page)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.checking_that_newly_created_user_has_status_Disabled_ua()
    time.sleep(3)


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

def test_change_of_employer_status_from_On_moderation_to_Aktivet_ua(browser):  # изменение статуса работодателя с "На модерации" на "Активет" ua
    url_admin_page = "http://admin-work.pw.preprod.pw/x"
    admin_page = AdminPage(browser, url_admin_page)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.change_of_user_status_from_On_moderation_to_Active_ua()

def test_change_of_employer_status_from_On_moderation_to_Aktivet_ru(browser):  # изменение статуса работодателя с "На модерации" на "Активет" ru
    url_admin_page = "http://admin-work.pw.preprod.pw/x"
    admin_page = AdminPage(browser, url_admin_page)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.change_of_user_status_from_On_moderation_to_Active_ru()






