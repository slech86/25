from .base_page import BasePage
from .locators import JobSeekerPersonalCabinetPageLocators

class JobSeekerPersonalCabinetPage(BasePage):
    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.PERSONAL_DATA).click()
