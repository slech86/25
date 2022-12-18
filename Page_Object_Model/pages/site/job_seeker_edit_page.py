from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerRegistrationEditPageLocators
import time
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class JobSeekerEditPage(BasePage):
    def change_data_in_all_fields(self, language):  # изменение данных во всех полях
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_SURNAME).send_keys('_editing')
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.YEAR_2001).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.MONTH_JANUARY).click()
        time.sleep(0.2)
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DAY_1).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.FIELD_GENDER_MALE).click()

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*JobSeekerRegistrationEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '122')  # 122 - id Казахстан

        locator_with_position_country = JobSeekerRegistrationEditPageLocators()
        country_kazakhstan = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_kazakhstan).click()

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*JobSeekerRegistrationEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '609655')  # 609655 - id Караганда

        locator_with_position_city = JobSeekerRegistrationEditPageLocators()
        city_karaganda = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_karaganda).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute((JobSeekerRegistrationEditPageLocators.DROPDOWN_CITI), 'aria-expanded', 'false'))
        # редактирование блока "Личная информация"

        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.BUTTON_EDIT_IN_SETTINGS_BLOCK).click()
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL).click()
        if language == "/ua":
            self.browser.find_element(*JobSeekerRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU).click()
        elif language == "":
            self.browser.find_element(*JobSeekerRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_EN).click()
        elif language == "/en":
            self.browser.find_element(*JobSeekerRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA).click()
        # редактирование блока "Настройки"

    def saving_data_after_modification(self):  # сохранение данных после изменений
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.BUTTON_SUBMIT).click()

    def checking_message_after_saving_changes_to_personal_information(self, language):  # проверка сообщения после сохранения изменений личной информации
        info_text = self.browser.find_element(*JobSeekerRegistrationEditPageLocators.INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION).text
        if language == "/ua":
            assert "Зміни особистої інформації збережені" == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Изменения личной информации сохранены" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Changes to personal information saved" == info_text, 'Не верное сообщение'
        self.browser.find_element(*JobSeekerRegistrationEditPageLocators.CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION).click()