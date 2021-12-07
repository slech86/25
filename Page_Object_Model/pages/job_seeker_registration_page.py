from .base_page import BasePage
from .locators import JobSeekerRegistrationPageLocators
from Page_Object_Model.data_for_testing import TestData
import time



class JobSeekerRegistrationPage(BasePage):
    def filling_in_all_fields(self):  # заполнение всех полей
        if "ua" in self.browser.current_url:
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_LOGIN).send_keys(TestData.login_ua)
        else:
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_LOGIN).send_keys(TestData.login_ru)

        if "ua" in self.browser.current_url:
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_EMAIL).send_keys(TestData.email_ua)
        else:
            self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_EMAIL).send_keys(TestData.email_ru)

        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_REPEAT_PASSWORD).send_keys(TestData.password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_NAME).send_keys('name' + TestData.time_Now)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_SURNAME).send_keys('surname' + TestData.time_Now)
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_MONTH).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_DAY).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_GENDER).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_COUNTRY).click()
        self.browser.find_element(*JobSeekerRegistrationPageLocators.FIELD_CITY).click()
        # заполнение блока "Личная информация"

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*JobSeekerRegistrationPageLocators.BUTTON_SUBMIT).click()
        time.sleep(12)
