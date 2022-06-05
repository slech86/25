from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import InterkassaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InterkassaPage(BasePage):
    def transition_to_test_payment_page(self):  # переход на страницу тестового платежа
        self.browser.find_element(*InterkassaPageLocators.BUTTON_TEST_PAYSYSTEM).click()
        self.browser.find_element(*InterkassaPageLocators.CHECKBOX_CONSENT_WITH_INTERKASSA_RULES).click()
        WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(InterkassaPageLocators.BUTTON_PAY)).click()

    def creating_test_payment(self):  # создание тестового платежа
        self.browser.find_element(*InterkassaPageLocators.BUTTON_CREATE_TEST_PAYMENT).click()

    def create_cancel_test_payment(self):  # Создать отмененный тестовый платеж
        self.browser.find_element(*InterkassaPageLocators.BUTTON_CREATE_CANCEL_TEST_PAYMENT).click()

    def create_pending_payment(self):  # создать платеж в ожидании
        self.browser.find_element(*InterkassaPageLocators.BUTTON_PENDING).click()
