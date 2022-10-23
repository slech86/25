from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import ResumePreviewPageLocators


class ResumePreviewPage(BasePage):
    def checking_for_preview_page_to_open(self, job_title_resume):  # проверка открытия страницы предпросмотра
        text_h1 = self.browser.find_element(*ResumePreviewPageLocators.H1).text
        assert text_h1 == job_title_resume, f"Не верный h1, expected result: '{job_title_resume}', actual result: '{text_h1}'"
        self.browser.switch_to.window(self.browser.window_handles[0])
