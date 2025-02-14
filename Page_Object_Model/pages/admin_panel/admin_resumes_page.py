from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminResumesPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class AdminResumesPage(BasePage):
    def resume_search_by_job_title(self, job_title):  # поиск резюме по названию должности
        self.browser.find_element(*AdminResumesPageLocators.FIELD_JOB_TITLE_SEARCH_RESUME).send_keys(job_title, Keys.ENTER)
        time.sleep(2)
        admin_resumes_page_locators = AdminResumesPageLocators()
        resume_by_job_title = admin_resumes_page_locators.assembly_of_locators_with_job_title_resume(job_title)
        assert self.is_element_present(*resume_by_job_title), 'Резюме не найдено'

    def resume_search_by_job_title_after_editing(self):  # поиск резюме по названию должности после редактирования
        self.browser.find_element(*AdminResumesPageLocators.FIELD_JOB_TITLE_SEARCH_RESUME).send_keys(TestDataEditing.job_title_resume, Keys.ENTER)
        time.sleep(2)
        assert self.is_element_present(*AdminResumesPageLocators.RESUME_BY_JOB_TITLE_AFTER_EDITING), 'Резюме не найдено'

    def getting_resume_id(self):  # получение id резюме
        id_resume = self.browser.find_element(*AdminResumesPageLocators.ID_RESUME).text
        return id_resume

    def get_status_of_resume(self):  # получить статус резюме
        status = self.browser.find_element(*AdminResumesPageLocators.RESUME_STATUS).text
        return status

    def checking_that_resume_status_is_on_moderated(self):  # проверка что статус резюме 'На модерацию'
        status = self.browser.find_element(*AdminResumesPageLocators.RESUME_STATUS).text
        assert status == 'На модерацию', 'Статус не "На модерацию"'

    def checking_that_resume_status_is_draft(self):  # проверка что статус резюме 'Черновик'
        status = self.browser.find_element(*AdminResumesPageLocators.RESUME_STATUS).text
        assert status == 'Черновик', f"Не верный статус, expected result: 'Черновик', actual result: '{status}'"

    def checking_that_resume_status_is_deleted(self):  # проверка что статус резюме 'Удалено'
        status = self.browser.find_element(*AdminResumesPageLocators.RESUME_STATUS).text
        assert status == 'Удалено', f"Не верный статус, expected result: 'Удалено', actual result: '{status}'"
    # страница вакансий

    def go_to_object_editing_page(self):  # переход на страницу редактирования объекта
        self.browser.find_element(*AdminResumesPageLocators.BUTTON_RESUME_MENU).click()  # костыль из-за ховер эффекта на кнопке меню пользователя

    def waiting_to_save_status_and_open_resume_page(self):  # ожидание сохранения статуса и открытия страницы всех рузюме
        WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element(AdminResumesPageLocators.H1_RESUMES, 'Резюме'))

    def complete_objects_deletion(self):  # полное удаление объектов (кроме пользователя)
        element_to_hover_over = self.browser.find_element(*AdminResumesPageLocators.BUTTON_RESUME_MENU)
        ActionChains(self.browser).move_to_element(element_to_hover_over).perform()
        self.browser.find_element(*AdminResumesPageLocators.BUTTON_COMPLETE_RESUME_DELETED).click()
        self.browser.find_element(*AdminResumesPageLocators.BUTTON_RESUME_DELETE_CONFIRMATION).click()
        assert self.is_element_present(*AdminResumesPageLocators.ALERT_CONFIRMATION_OF_RESUME_DELETION), 'Нет сообщения о удалении резюме'
