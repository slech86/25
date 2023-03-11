from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import OllPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.users import users_variables
import time


class OllPage(BasePage):
    def age_confirmation(self):
        time.sleep(5)
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(OllPageLocators.BUTTON_YES_WHEN_CHECKING_AGE)).click()
        time.sleep(0.3)
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

    def clicking_on_button_forgot_password(self):  # нажатие на кнопку "Забыли пароль"
        self.browser.find_element(*OllPageLocators.BUTTON_FORGOT_PASSWORD).click()

    def submitting_password_recovery_request(self, language, user):  # отправка запроса на восстановление пароля
        self.browser.find_element(*OllPageLocators.FIELD_FORGOT_PASSWORD_FORM_EMAIL).send_keys(users_variables[user]["mail"])
        self.browser.find_element(*OllPageLocators.BUTTON_CHANGE_PASSWORD).click()
        info_text = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(OllPageLocators.INFO_TEXT_AFTER_PASSWORD_RESET_REQUEST)).text
        if language == "":
            expected_text = "Если адрес " + users_variables[user]["mail"] + " зарегистрирован в системе, на него будет выслано письмо."
            assert expected_text == info_text, f"Не верное сообщение, expected result: '{expected_text}', actual result: '{info_text}'"
        elif language == "/ua":
            expected_text = "Якщо адреса " + users_variables[user]["mail"] + " зареєстрована в системі, на неї буде відіслано лист."
            assert expected_text == info_text, f"Не верное сообщение, expected result: '{expected_text}', actual result: '{info_text}'"
        elif language == "/en":
            expected_text = "If " + users_variables[user]["mail"] + " is registered in the system, an email will be sent to it."
            assert expected_text == info_text, f"Не верное сообщение, expected result: '{expected_text}', actual result: '{info_text}'"

    def user_new_authorization(self, language, key):  # авторизация нового пользователя
        if language == "":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key]['ru']['login_ru'])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')
        elif language == "/ua":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key]['ua']['login_ua'])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')
        elif language == "/en":
            self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key]['en']['login_en'])
            # self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys('p.verbenets')

        self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        # self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys('l6FOt9tvJT')

        self.browser.find_element(*OllPageLocators.BUTTON_LOG_IN).click()
        time.sleep(2)

    def user_authorization(self, user, login=None, password=None):  # авторизация пользователя
        if login is None:
            login = users_variables[user]["login"]
        if password is None:
            password = users_variables[user]["password"]

        self.browser.find_element(*OllPageLocators.FIELD_LOGIN).send_keys(login)
        self.browser.find_element(*OllPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*OllPageLocators.BUTTON_LOG_IN).click()
        time.sleep(2)

    def logout(self):  # выход из учетной записи
        self.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        self.pressing_leave_button()  # нажатие на кнопку выйти
        self.browser.find_element(*OllPageLocators.BUTTON_YES_LOGOUT).click()
        self.check_for_non_authorization_of_user()  # проверка на не авторизацию пользователя

    def check_for_non_authorization_of_user(self):  # проверка на не авторизацию пользователя
        assert self.is_element_present(*OllPageLocators.BUTTON_POP_UP_FOR_LOGIN), 'Пользователь авторизирован, но не должен'

    def opening_authorized_user_menu(self):  # нажатие на кнопку для открытия меню авторизированного пользователя
        self.browser.find_element(*OllPageLocators.BUTTON_AUTHORIZED_USER).click()

    def go_to_personal_cabinet_page(self):  # нажатие на кнопку для перехода на страницу личного кабинета
        self.browser.find_element(*OllPageLocators.LINK_PERSONAL_ACCOUNT).click()

    def pressing_leave_button(self):  # нажатие на кнопку выйти
        self.browser.find_element(*OllPageLocators.BUTTON_LEAVE).click()

    def info_text_for_authorization_in_user_status_disabled(self, language):  # инфо текст при авторизации в статусе пользователя "Отключен"
        info_text = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if language == "":
            assert "Пользователь еще не активирован. Для завершения активации своего аккаунта перейдите по ссылке в письме, которое было отправлено на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Користувач ще не активований. Для завершення активації облікового запису перейдіть за посиланням у листі, який було надіслано на ваш e-mail." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "The user has not yet been activated. To complete the activation of your account, follow the link in the letter that was sent to your e-mail." == info_text, 'Не верное сообщение'

    def info_text_for_authorization_in_user_status_on_moderation(self, language):  # инфо текст при авторизации в статусе пользователя "На модерации"
        info_text = self.browser.find_element(*OllPageLocators.INFO_TEXT_IN_POP_UP_WINDOW).text
        if language == "":
            assert "Модерация вашего аккаунта завершится в течение 24 часов." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Модерація вашого облікового запису завершиться впродовж 24 годин" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your account will be moderated within 24 hours." == info_text, 'Не верное сообщение'
