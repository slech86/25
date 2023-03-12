import pytest
from Page_Object_Model.configuration import UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage


# @pytest.mark.skip
def test_verification_of_saving_data_entered_by_user_after_company_registration(browser, language):  # проверка сохранения введенных пользователем данных после регистрации компании
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.new_user_search_by_email(language, 'company')  # поиск пользователя по e-mail
    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.verification_of_saving_data_entered_by_user_after_company_registration_ru(language, 'company')  # проверка сохранения введенных пользователем данных после регистрации компании RU
