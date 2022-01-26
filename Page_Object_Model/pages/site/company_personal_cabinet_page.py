from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import CompanyPersonalCabinetPageLocators


class CompanyPersonalCabinetPage(BasePage):
    def go_to_my_vacancies_page(self):  # переход на страницу "Мои вакансии"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.MY_VACANCIES).click()

    def go_to_services_and_prices_page(self):  # переход на страницу "Услуги и цены"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.SERVICES_AND_PRICES).click()

    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.PERSONAL_DATA).click()
