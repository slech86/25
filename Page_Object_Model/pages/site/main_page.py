import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import MainPageLocators
from Page_Object_Model.configuration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.utility.utility import generate_alphanum_random_string


class MainPage(BasePage):
    def waiting_for_main_page_to_open(self, language):  # ожидание открытия главной страницы
        if language == "":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Работа в игорном бизнесе и IT'))
        elif language == "/ua":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Робота у гральному бізнесі та IT'))
        elif language == "/en":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Work in the Gambling Business and IT'))
        elif language == "/pl":
            WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((MainPageLocators.H1), 'Praca w branży hazardowej i IT'))

    def confirmation_opening_of_main_page(self, language):  # подтверждение открытия главной страницы
        if language == '':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/', 'Не правильный URL'
        elif language == '/ua':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua', 'Не правильный URL'
        elif language == '/en':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en', 'Не правильный URL'
        elif language == '/pl':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/pl', 'Не правильный URL'

    def checking_message_for_sending_registration_form(self, language):  # проверка сообщения о подтверждении отправки формы регистрации работодателя, соискателя
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM).text
        if language == "":
            assert "Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "To complete account activation, follow the link in the letter sent to your email." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Aby dokończyć aktywację konta, skorzystaj z linku zawartego w wysłanej do Ciebie wiadomości e-mail." == info_text, 'Не верное сообщение'

    def checking_employer_email_confirmation_message_after_registration(self, language):  # проверка сообщения о подтверждении электронной почты работодателя после регистрации
        time.sleep(1)
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION).text
        if language == "":
            assert "Профиль Вашей компании был отправлен на модерацию, ожидайте подтверждения!" == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Профіль Вашої компанії був відправлений на модерацію, очікуйте на підтвердження!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your company profile has been sent for moderation, wait for confirmation!" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Twój profil firmowy został wysłany do moderacji, oczekuj potwierdzenia!" == info_text, 'Не верное сообщение'

    def entering_new_password_when_recovering_it(self, language):  # ввод нового пароля при его восстановлении
        new_password = generate_alphanum_random_string(22)
        time.sleep(1)
        self.browser.find_element(*MainPageLocators.FIELD_PASSWORD_IN_RESET_PASSWORD_FORM).send_keys(new_password)
        self.browser.find_element(*MainPageLocators.FIELD_REPEAT_PASSWORD_IN_RESET_PASSWORD_FORM).send_keys(new_password)
        self.browser.find_element(*MainPageLocators.BUTTON_CHANGE_PASSWORD).click()

        info_text = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(MainPageLocators.INFO_TEXT_AFTER_PASSWORD_RECOVERY)).text
        if language == "":
            assert "Ваш пароль был успешно изменен." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Ваш пароль був успішно оновлений." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your password has been successfully changed" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Twoje hasło zostało zaktualizowane pomyślnie." == info_text, 'Не верное сообщение'
        return new_password

    def checking_message_after_confirmation_of_password_change(self, language):  # проверка сообщения после подтверждения смены пароля
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_IN_MODAL).text
        if language == "":
            assert "Ваш пароль был обновлен." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Ваш пароль був оновлений." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your password has been updated." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Twoje hasło zostało zaktualizowane." == info_text, 'Не верное сообщение'

    def checking_message_after_confirmation_of_email_change(self, language):  # проверка сообщения после подтверждения смены email
        info_text = self.browser.find_element(*MainPageLocators.INFO_TEXT_IN_MODAL).text
        if language == "":
            assert "Ваш e-mail был обновлен." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Ваша електронна адреса була оновлена." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your email has been updated." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Pański/Pani adres e-mail został zaktualizowany." == info_text, 'Не верное сообщение'