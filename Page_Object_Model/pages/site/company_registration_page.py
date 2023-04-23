import time
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import CompanyRegistrationEditPageLocators
from Page_Object_Model.data_for_testing import TestData
import os
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyRegistrationPage(BasePage):
    def hiding_copy_to_other_languages(self):  # скрытие кнопки "Скопировать на другие языки"
        self.browser.find_element(*CompanyRegistrationEditPageLocators.CROSS_IN_COPY_TO_OTHER_LANGUAGES).click()

    def filling_in_required_fields(self, key):  # заполнение обязательных полей
        login_and_mail = TestData()
        login_and_mail.login_and_mail_generation(key)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_LOGIN).send_keys(Singleton.logins_and_mails[key]['login'])
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_EMAIL).send_keys(Singleton.logins_and_mails[key]['email'])

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_PASSWORD).send_keys(TestData.password)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_REPEAT_PASSWORD).send_keys(TestData.password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_NAME).send_keys(TestData.name)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_SURNAME).send_keys(TestData.surname)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_POSITION).send_keys(TestData.position)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_PHONE).send_keys(TestData.phone)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_CONTACT_EMAIL).send_keys(TestData.contact_email)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_NAME).send_keys(TestData.company_name)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).click()
        time.sleep(1)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).clear()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SLUG).send_keys(TestData.company_slug)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_CODE_COMPANY).send_keys(TestData.code_company)

        self.browser.find_element(*CompanyRegistrationEditPageLocators.COMPANY_ACTIVITY_FINANCE).click()  # "Сфера деятельности компании" передается параметр уже с ".click()"

        iframe = self.browser.find_element(*CompanyRegistrationEditPageLocators.IFRAME_CKEDITOR_COMPANY_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*CompanyRegistrationEditPageLocators.CKEDITOR_COMPANY_DESCRIPTION)
        # CKEditor.clear()
        CKEditor.send_keys(TestData.ckeditor_company_description)
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        self.browser.execute_script("window.scrollBy(0, 1400);")

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        time.sleep(3)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_PREVIEW).click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_SKYPE).send_keys(TestData.skype)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*CompanyRegistrationEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = CompanyRegistrationEditPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*CompanyRegistrationEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '703448')  # 703448 - id Kyiv

        locator_with_position_city = CompanyRegistrationEditPageLocators()
        city_kyiv = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_kyiv).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(CompanyRegistrationEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_STREET).send_keys(TestData.street)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.YEAR_2019).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.MONTH_DECEMBER).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.DAY_31).click()

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COMPANY_SITE).send_keys(TestData.company_site)

        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_VK).click()

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_FACEBOOK).send_keys(TestData.facebook)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_LINKEDIN).send_keys(TestData.linkedin)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_INSTAGRAM).send_keys(TestData.instagram)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_TWITTER).send_keys(TestData.twitter)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VK).send_keys(TestData.vk)

        self.browser.find_element(*CompanyRegistrationEditPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании
        # заполнение блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 170х85.jpg')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 1920х230.png')
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"

        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_1).send_keys(TestData.video_1)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_VIDEO_ADD).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_2).send_keys(TestData.video_2)
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_VIDEO_ADD_2).click()
        self.browser.find_element(*CompanyRegistrationEditPageLocators.FIELD_VIDEO_3).send_keys(TestData.video_3)
        # заполнение блока "Видео"

        checkbox_get_news = self.browser.find_element(*CompanyRegistrationEditPageLocators.CHECKBOX_GET_NEWS)
        checkbox_get_news_checked = checkbox_get_news.get_attribute("checked")
        assert checkbox_get_news_checked is not None, "Не установлено получение новостей по умолчанию"


    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*CompanyRegistrationEditPageLocators.BUTTON_SUBMIT).click()
