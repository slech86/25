from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
import time

domain_sender_letter = '@logincasino.work'


def change_language_of_notifications_on_email(browser, language, user_id):  # изменение языка уведомлений на email
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/user/update?pk=' + user_id + '')
    admin_page.open()
    admin_page.change_language_of_notifications_on_email(language)  # изменение языка уведомлений на email
    admin_page.saving_user_card()  # сохранение карточки пользователя
    admin_page.waiting_to_save_user_and_open_all_users_page()  # ожидание сохранения пользователя и открытия страницы всех пользователей


def admin_authorization(browser):  # авторизация в админку
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    time.sleep(0.5)


def waiting_letter(class_object, domain, subject):  # ожидание письма
    letter = None
    for i in range(12):
        letter = class_object.filtred_mail(domain=domain, subject=subject)
        if isinstance(letter, list):
            return letter
        else:
            time.sleep(5)
    assert isinstance(letter, list), f'Нет письма с темой: "{subject}"'


def checking_content_of_letter(class_object, letter, expected_text):  # проверка содержания письма
    object_email = class_object.mailjobs('read', letter[0])
    body_email = object_email.json()['body']
    assert expected_text in body_email, f'В письме нет текста: "{expected_text}"'