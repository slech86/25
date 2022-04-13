from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerRegistrationPageLocators
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.singleton import Singleton


class JobSeekerRegistrationPage(BasePage):
    def filling_in_all_fields(self, language, key):  # заполнение всех полей
        login_and_mail = TestData()
        login_and_mail.login_and_mail_generation(key)
        if language == "/ua":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][1][0])
        elif language == "":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][0][0])
        elif language == "/en":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key][2][0])

        if language == "/ua":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_EMAIL).send_keys(Singleton.logins_and_mails[key][1][1])
        elif language == "":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_EMAIL).send_keys(Singleton.logins_and_mails[key][0][1])
        elif language == "/en":
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_EMAIL).send_keys(Singleton.logins_and_mails[key][2][1])

        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_REPEAT_PASSWORD).send_keys(TestData.password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_NAME).send_keys(TestData.name)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_SURNAME).send_keys(TestData.surname)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_MONTH).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_DAY).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_GENDER).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_COUNTRY).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_CITY).click()
        # заполнение блока "Личная информация"

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*JobSeekerRegistrationPageLocators.BUTTON_SUBMIT).click()
