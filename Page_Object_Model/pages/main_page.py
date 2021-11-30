from .base_page import BasePage
from .locators import MainPageLocators
from Page_Object_Model.url_start_page import UrlStartPage



class MainPage(BasePage):
    def confirmation_message_for_sending_registration_form(self):  # проверка сообщения о подтверждении отправки формы регистрации работодателем
        infoText = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_SENDING_EMPLOYER_REGISTRATION_FORM).text
        if "ua" in self.browser.current_url:
            assert "Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == infoText
        else:
            assert "Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == infoText

    def confirmation_opening_of_main_page(self):  # подтверждение открытия главной страницы
        if "ua" in self.browser.current_url:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua", "Не правильный URL"
        else:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/", "Не правильный URL"

