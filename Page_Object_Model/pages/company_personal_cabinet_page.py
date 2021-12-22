from .base_page import BasePage
from .locators import CompanyPersonalCabinetPageLocators

class CompanyPersonalCabinetPage(BasePage):
    def go_to_my_vacancies_page(self):  # переход на страницу "Мои вакансии"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.BUTTON_MY_VACANCIES).click()

    def go_to_services_and_prices_page(self):  # переход на страницу "Услуги и цены"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.BUTTON_SERVICES_AND_PRICES).click()
