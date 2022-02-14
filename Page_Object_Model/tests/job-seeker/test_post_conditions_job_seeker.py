from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlPageAdmin


def test_delete_user(browser, language):  # удаление пользователя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.changing_user_status_to_Deleted()  # изменение статуса пользователя на "Удалено"


def test_change_field_Login_and_Email(browser, language):  # изменение поля "Login" и "Электронный адрес"
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей

    if language == "/ua":
        admin_page.search_user_by_email_ua()  # поиск пользователя по e-mail ua
    else:
        admin_page.search_user_by_email_ru()  # поиск пользователя по e-mail ru

    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.adding_unique_values_to_Login_and_Email_fields()  # внесение в поля "Login" и "Электронный адрес" уникальные значения
    admin_page.saving_user_card()  # сохранение карточки пользователя