import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminSqlPageLocators


class AdminSqlPage(BasePage):
    def sql_change_number_of_contact_views_per_day(self, purchase_id, number='1'):  # изменение количества просмотров контактов в день
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).clear()
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).send_keys('UPDATE `tbl_purchases` SET `view_contacts_at_day`=' + number + ' WHERE `id`=' + purchase_id + ';')
        self.browser.find_element(*AdminSqlPageLocators.BUTTON_EXECUTE).click()
        time.sleep(1)

    def sql_delete_record_opening_contacts(self, user_id, resume_id):  # удаление записи о открытии контакта
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).clear()
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).send_keys('DELETE FROM `tbl_resume_contacts` WHERE `user_id`=' + user_id + ' AND `resume_id`=' + resume_id + ';')
        self.browser.find_element(*AdminSqlPageLocators.BUTTON_EXECUTE).click()
        time.sleep(1)

    def sql_delete_record_response_to_vacancy(self, user_id_job_seeker, resume_id, vacancy_id):  # удаление записи отклика на вакансию
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).clear()
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).send_keys('DELETE FROM `tbl_responses` WHERE `user_id`=' + user_id_job_seeker + ' AND `resume_id`=' + resume_id + ' AND `vacancy_id`=' + vacancy_id + ';')
        self.browser.find_element(*AdminSqlPageLocators.BUTTON_EXECUTE).click()
        time.sleep(1)

    def sql_deleting_all_user_orders(self, user_id_job_seeker):  # удаление всех заказов пользователя
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).clear()
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).send_keys('DELETE FROM `tbl_orders` WHERE `user_id`=' + user_id_job_seeker + ';')
        self.browser.find_element(*AdminSqlPageLocators.BUTTON_EXECUTE).click()
        time.sleep(1)

    def sql_deleting_all_user_vacancies(self, user_id_job_seeker):  # удаление всех вакансий пользователя
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).clear()
        self.browser.find_element(*AdminSqlPageLocators.FIELD_SQL).send_keys('DELETE FROM `tbl_vacancies` WHERE `user_id`=' + user_id_job_seeker + ';')
        self.browser.find_element(*AdminSqlPageLocators.BUTTON_EXECUTE).click()
        time.sleep(1)
