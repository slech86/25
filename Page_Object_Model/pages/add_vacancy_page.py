import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.data_for_testing import TestData
from .base_page import BasePage
from .locators import AddVacancyPageLocators


class AddVacancyPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        assert self.is_not_element_present(*AddVacancyPageLocators.BUTTON_PUBLISH), "Не должно быть кнопки 'Опубликовать'"

    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*AddVacancyPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title)
        self.browser.execute_script(AddVacancyPageLocators.CATEGORY_VACANCIES)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        time.sleep(0.2)
        self.browser.execute_script(AddVacancyPageLocators.SUBCATEGORIES)  # "Подкатегории" передается параметр уже с ".click()"
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_COUNTRY).click()
        self.browser.find_element(*AddVacancyPageLocators.COUNTRY_RUSSIA).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_CITI).click()
        self.browser.find_element(*AddVacancyPageLocators.CITI_MOSCOW).click()
        self.browser.find_element(*AddVacancyPageLocators.FULL_EMPLOYMENT).click()
        self.browser.find_element(*AddVacancyPageLocators.WORK_EXPERIENCE_1_YEAR).click()
        # блок 'Основная информация'

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*AddVacancyPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestData.salary_min)
        self.browser.find_element(*AddVacancyPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestData.salary_max)
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*AddVacancyPageLocators.CURRENCY_USD).click()
        self.browser.find_element(*AddVacancyPageLocators.FIELD_STREET).send_keys(TestData.street_vacancy)
        self.browser.find_element(*AddVacancyPageLocators.FIELD_PHONE).send_keys(TestData.phone_vacancy)
        self.browser.find_element(*AddVacancyPageLocators.FIELD_EMAIL).send_keys(TestData.email_vacancy)
        self.browser.find_element(*AddVacancyPageLocators.FIELD_SKYPE).send_keys(TestData.skype_vacancy)
        self.browser.find_element(*AddVacancyPageLocators.FIELD_CONTACT_PERSON).send_keys(TestData.contact_person)
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_EDUCATION).click()
        self.browser.find_element(*AddVacancyPageLocators.HIGHER_EDUCATION).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_VACANCY_BENEFITS).click()
        self.browser.find_element(*AddVacancyPageLocators.TRANSPORTATION).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_VACANCY_BENEFITS).click()  # закрытие выпадающего списка
        self.browser.find_element(*AddVacancyPageLocators.READY_TO_TAKE_STUDENT).click()
        # блок 'Основная информация'

        self.browser.find_element(*AddVacancyPageLocators.BUTTON_ADD_LANGUAGE).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*AddVacancyPageLocators.ENGLISH_LANGUAGE_1).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*AddVacancyPageLocators.MIDDLE_LEVEL_1).click()
        self.browser.find_element(*AddVacancyPageLocators.ADD_LANGUAGE).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*AddVacancyPageLocators.ENGLISH_LANGUAGE_2).click()
        self.browser.find_element(*AddVacancyPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*AddVacancyPageLocators.MIDDLE_LEVEL_2).click()
        # блок "Знание языков"

        self.browser.find_element(*AddVacancyPageLocators.ADD_DESCRIPTION_OF_VACANCIES).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.description_vacancy)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Описание вакансии"

        self.browser.find_element(*AddVacancyPageLocators.ADD_ABOUT_COMPANY).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.about_company)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "О компании"

        self.browser.find_element(*AddVacancyPageLocators.ADD_WORKING_CONDITIONS).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.working_conditions)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Условия работы"

        self.browser.find_element(*AddVacancyPageLocators.ADD_TASKS).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_TASKS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.tasks)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Задачи"

        self.browser.find_element(*AddVacancyPageLocators.ADD_REQUIREMENTS).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_REQUIREMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.requirements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Требования к соискателю"

        self.browser.find_element(*AddVacancyPageLocators.ADD_ADDITIONAL_INFORMATION).click()
        iframe = self.browser.find_element(*AddVacancyPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddVacancyPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additionally_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.execute_script("window.scrollBy(0, 600);")

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        self.browser.find_element(*AddVacancyPageLocators.BUTTON_PUBLISH).click()
