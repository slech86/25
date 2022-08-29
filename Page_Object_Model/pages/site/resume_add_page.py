import time
import os
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import ResumeAddEditPageLocators
from Page_Object_Model.utility.utility import determining_position_of_object_in_drop_down_list
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumeAddPage(BasePage):
    def filling_in_field_job_title_for_draft(self):  # заполнение поля "Название должности" для черновика
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_resume_for_draft)

    def filling_in_required_fields(self, job_title):  # заполнение обязательных полей
        self.browser.find_element(*ResumeAddEditPageLocators.TAB).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME).send_keys(TestData.name_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SURNAME).send_keys(TestData.surname_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR).click()

        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_OF_BIRTH_1981).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_SEPTEMBER).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DAY_5).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_GENDER_FEMALE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY).click()

        country_list = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_LIST)

        determining_position_of_object_in_drop_down_list(country_list, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeAddEditPageLocators()
        country_ukraine = locator_with_position_country.assembly_of_locators_with_position_country()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI).click()
        time.sleep(0.7)
        city_list = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_LIST)

        determining_position_of_object_in_drop_down_list(city_list, '698740')  # 698740 - id Odessa

        locator_with_position_city = ResumeAddEditPageLocators()
        city_odessa = locator_with_position_city.assembly_of_locators_with_position_city()  # сборка локаторов с позицией города

        self.browser.find_element(*city_odessa).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI, 'aria-expanded', 'false'))
        # блок "Личная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_1).clear()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_1).send_keys(TestData.phone_1_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_EMAIL).send_keys(TestData.email_resume)
        # блок "Контактная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_JOB_TITLE).send_keys(job_title)
        self.browser.find_element(*ResumeAddEditPageLocators.CATEGORY_RESUME_DESIGN_GRAPHICS_ANIMATION).click()
        time.sleep(0.5)
        self.browser.find_element(*ResumeAddEditPageLocators.SUBCATEGORIES_UX_DESIGNER).click()  # "Подкатегории"
        # блок "Желаемая должность"

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.WITHOUT_EXPERIENCE).click()
        # блок "Опыт работы в игорной индустрии"

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_JOB_SEARCH_STATUS).click()
        self.browser.find_element(*ResumeAddEditPageLocators.ACTIVELY_LOOKING_FOR_JOB).click()
        # блок "Статус поиска работы"

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'фото 120x150.jpeg')
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHOTO).send_keys(file_path)

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_WILLING_TO_RELOCATE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.NOT_READY_TO_RELOCATE).click()
        # блок "Личная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_PHONE).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PHONE_2).send_keys(TestData.phone_2_resume)

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SKYPE).send_keys(TestData.skype_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_PORTFOLIO).send_keys(TestData.portfolio)

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_VK).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_FACEBOOK).send_keys(TestData.facebook_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_LINKEDIN).send_keys(TestData.linkedin_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_INSTAGRAM).send_keys(TestData.instagram_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_TWITTER).send_keys(TestData.twitter_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_VK).send_keys(TestData.vk_resume)
        # блок "Контактная информация"

        self.browser.find_element(*ResumeAddEditPageLocators.DISTANT_WORK).click()
        self.browser.find_element(*ResumeAddEditPageLocators.SALARY).send_keys(TestData.salary_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*ResumeAddEditPageLocators.CURRENCY_UAH).click()
        # блок "Желаемая должность"

        locators_from_id_block = ResumeAddEditPageLocators()
        button_add_skills = locators_from_id_block.assembly_of_locators_from_id_block('skills-and-achievements')
        self.browser.find_element(*button_add_skills['button_add_block']).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.skills_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        # блок "Опыт работы"
        button_add_work_experience = locators_from_id_block.assembly_of_locators_from_id_block('work-experience')
        self.browser.find_element(*button_add_work_experience['button_add_block']).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_COMPANY_NAME).send_keys(TestData.company_name_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SITE_COMPANY).send_keys(TestData.company_site_resume)
        self.browser.find_element(*ResumeAddEditPageLocators.SCOPE_OF_COMPANY_CASINO_STAFF).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_POSITION).send_keys(TestData.position_resume)

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_AUGUST_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_START_2018).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_MARCH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_FINISH_2020).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_WORK_EXPERIENCE_NUMBER_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_COMPANY_NAME_2).send_keys(TestData.company_name_resume_2)
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_SITE_COMPANY_2).send_keys(TestData.company_site_resume_2)
        self.browser.find_element(*ResumeAddEditPageLocators.SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_POSITION_2).send_keys(TestData.position_resume_2)

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_APRIL_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_WORK_EXPERIENCE_START_2020_2).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.WORKING_NOW_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_FINISH_2).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements_2)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Опыт работы"

        button_add_education = locators_from_id_block.assembly_of_locators_from_id_block('education')
        self.browser.find_element(*button_add_education['button_add_block']).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION).send_keys(TestData.name_of_institution)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION).click()
        self.browser.find_element(*ResumeAddEditPageLocators.HIGHER_EDUCATION).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY_EDUCATION).click()

        country_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_EDUCATION_LIST)

        determining_position_of_object_in_drop_down_list(country_list_education, '222')  # 222 - id Ukraine

        locator_with_position_country = ResumeAddEditPageLocators()
        country_ukraine_education = locator_with_position_country.assembly_of_locators_with_position_country_education()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_ukraine_education).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_EDUCATION_LIST)

        determining_position_of_object_in_drop_down_list(city_list_education, '706483')  # 706483 - id Kharkov

        locator_with_position_city = ResumeAddEditPageLocators()
        city_kharkov_education = locator_with_position_city.assembly_of_locators_with_position_city_education()  # сборка локаторов с позицией города

        self.browser.find_element(*city_kharkov_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY).send_keys(TestData.department_and_speciality)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_SEPTEMBER_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_START_2010).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_MAY_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_FINISH_2015).click()

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_EDUCATION_NUMBER_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_2).send_keys(TestData.name_of_institution_2)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.SECONDARY_SPECIAL_EDUCATION_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_COUNTRY_EDUCATION_2).click()

        country_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.COUNTRY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(country_list_education, '36')  # 36 - id Belarus

        locator_with_position_country = ResumeAddEditPageLocators()
        country_belarus_education = locator_with_position_country.assembly_of_locators_with_position_country_education_2()  # сборка локаторов с позицией страны
        self.browser.find_element(*country_belarus_education).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_2).click()
        time.sleep(0.5)
        city_list_education = self.browser.find_elements(*ResumeAddEditPageLocators.CITY_EDUCATION_LIST_2)

        determining_position_of_object_in_drop_down_list(city_list_education, '625144')  # 625144 - id Minsk

        locator_with_position_city = ResumeAddEditPageLocators()
        city_minsk_education = locator_with_position_city.assembly_of_locators_with_position_city_education_2()  # сборка локаторов с позицией города

        self.browser.find_element(*city_minsk_education).click()
        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element_attribute(ResumeAddEditPageLocators.DROPDOWN_CITI_EDUCATION_2, 'aria-expanded', 'false'))

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2).send_keys(TestData.department_and_speciality_2)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_NOVEMBER_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_START_2018_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JANUARY_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_EDUCATION_FINISH_2020_2).click()
        # блок "Образование"

        button_add_courses_and_certificates = locators_from_id_block.assembly_of_locators_from_id_block('courses-and-certificates')
        self.browser.find_element(*button_add_courses_and_certificates['button_add_block']).click()

        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE).send_keys(TestData.name_course)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JUNE_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_START).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_START_2020).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_JUNE_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_FINISH_2021).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_COURSES_NUMBER_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2).send_keys(TestData.name_course_2)
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_OCTOBER_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_START_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_START_2014_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_MONTH_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.MONTH_OCTOBER_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_YEAR_COURSES_FINISH_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.YEAR_COURSES_FINISH_2015_2).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description_2)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Курсы и сертификаты"

        button_add_language = locators_from_id_block.assembly_of_locators_from_id_block('knowledge-of-languages')
        self.browser.find_element(*button_add_language['button_add_block']).click()

        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.POLISH_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*ResumeAddEditPageLocators.HIGH_LEVEL_1).click()

        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_ADD_LANGUAGE_NUMBER_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.GERMAN_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*ResumeAddEditPageLocators.FREE_LEVEL_2).click()
        # блок "Знание языков"

        radio = self.browser.find_element(*ResumeAddEditPageLocators.RADIO_I_DONT_HAVE_DISABILITY)
        radio_checked = radio.get_attribute("checked")
        assert radio_checked is not None, "Не установлено 'У меня нет инвалидности' по умолчанию"
        # блок "Инвалидность"

        button_add_additional_information = locators_from_id_block.assembly_of_locators_from_id_block('additional-information')
        self.browser.find_element(*button_add_additional_information['button_add_block']).click()

        iframe = self.browser.find_element(*ResumeAddEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*ResumeAddEditPageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additional_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

    def percentage_check_of_resume_completion(self):  # проверка заполнения резюме в процентах
        percent = self.browser.find_element(*ResumeAddEditPageLocators.RESUME_COMPLETED_ON).text
        assert percent == '100', 'Не верный процент заполнения резюме'

    def checking_status_level_filling_resume(self, language):  # проверка статуса уровня заполнения резюме
        status_level_filling = self.browser.find_element(*ResumeAddEditPageLocators.STATUS_OF_YOUR_RESUME).text
        if language == "/ua":
            assert status_level_filling == 'Професійне', 'Не верный статус уровня заполнения'
        elif language == "":
            assert status_level_filling == 'Профессиональное', 'Не верный статус уровня заполнения'
        elif language == "/en":
            assert status_level_filling == 'Professional', 'Не верный статус уровня заполнения'

    def checking_field_job_title_validation_message_about_need_to_fill_out(self, language):  # проверка сообщения валидации поля "Название должности" о необходимости его заполнения
        validation_message = WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(ResumeAddEditPageLocators.VALIDATION_MESSAGE_FIELD_JOB_TITLE)).text
        if language == "":
            assert validation_message == "Необходимо заполнить «Название должности».", f"Не верное сообщение валидации, expected result: 'Необходимо заполнить «Название должности».', actual result: '{validation_message}'"
        elif language == "/ua":
            assert validation_message == 'Необхідно заповнити "Назва посади".', f'Не верное сообщение валидации, expected result: "Необхідно заповнити "Назва посади".", actual result: "{validation_message}"'
        elif language == "/en":
            assert validation_message == "Job title cannot be blank.", f"Не верное сообщение валидации, expected result: 'Job title cannot be blank.', actual result: '{validation_message}'"

    def submitting_resume_for_publication(self,):  # отправка резюме на публикацию
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_PUBLISH).click()

    def adding_resume_to_draft(self):  # добавление резюме в черновик
        self.browser.find_element(*ResumeAddEditPageLocators.BUTTON_TO_DRAFTS).click()
