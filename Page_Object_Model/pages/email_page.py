from .base_page import BasePage
from .locators import EmailPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EmailPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailPageLocators.FIELD_EMAIL).send_keys('test_automation@smileexpo.com.ua')
        self.browser.find_element(*EmailPageLocators.FIELD_PASSWORD).send_keys('BwX37KJyiw02Cl')
        self.browser.find_element(*EmailPageLocators.BUTTON_LOG_IN).click()

    def confirmation_of_employer_registration_in_letter_ru(self):  # подтверждение регистрации работодателя в письме RU
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_EMPLOYER_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.BUTTON_REGISTRATION_CONFIRM).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def confirmation_of_employer_registration_in_letter_ua(self):  # подтверждение регистрации работодателя в письме UA
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_EMPLOYER_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.BUTTON_REGISTRATION_CONFIRM).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def letter_after_first_moderation_ru(self):  # письмо после первой модерации ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_FIRST_MODERATION_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU).text
        assert "Ура! Ваш аккаунт прошел модерацию." == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def letter_after_first_moderation_ua(self):  # письмо после первой модерации ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_FIRST_MODERATION_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA).text
        assert "Ура!" == letter_text, 'Не верное сообщение'  # ???
        self.browser.switch_to.default_content()  # выход из фрейма