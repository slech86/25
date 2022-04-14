import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_registration_page import JobSeekerRegistrationPage
from Page_Object_Model.pages.site.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.data_for_testing import Accounts


@pytest.mark.s_r_c
def test_job_seeker_registration_with_filling_in_all_fields(browser, language):  # регистрация соискателя с заполнением всех полей
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.go_to_job_seeker_registration_page()  # нажатие на кнопку для перехода на страницу регистрации соискателя

    job_seeker_registration_page = JobSeekerRegistrationPage(browser, browser.current_url)
    job_seeker_registration_page.filling_in_all_fields(language, 2)  # заполнение всех полей
    job_seeker_registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

    main_page = MainPage(browser, browser.current_url)
    main_page.waiting_for_main_page_to_open(language)  # ожидание открытия главной страницы
    main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
    main_page.checking_message_for_sending_registration_form(language)  # проверка сообщения о подтверждении отправки формы регистрации


def test_checking_creation_of_user_in_admin_panel(browser, language):  # проверка создания пользователя в админке
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language, 2)  # поиск пользователя по e-mail
    admin_page.checking_that_newly_created_user_has_status_disabled()  # проверка что новосозданный пользователь имеет статус "Отключено"


# @pytest.mark.skip
@pytest.mark.s_r_c
def test_changing_user_role_from_user_to_super_admin(browser, language):  # изменение роли пользователя с "User" на "SuperAdmin"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language, 2)  # поиск пользователя по e-mail
    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.changing_role_from_user_to_super_admin()  # изменение роли с "User" на "SuperAdmin"
    admin_page.saving_user_card()  # сохранение карточки пользователя


def test_authorization_of_user_in_disabled_status(browser, language):  # авторизация пользователя в статусе "Отключен"
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(language, 2)  # авторизация пользователя
    page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
    page.info_text_for_authorization_in_user_status_disabled(language)  # инфо текст при авторизации в статусе пользователя "Отключен"


@pytest.mark.s_r_c
def test_confirmation_of_registration_of_applicant_and_authorization_on_site(browser, language):  # подтверждение регистрации соискателя и авторизация на сайте
    link = Accounts.url_email
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.confirmation_of_job_seeker_registration_in_letter(language)  # подтверждение регистрации соискателя в письме
    main_page = MainPage(browser, browser.current_url)
    main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы

    page = OllPage(browser, browser.current_url)
    page.age_confirmation()  # подтверждение возраста больше 21 года
    page.user_authorization(language, 2)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя


def test_check_that_user_has_status_active(browser, language):  # проверка что пользователь имеет статус "Активен"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language, 2)  # поиск пользователя по e-mail
    admin_page.check_that_user_has_status_active()  # проверка что пользователь имеет статус "Активен"
