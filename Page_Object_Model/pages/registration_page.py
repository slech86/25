from .base_page import BasePage
from .locators import RegistrationPageLocators
import time
import os

time_Now = str(int(time.time()))
login = 'testLogin_' + time_Now
password = 'password' + time_Now
email = ['test_automation+', '@smileexpo.com.ua']

class RegistrationPage(BasePage):
    def filling_in_required_fields(self):  # заполнение обязательных полей
        if "ua" in self.browser.current_url:
            self.browser.find_element(*RegistrationPageLocators.FIELD_LOGIN).send_keys(login + 'ua')
        else:
            self.browser.find_element(*RegistrationPageLocators.FIELD_LOGIN).send_keys(login)

        if "ua" in self.browser.current_url:
            self.browser.find_element(*RegistrationPageLocators.FIELD_EMAIL).send_keys(email[0] + time_Now + 'ua' + email[1])
        else:
            self.browser.find_element(*RegistrationPageLocators.FIELD_EMAIL).send_keys(email[0] + time_Now + email[1])

        self.browser.find_element(*RegistrationPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.FIELD_REPEAT_PASSWORD).send_keys(password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*RegistrationPageLocators.FIELD_NAME).send_keys('name' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_SURNAME).send_keys('surname' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_POSITION).send_keys('position' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_TELEPHONE).send_keys('+01(010)101-01-01' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_CONTACT_EMAIL).send_keys('contact_email' + time_Now + email[1])
        # заполнение блока "Контактная информация"

        self.browser.find_element(*RegistrationPageLocators.FIELD_COMPANY_NAME).send_keys('company_name' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_CODE_COMPANY).send_keys('qы12345678')

        self.browser.execute_script(RegistrationPageLocators.COMPANY_ACTIVITY)  # "Сфера деятельности компании" передается параметр уже с ".click()"

        iframe = self.browser.find_element(*RegistrationPageLocators.IFRAME_CKEDITOR)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*RegistrationPageLocators.CKEDITOR)
        CKEditor.clear()
        CKEditor.send_keys("CKEditor" + time_Now)
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        self.browser.execute_script("window.scrollBy(0, 1400);")

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*RegistrationPageLocators.FIELD_SKYPE).send_keys('skype' + time_Now)
        # заполнение блока "Контактная информация"

        self.browser.find_element(*RegistrationPageLocators.FIELD_COUNTRY).click()
        self.browser.find_element(*RegistrationPageLocators.FIELD_CITY).click()
        self.browser.find_element(*RegistrationPageLocators.FIELD_STREET).send_keys('street' + time_Now)
        self.browser.find_element(*RegistrationPageLocators.FIELD_YEAR).click()
        self.browser.find_element(*RegistrationPageLocators.FIELD_MONTH).click()
        self.browser.find_element(*RegistrationPageLocators.FIELD_DAY).click()

        self.browser.find_element(*RegistrationPageLocators.FIELD_COMPANY_SITE).send_keys('http://company_site' + time_Now + '.com')

        self.browser.find_element(*RegistrationPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_VK).click()

        self.browser.find_element(*RegistrationPageLocators.FIELD_FACEBOOK).send_keys('http://facebook' + time_Now + '.com')
        self.browser.find_element(*RegistrationPageLocators.FIELD_LINKEDIN).send_keys('http://linkedin' + time_Now + '.com')
        self.browser.find_element(*RegistrationPageLocators.FIELD_INSTAGRAM).send_keys('http://instagram' + time_Now + '.com')
        self.browser.find_element(*RegistrationPageLocators.FIELD_TELEGRAM).send_keys('http://telegram' + time_Now + '.com')
        self.browser.find_element(*RegistrationPageLocators.FIELD_TWITTER).send_keys('http://twitter' + time_Now + '.com')
        self.browser.find_element(*RegistrationPageLocators.FIELD_VK).send_keys('http://vk' + time_Now + '.com')

        self.browser.find_element(*RegistrationPageLocators.NUMBER_OF_COMPANY_EMPLOYEES).click()  # Количество сотрудников компании
        # заполнение блока "Информация о компании"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 170х85.jpg')
        self.browser.find_element(*RegistrationPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 1920х230.png')
        self.browser.find_element(*RegistrationPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"

        self.browser.find_element(*RegistrationPageLocators.FIELD_VIDEO1).send_keys('https://www.youtube.com/watch?v=-8tBpQi5cto')
        self.browser.find_element(*RegistrationPageLocators.FIELD_VIDEO2).send_keys('https://www.youtube.com/watch?v=ZsMKc7EecNs')
        self.browser.find_element(*RegistrationPageLocators.BUTTON_VIDEO_ADD).click()
        self.browser.find_element(*RegistrationPageLocators.FIELD_VIDEO3).send_keys('https://www.youtube.com/watch?v=kCunPyM8AQ0')
        # заполнение блока "Видео"

    def submitting_form_for_registration(self):  # отправка формы на регистрацию
        self.browser.find_element(*RegistrationPageLocators.BUTTON_SUBMIT).click()
