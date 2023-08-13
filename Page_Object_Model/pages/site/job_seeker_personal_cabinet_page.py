from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import JobSeekerPersonalCabinetPageLocators


class JobSeekerPersonalCabinetPage(BasePage):
    def go_to_my_resume_page(self):  # переход на страницу "Мои резюме"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.MY_RESUME).click()

    def go_to_my_responses_page(self):  # переход на страницу "Мои отклики"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.MY_RESPONSES).click()

    def go_to_personal_data_page(self):  # переход на страницу "Личные данные"
        self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.PERSONAL_DATA).click()

    def checking_opening_of_page_of_personal_office(self, language):  # проверка открытия страницы персонального кабинета
        h1 = self.browser.find_element(*JobSeekerPersonalCabinetPageLocators.H1).text
        if language == "":
            assert h1 == 'Личный кабинет', "Не корректный h1"
        elif language == "/ua":
            assert h1 == 'Особистий кабінет', "Не корректный h1"
        elif language == "/en":
            assert h1 == 'Personal Account', "Не корректный h1"
        elif language == "/pl":
            assert h1 == 'Personal Account', "Не корректный h1"
