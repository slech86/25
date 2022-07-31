from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import CompanyPreviewPageLocators


class CompanyPreviewPage(BasePage):
    def checking_for_preview_page_to_open(self, company_name):  # проверка открытия страницы предпросмотра
        text_h1 = self.browser.find_element(*CompanyPreviewPageLocators.H1).text
        assert text_h1 == company_name, f"Не верный h1, expected result: '{company_name}', actual result: '{text_h1}'"
        self.browser.switch_to.window(self.browser.window_handles[0])
