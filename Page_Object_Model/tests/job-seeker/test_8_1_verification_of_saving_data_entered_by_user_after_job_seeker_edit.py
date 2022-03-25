from Page_Object_Model.сonfiguration import UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage


def test_verification_of_saving_data_entered_by_user_after_job_seeker_edit(browser, language):  # проверка сохранения введенных пользователем данных после редактирования соискателя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.search_user_by_email(language)  # поиск пользователя по e-mail
    admin_page.go_to_object_editing_page()  # переход на страницу пользователя
    admin_page.verification_of_saving_data_entered_by_user_after_job_seeker_edit_ru(language)  # проверка сохранения введенных пользователем данных после редактирования соискателя RU
