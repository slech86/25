from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.pages.locators import JobSeekerPersonalCabinetPageLocators

class JobSeekerPersonalCabinetPage(BasePage):
    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.PERSONAL_DATA).click()
