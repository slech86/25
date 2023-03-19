import time
import pytest
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.users import Accounts
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.main_page import MainPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.pages.site.job_seeker_edit_page import JobSeekerEditPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage

# pytest --reruns 1 --html=./reports/report.html -s tests/password/password_change

user = 'job_seeker_change_password'
new_password = None


# @pytest.mark.skip
class TestPasswordChange:
    def test_precondition(self, browser):
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        time.sleep(0.5)
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/user')
        admin_page.open()
        admin_page.search_user_by_email(users_variables[user]["mail"])  # поиск пользователя по e-mail
        admin_page.go_to_object_editing_page()  # переход на страницу пользователя
        admin_page.password_field_filling(users_variables[user]["password"])  # заполнение поля пароль
        admin_page.saving_user_card()  # сохранение карточки пользователя
        admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения пользователя и открытия страницы всех пользователей

    def test_password_changes(self, browser, language):  # изменение пароля
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

        job_seeker_edit_page = JobSeekerEditPage(browser, browser.current_url)
        global new_password
        new_password = job_seeker_edit_page.password_changes(users_variables[user]["password"], language)  # изменение пароля

    def test_confirmation_of_password_changes_through_email(self, browser, language):  # подтверждения смены пароля через email
        link = Accounts.url_email
        email_page = EmailPage(browser, link)
        email_page.open()
        email_page.email_authorization()  # авторизация email
        email_page.click_on_link_in_email_to_confirm_password_change(language)  # переход по ссылке с письма для подтверждение смены пароля

        main_page = MainPage(browser, browser.current_url)
        main_page.waiting_for_main_page_to_open(language)  # ожидание открытия главной страницы
        main_page.confirmation_opening_of_main_page(language)  # подтверждение открытия главной страницы
        main_page.checking_message_after_confirmation_of_password_change(language)  # проверка сообщения после подтверждения смены пароля

    def test_login_with_new_password(self, browser, language):  # авторизация с новым паролем
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user, password=new_password)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета
