import time
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyEditPageLocators


class VacancyEditPage(BasePage):
    def change_data_in_all_fields(self):  # изменение данных во всех полях
        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_BASIC_INFORMATION_BLOCK).click()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_JOB_TITLE).send_keys('_editing')
        self.browser.execute_script(VacancyEditPageLocators.CATEGORY_VACANCIES)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        self.browser.find_element(*VacancyEditPageLocators.SUBCATEGORIES).click()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_MINIMAL_SALARY).clear()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestDataEditing.salary_min)
        self.browser.find_element(*VacancyEditPageLocators.FIELD_MAXIMUM_SALARY).clear()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestDataEditing.salary_max)
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*VacancyEditPageLocators.CURRENCY_RUB).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_COUNTRY).click()
        self.browser.find_element(*VacancyEditPageLocators.COUNTRY_UKRAINE).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.3)
        self.browser.find_element(*VacancyEditPageLocators.CITI_DNIPRO).click()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_STREET).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_PHONE).send_keys(TestDataEditing.phone_vacancy)
        self.browser.find_element(*VacancyEditPageLocators.FIELD_EMAIL).send_keys('editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_CONTACT_PERSON).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.REMOTE_WORK).click()
        self.browser.find_element(*VacancyEditPageLocators.WORK_EXPERIENCE_2_YEAR).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_EDUCATION).click()
        self.browser.find_element(*VacancyEditPageLocators.SECONDARY_EDUCATION).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()
        self.browser.find_element(*VacancyEditPageLocators.FOREIGN_LANGUAGE_COURSES).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()  # закрытие выпадающего списка
        self.browser.find_element(*VacancyEditPageLocators.READY_TO_TAKE_PERSON_WITH_DISABILITY).click()
        # блок 'Основная информация'

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_KNOWLEDGE_OF_LANGUAGES_BLOCK).click()
        self.browser.find_element(*VacancyEditPageLocators.BUTTON_TO_DELETE_FIRST_LANGUAGE).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*VacancyEditPageLocators.ENGLISH_LANGUAGE_1).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*VacancyEditPageLocators.ABOVE_AVERAGE_LEVEL_1).click()
        # блок "Знание языков"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_VACANCY_DESCRIPTION_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Описание вакансии"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_ABOUT_COMPANY_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "О компании"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_WORKING_CONDITIONS_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Условия работы"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_TASKS_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_TASKS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Задачи"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_REQUIREMENTS_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_REQUIREMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Требования к соискателю"

        self.browser.find_element(*VacancyEditPageLocators.BUTTON_EDIT_IN_ADDITIONAL_INFORMATION_BLOCK).click()
        iframe = self.browser.find_element(*VacancyEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.execute_script("window.scrollBy(0, 600);")

    def submitting_vacancy_change_for_publication(self):  # отправка изменений вакансии на публикацию
        self.browser.find_element(*VacancyEditPageLocators.BUTTON_PUBLISH).click()