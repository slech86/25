import time
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyAddPageLocators


class VacancyAddPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        assert self.is_not_element_present(*VacancyAddPageLocators.BUTTON_PUBLISH), "Не должно быть кнопки 'Опубликовать'"

    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*VacancyAddPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_vacancy)
        self.browser.execute_script(VacancyAddPageLocators.CATEGORY_VACANCIES)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        self.browser.find_element(*VacancyAddPageLocators.SUBCATEGORIES).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_COUNTRY).click()
        self.browser.find_element(*VacancyAddPageLocators.COUNTRY_RUSSIA).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_CITI).click()
        self.browser.find_element(*VacancyAddPageLocators.CITI_MOSCOW).click()
        self.browser.find_element(*VacancyAddPageLocators.FULL_EMPLOYMENT).click()
        self.browser.find_element(*VacancyAddPageLocators.WORK_EXPERIENCE_1_YEAR).click()
        # блок 'Основная информация'

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*VacancyAddPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestData.salary_min)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestData.salary_max)
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*VacancyAddPageLocators.CURRENCY_USD).click()
        self.browser.find_element(*VacancyAddPageLocators.FIELD_STREET).send_keys(TestData.street_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_PHONE).send_keys(TestData.phone_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_EMAIL).send_keys(TestData.email_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_SKYPE).send_keys(TestData.skype_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_CONTACT_PERSON).send_keys(TestData.contact_person)
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_EDUCATION).click()
        self.browser.find_element(*VacancyAddPageLocators.HIGHER_EDUCATION).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_VACANCY_BENEFITS).click()
        self.browser.find_element(*VacancyAddPageLocators.TRANSPORTATION).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_VACANCY_BENEFITS).click()  # закрытие выпадающего списка
        self.browser.find_element(*VacancyAddPageLocators.READY_TO_TAKE_STUDENT).click()
        # блок 'Основная информация'

        self.browser.find_element(*VacancyAddPageLocators.BUTTON_ADD_LANGUAGE).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*VacancyAddPageLocators.ENGLISH_LANGUAGE_1).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*VacancyAddPageLocators.MIDDLE_LEVEL_1).click()

        self.browser.find_element(*VacancyAddPageLocators.BUTTON_ADD_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddPageLocators.RUSSIAN_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddPageLocators.NATIVE_LEVEL_2).click()
        # блок "Знание языков"

        self.browser.find_element(*VacancyAddPageLocators.ADD_DESCRIPTION_OF_VACANCIES).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.description_vacancy)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Описание вакансии"

        self.browser.find_element(*VacancyAddPageLocators.ADD_ABOUT_COMPANY).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.about_company)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "О компании"

        self.browser.find_element(*VacancyAddPageLocators.ADD_WORKING_CONDITIONS).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.working_conditions)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Условия работы"

        self.browser.find_element(*VacancyAddPageLocators.ADD_TASKS).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_TASKS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.tasks)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Задачи"

        self.browser.find_element(*VacancyAddPageLocators.ADD_REQUIREMENTS).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_REQUIREMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.requirements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Требования к соискателю"

        self.browser.find_element(*VacancyAddPageLocators.ADD_ADDITIONAL_INFORMATION).click()
        iframe = self.browser.find_element(*VacancyAddPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additionally_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.execute_script("window.scrollBy(0, 600);")

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        self.browser.find_element(*VacancyAddPageLocators.BUTTON_PUBLISH).click()
