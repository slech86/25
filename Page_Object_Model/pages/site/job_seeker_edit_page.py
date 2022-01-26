from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerEditPageLocators
import time


class JobSeekerEditPage(BasePage):
    def change_data_in_all_fields(self, language):  # изменение данных во всех полях
        self.browser.find_element(*JobSeekerEditPageLocators.BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK).click()
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_SURNAME).send_keys('_editing')
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_MONTH).click()
        time.sleep(0.2)
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_DAY).click()
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_GENDER).click()
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_COUNTRY).click()
        time.sleep(0.2)
        self.browser.find_element(*JobSeekerEditPageLocators.FIELD_CITY).click()
        # редактирование блока "Личная информация"

        self.browser.find_element(*JobSeekerEditPageLocators.BUTTON_EDIT_IN_SETTINGS_BLOCK).click()
        self.browser.find_element(*JobSeekerEditPageLocators.DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL).click()
        if language == "/ua":
            self.browser.find_element(*JobSeekerEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU).click()
        else:
            self.browser.find_element(*JobSeekerEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA).click()
        # редактирование блока "Настройки"

    def saving_data_after_modification(self):  # сохранение данных после изменений
        self.browser.find_element(*JobSeekerEditPageLocators.BUTTON_SAVE_CHANGES).click()

    def checking_message_after_saving_changes_to_personal_information(self):  # проверка сообщения после сохранения изменений личной информации
        infoText = self.browser.find_element(*JobSeekerEditPageLocators.INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION).text
        if "/ua" in self.browser.current_url:
            assert "Зміни особистої інформації збережені" == infoText, 'Не верное сообщение'
        else:
            assert "Изменения личной информации сохранены" == infoText, 'Не верное сообщение'
        self.browser.find_element(*JobSeekerEditPageLocators.CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION).click()