from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import MyResponsesPageLocators


class MyResponsesPage(BasePage):
    def go_to_vacancy_page_of_response(self):  # нажатие на блок вакансии отклика для перехода на ее страницу
        vacancy_locator = MyResponsesPageLocators()
        vacancy = vacancy_locator.assembly_of_locators_with_id_vacancies()
        self.browser.find_element(*vacancy).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
