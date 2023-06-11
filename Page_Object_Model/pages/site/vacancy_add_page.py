import time
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyAddEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VacancyAddPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        assert self.is_not_element_present(*VacancyAddEditPageLocators.BUTTON_PUBLISH), "Не должно быть кнопки 'Опубликовать'"

    def filling_in_field_job_title_for_draft(self):  # заполнение поля "Название должности" для черновика
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_vacancy_for_draft)

    def hiding_copy_to_other_languages(self):  # скрытие кнопки "Скопировать на другие языки"
        self.browser.find_element(*VacancyAddEditPageLocators.CROSS_IN_COPY_TO_OTHER_LANGUAGES).click()

    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_JOB_TITLE).clear()
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.CATEGORY_VACANCIES_HUMAN_RESOURCES_DEPARTMENT).click()
        time.sleep(2)
        self.browser.find_element(*VacancyAddEditPageLocators.SUBCATEGORIES_HR_MANAGER).click()
        time.sleep(2)

        self.browser.find_element(*VacancyAddEditPageLocators.FULL_EMPLOYMENT).click()
        self.browser.find_element(*VacancyAddEditPageLocators.WORK_EXPERIENCE_1_YEAR).click()
        time.sleep(2)
        # блок 'Основная информация'

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_PREVIEW).click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*VacancyAddEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '79')  # 79 - id Georgia

        locator_with_position_country = VacancyAddEditPageLocators()
        country_georgia = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_georgia).click()

        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*VacancyAddEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '9000009')  # 9000009 - id Batumi

        locator_with_position_city = VacancyAddEditPageLocators()
        city_batumi = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_batumi).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(VacancyAddEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))

        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestData.salary_min)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestData.salary_max)
        time.sleep(2)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_CURRENCY).click()
        time.sleep(1)
        self.browser.find_element(*VacancyAddEditPageLocators.CURRENCY_USD).click()
        time.sleep(2)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_STREET).send_keys(TestData.street_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_PHONE).send_keys(TestData.phone_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_EMAIL).send_keys(TestData.email_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_SKYPE).send_keys(TestData.skype_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_CONTACT_PERSON).send_keys(TestData.contact_person)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_EDUCATION).click()
        self.browser.find_element(*VacancyAddEditPageLocators.HIGHER_EDUCATION).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()
        self.browser.find_element(*VacancyAddEditPageLocators.TRANSPORTATION).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()  # закрытие выпадающего списка
        self.browser.find_element(*VacancyAddEditPageLocators.READY_TO_TAKE_STUDENT).click()
        # блок 'Основная информация'

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('knowledge-of-languages')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        time.sleep(1)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*VacancyAddEditPageLocators.ENGLISH_LANGUAGE_1).click()
        time.sleep(3)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*VacancyAddEditPageLocators.MIDDLE_LEVEL_1).click()

        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_ADD_LANGUAGE_NUMBER_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.RUSSIAN_LANGUAGE_2).click()
        time.sleep(1)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.NATIVE_LEVEL_2).click()
        # блок "Знание языков"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('vacancy-description')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.description_vacancy)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Описание вакансии"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('about-company')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.about_company)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "О компании"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('working-conditions')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.working_conditions)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Условия работы"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('tasks')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_TASKS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.tasks)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Задачи"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('requirements-candidate')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_REQUIREMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.requirements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Требования к соискателю"

        locators_from_id_block = VacancyAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('additional-information')
        self.browser.find_element(*button_add_skills['button_add_block']).click()
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additionally_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.execute_script("window.scrollBy(0, 600);")

    def checking_field_job_title_validation_message_about_need_to_fill_out(self, language):  # проверка сообщения валидации поля "Название должности" о необходимости его заполнения
        validation_message = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(VacancyAddEditPageLocators.VALIDATION_MESSAGE_FIELD_JOB_TITLE)).text
        if language == "":
            assert validation_message == "Необходимо заполнить «Название должности».", f"Не верное сообщение валидации, expected result: 'Необходимо заполнить «Название должности».', actual result: '{validation_message}'"
        elif language == "/ua":
            assert validation_message == 'Необхідно заповнити "Назва посади".', f'Не верное сообщение валидации, expected result: "Необхідно заповнити "Назва посади".", actual result: "{validation_message}"'
        elif language == "/en":
            assert validation_message == "Job title cannot be blank.", f"Не верное сообщение валидации, expected result: 'Job title cannot be blank.', actual result: '{validation_message}'"
        elif language == "/pl":
            assert validation_message == "Zasadź nazwę nie może pozostać bez wartości.", f"Не верное сообщение валидации, expected result: 'Job title cannot be blank.', actual result: '{validation_message}'"

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        time.sleep(3)
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_PUBLISH).click()

    def adding_vacancy_to_draft(self):  # добавление вакансии в черновик
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_TO_DRAFTS).click()
