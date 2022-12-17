from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import CompanyRegistrationEditPageLocators
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyEditPage(BasePage):
    def hiding_copy_to_other_languages(self):  # скрытие кнопки "Скопировать на другие языки"
        self.browser.find_element(*CompanyRegistrationEditPageLocators.CROSS_IN_COPY_TO_OTHER_LANGUAGES).click()

    def change_data_in_all_fields(self, language):  # изменение данных во всех полях
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_SURNAME).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_POSITION).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_PHONE).send_keys(TestDataEditing.phone)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_CONTACT_EMAIL).send_keys('editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        # редактирование блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_NAME).send_keys('_editing')

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).click()
        time.sleep(1)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).send_keys(TestDataEditing.company_slug)

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_CODE_COMPANY).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_CODE_COMPANY).send_keys(TestDataEditing.code_company)

        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*CompanyRegistrationEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '122')  # 122 - id Казахстан

        locator_with_position_country = CompanyRegistrationEditPageLocators()
        country_kazakhstan = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_kazakhstan).click()

        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.2)
        city_list = self.browser.find_elements(*CompanyRegistrationEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '609655')  # 609655 - id Караганда

        locator_with_position_city = CompanyRegistrationEditPageLocators()
        city_karaganda = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_karaganda).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute((CompanyRegistrationEditPageLocators.DROPDOWN_CITI), 'aria-expanded', 'false'))

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_STREET).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.YEAR_1991).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.MONTH_MARCH).click()
        time.sleep(0.5)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DAY_17).click()

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SITE).send_keys('_editing')

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_FACEBOOK).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_LINKEDIN).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_INSTAGRAM).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_TELEGRAM).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_TWITTER).send_keys('_editing')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VK).send_keys('_editing')

        self.browser.find_element(*CompanyRegistrationEditPageLocators.COMPANY_ACTIVITY_GAMBLING).click()  # "Сфера деятельности компании"
        self.browser.find_element(*CompanyRegistrationEditPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании

        iframe = self.browser.find_element(*CompanyRegistrationEditPageLocators.IFRAME_CKEDITOR_COMPANY_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*CompanyRegistrationEditPageLocators.CKEDITOR_COMPANY_DESCRIPTION)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # редактирование блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 2 170х85.png')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 2 1920х230.jpg')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COVER).send_keys(file_path)
        # редактирование блока "Оформление профиля"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_1).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_1).send_keys(TestDataEditing.video_1)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_2).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_2).send_keys(TestDataEditing.video_2)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_3).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_3).send_keys(TestDataEditing.video_3)
        # редактирование блока "Видео"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL).click()
        if language == "/ua":
            self.browser.find_element(*CompanyRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU).click()
        elif language == "":
            self.browser.find_element(*CompanyRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_EN).click()
        elif language == "/en":
            self.browser.find_element(*CompanyRegistrationEditPageLocators.LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA).click()
        # редактирование блока "Настройки"

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_PREVIEW).click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def submitting_form_for_moderation_after_changing_data(self):  # отправка формы на модерацию после изменения данных
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_SUBMIT).click()

    def checking_message_after_saving_changes_to_personal_information(self, language):  # проверка сообщения после сохранения изменений личной информации
        infoText = self.browser.find_element(*CompanyRegistrationEditPageLocators.INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION).text
        if language == "":
            assert "Редактирование информации о вашей компании принято и отправлено на модерацию. Обновленная информация будет доступна на сайте в течение 24 часов." == infoText, 'Не верное сообщение'
        elif language == "/ua":
            assert "Редагування інформації про вашу компанію прийнято та відправлено на модерацію. Оновлена інформація буде доступна на сайті протягом 24 годин." == infoText, 'Не верное сообщение'
        elif language == "/en":
            assert "Editing information about your company is accepted and sent for moderation. Updated information will be available on the site within 24 hours." == infoText, 'Не верное сообщение'
        self.browser.find_element(*CompanyRegistrationEditPageLocators.CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION).click()
