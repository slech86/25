from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import ResumesPageLocators


class ResumesPage(BasePage):
    def search_resume_by_job_title(self, job_title_resume):  # поиск резюме по названию
        self.browser.find_element(*ResumesPageLocators.FIELD_JOB_TITLE_TO_SEARCH).send_keys(job_title_resume)
        self.browser.find_element(*ResumesPageLocators.BUTTON_SEARCH).click()

    def go_to_first_resume_page_in_list(self):  # нажатие на блок первого резюме в списке для перехода на его страницу
        self.browser.find_element(*ResumesPageLocators.FIRST_RESUME_IN_LIST).click()

    def go_to_resume_page(self, id_resume):  # нажатие на блок резюме для перехода на его страницу
        resume_locator = ResumesPageLocators()
        resume = resume_locator.assembly_of_locators_with_id_resume(id_resume)  # сборка локаторов с id резюме
        self.browser.find_element(*resume).click()
