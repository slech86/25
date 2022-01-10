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
        time.sleep(0.2)
        # подтверждение возраста больше 21 года

    def opening_pop_up_for_login(self):  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        self.browser.find_element(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN).click()

    def go_to_company_registration_page(self):  # нажатие на кнопку для перехода на страницу регистрации работодателя
        self.browser.find_element(*OllPageLocators.COMPANY_REGISTRATION_LINK).click()

    def go_to_job_seeker_registration_page(self):  # нажатие на кнопку для перехода на страницу регистрации соискателя
        self.browser.find_element(*OllPageLocators.JOB_SEEKER_TAB).click()
        self.browser.find_element(*OllPageLocators.JOB_SEEKER_REGISTRATION_LINK).click()

    def user_authorization(self):  # авторизация пользователя
        if "ua" in self.browser.current_url:
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(TestData.login_ua)
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')

        else:
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(TestData.login_ru)
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')

        self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        # self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys('l6FOt9tvJT')

        self.browser.find_element(*OllPageLocators.BUTTON_LOG_IN).click()
        time.sleep(2)

    def check_for_non_authorization_of_user(self):  # проверка на не авторизацию пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN)

    def opening_authorized_user_menu(self):  # нажатие на кнопку для открытия меню авторизированного пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_AUTHORIZED_USER).click()

    def go_to_personal_cabinet_page(self):  # нажатие на кнопку для перехода на страницу личного кабинета
        self.browser.find_element(*OllPageLocators.LINK_PERSONAL_ACCOUNT).click()



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
