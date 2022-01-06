from .base_page import BasePage
from .locators import CompanyEditPageLocators
from Page_Object_Model.data_for_testing import TestData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

class CompanyEditPage(BasePage):
    def change_data_in_all_fields(self):  # изменение данных во всех полях
        self.browser.find_element(*CompanyEditPageLocators.BUTTON_EDIT_IN_CONTACT_INFORMATION_BLOCK).click()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_SURNAME).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_POSITION).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_TELEPHONE).clear()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_TELEPHONE).send_keys(TestData.phone_editing)
        self.browser.find_element(*CompanyEditPageLocators.FIELD_CONTACT_EMAIL).send_keys('editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        # редактирование блока "Контактная информация"

        self.browser.find_element(*CompanyEditPageLocators.BUTTON_EDIT_IN_COMPANY_INFORMATION_BLOCK).click()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_COMPANY_NAME).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_CODE_COMPANY).clear()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_CODE_COMPANY).send_keys(TestData.code_company_editing)

        self.browser.find_element(*CompanyEditPageLocators.FIELD_COUNTRY).click()
        time.sleep(0.2)
        self.browser.find_element(*CompanyEditPageLocators.FIELD_CITY).click()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_STREET).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_MONTH).click()
        time.sleep(0.2)
        self.browser.find_element(*CompanyEditPageLocators.FIELD_DAY).click()

        self.browser.find_element(*CompanyEditPageLocators.FIELD_COMPANY_SITE).send_keys('_editing')

        self.browser.find_element(*CompanyEditPageLocators.FIELD_FACEBOOK).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_LINKEDIN).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_INSTAGRAM).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_TELEGRAM).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_TWITTER).send_keys('_editing')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VK).send_keys('_editing')

        self.browser.execute_script(CompanyEditPageLocators.COMPANY_ACTIVITY)  # "Сфера деятельности компании" передается параметр уже с ".click()"
        self.browser.find_element(*CompanyEditPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании


        iframe = self.browser.find_element(*CompanyEditPageLocators.IFRAME_CKEDITOR_COMPANY_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*CompanyEditPageLocators.CKEDITOR_COMPANY_DESCRIPTION)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 2 170х85.png')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 2 1920х230.jpg')
        self.browser.find_element(*CompanyEditPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"

        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_1).clear()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_1).send_keys(TestData.video_1_editing)
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_2).clear()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_2).send_keys(TestData.video_2_editing)
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_3).clear()
        self.browser.find_element(*CompanyEditPageLocators.FIELD_VIDEO_3).send_keys(TestData.video_3_editing)
        # заполнение блока "Видео"

        self.browser.find_element(*CompanyEditPageLocators.BUTTON_EDIT_IN_SETTINGS_BLOCK).click()
        self.browser.find_element(*CompanyEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL).click()
        self.browser.find_element(*CompanyEditPageLocators.UKRAINIAN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL).click()

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*CompanyEditPageLocators.BUTTON_SUBMIT).click()
        # time.sleep(4)

    def checking_message_after_saving_changes_to_personal_information(self):  # проверка сообщения после сохранения изменений личной информации
        infoText = self.browser.find_element(*CompanyEditPageLocators.INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION).text
        if "/ua" in self.browser.current_url:
            assert "Зміни особистої інформації збережені" == infoText, 'Не верное сообщение'
        else:
            assert "Изменения личной информации сохранены" == infoText, 'Не верное сообщение'
        self.browser.find_element(*CompanyEditPageLocators.CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION).click()
        time.sleep(30)
