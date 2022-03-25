import pytest
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlPageAdmin


def test_delete_user(browser, language):  # удаление пользователя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language)  # поиск пользователя по e-mail
    admin_page.changing_user_status_to_deleted()  # изменение статуса пользователя на "Удалено"


# @pytest.mark.s_r_c
def test_change_field_login_and_email(browser, language):  # изменение поля "Login" и "Электронный адрес"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language)  # поиск пользователя по e-mail
    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.adding_unique_values_to_login_and_email_fields()  # внесение в поля "Login" и "Электронный адрес" уникальные значения
    admin_page.saving_user_card()  # сохранение карточки пользователя
