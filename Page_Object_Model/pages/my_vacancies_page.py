from .base_page import BasePage
from .locators import MyVacanciesPageLocators


class MyVacanciesPage(BasePage):
    def go_to_add_vacancy_page(self):  # переход на страницу "Добавить вакансию"
        self.browser.find_element(*MyVacanciesPageLocators.BUTTON_ADD_VACANCY).click()
