from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import MyResponsesPageLocators


class MyResponsesPage(BasePage):
    def go_to_vacancy_page_of_response(self, vacancy_id):  # нажатие на блок вакансии отклика для перехода на ее страницу
        vacancy_locator = MyResponsesPageLocators()
        locators = vacancy_locator.assembly_of_locators_with_id_vacancies(vacancy_id)
        self.browser.find_element(*locators['block_vacancy']).click()
        self.browser.switch_to.window(self.browser.window_handles[1])

    def checking_status_display_in_response_block(self, vacancy_id, status):  # проверка отображения статуса в блоке отклика
        locators_with_id_vacancies = MyResponsesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        status_text = self.browser.find_element(*locators['status_response']).text
        assert status == status_text, 'Не верный статус отклика'

    def deleting_response(self, vacancy_id):  # удаление отклика
        vacancy_locator = MyResponsesPageLocators()
        locators = vacancy_locator.assembly_of_locators_with_id_vacancies(vacancy_id)
        self.browser.find_element(*locators['button_delete']).click()
        assert self.is_disappeared(*locators['block_vacancy']), "Не должно быть блока вакансии"