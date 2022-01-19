from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.pages.locators import CompanyRegistrationPageLocators
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

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_NAME).send_keys(TestData.name)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_SURNAME).send_keys(TestData.surname)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_POSITION).send_keys(TestData.position)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_PHONE).send_keys(TestData.phone)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CONTACT_EMAIL).send_keys(TestData.contact_email)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COMPANY_NAME).send_keys(TestData.company_name)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CODE_COMPANY).send_keys(TestData.code_company)

        self.browser.execute_script(CompanyRegistrationPageLocators.COMPANY_ACTIVITY)  # "Сфера деятельности компании" передается параметр уже с ".click()"

        iframe = self.browser.find_element(*CompanyRegistrationPageLocators.IFRAME_CKEDITOR_COMPANY_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*CompanyRegistrationPageLocators.CKEDITOR_COMPANY_DESCRIPTION)
        # CKEditor.clear()
        CKEditor.send_keys(TestData.ckeditor_company_description)
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        self.browser.execute_script("window.scrollBy(0, 1400);")

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_SKYPE).send_keys(TestData.skype)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COUNTRY).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_CITY).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_STREET).send_keys(TestData.street)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_MONTH).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_DAY).click()

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COMPANY_SITE).send_keys(TestData.company_site)

        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_VK).click()

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_FACEBOOK).send_keys(TestData.facebook)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LINKEDIN).send_keys(TestData.linkedin)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_INSTAGRAM).send_keys(TestData.instagram)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_TWITTER).send_keys(TestData.twitter)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VK).send_keys(TestData.vk)

        self.browser.find_element(*CompanyRegistrationPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании
        # заполнение блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 170х85.jpg')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 1920х230.png')
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"

        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO_1).send_keys(TestData.video_1)
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO_2).send_keys(TestData.video_2)
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_VIDEO_ADD).click()
        self.browser.find_element(*CompanyRegistrationPageLocators.FIELD_VIDEO_3).send_keys(TestData.video_3)
        # заполнение блока "Видео"

        checkbox_get_news = self.browser.find_element(*CompanyRegistrationPageLocators.CHECKBOX_GET_NEWS)
        checkbox_get_news_checked = checkbox_get_news.get_attribute("checked")
        assert checkbox_get_news_checked is not None, "Не установлено получение новостей по умолчанию"


    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*CompanyRegistrationPageLocators.BUTTON_SUBMIT).click()
