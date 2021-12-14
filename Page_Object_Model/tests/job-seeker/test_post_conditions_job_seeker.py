from Page_Object_Model.pages.admin_page import AdminPage
from Page_Object_Model.data_for_testing import UrlPageAdmin


def test_delete_user_ru(browser):  # удаление пользователя ru
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
    admin_page.changing_user_status_to_Deleted()  # изменение статуса пользователя на "Удалено"
def test_delete_user_ua(browser):  # удаление пользователя ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    admin_page.changing_user_status_to_Deleted()  # изменение статуса пользователя на "Удалено"

def test_change_field_Login_and_Email_ru(browser):  # изменение поля "Login" и "Электронный адрес" ru
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru
    admin_page.go_to_user_page()  # переход на страницу пользователя
    admin_page.adding_unique_values_to_Login_and_Email_fields()  # внесение в поля "Login" и "Электронный адрес" уникальные значения
    admin_page.saving_user_card()  # сохранение карточки пользователя
def test_change_field_Login_and_Email_ua(browser):  # изменение поля "Login" и "Электронный адрес" ua
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    admin_page.go_to_user_page()  # переход на страницу пользователя
    admin_page.adding_unique_values_to_Login_and_Email_fields()  # внесение в поля "Login" и "Электронный адрес" уникальные значения
    admin_page.saving_user_card()  # сохранение карточки пользователя