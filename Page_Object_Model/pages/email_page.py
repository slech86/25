from .base_page import BasePage
from .locators import EmailPageLocators
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EmailPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailPageLocators.FIELD_EMAIL).send_keys('test_automation@smileexpo.com.ua')

        self.browser.find_element(*EmailPageLocators.FIELD_PASSWORD).send_keys('BwX37KJyiw02Cl')

        self.browser.find_element(*EmailPageLocators.BUTTON_LOG_IN).click()

    def confirmation_of_employer_registration_in_letter(self):  # подтверждение регистрации работодателя в письме
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_EMPLOYER).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.BUTTON_REGISTRATION_CONFIRM).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

        infoText = self.browser.find_element(*MainPageLocators.INFORMATION_TEXT_ABOUT_CONFIRMATION_OF_EMPLOYER_EMAIL_AFTER_REGISTRATION).text
        if "ua" in self.browser.current_url:
            assert "Профіль Вашої компанії був відправлений на модерацію, очікуйте на підтвердження!" == infoText
        else:
            assert "Профиль Вашей компании был отправлен на модерацию, ожидайте подтверждения!" == infoText
        self.browser.switch_to.window(self.browser.window_handles[0])

        self.browser.switch_to.default_content()  # выход из фрейма
