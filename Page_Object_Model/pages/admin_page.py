from .base_page import BasePage
from .locators import AdminPageLocators
from Page_Object_Model.data_for_testing import TestData, Accounts
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class AdminPage(BasePage):
    def admin_authorization(self):  # авторизация админки
        self.browser.find_element(*AdminPageLocators.FIELD_LOGIN).send_keys(Accounts.main_login_admin)
        self.browser.find_element(*AdminPageLocators.FIELD_PASSWORD).send_keys(Accounts.main_password_admin)
        self.browser.find_element(*AdminPageLocators.BUTTON_LOG_IN).click()

    def go_to_users_page(self):  # переход на страницу пользователей
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()
        self.browser.find_element(*AdminPageLocators.USERS).click()


    def go_to_user_page(self):  # переход на страницу пользователя
        self.browser.find_element(*AdminPageLocators.BUTTON_USER_EDIT).click()

    def changing_role_from_User_to_SuperAdmin(self):  # изменение роли с "User" на "SuperAdmin"
        self.browser.find_element(*AdminPageLocators.FIELD_WITH_ROLE_USER).click()
        self.browser.find_element(*AdminPageLocators.ROLE_SUPER_ADMIN).click()


    def adding_unique_values_to_Login_and_Email_fields(self):  # внескние в поля "Login" и "Электронный адрес" уникальные значения
        self.browser.find_element(*AdminPageLocators.FIELD_USER_LOGIN).send_keys(str(random.random()))
        field_user_email = self.browser.find_element(*AdminPageLocators.FIELD_USER_EMAIL)
        field_user_email.clear()
        field_user_email.send_keys(TestData.time_Now + '@test.com' + str(random.random()))

    def saving_user_card(self):  # сохранение карточки пользователя
        self.browser.find_element(*AdminPageLocators.BUTTON_SAVE_AND_EDIT).click()  # вынести в отдельный метод ???
        time.sleep(4)


    def search_user_by_email_ru(self):  # поиск пользователя по e-mail ru
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ru, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_RU)
    def search_user_by_email_ua(self):  # поиск пользователя по e-mail ua
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ua, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_UA)


    def checking_that_newly_created_user_has_status_Disabled(self):  # проверка что новосозданный пользователь имеет статус "Отключено"
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Отключен', 'Статус не "Отключен"'


    def change_of_user_status_from_On_moderation_to_Active(self):  # изменение статуса пользователя с "На модерации" на "Активет"
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'На модерации', 'Статус не "На модерации"'
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.USER_STATUS).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_ACTIVE).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_SAVING).click()
        time.sleep(5)
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Активен', 'Статус не "Активен"'


    def changing_user_status_to_Deleted(self):  # изменение статуса пользователя на "Удалено"
        self.browser.find_element(*AdminPageLocators.USER_STATUS).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_DELETED).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_SAVING).click()
        time.sleep(5)
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Удалено', 'Статус не "Удалено"'
