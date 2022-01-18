from .base_page import BasePage
from .locators import VacancyPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing, Accounts



class VacancyPage(BasePage):
    def checking_opening_of_page_of_an_unpublished_vacancy(self, language):  # проверка открытия страницы не опубликованой вакансии
        h1 = self.browser.find_element(*VacancyPageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Пошук завершено', "Не корректный h1"
        else:
            assert h1 == 'Поиск завершен', "Не корректный h1"

    def checking_opening_of_page_of_published_vacancy(self):  # проверка открытия страницы опубликованой вакансии
        h1 = self.browser.find_element(*VacancyPageLocators.H1).text
        assert h1 == TestData.job_title, "Вакансия не опубликована"
