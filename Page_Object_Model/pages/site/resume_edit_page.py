import time
import os
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import ResumeEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumeEditPage(BasePage):
    def change_data_in_all_fields(self):  # изменение данных во всех полях
        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK).click()
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'фото 2 120x150.png')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PHOTO).send_keys(file_path)

        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_SURNAME).send_keys('_edit')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_OF_BIRTH).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_MARCH).click()
        time.sleep(0.5)
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*ResumeEditPageLocators.DAY_8).click()

        self.browser.find_element(*ResumeEditPageLocators.FIELD_GENDER).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*ResumeEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '174')  # 174 - id Poland

        locator_with_position_country = ResumeEditPageLocators()
        country_poland = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_poland).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*ResumeEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '3088171')  # 3088171 - id Poznan

        locator_with_position_city = ResumeEditPageLocators()
        city_poznan = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_poznan).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_WILLING_TO_RELOCATE).click()
        self.browser.find_element(*ResumeEditPageLocators.READY_TO_RELOCATE).click()
        # блок "Личная информация"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_CONTACT_INFORMATION_BLOCK).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PHONE_1).clear()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PHONE_1).send_keys(TestDataEditing.phone_1_resume)
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PHONE_2).clear()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PHONE_2).send_keys(TestDataEditing.phone_2_resume)
        self.browser.find_element(*ResumeEditPageLocators.FIELD_EMAIL).send_keys('editing')

        self.browser.find_element(*ResumeEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_PORTFOLIO).send_keys('_editing')

        self.browser.find_element(*ResumeEditPageLocators.FIELD_FACEBOOK).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_LINKEDIN).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_INSTAGRAM).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_TELEGRAM).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_TWITTER).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_VK).send_keys('_editing')
        # блок "Контактная информация"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_POSITION_DESIRED_BLOCK).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_JOB_TITLE).send_keys('_editing')
        self.browser.execute_script(ResumeEditPageLocators.CATEGORY_RESUME)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        self.browser.find_element(*ResumeEditPageLocators.SUBCATEGORIES).click()  # "Подкатегории"

        self.browser.find_element(*ResumeEditPageLocators.UNDEREMPLOYMENT).click()
        self.browser.find_element(*ResumeEditPageLocators.SALARY).clear()
        self.browser.find_element(*ResumeEditPageLocators.SALARY).send_keys(TestDataEditing.salary_resume)
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*ResumeEditPageLocators.CURRENCY_USD).click()
        # блок "Желаемая должность"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_SKILLS_AND_ACHIEVEMENTS_BLOCK).click()
        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_WORK_EXPERIENCE_BLOCK).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_COMPANY_NAME).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_SITE_COMPANY).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.SCOPE_OF_COMPANY_SECURITY_SERVICE).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_POSITION).send_keys('_editing')

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_DECEMBER_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_START).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_JANUARY_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeEditPageLocators.FIELD_COMPANY_NAME_2).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.FIELD_SITE_COMPANY_2).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.SCOPE_OF_COMPANY_WEBSITE_PROMOTION_2).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_POSITION_2).send_keys('_editing')

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_FEBRUARY_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_START_2).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_MARCH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH_2).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_ADD_WORK_EXPERIENCE_NUMBER_3).click()

        self.browser.find_element(*ResumeEditPageLocators.FIELD_COMPANY_NAME_3).send_keys(TestDataEditing.company_name_resume_3)
        self.browser.find_element(*ResumeEditPageLocators.FIELD_SITE_COMPANY_3).send_keys(TestDataEditing.company_site_resume_3)
        self.browser.find_element(*ResumeEditPageLocators.SCOPE_OF_COMPANY_WEBSITE_PROMOTION_3).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_POSITION_3).send_keys(TestDataEditing.position_resume_3)

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_APRIL_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_START_3).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_3).click()
        self.browser.find_element(*ResumeEditPageLocators.WORKING_NOW_WORK_EXPERIENCE_FINISH_3).click()
        # self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_3).click()
        # self.browser.find_element(*ResumeEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH_3).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_3)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestDataEditing.responsibilities_and_achievements_3)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Опыт работы"

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY).click()
        self.browser.find_element(*ResumeEditPageLocators.EXPERIENCE_2_TO_5_YEARS).click()
        # блок "Опыт работы в игорной индустрии"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_EDUCATION_BLOCK).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.UNFINISHED_HIGHER_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_COUNTRY_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.COUNTRY_NOT_SELECTED_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_CITI_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.CITI_NOT_SELECTED_EDUCATION).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_START).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_NOT_SELECTED_EDUCATION_START).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_START).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_NOT_SELECTED_EDUCATION_START).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_NOT_SELECTED_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_NOT_SELECTED_EDUCATION_FINISH).click()

        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_2).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_2).click()
        self.browser.find_element(*ResumeEditPageLocators.SECONDARY_EDUCATION_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_COUNTRY_EDUCATION_2).click()

        country_list_education = self.browser.find_elements(*ResumeEditPageLocators.COUNTRY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(country_list_education, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeEditPageLocators()
        country_ukraine_education = locator_with_position_country.assembly_of_locators_with_position_country_education_2()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine_education).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_CITI_EDUCATION_2).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeEditPageLocators.CITY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(city_list_education, '710791')  # 710791 - id Cherkasy

        locator_with_position_city = ResumeEditPageLocators()
        city_cherkasy_education = locator_with_position_city.assembly_of_locators_with_position_city_education_2()  # сборка локаторов с позицией города

        self.browser.find_element(*city_cherkasy_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeEditPageLocators.DROPDOWN_CITI_EDUCATION_2, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_JUNE_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_JULY_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_EDUCATION_FINISH_2).click()

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_ADD_EDUCATION_NUMBER_3).click()

        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_3).send_keys(TestDataEditing.name_of_institution_3)
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_3).click()
        self.browser.find_element(*ResumeEditPageLocators.HIGHER_EDUCATION_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_COUNTRY_EDUCATION_3).click()

        country_list_education = self.browser.find_elements(*ResumeEditPageLocators.COUNTRY_EDUCATION_LIST_3)

        determining_position_of_object_in_drop_down_list(country_list_education, '54')  # 54 - id Cyprus

        locator_with_position_country = ResumeEditPageLocators()
        country_cyprus_education = locator_with_position_country.assembly_of_locators_with_position_country_education_3()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_cyprus_education).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_CITI_EDUCATION_3).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeEditPageLocators.CITY_EDUCATION_LIST_3)

        determining_position_of_object_in_drop_down_list(city_list_education, '146384')  # 146384 - id Limassol

        locator_with_position_city = ResumeEditPageLocators()
        city_limassol_education = locator_with_position_city.assembly_of_locators_with_position_city_education_3()  # сборка локаторов с позицией города

        self.browser.find_element(*city_limassol_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeEditPageLocators.DROPDOWN_CITI_EDUCATION_3, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_3).send_keys(TestDataEditing.department_and_speciality_3)
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_AUGUST_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_3).click()
        self.browser.find_element(*ResumeEditPageLocators.STUDY_NOW_EDUCATION_FINISH_3).click()
        # self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_3).click()
        # self.browser.find_element(*ResumeEditPageLocators.YEAR_EDUCATION_FINISH_3).click()
        # блок "Образование"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_COURSES_AND_CERTIFICATES_BLOCK).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_START).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_SEPTEMBER_COURSES_START).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_OCTOBER_COURSES_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_FINISH).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2).send_keys('_editing')
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_NOVEMBER_COURSES_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_NOVEMBER_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_FINISH_2).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_ADD_COURSES_NUMBER_3).click()

        self.browser.find_element(*ResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_3).send_keys(TestDataEditing.name_course_3)
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_DECEMBER_COURSES_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_START_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeEditPageLocators.MONTH_JANUARY_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeEditPageLocators.YEAR_COURSES_FINISH_3).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_3)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestDataEditing.course_description_3)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Курсы и сертификаты"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_KNOWLEDGE_OF_LANGUAGES_BLOCK).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*ResumeEditPageLocators.ENGLISH_LANGUAGE_1).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*ResumeEditPageLocators.BASIC_LEVEL_1).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeEditPageLocators.FRENCH_LANGUAGE_2).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*ResumeEditPageLocators.ABOVE_AVERAGE_LEVEL_2).click()

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_ADD_LANGUAGE_NUMBER_3).click()

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LANGUAGE_3).click()
        self.browser.find_element(*ResumeEditPageLocators.HEBREW_LANGUAGE_3).click()
        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_3).click()
        self.browser.find_element(*ResumeEditPageLocators.MIDDLE_LEVEL_3).click()
        # блок "Знание языков"

        self.browser.find_element(*ResumeEditPageLocators.I_HAVE_DISABILITY).click()
        self.browser.find_element(*ResumeEditPageLocators.FIELD_DESCRIPTION_OF_DISABILITY).send_keys(TestDataEditing.description_of_disability)
        # блок "Инвалидность"

        self.browser.find_element(*ResumeEditPageLocators.BUTTON_EDIT_IN_ADDITIONAL_INFORMATION_BLOCK).click()

        iframe = self.browser.find_element(*ResumeEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.find_element(*ResumeEditPageLocators.DROPDOWN_JOB_SEARCH_STATUS).click()
        self.browser.find_element(*ResumeEditPageLocators.WORKING_BUT_OPEN_TO_SUGGESTIONS).click()
        # блок "Статус поиска работы"

    def percentage_check_of_resume_completion(self):  # проверка заполнения резюме в процентах
        percent = self.browser.find_element(*ResumeEditPageLocators.RESUME_COMPLETED_ON).text
        assert percent == '100', 'Не верный процент заполнения резюме'

    def checking_status_level_filling_resume(self, language):  # проверка статуса уровня заполнения резюме
        status_level_filling = self.browser.find_element(*ResumeEditPageLocators.STATUS_OF_YOUR_RESUME).text
        if language == "/ua":
            assert status_level_filling == 'Професійне', 'Не верный статус уровня заполнения'
        elif language == "":
            assert status_level_filling == 'Профессиональное', 'Не верный статус уровня заполнения'
        elif language == "/en":
            assert status_level_filling == 'Professional', 'Не верный статус уровня заполнения'

    def submitting_resume_change_for_publication(self,):  # отправка изменений резюме на публикацию
        self.browser.find_element(*ResumeEditPageLocators.BUTTON_PUBLISH).click()
