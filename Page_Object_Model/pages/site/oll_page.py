from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import OllPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.singleton import Singleton
import time


class OllPage(BasePage):
    def age_confirmation(self):
        time.sleep(5)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(OllPageLocators.BUTTON_YES_WHEN_CHECKING_AGE)).click()
        time.sleep(0.2)
        # подтверждение возраста больше 21 года

    def go_to_resume_page_through_header(self):  # переход на страницу всех резюме через хедер
        self.browser.find_element(*OllPageLocators.DROPDOWN_LIST_EMPLOYER).click()
        self.browser.find_element(*OllPageLocators.RESUME_IN_HEDER).click()

    def go_to_vacancies_page_through_header(self):  # переход на страницу вакансий через хедер
        self.browser.find_element(*OllPageLocators.DROPDOWN_LIST_APPLICANT).click()
        self.browser.find_element(*OllPageLocators.VACANCIES_IN_HEDER).click()

    def opening_pop_up_for_login(self):  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        self.browser.find_element(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN).click()

    def go_to_company_registration_page(self):  # нажатие на кнопку для перехода на страницу регистрации работодателя
        self.browser.find_element(*OllPageLocators.COMPANY_REGISTRATION_LINK).click()

    def go_to_job_seeker_registration_page(self):  # нажатие на кнопку для перехода на страницу регистрации соискателя
        self.browser.find_element(*OllPageLocators.JOB_SEEKER_TAB).click()
        self.browser.find_element(*OllPageLocators.JOB_SEEKER_REGISTRATION_LINK).click()

    def user_authorization(self, language, key):  # авторизация пользователя
        if language == "/ua":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][1][0])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')
        elif language == "":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][0][0])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')
        elif language == "/en":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][2][0])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')

        self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        # self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys('l6FOt9tvJT')

        self.browser.find_element(*OllPageLocators.BUTTON_LOG_IN).click()
        time.sleep(2)

    def check_for_non_authorization_of_user(self):  # проверка на не авторизацию пользователя
        assert self.is_element_present(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN), 'Пользователь авторизирован, но не должен'

    def opening_authorized_user_menu(self):  # нажатие на кнопку для открытия меню авторизированного пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_AUTHORIZED_USER).click()

    def go_to_personal_cabinet_page(self):  # нажатие на кнопку для перехода на страницу личного кабинета
        self.browser.find_element(*OllPageLocators.LINK_PERSONAL_ACCOUNT).click()

    def info_text_for_authorization_in_user_status_disabled(self, language):  # инфо текст при авторизации в статусе пользователя "Отключен"
        info_text = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if language == "/ua":
            assert "Користувач ще не активований. Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Пользователь еще не активирован. Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "The user has not yet been activated. To complete the activation of your account, follow the link in the letter that was sent to your e-mail." == info_text, 'Не верное сообщение'

    def info_text_for_authorization_in_user_status_on_moderation(self, language):  # инфо текст при авторизации в статусе пользователя "На модерации"
        info_text = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if language == "/ua":
            assert "Модерація вашого облікового запису завершиться впродовж 24 годин" == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Модерация вашего аккаунта завершится в течение 24 часов." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your account will be moderated within 24 hours." == info_text, 'Не верное сообщение'
