import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.company_registration_page import CompanyRegistrationPage
from Page_Object_Model.pages.main_page import MainPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage
import time


def test_verification_of_saving_data_entered_by_user_during_company_registration(browser, language):  # проверка сохранения введенных пользователем данных при регистрации компании
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

    admin_page.verification_of_saving_data_entered_by_user_during_company_registration_ru(language)  # проверка сохранения введенных пользователем данных при регистрации компании RU