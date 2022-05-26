import time
import os
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import ResumeAddPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumeAddPage(BasePage):
    def filling_in_required_fields(self, job_title):  # заполнение обязательных полей
        self.browser.find_element(*ResumeAddPageLocators.FIELD_NAME).send_keys(TestData.name_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_SURNAME).send_keys(TestData.surname_resume)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_OF_BIRTH).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_SEPTEMBER).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*ResumeAddPageLocators.DAY_5).click()

        self.browser.find_element(*ResumeAddPageLocators.FIELD_GENDER).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*ResumeAddPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeAddPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.5)
        city_list = self.browser.find_elements(*ResumeAddPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '698740')  # 698740 - id Odessa

        locator_with_position_city = ResumeAddPageLocators()
        city_odessa = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_odessa).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))
        # блок "Личная информация"

        self.browser.find_element(*ResumeAddPageLocators.FIELD_PHONE_1).send_keys(TestData.phone_1_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_EMAIL).send_keys(TestData.email_resume)
        # блок "Контактная информация"

        self.browser.find_element(*ResumeAddPageLocators.FIELD_JOB_TITLE).send_keys(job_title)
        self.browser.execute_script(ResumeAddPageLocators.CATEGORY_RESUME)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        self.browser.find_element(*ResumeAddPageLocators.SUBCATEGORIES).click()  # "Подкатегории"
        # блок "Желаемая должность"

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY).click()
        self.browser.find_element(*ResumeAddPageLocators.WITHOUT_EXPERIENCE).click()
        # блок "Опыт работы в игорной индустрии"

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_JOB_SEARCH_STATUS).click()
        self.browser.find_element(*ResumeAddPageLocators.ACTIVELY_LOOKING_FOR_JOB).click()
        # блок "Статус поиска работы"

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'фото 120x150.jpeg')
        self.browser.find_element(*ResumeAddPageLocators.FIELD_PHOTO).send_keys(file_path)

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_WILLING_TO_RELOCATE).click()
        self.browser.find_element(*ResumeAddPageLocators.NOT_READY_TO_RELOCATE).click()
        # блок "Личная информация"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_PHONE).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_PHONE_2).send_keys(TestData.phone_2_resume)

        self.browser.find_element(*ResumeAddPageLocators.FIELD_SKYPE).send_keys(TestData.skype_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_PORTFOLIO).send_keys(TestData.portfolio)

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_VK).click()

        self.browser.find_element(*ResumeAddPageLocators.FIELD_FACEBOOK).send_keys(TestData.facebook_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_LINKEDIN).send_keys(TestData.linkedin_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_INSTAGRAM).send_keys(TestData.instagram_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_TWITTER).send_keys(TestData.twitter_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_VK).send_keys(TestData.vk_resume)
        # блок "Контактная информация"

        self.browser.find_element(*ResumeAddPageLocators.DISTANT_WORK).click()
        self.browser.find_element(*ResumeAddPageLocators.SALARY).send_keys(TestData.salary_resume)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*ResumeAddPageLocators.CURRENCY_UAH).click()
        # блок "Желаемая должность"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_SKILLS).click()
        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.skills_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_WORK_EXPERIENCE).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_COMPANY_NAME).send_keys(TestData.company_name_resume)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_SITE_COMPANY).send_keys(TestData.company_site_resume)
        self.browser.find_element(*ResumeAddPageLocators.SCOPE_OF_COMPANY_CASINO_STAFF).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_POSITION).send_keys(TestData.position_resume)

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_AUGUST_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_WORK_EXPERIENCE_START).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_MARCH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_WORK_EXPERIENCE_FINISH).click()

        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_WORK_EXPERIENCE_2).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_COMPANY_NAME_2).send_keys(TestData.company_name_resume_2)
        self.browser.find_element(*ResumeAddPageLocators.FIELD_SITE_COMPANY_2).send_keys(TestData.company_site_resume_2)
        self.browser.find_element(*ResumeAddPageLocators.SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_POSITION_2).send_keys(TestData.position_resume_2)

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_APRIL_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_WORK_EXPERIENCE_START_2).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.WORKING_NOW_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_FINISH_2).click()

        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements_2)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Опыт работы"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_EDUCATION).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_NAME_OF_INSTITUTION).send_keys(TestData.name_of_institution)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LEVEL_OF_EDUCATION).click()
        self.browser.find_element(*ResumeAddPageLocators.HIGHER_EDUCATION).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_COUNTRY_EDUCATION).click()

        country_list_education = self.browser.find_elements(*ResumeAddPageLocators.COUNTRY_EDUCATION_LIST)

        determining_position_of_object_in_drop_down_list(country_list_education, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeAddPageLocators()
        country_ukraine_education = locator_with_position_country.assembly_of_locators_with_position_country_education()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine_education).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_CITI_EDUCATION).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddPageLocators.CITY_EDUCATION_LIST)

        determining_position_of_object_in_drop_down_list(city_list_education, '706483')  # 706483 - id Kharkov

        locator_with_position_city = ResumeAddPageLocators()
        city_kharkov_education = locator_with_position_city.assembly_of_locators_with_position_city_education()  # сборка локаторов с позицией города

        self.browser.find_element(*city_kharkov_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddPageLocators.DROPDOWN_CITI_EDUCATION, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY).send_keys(TestData.department_and_speciality)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_SEPTEMBER_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_MAY_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_EDUCATION_FINISH).click()

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_NAME_OF_INSTITUTION_2).send_keys(TestData.name_of_institution_2)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddPageLocators.SECONDARY_SPECIAL_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_COUNTRY_EDUCATION_2).click()

        country_list_education = self.browser.find_elements(*ResumeAddPageLocators.COUNTRY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(country_list_education, '36')  # 36 - id Belarus

        locator_with_position_country = ResumeAddPageLocators()
        country_belarus_education = locator_with_position_country.assembly_of_locators_with_position_country_education_2()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_belarus_education).click()

        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_CITI_EDUCATION_2).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddPageLocators.CITY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(city_list_education, '625144')  # 625144 - id Minsk

        locator_with_position_city = ResumeAddPageLocators()
        city_minsk_education = locator_with_position_city.assembly_of_locators_with_position_city_education_2()  # сборка локаторов с позицией города

        self.browser.find_element(*city_minsk_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddPageLocators.DROPDOWN_CITI_EDUCATION_2, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2).send_keys(TestData.department_and_speciality_2)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_NOVEMBER_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_JANUARY_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_EDUCATION_FINISH_2).click()
        # блок "Образование"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_COURSES_AND_CERTIFICATES).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE).send_keys(TestData.name_course)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_COURSES_START).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_JUNE_COURSES_START).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_JUNE_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_COURSES_FINISH).click()

        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_COURSES_AND_CERTIFICATES_2).click()
        self.browser.find_element(*ResumeAddPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2).send_keys(TestData.name_course_2)
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_OCTOBER_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_MONTH_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.MONTH_OCTOBER_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_YEAR_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddPageLocators.YEAR_COURSES_FINISH_2).click()

        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description_2)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Курсы и сертификаты"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_LANGUAGE).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddPageLocators.POLISH_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddPageLocators.HIGH_LEVEL_1).click()

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddPageLocators.GERMAN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddPageLocators.FREE_LEVEL_2).click()
        # блок "Знание языков"

        radio = self.browser.find_element(*ResumeAddPageLocators.RADIO_I_DONT_HAVE_DISABILITY)
        radio_checked = radio.get_attribute("checked")
        assert radio_checked is not None, "Не установлено 'У меня нет инвалидности' по умолчанию"
        # блок "Инвалидность"

        self.browser.find_element(*ResumeAddPageLocators.BUTTON_ADD_ADDITIONAL_INFORMATION).click()

        iframe = self.browser.find_element(*ResumeAddPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additional_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

    def percentage_check_of_resume_completion(self):  # проверка заполнения резюме в процентах
        percent = self.browser.find_element(*ResumeAddPageLocators.RESUME_COMPLETED_ON).text
        assert percent == '100', 'Не верный процент заполнения резюме'

    def checking_status_level_filling_resume(self, language):  # проверка статуса уровня заполнения резюме
        status_level_filling = self.browser.find_element(*ResumeAddPageLocators.STATUS_OF_YOUR_RESUME).text
        if language == "/ua":
            assert status_level_filling == 'Професійне', 'Не верный статус уровня заполнения'
        elif language == "":
            assert status_level_filling == 'Профессиональное', 'Не верный статус уровня заполнения'
        elif language == "/en":
            assert status_level_filling == 'Professional', 'Не верный статус уровня заполнения'

    def submitting_resume_for_publication(self,):  # отправка резюме на публикацию
        self.browser.find_element(*ResumeAddPageLocators.BUTTON_PUBLISH).click()