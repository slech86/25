from .base_page import BasePage
from .locators import UserPersonalAccountPageLocators

class UserPersonalAccountPage(BasePage):
    def go_to_services_and_prices_page(self):  # переход на страницу "Услуги и цены"
        self.browser.find_element(*UserPersonalAccountPageLocators.BUTTON_SERVICES_AND_PRICES).click()
