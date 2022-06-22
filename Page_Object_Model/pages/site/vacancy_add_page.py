import time
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyAddPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VacancyAddPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        assert self.is_not_element_present(*VacancyAddPageLocators.BUTTON_PUBLISH), "Не должно быть кнопки 'Опубликовать'"

    def filling_in_field_job_title_for_draft(self):  # заполнение поля "Название должности" для черновика
        self.browser.find_element(*VacancyAddPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_vacancy_for_draft)

    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*VacancyAddPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_vacancy)
        self.browser.execute_script(VacancyAddPageLocators.CATEGORY_VACANCIES)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        self.browser.find_element(*VacancyAddPageLocators.SUBCATEGORIES).click()

        self.browser.find_element(*VacancyAddPageLocators.FULL_EMPLOYMENT).click()
        self.browser.find_element(*VacancyAddPageLocators.WORK_EXPERIENCE_1_YEAR).click()
        # блок 'Основная информация'

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*VacancyAddPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '79')  # 79 - id Georgia

        locator_with_position_country = VacancyAddPageLocators()
        country_georgia = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_georgia).click()

        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*VacancyAddPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '9000009')  # 9000009 - id Batumi

        locator_with_position_city = VacancyAddPageLocators()
        city_batumi = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_batumi).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(VacancyAddPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))

        self.browser.find_element(*VacancyAddPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestData.salary_min)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestData.salary_max)
        self.browser.find_element(*VacancyAddPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*VacancyAddPageLocators.CURRENCY_USD).click()
        self.browser.find_element(*VacancyAddPageLocators.FIELD_STREET).send_keys(TestData.street_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_PHONE).send_keys(TestData.phone_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_EMAIL).send_keys(TestData.email_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_SKYPE).send_keys(TestData.skype_vacancy)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_CONTACT_PERSON).send_keys(TestData.contact_person)
        self.browser.find_element(*VacancyAddPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram_vacancy)
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

    def checking_field_job_title_validation_message_about_need_to_fill_out(self, language):  # проверка сообщения валидации поля "Название должности" о необходимости его заполнения
        validation_message = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(VacancyAddPageLocators.VALIDATION_MESSAGE_FIELD_JOB_TITLE)).text
        if language == "":
            assert validation_message == "Необходимо заполнить «Название должности».", f"Не верное сообщение валидации, expected result: 'Необходимо заполнить «Название должности».', actual result: '{validation_message}'"
        elif language == "/ua":
            assert validation_message == 'Необхідно заповнити "Назва посади".', f'Не верное сообщение валидации, expected result: "Необхідно заповнити "Назва посади".", actual result: "{validation_message}"'
        elif language == "/en":
            assert validation_message == "Job title cannot be blank.", f"Не верное сообщение валидации, expected result: 'Job title cannot be blank.', actual result: '{validation_message}'"

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        self.browser.find_element(*VacancyAddPageLocators.BUTTON_PUBLISH).click()

    def adding_vacancy_to_draft(self):  # добавление вакансии в черновик
        self.browser.find_element(*VacancyAddPageLocators.BUTTON_TO_DRAFTS).click()
