from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ResumePageLocators
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.сonfiguration import UrlStartPage
from Page_Object_Model.singleton import Singleton


class ResumePage(BasePage):
    def confirmation_opening_of_vacancy_page(self, language):  # подтверждение открытия страницы вакансии
        if language == '/ua':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/resume/' + Singleton.id_resume, 'Не правильный URL'
        elif language == '':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/resume/' + Singleton.id_resume, 'Не правильный URL'
        elif language == '/en':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/resume/' + Singleton.id_resume, 'Не правильный URL'

    def checking_opening_of_page_of_an_unpublished_resume(self, language):  # проверка открытия страницы не опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Резюме приховано', "Не корректный h1"
        elif language == "":
            assert h1 == 'Резюме скрыто', "Не корректный h1"
        elif language == "/en":
            assert h1 == 'CV is hidden', "Не корректный h1"

    def checking_opening_of_page_of_published_resume(self):  # проверка открытия страницы опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == TestData.job_title_resume, "Резюме не опубликована"

    def checking_cover_letter_text(self):  # проверка текста сопроводительного письма
        cover_letter_text = self.browser.find_element(*ResumePageLocators.COVER_LETTER_TEXT).text
        assert cover_letter_text == TestData.cover_letter, "Сопроводительное письмо не совпадает"


