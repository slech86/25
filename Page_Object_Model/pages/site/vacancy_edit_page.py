import time
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.browser.find_element(*VacancyEditPageLocators.CURRENCY_UAH).click()
        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*VacancyEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = VacancyEditPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*VacancyEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*VacancyEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '709930')  # 709930 - id Dnipro

        locator_with_position_city = VacancyEditPageLocators()
        city_dnipro = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_dnipro).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute((VacancyEditPageLocators.DROPDOWN_CITI), 'aria-expanded', 'false'))

        self.browser.find_element(*VacancyEditPageLocators.FIELD_STREET).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*VacancyEditPageLocators.FIELD_PHONE).send_keys(TestDataEditing.phone_vacancy)
        self.browser.find_element(*VacancyEditPageLocators.FIELD_EMAIL).send_keys('editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_CONTACT_PERSON).send_keys('_editing')
        self.browser.find_element(*VacancyEditPageLocators.FIELD_TELEGRAM).send_keys('_editing')
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

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        self.browser.find_element(*VacancyEditPageLocators.BUTTON_PREVIEW).click()
        time.sleep(1)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def submitting_vacancy_change_for_publication(self):  # отправка изменений вакансии на публикацию
        self.browser.find_element(*VacancyEditPageLocators.BUTTON_PUBLISH).click()
