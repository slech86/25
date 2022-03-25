import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import MainPageLocators
from Page_Object_Model.сonfiguration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def waiting_for_main_page_to_open(self, language):  # ожидание открытия главной страницы
        if language == "/ua":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Робота у гральному бізнесі та IT'))
        elif language == "":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Работа в игорном бизнесе и IT'))
        elif language == "/en":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Work in the Gambling Business and IT'))

    def confirmation_opening_of_main_page(self, language):  # подтверждение открытия главной страницы
        if language == "/ua":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua", "Не правильный URL"
        elif language == "":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/", "Не правильный URL"
        elif language == "/en":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en", "Не правильный URL"

    def checking_message_for_sending_registration_form(self, language):  # проверка сообщения о подтверждении отправки формы регистрации работодателя, соискателя
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM).text
        if language == "/ua":
            assert "Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "???" == info_text, 'Не верное сообщение'

    def checking_employer_email_confirmation_message_after_registration(self, language):  # проверка сообщения о подтверждении электронной почты работодателя после регистрации
        time.sleep(1)
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION).text
        if language == "/ua":
            assert "Профіль Вашої компанії був відправлений на модерацію, очікуйте на підтвердження!" == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Профиль Вашей компании был отправлен на модерацию, ожидайте подтверждения!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "???" == info_text, 'Не верное сообщение'



