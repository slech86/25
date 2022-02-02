from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminVacancyEditPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing, Accounts
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class AdminVacancyEditPage(BasePage):
    def change_vacancy_status_to_published(self):  # изменение статуса вакансии на 'Опубликовано'
        self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_VACANCY_STATUS).click()
        self.browser.find_element(*AdminVacancyEditPageLocators.STATUS_PUBLISHED).click()
        time.sleep(2)
        self.browser.find_element(*AdminVacancyEditPageLocators.BUTTON_SAVE).click()