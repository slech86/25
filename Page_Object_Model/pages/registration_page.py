from .base_page import BasePage
from .locators import RegistrationPageLocators
import time
import os

timeNow = str(int(time.time()))
login = 'testLogin_' + timeNow
password = 'password' + timeNow
email = ['test.p.verbenec+', '@gmail.com']

class RegistrationPage(BasePage):
    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*RegistrationPageLocators.FIELD_LOGIN).send_keys(login)
        self.browser.find_element(*RegistrationPageLocators.FIELD_EMAIL).send_keys(email[0] + timeNow + email[1])
        self.browser.find_element(*RegistrationPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.FIELD_REPEAT_PASSWORD).send_keys(password)
        # заполнение блока "Данные для авторизации"

        self.browser.find_element(*RegistrationPageLocators.FIELD_NAME).send_keys('name' + timeNow)
        self.browser.find_element(*RegistrationPageLocators.FIELD_SURNAME).send_keys('surname' + timeNow)
        self.browser.find_element(*RegistrationPageLocators.FIELD_POSITION).send_keys('position' + timeNow)
        self.browser.find_element(*RegistrationPageLocators.FIELD_TELEPHONE).send_keys('+01(010)101-01-01' + timeNow)
        self.browser.find_element(*RegistrationPageLocators.FIELD_CONTACT_EMAIL).send_keys('contact_email' + timeNow + email[1])

        self.browser.find_element(*RegistrationPageLocators.FIELD_COMPANY_NAME).send_keys('company_name' + timeNow)
        self.browser.find_element(*RegistrationPageLocators.FIELD_CODE_COMPANY).send_keys('qы12345678')

        self.browser.execute_script(RegistrationPageLocators.COMPANY_ACTIVITY)  # передается параметр уже с ".click()"

        iframe = self.browser.find_element(*RegistrationPageLocators.IFRAME)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*RegistrationPageLocators.CKEDITOR)
        CKEditor.clear()
        CKEditor.send_keys("CKEditor" + timeNow)
        self.browser.switch_to.default_content()  # выход из фрейма
        # ввод данных в CKEditor (поле " Описание компании")
        # заполнение блока "Информация о компании"

        self.browser.execute_script("window.scrollBy(0, 1400);")
        # self.browser.find_element(*RegistrationPageLocators.BUTTON_SUBMIT).click()
        time.sleep(3)

    def filling_in_optional_fields(self):  # заполнение не обязательных полей


        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'логотип 170х85.jpg')
        self.browser.find_element(*RegistrationPageLocators.FIELD_LOGO).send_keys(file_path)

        file_path = os.path.join(current_dir, 'обложка 1920х230.png')
        self.browser.find_element(*RegistrationPageLocators.FIELD_COVER).send_keys(file_path)
        # заполнение блока "Оформление профиля"