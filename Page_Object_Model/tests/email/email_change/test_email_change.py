import time
import pytest
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.company_edit_page import CompanyEditPage
from Page_Object_Model.pages.site.main_page import MainPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.tests import _resources_tests
from Page_Object_Model.mail.onesec_api import Mailbox

# pytest --reruns 1 --html=./reports/report.html -s tests/email/email_change

user = 'employer_change_email'
new_password = None
domain_sender_letter = _resources_tests.domain_sender_letter
new_mail_name = users_variables[user]['mail_name'] + '_' + str(int(time.time()))
new_email = new_mail_name + '@1secmail.com'


# @pytest.mark.skip
class TestEmailChange:
    def test_precondition(self, browser, language):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[user]["id"])  # изменение языка уведомлений на email

    def test_email_changes(self, browser, language):  # изменение email
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

        company_edit_page = CompanyEditPage(browser, browser.current_url)
        company_edit_page.email_changes(users_variables[user]["password"], language, new_email)  # изменение email

    def test_confirmation_changes_email(self, browser, language):  # подтверждение смены email
        email = Mailbox(new_mail_name)

        subject = None
        if language == "":
            subject = 'Подтверждение смены email на LCwork'
        elif language == "/ua":
            subject = 'Підтвердження зміни email на LCwork'
        elif language == "/en":
            subject = 'Confirm email change on LC Work'
        elif language == "/pl":
            subject = 'Potwierdzenie zmiany adresu e-mail w LCwork'
        _resources_tests.waiting_letter(email, domain_sender_letter, subject)  # ожидание письма
        link = email.get_link(domain_sender_letter, subject, clear=False)

        main_page = MainPage(browser, link)
        main_page.open(cookie=False)
        main_page.waiting_for_main_page_to_open(language)  # ожидание открытия главной страницы
        main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
        main_page.checking_message_after_confirmation_of_email_change(language)  # проверка сообщения после подтверждения смены email

    def test_email_replacement_check(self, browser, language):  # проверка замены email
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

        company_edit_page = CompanyEditPage(browser, browser.current_url)
        company_edit_page.user_email_verification(new_email)  # проверка email пользователя

        _resources_tests.admin_authorization(browser)  # авторизация в админку
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/user')
        admin_page.open()
        admin_page.search_user_by_id(users_variables[user]["id"])  # поиск пользователя по id
        admin_page.go_to_object_editing_page()  # переход на страницу пользователя
        admin_page.email_field_validation(new_email)  # проверка поля email
