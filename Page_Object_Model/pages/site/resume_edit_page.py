import time
import os
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import ResumeAddEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumeEditPage(BasePage):
    def hiding_copy_to_other_languages(self):  # скрытие кнопки "Скопировать на другие языки"
        self.browser.find_element(*ResumeAddEditPageLocators.CROSS_IN_COPY_TO_OTHER_LANGUAGES).click()

    def change_data_in_all_fields(self):  # изменение данных во всех полях
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'фото 2 120x150.png')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHOTO).send_keys(file_path)

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SURNAME).send_keys('_edit')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_OF_BIRTH_1976).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_MARCH).click()
        time.sleep(0.5)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DAY_8).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_GENDER_MALE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '174')  # 174 - id Poland

        locator_with_position_country = ResumeAddEditPageLocators()
        country_poland = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_poland).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '3088171')  # 3088171 - id Poznan

        locator_with_position_city = ResumeAddEditPageLocators()
        city_poznan = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_poznan).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_WILLING_TO_RELOCATE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.READY_TO_RELOCATE).click()
        # блок "Личная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_1).clear()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_1).send_keys(TestDataEditing.phone_1_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_2).clear()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_2).send_keys(TestDataEditing.phone_2_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_EMAIL).send_keys('editing')

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SKYPE).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PORTFOLIO).send_keys('_editing/')

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_FACEBOOK).send_keys('_editing/')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_LINKEDIN).send_keys('_editing/')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_INSTAGRAM).send_keys('_editing/')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_TELEGRAM).send_keys('_editing/')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_TWITTER).send_keys('_editing/')
        # self.browser.find_element(*ResumeAddEditPageLocators.FIELD_VK).send_keys('_editing/')
        # блок "Контактная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_JOB_TITLE).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.CATEGORY_RESUME_SALES_CUSTOMER_MANAGEMENT).click()
        subcategories = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(ResumeAddEditPageLocators.SUBCATEGORIES_ACCOUNT_MANAGER))  # "Подкатегории"
        time.sleep(3)
        subcategories.click()
        time.sleep(3)

        self.browser.find_element(*ResumeAddEditPageLocators.UNDEREMPLOYMENT).click()
        self.browser.find_element(*ResumeAddEditPageLocators.SALARY).clear()
        self.browser.find_element(*ResumeAddEditPageLocators.SALARY).send_keys(TestDataEditing.salary_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CURRENCY).click()
        time.sleep(1)
        self.browser.find_element(*ResumeAddEditPageLocators.CURRENCY_USD).click()
        time.sleep(1)
        # блок "Желаемая должность"

        # self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_EDIT_IN_SKILLS_AND_ACHIEVEMENTS_BLOCK).click()
        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_COMPANY_NAME).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SITE_COMPANY).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.SCOPE_OF_COMPANY_SECURITY_SERVICE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_POSITION).send_keys('_editing')

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_DECEMBER_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_START_2010).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JANUARY_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH_2012).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_COMPANY_NAME_2).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SITE_COMPANY_2).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.SCOPE_OF_COMPANY_WEBSITE_PROMOTION_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_POSITION_2).send_keys('_editing')

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_FEBRUARY_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_START_1993_2).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_MARCH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH_1996_2).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_WORK_EXPERIENCE_NUMBER_3).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_COMPANY_NAME_3).send_keys(TestDataEditing.company_name_resume_3)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SITE_COMPANY_3).send_keys(TestDataEditing.company_site_resume_3)
        self.browser.find_element(*ResumeAddEditPageLocators.SCOPE_OF_COMPANY_WEBSITE_PROMOTION_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_POSITION_3).send_keys(TestDataEditing.position_resume_3)

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_APRIL_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_START_2003_3).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.WORKING_NOW_WORK_EXPERIENCE_FINISH_3).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_3)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestDataEditing.responsibilities_and_achievements_3)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Опыт работы"

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.EXPERIENCE_2_TO_5_YEARS).click()
        # блок "Опыт работы в игорной индустрии"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.INCOMPLETE_HIGHER_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.CITI_NOT_SELECTED_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.COUNTRY_NOT_SELECTED_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_NOT_SELECTED_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_NOT_SELECTED_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_NOT_SELECTED_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_NOT_SELECTED_EDUCATION_FINISH).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_2).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.SECONDARY_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY_EDUCATION_2).click()

        country_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(country_list_education, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeAddEditPageLocators()
        country_ukraine_education = locator_with_position_country.assembly_of_locators_with_position_country_education_2()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine_education).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_2).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(city_list_education, '710791')  # 710791 - id Cherkasy

        locator_with_position_city = ResumeAddEditPageLocators()
        city_cherkasy_education = locator_with_position_city.assembly_of_locators_with_position_city_education_2()  # сборка локаторов с позицией города

        self.browser.find_element(*city_cherkasy_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_2, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JUNE_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_START_2005_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JULY_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_FINISH_2008_2).click()

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_EDUCATION_NUMBER_3).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_3).send_keys(TestDataEditing.name_of_institution_3)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.HIGHER_EDUCATION_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY_EDUCATION_3).click()

        country_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_EDUCATION_LIST_3)

        determining_position_of_object_in_drop_down_list(country_list_education, '54')  # 54 - id Cyprus

        locator_with_position_country = ResumeAddEditPageLocators()
        country_cyprus_education = locator_with_position_country.assembly_of_locators_with_position_country_education_3()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_cyprus_education).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_3).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_EDUCATION_LIST_3)

        determining_position_of_object_in_drop_down_list(city_list_education, '146384')  # 146384 - id Limassol

        locator_with_position_city = ResumeAddEditPageLocators()
        city_limassol_education = locator_with_position_city.assembly_of_locators_with_position_city_education_3()  # сборка локаторов с позицией города

        self.browser.find_element(*city_limassol_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_3, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_3).send_keys(TestDataEditing.department_and_speciality_3)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_AUGUST_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_START_2020_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.STUDY_NOW_EDUCATION_FINISH_3).click()
        # блок "Образование"

        # блок "Курсы и сертификаты"
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_SEPTEMBER_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_START_2016).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_OCTOBER_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_FINISH_2016).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2).send_keys('_editing')
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_NOVEMBER_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_START_2020_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_NOVEMBER_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH_2).click()
        time.sleep(0.6)
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_FINISH_2021_2).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_COURSES_NUMBER_3).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_3).send_keys(TestDataEditing.name_course_3)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_DECEMBER_COURSES_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_START_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_START_2017_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JANUARY_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_FINISH_2018_3).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_3)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestDataEditing.course_description_3)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Курсы и сертификаты"

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.ENGLISH_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BASIC_LEVEL_1).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FRENCH_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.ABOVE_AVERAGE_LEVEL_2).click()

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_LANGUAGE_NUMBER_3).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LANGUAGE_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.HEBREW_LANGUAGE_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_3).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MIDDLE_LEVEL_3).click()
        # блок "Знание языков"

        self.browser.find_element(*ResumeAddEditPageLocators.RADIO_I_HAVE_DISABILITY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DESCRIPTION_OF_DISABILITY).send_keys(TestDataEditing.description_of_disability)
        # блок "Инвалидность"

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys('editing_')
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_JOB_SEARCH_STATUS).click()
        self.browser.find_element(*ResumeAddEditPageLocators.WORKING_BUT_OPEN_TO_SUGGESTIONS).click()
        # блок "Статус поиска работы"

    def percentage_check_of_resume_completion(self):  # проверка заполнения резюме в процентах
        percent = self.browser.find_element(*ResumeAddEditPageLocators.RESUME_COMPLETED_ON).text
        assert percent == '100', 'Не верный процент заполнения резюме'

    def checking_status_level_filling_resume(self, language):  # проверка статуса уровня заполнения резюме
        status_level_filling = self.browser.find_element(*ResumeAddEditPageLocators.STATUS_OF_YOUR_RESUME).text
        if language == "":
            assert status_level_filling == 'Профессиональное', 'Не верный статус уровня заполнения'
        elif language == "/ua":
            assert status_level_filling == 'Професійне', 'Не верный статус уровня заполнения'
        elif language == "/en":
            assert status_level_filling == 'Professional', 'Не верный статус уровня заполнения'
        elif language == "/pl":
            assert status_level_filling == 'Professional', 'Не верный статус уровня заполнения'

    def go_to_preview_page(self):  # переход на страницу предпросмотра
        self.browser.execute_script("window.scrollBy(0, 4000);")
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_PREVIEW).click()
        for i in range(10):
            browser_tabs = self.browser.window_handles
            number_of_tabs = len(browser_tabs)
            if number_of_tabs == 2:
                break
            else:
                time.sleep(1)
        self.browser.switch_to.window(self.browser.window_handles[1])

    def submitting_resume_change_for_publication(self,):  # отправка изменений резюме на публикацию
        time.sleep(3)
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_PUBLISH).click()
