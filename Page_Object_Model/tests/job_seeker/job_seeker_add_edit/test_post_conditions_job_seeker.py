from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.configuration import UrlStartPageAdmin


def test_delete_user(browser):  # удаление пользователя
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.new_user_search_by_email('job_seeker')  # поиск пользователя по e-mail
    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.changing_user_status_to_deleted()  # изменение статуса пользователя на "Удалено"
    admin_page.saving_user_card()  # сохранение карточки пользователя
    admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения статуса и открытия страницы всех пользователей
    admin_page.new_user_search_by_email('job_seeker')  # поиск пользователя по e-mail
    admin_page.check_that_user_has_status_delete()  # проверка что пользователь имеет статус "Удалено"


# def test_change_field_login_and_email(browser, language):  # изменение поля "Login" и "Электронный адрес"
#     admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
#     admin_page.open()
#     admin_page.admin_authorization()
#     admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
#     admin_page.go_to_users_page()  # переход на страницу пользователей
#     admin_page.new_user_search_by_email(language, 'job_seeker')  # поиск пользователя по e-mail
#     admin_page.go_to_object_editing_page()  # переход на страницу пользователя
#     admin_page.adding_unique_values_to_login_and_email_fields()  # внесение в поля "Login" и "Электронный адрес" уникальные значения
#     admin_page.saving_user_card()  # сохранение карточки пользователя
