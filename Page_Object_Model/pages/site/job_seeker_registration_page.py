import time
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerRegistrationEditPageLocators
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobSeekerRegistrationPage(BasePage):
    def filling_in_all_fields(self, key):  # заполнение всех полей
        login_and_mail = TestData()
        login_and_mail.login_and_mail_generation(key)
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key]['login'])

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_EMAIL).send_keys(Singleton.logins_and_mails[key]['email'])

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_REPEAT_PASSWORD).send_keys(TestData.password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_NAME).send_keys(TestData.name)
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_SURNAME).send_keys(TestData.surname)
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.YEAR_1999).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.MONTH_NOVEMBER).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DAY_30).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_GENDER_FEMALE).click()

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*JobSeekerRegistrationEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = JobSeekerRegistrationEditPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(1)
        city_list = self.browser.find_elements(*JobSeekerRegistrationEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '703448')  # 703448 - id Kyiv

        locator_with_position_city = JobSeekerRegistrationEditPageLocators()
        city_kyiv = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_kyiv).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(JobSeekerRegistrationEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))
        # заполнение блока "Личная информация"

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.BUTTON_SUBMIT).click()
