from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.locators import VacanciesPageLocators
from Page_Object_Model.elements.button import Button
# /vacancy


class VacanciesPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.button = Button()

    def search_vacancy_by_job_title(self, job_title_vacancy):  # поиск вакансии по названию
        self.browser.find_element(*VacanciesPageLocators.FIELD_JOB_TITLE_TO_SEARCH).send_keys(job_title_vacancy)
        self.browser.find_element(*VacanciesPageLocators.BUTTON_SEARCH).click()

    def go_to_first_vacancy_page_in_list(self):  # нажатие на блок первой вакансии в списке для перехода на ее страницу
        self.browser.find_element(*VacanciesPageLocators.FIRST_VACANCY_IN_LIST).click()

    def add_vacancy_to_bookmarks(self, browser):  # добавить вакансию в закладки (первую в списке)
        self.button.button_type_button_click_by_label(browser, 'Bookmark Vacancy')

    def go_to_vacancy_page(self, vacancy_id):  # нажатие на блок вакансии для перехода на ее страницу
        vacancy_locator = VacanciesPageLocators()
        vacancy = vacancy_locator.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*vacancy).click()
