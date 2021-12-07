from .base_page import BasePage
from .locators import EmailPageLocators
from Page_Object_Model.data_for_testing import Accounts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EmailPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailPageLocators.FIELD_EMAIL).send_keys(Accounts.main_login_email)
        self.browser.find_element(*EmailPageLocators.FIELD_PASSWORD).send_keys(Accounts.main_password_email)
        self.browser.find_element(*EmailPageLocators.BUTTON_LOG_IN).click()

    def confirmation_of_employer_registration_in_letter_ru(self):  # подтверждение регистрации работодателя в письме RU
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.BUTTON_REGISTRATION_CONFIRM).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def confirmation_of_employer_registration_in_letter_ua(self):  # подтверждение регистрации работодателя в письме UA
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.BUTTON_REGISTRATION_CONFIRM).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def letter_after_first_moderation_of_company_ru(self):  # письмо после первой модерации компании ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU).text
        assert "Ура! Ваш аккаунт прошел модерацию." == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def letter_after_first_moderation_of_company_ua(self):  # письмо после первой модерации компании ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA).text
        assert "Ура! Ваш акаунт пройшов модерацiю." == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма