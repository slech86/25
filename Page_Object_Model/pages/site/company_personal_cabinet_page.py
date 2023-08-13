from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import CompanyPersonalCabinetPageLocators


class CompanyPersonalCabinetPage(BasePage):
    def go_to_my_vacancies_page(self):  # переход на страницу "Мои вакансии"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.MY_VACANCIES).click()

    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.PERSONAL_DATA).click()

    def go_to_services_and_prices_page(self):  # переход на страницу "Услуги и цены"
        self.browser.find_element(*CompanyPersonalCabinetPageLocators.SERVICES_AND_PRICES).click()

    def checking_opening_of_page_of_personal_office(self, language):  # проверка открытия страницы персонального кабинета
        h1 = self.browser.find_element(*CompanyPersonalCabinetPageLocators.H1).text
        if language == "":
            assert h1 == 'Личный кабинет', "Не корректный h1"
        elif language == "/ua":
            assert h1 == 'Особистий кабінет', "Не корректный h1"
        elif language == "/en":
            assert h1 == 'Personal Account', "Не корректный h1"
        elif language == "/pl":
            assert h1 == 'Personal Account', "Не корректный h1"
