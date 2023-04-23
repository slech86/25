import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_registration_page import CompanyRegistrationPage
from Page_Object_Model.pages.site.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.users import Accounts
from Page_Object_Model.mail.onesec_api import Mailbox
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.tests.company.company_add_edit import _resources_company_add_edit
from Page_Object_Model.tests import _resources_tests
import time
import json

domain_sender_letter = _resources_tests.domain_sender_letter


@pytest.mark.s_r_c
# @pytest.mark.skip
class TestCompanyRegistration:
    @pytest.mark.s_r_c
    def test_company_registration_with_filling_in_all_fields(self, browser, language):  # регистрация работодателя с заполнением всех полей
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        print(url_page)
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open(False)
        page.age_confirmation()  # подтверждение возраста больше 21 года
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.go_to_company_registration_page()  # нажатие на кнопку для перехода на страницу регистрации работодателя

        company_registration_page = CompanyRegistrationPage(browser, browser.current_url)
        page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
        company_registration_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
        company_registration_page.filling_in_required_fields(_resources_company_add_edit.user)  # заполнение обязательных полей

        company_registration_page.filling_in_optional_fields()  # заполнение не обязательных полей
        company_registration_page.browser.execute_script("window.scrollBy(0, 1300);")
        company_registration_page.submitting_form_for_registration()  # отправка формы на регистрацию

        main_page = MainPage(browser, browser.current_url)
        main_page.waiting_for_main_page_to_open(language)  # ожидание открытия главной страницы
        main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
        main_page.checking_message_for_sending_registration_form(language)  # проверка сообщения о подтверждении отправки формы регистрации

    def test_checking_creation_of_user_in_admin_panel(self, browser):  # проверка создания пользователя в админке
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_users_page()  # переход на страницу пользователей
        admin_page.new_user_search_by_email(_resources_company_add_edit.user)  # поиск пользователя по e-mail
        admin_page.checking_that_newly_created_user_has_status_disabled()  # проверка что новосозданный пользователь имеет статус "Отключено"

    @pytest.mark.s_r_c
    def test_changing_user_role_from_user_to_super_admin(self, browser):  # изменение роли пользователя с "User" на "SuperAdmin"
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_users_page()  # переход на страницу пользователей
        admin_page.new_user_search_by_email(_resources_company_add_edit.user)  # поиск пользователя по e-mail
        admin_page.go_to_object_editing_page()  # переход на страницу пользователя
        admin_page.changing_role_from_user_to_super_admin()  # изменение роли с "User" на "SuperAdmin"
        admin_page.saving_user_card()  # сохранение карточки пользователя
        admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения статуса и открытия страницы всех пользователей

    def test_authorization_of_user_in_disabled_status(self, browser, language):  # авторизация пользователя в статусе "Отключен"
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_new_authorization(_resources_company_add_edit.user)  # авторизация пользователя
        page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
        page.info_text_for_authorization_in_user_status_disabled(language)  # инфо текст при авторизации в статусе пользователя "Отключен"

    @pytest.mark.s_r_c
    def test_email_verification_after_company_registration(self, browser, language):  # верификация почты после регистрации работодателя
        # link = Accounts.url_email
        # email_page = EmailPage(browser, link)
        # email_page.open()
        # # browser.maximize_window()
        # email_page.email_authorization()  # авторизация email
        # email_page.confirmation_of_company_registration_in_letter(language)  # переход по ссылке для подтверждения регистрации работодателя в письме
        # main_page = MainPage(browser, browser.current_url)
        # main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
        # main_page.checking_employer_email_confirmation_message_after_registration(language)  # проверка сообщения о подтверждении электронной почты работодателя после регистрации

        email = Mailbox(Singleton.logins_and_mails[_resources_company_add_edit.user]['mail_name'])

        subject = None
        if language == "":
            subject = 'Регистрация работодателя на LCwork'
        elif language == "/ua":
            subject = 'Реєстрація роботодавця на LCwork'
        elif language == "/en":
            subject = 'Employer registration on LCwork'
        _resources_tests.waiting_letter(email, domain_sender_letter, subject)  # ожидание письма
        link = email.get_link(domain_sender_letter, subject, clear=False)
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
        main_page.checking_employer_email_confirmation_message_after_registration(language)  # проверка сообщения о подтверждении электронной почты работодателя после регистрации

    def test_authorization_of_user_in_on_moderation_status(self, browser, language):  # авторизация пользователя в статусе "На модерации"
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_new_authorization(_resources_company_add_edit.user)  # авторизация пользователя
        page.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя
        page.info_text_for_authorization_in_user_status_on_moderation(language)  # инфо текст при авторизации в статусе пользователя "На модерации"

    @pytest.mark.s_r_c
    def test_change_of_employer_status_from_on_moderation_to_activet(self, browser):  # изменение статуса работодателя с "На модерации" на "Активен"
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_users_page()  # переход на страницу пользователей
        admin_page.new_user_search_by_email(_resources_company_add_edit.user)  # поиск пользователя по e-mail
        admin_page.go_to_object_editing_page()  # переход на страницу пользователя
        admin_page.change_of_user_status_from_on_moderation_to_active()  # изменение статуса пользователя с "На модерации" на "Активен"
        admin_page.saving_user_card()  # сохранение карточки пользователя
        admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения статуса и открытия страницы всех пользователей
        admin_page.new_user_search_by_email(_resources_company_add_edit.user)  # поиск пользователя по e-mail
        admin_page.check_that_user_has_status_active()  # проверка что пользователь имеет статус "Активен"

    # def test_authorization_of_user_in_Active_status(browser, language):  # авторизация пользователя в статусе "Активен"
    #     url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    #     page = OllPage(browser, url_Page)
    #     # browser.maximize_window()
    #     page.open()
    #     page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    #     page.user_new_authorization()  # авторизация пользователя
    #     page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя

    def test_checking_letter_after_first_moderation(self,browser, language):  # проверка письма после первой модерации компании
        # link = Accounts.url_email
        # email_page = EmailPage(browser, link)
        # email_page.open()
        # # browser.maximize_window()
        # email_page.email_authorization()  # авторизация email
        # email_page.letter_after_first_moderation_of_company(language)  # письмо после первой модерации компании

        subject = None
        if language == "":
            subject = 'Добро пожаловать на LСwork'
        elif language == "/ua":
            subject = 'Ласкаво просимо на LCwork"]'
        elif language == "/en":
            subject = 'Welcome to LC Work!'

        expected_text = None
        if language == "":
            expected_text = 'Ура! Ваш аккаунт прошел модерацию.'
        elif language == "/ua":
            expected_text = 'Ура! Ваш акаунт пройшов модерацiю.'
        elif language == "/en":
            expected_text = 'Your account has been moderated.'

        email = Mailbox(Singleton.logins_and_mails[_resources_company_add_edit.user]['mail_name'])
        letter = _resources_tests.waiting_letter(email, domain_sender_letter, subject)  # ожидание письма
        _resources_tests.checking_content_of_letter(email, letter, expected_text)  # проверка содержания письма
