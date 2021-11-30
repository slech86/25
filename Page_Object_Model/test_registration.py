import pytest
from .pages.oll_page import OllPage
from .pages.registration_page import RegistrationPage
from .pages.main_page import MainPage
from .pages.email_page import EmailPage
from .url_start_page import UrlStartPage
import time


@pytest.mark.parametrize('language', ["", "/ua"])
def test_employer_registration_with_filling_in_only_required_fields(browser, language):  # регистрация работодателя с заполнением только обязательных полей
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    browser.maximize_window()
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

@pytest.mark.parametrize('language', ["RU", "UA"])
def test_email_verification_after_employer_registration_UA(browser, language):  # верификация почты после регистрации работодателя
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    browser.maximize_window()

    email_page.email_authorization()  # авторизация email
    email_page.confirmation_of_employer_registration_in_letter()  # переход по ссылке для подтверждения регистрации работодателя в письме



