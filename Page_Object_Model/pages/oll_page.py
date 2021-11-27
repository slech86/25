from .base_page import BasePage
from .locators import OllPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class OllPage(BasePage):
    def age_confirmation(self):
        WebDriverWait(self.browser, 6).until(EC.element_to_be_clickable(OllPageLocators.BUTTON_YES_WHEN_CHECKING_AGE)).click()
        time.sleep(2)
        # подтверждение возраста больше 21 года
    def opening_pop_up_for_login(self):

        self.browser.find_element(*OllPageLocators.POP_UP_FOR_LOGIN).click()
        # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    def go_to_registration_page(self):
        self.browser.find_element(*OllPageLocators.REGISTRATION_LINK).click()
        # нажатие на кнопку для перехона на страницу регистрации
