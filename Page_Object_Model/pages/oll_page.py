from .base_page import BasePage
from .locators import OllPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.data_for_testing import TestData
import time

class OllPage(BasePage):
    def age_confirmation(self):
        time.sleep(5)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(OllPageLocators.BUTTON_YES_WHEN_CHECKING_AGE)).click()
        time.sleep(1)
        # подтверждение возраста больше 21 года

    def opening_pop_up_for_login(self):
        self.browser.find_element(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN).click()
        # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации

    def go_to_registration_page(self):
        self.browser.find_element(*OllPageLocators.COMPANY_REGISTRATION_LINK).click()
        # нажатие на кнопку для перехода на страницу регистрации работодателя

    def authorization_after_registration(self):  # авторизация после регистрации
        if "ua" in self.browser.current_url:
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(TestData.login_ru)
        else:
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(TestData.login_ua)
        self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*OllPageLocators.BUTTON_LOG_IN).click()
        time.sleep(1)

    def check_for_non_authorization_of_user(self):  # проверка на не авторизацию пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN)

    def check_for_user_authorization(self):  # проверка на авторизацию пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_AUTHORIZED_USER)

    def info_text_for_authorization_in_user_status_Disabled(self):  # инфо текст при авторизации в статусе пользователя "Отключен"
        infoText = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if "ua" in self.browser.current_url:
            assert "Користувач ще не активований. Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == infoText, 'Не верное сообщение'
        else:
            assert "Пользователь еще не активирован. Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == infoText, 'Не верное сообщение'

    def info_text_for_authorization_in_user_status_On_moderation(self):  # инфо текст при авторизации в статусе пользователя "На модерации"
        infoText = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if "ua" in self.browser.current_url:
            assert "Модерація вашого облікового запису завершиться впродовж 24 годин" == infoText, 'Не верное сообщение'
        else:
            assert "Модерация вашего аккаунта завершится в течение 24 часов." == infoText, 'Не верное сообщение'