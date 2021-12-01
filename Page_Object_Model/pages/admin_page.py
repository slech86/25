from .base_page import BasePage
from .locators import AdminPageLocators
from Page_Object_Model.data_for_testing import TestData
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AdminPage(BasePage):
    def admin_authorization(self):  # авторизация админки
        self.browser.find_element(*AdminPageLocators.FIELD_LOGIN).send_keys('p.verbenets')
        self.browser.find_element(*AdminPageLocators.FIELD_PASSWORD).send_keys('l6FOt9tvJT')
        self.browser.find_element(*AdminPageLocators.BUTTON_LOG_IN).click()


    def checking_that_newly_created_user_has_status_Disabled_ru(self):  # проверка что новосозданный пользователь имеет статус "Отключено" ru
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()
        self.browser.find_element(*AdminPageLocators.USERS).click()
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ru, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_RU)
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Отключен', 'Статус не "Отключен"'

    def checking_that_newly_created_user_has_status_Disabled_ua(self):  # проверка что новосозданный пользователь имеет статус "Отключено" ua
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()
        self.browser.find_element(*AdminPageLocators.USERS).click()
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ua, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_UA)
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Отключен', 'Статус не "Отключен"'


    def change_of_user_status_from_On_moderation_to_Active_ru(self):  # изменение статуса пользователя с "На модерации" на "Активет" ru
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()
        self.browser.find_element(*AdminPageLocators.USERS).click()
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ru, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_RU)
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

    def change_of_user_status_from_On_moderation_to_Active_ua(self):  # изменение статуса пользователя с "На модерации" на "Активет" ua
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()
        self.browser.find_element(*AdminPageLocators.USERS).click()
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(TestData.email_ua, Keys.ENTER)
        time.sleep(2)
        self.browser.find_element(*AdminPageLocators.USER_EMAIL_UA)
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
