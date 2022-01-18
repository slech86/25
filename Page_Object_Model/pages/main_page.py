import time

from .base_page import BasePage
from .locators import MainPageLocators
from Page_Object_Model.data_for_testing import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def waiting_for_main_page_to_open(self, language):  # ожидание открытия главной страницы
        if language == "/ua":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Робота у гральному бізнесі та IT'))
        else:
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Работа в игорном бизнесе и IT'))

    def confirmation_opening_of_main_page(self):  # подтверждение открытия главной страницы
        if "/ua" in self.browser.current_url:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua", "Не правильный URL"
        else:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/", "Не правильный URL"

    def checking_message_for_sending_registration_form(self):  # проверка сообщения о подтверждении отправки формы регистрации работодателя, соискателя
        infoText = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM).text
        if "/ua" in self.browser.current_url:
            assert "Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == infoText, 'Не верное сообщение'
        else:
            assert "Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == infoText, 'Не верное сообщение'

    def checking_employer_email_confirmation_message_after_registration(self):  # проверка сообщения о подтверждении электронной почты работодателя после регистрации
        time.sleep(1)
        infoText = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION).text
        if "/ua" in self.browser.current_url:
            assert "Профіль Вашої компанії був відправлений на модерацію, очікуйте на підтвердження!" == infoText, 'Не верное сообщение'
        else:
            assert "Профиль Вашей компании был отправлен на модерацию, ожидайте подтверждения!" == infoText, 'Не верное сообщение'



