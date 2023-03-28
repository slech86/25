from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin


def change_language_of_notifications_on_email(browser, language, user_id):  # изменение языка уведомлений на email
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/user/update?pk=' + user_id + '')
    admin_page.open()
    admin_page.change_language_of_notifications_on_email(language)  # изменение языка уведомлений на email
    admin_page.saving_user_card()  # сохранение карточки пользователя
    admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения пользователя и открытия страницы всех пользователей