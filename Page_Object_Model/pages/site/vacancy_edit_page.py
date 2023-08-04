import time
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import VacancyAddEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.elements.button import Button


class VacancyEditPage(BasePage):
    def hiding_copy_to_other_languages(self):  # скрытие кнопки "Скопировать на другие языки"
        self.browser.find_element(*VacancyAddEditPageLocators.CROSS_IN_COPY_TO_OTHER_LANGUAGES).click()

    @staticmethod
    def start_editing_block_main_information(browser):  # начать редактировать блок "Основная информация"
        root_xpath = '//div[@id="general-information"]'
        Button.button_btn_edit_click(browser, root_xpath=root_xpath)

    def change_data_in_all_fields(self, browser):  # изменение данных во всех полях
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_JOB_TITLE).send_keys('_editing')
        self.browser.find_element(*VacancyAddEditPageLocators.CATEGORY_VACANCIES_SITE_PROMOTION).click()
        subcategories = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(VacancyAddEditPageLocators.SUBCATEGORIES_SEO_SPECIALIST))  # "Подкатегории"
        time.sleep(3)
        subcategories.click()
        time.sleep(3)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MINIMAL_SALARY).clear()
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MINIMAL_SALARY).send_keys(TestDataEditing.salary_min)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MAXIMUM_SALARY).clear()
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_MAXIMUM_SALARY).send_keys(TestDataEditing.salary_max)
        time.sleep(2)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_CURRENCY).click()
        time.sleep(1)
        self.browser.find_element(*VacancyAddEditPageLocators.CURRENCY_UAH).click()
        time.sleep(2)
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_COUNTRY).click()
        country_list = self.browser.find_elements(*VacancyAddEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = VacancyAddEditPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*VacancyAddEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '709930')  # 709930 - id Dnipro

        locator_with_position_city = VacancyAddEditPageLocators()
        city_dnipro = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_dnipro).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute((VacancyAddEditPageLocators.DROPDOWN_CITI), 'aria-expanded', 'false'))

        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_STREET).send_keys('_editing')
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_PHONE).clear()
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_PHONE).send_keys(TestDataEditing.phone_vacancy)
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_EMAIL).send_keys('editing')
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_CONTACT_PERSON).send_keys('_editing')
        self.browser.find_element(*VacancyAddEditPageLocators.FIELD_TELEGRAM).send_keys('_editing')
        self.browser.find_element(*VacancyAddEditPageLocators.REMOTE_WORK).click()
        self.browser.find_element(*VacancyAddEditPageLocators.WORK_EXPERIENCE_2_YEAR).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_EDUCATION).click()
        self.browser.find_element(*VacancyAddEditPageLocators.SECONDARY_EDUCATION).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()
        self.browser.find_element(*VacancyAddEditPageLocators.FOREIGN_LANGUAGE_COURSES).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_VACANCY_BENEFITS).click()  # закрытие выпадающего списка
        self.browser.find_element(*VacancyAddEditPageLocators.READY_TO_TAKE_PERSON_WITH_DISABILITY).click()
        # блок 'Основная информация'

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="knowledge-of-languages"]')
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_TO_DELETE_FIRST_LANGUAGE).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.ENGLISH_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*VacancyAddEditPageLocators.ABOVE_AVERAGE_LEVEL_2).click()
        # блок "Знание языков"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="vacancy-description"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Описание вакансии"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="about-company"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "О компании"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="working-conditions"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Условия работы"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="tasks"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_TASKS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Задачи"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="requirements-candidate"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_REQUIREMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Требования к соискателю"

        Button.button_btn_edit_click(browser, root_xpath='//div[@id="additional-information"]')
        iframe = self.browser.find_element(*VacancyAddEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*VacancyAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys("editing_")
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.execute_script("window.scrollBy(0, 600);")

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_PREVIEW).click()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def submitting_vacancy_change_for_publication(self):  # отправка изменений вакансии на публикацию
        self.browser.find_element(*VacancyAddEditPageLocators.BUTTON_PUBLISH).click()
