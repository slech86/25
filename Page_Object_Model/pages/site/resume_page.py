from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import ResumePageLocators
from Page_Object_Model.data_for_testing import TestData


class ResumePage(BasePage):
    def checking_opening_of_page_of_an_unpublished_resume(self, language):  # проверка открытия страницы не опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Резюме приховано', "Не корректный h1"
        else:
            assert h1 == 'Резюме скрыто', "Не корректный h1"

    def checking_opening_of_page_of_published_resume(self):  # проверка открытия страницы опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == TestData.job_title_resume, "Резюме не опубликована"