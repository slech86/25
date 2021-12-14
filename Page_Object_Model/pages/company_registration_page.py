from .base_page import BasePage
from .locators import CompanyRegistrationPageLocators
from Page_Object_Model.data_for_testing import TestData
import time
import os


class CompanyRegistrationPage(BasePage):
    def filling_in_required_fields(self):  # заполнение обязательных полей
        if "/ua" in self.browser.current_url:
            self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LOGIN).send_keys(TestData.login_ua)
        else:
            self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LOGIN).send_keys(TestData.login_ru)

        if "/ua" in self.browser.current_url:
            self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_EMAIL).send_keys(TestData.email_ua)
        else:
            self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_EMAIL).send_keys(TestData.email_ru)

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_REPEAT_PASSWORD).send_keys(TestData.password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_NAME).send_keys('name' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_SURNAME).send_keys('surname' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_POSITION).send_keys('position' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_TELEPHONE).send_keys('+01(010)101-01-01' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CONTACT_EMAIL).send_keys('contact_email' + TestData.time_Now + TestData.email[1])
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COMPANY_NAME).send_keys('company_name' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CODE_COMPANY).send_keys('qы12345678')

        self.browser.execute_script(CompanyRegistrationPageLocators.COMPANY_ACTIVITY)  # "Сфера деятельности компании" передается параметр уже с ".click()"

        iframe = self.browser.find_element(*CompanyRegistrationPageLocators.IFRAME_CKEDITOR)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*CompanyRegistrationPageLocators.CKEDITOR)
        CKEditor.clear()
        CKEditor.send_keys("CKEditor" + TestData.time_Now)
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        self.browser.execute_script("window.scrollBy(0, 1400);")

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_SKYPE).send_keys('skype' + TestData.time_Now)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COUNTRY).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CITY).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_STREET).send_keys('street' + TestData.time_Now)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_MONTH).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_DAY).click()

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COMPANY_SITE).send_keys('http://company_site' + TestData.time_Now + '.com')

        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_VK).click()

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_FACEBOOK).send_keys('http://facebook' + TestData.time_Now + '.com')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LINKEDIN).send_keys('http://linkedin' + TestData.time_Now + '.com')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_INSTAGRAM).send_keys('http://instagram' + TestData.time_Now + '.com')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_TELEGRAM).send_keys('http://telegram' + TestData.time_Now + '.com')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_TWITTER).send_keys('http://twitter' + TestData.time_Now + '.com')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VK).send_keys('http://vk' + TestData.time_Now + '.com')

        self.browser.find_element(*CompanyRegistrationPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании
        # заполнение блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 170х85.jpg')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 1920х230.png')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO1).send_keys('https://www.youtube.com/watch?v=-8tBpQi5cto')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO2).send_keys('https://www.youtube.com/watch?v=ZsMKc7EecNs')
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_VIDEO_ADD).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO3).send_keys('https://www.youtube.com/watch?v=kCunPyM8AQ0')
        # заполнение блока "Видео"

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_SUBMIT).click()
        time.sleep(12)
