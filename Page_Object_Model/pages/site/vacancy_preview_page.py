from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyPreviewPageLocators


class VacancyPreviewPage(BasePage):
    def checking_for_preview_page_to_open(self, job_title_vacancy):  # проверка открытия страницы предпросмотра
        text_h1 = self.browser.find_element(*VacancyPreviewPageLocators.H1).text
        assert text_h1 == job_title_vacancy, f"Не верный h1, expected result: '{job_title_vacancy}', actual result: '{text_h1}'"
        self.browser.switch_to.window(self.browser.window_handles[0])
