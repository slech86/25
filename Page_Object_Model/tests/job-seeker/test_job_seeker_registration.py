import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.job_seeker_registration_page import JobSeekerRegistrationPage
from Page_Object_Model.pages.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage
import time


def test_job_seeker_registration_with_filling_in_all_fields(browser, language):  # регистрация соискателя с заполнением всех полей
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.go_to_job_seeker_registration_page()  # нажатие на кнопку для перехода на страницу регистрации соискателя

    job_seeker_registration_page = JobSeekerRegistrationPage(browser, browser.current_url)
    job_seeker_registration_page.filling_in_all_fields()  # заполнение всех полей
    job_seeker_registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы
    main_page.confirmation_message_for_sending_registration_form()  # проверка сообщения о подтверждении отправки формы регистрации

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


def test_confirmation_of_registration_of_applicant_and_authorization_on_site(browser, language):  # подтверждение регистрации соискателя и авторизация на сайте
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email

    if language == "/ua":
        email_page.confirmation_of_job_seeker_registration_in_letter_ua()  # подтверждение регистрации соискателя в письме ua
    else:
        email_page.confirmation_of_job_seeker_registration_in_letter_ru()  # подтверждение регистрации соискателя в письме ru

    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page()  # подтверждение открытия главной страницы

    page = OllPage(browser, browser.current_url)
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.user_authorization()  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя


def test_check_that_user_has_status_Active(browser, language):  # проверка что пользователь имеет статус "Активен"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.check_that_user_has_status_Active()  # проверка что пользователь имеет статус "Активен"
