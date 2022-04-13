from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerPersonalCabinetPageLocators


class JobSeekerPersonalCabinetPage(BasePage):
    def go_to_my_resume_page(self):  # переход на страницу "Мои резюме"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.MY_RESUME).click()

    def go_to_my_responses_page(self):  # переход на страницу "Мои отклики"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.MY_RESPONSES).click()

    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.PERSONAL_DATA).click()
