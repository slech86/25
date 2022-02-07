import time
import os
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import AddResumePageLocators


class AddResumePage(BasePage):
    def filling_in_required_fields(self):  # заполнение обязательных полей
        self.browser.find_element(*AddResumePageLocators.FIELD_NAME).send_keys(TestData.name_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_SURNAME).send_keys(TestData.surname_resume)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_OF_BIRTH).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_SEPTEMBER).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_DAY).click()
        self.browser.find_element(*AddResumePageLocators.DAY_5).click()

        self.browser.find_element(*AddResumePageLocators.FIELD_GENDER).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_COUNTRY).click()
        self.browser.find_element(*AddResumePageLocators.COUNTRY_UKRAINE).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_CITI).click()
        self.browser.find_element(*AddResumePageLocators.CITI_ODESSA).click()
        # блок "Личная информация"

        self.browser.find_element(*AddResumePageLocators.FIELD_PHONE_1).send_keys(TestData.phone_1_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_EMAIL).send_keys(TestData.email_resume)
        # блок "Контактная информация"

        self.browser.find_element(*AddResumePageLocators.FIELD_JOB_TITLE).send_keys(TestData.job_title_resume)
        self.browser.execute_script(AddResumePageLocators.CATEGORY_RESUME)  # "Категория размещения вакансии" передается параметр уже с ".click()"
        time.sleep(0.2)
        self.browser.find_element(*AddResumePageLocators.SUBCATEGORIES).click()  # "Подкатегории"
        # блок "Желаемая должность"

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY).click()
        self.browser.find_element(*AddResumePageLocators.WITHOUT_EXPERIENCE).click()
        # блок "Опыт работы в игорной идустрии"

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_JOB_SEARCH_STATUS).click()
        self.browser.find_element(*AddResumePageLocators.ACTIVELY_LOOKING_FOR_JOB).click()
        # блок "Статус поиска работы"

    def filling_in_optional_fields(self):  # заполнение не обязательных полей
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'фото 120x150.jpeg')
        self.browser.find_element(*AddResumePageLocators.FIELD_PHOTO).send_keys(file_path)

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_WILLING_TO_RELOCATE).click()
        self.browser.find_element(*AddResumePageLocators.NOT_READY_TO_RELOCATE).click()
        # блок "Личная информация"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_PHONE).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_PHONE_2).send_keys(TestData.phone_2_resume)

        self.browser.find_element(*AddResumePageLocators.FIELD_SKYPE).send_keys(TestData.skype_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_PORTFOLIO).send_keys(TestData.portfolio)

        self.browser.find_element(*AddResumePageLocators.BUTTON_FACEBOOK).click()
        self.browser.find_element(*AddResumePageLocators.BUTTON_LINKEDIN).click()
        self.browser.find_element(*AddResumePageLocators.BUTTON_INSTAGRAM).click()
        self.browser.find_element(*AddResumePageLocators.BUTTON_TELEGRAM).click()
        self.browser.find_element(*AddResumePageLocators.BUTTON_TWITTER).click()
        self.browser.find_element(*AddResumePageLocators.BUTTON_VK).click()

        self.browser.find_element(*AddResumePageLocators.FIELD_FACEBOOK).send_keys(TestData.facebook_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_LINKEDIN).send_keys(TestData.linkedin_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_INSTAGRAM).send_keys(TestData.instagram_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_TELEGRAM).send_keys(TestData.telegram_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_TWITTER).send_keys(TestData.twitter_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_VK).send_keys(TestData.vk_resume)
        # блок "Контактная информация"

        self.browser.find_element(*AddResumePageLocators.DISTANT_WORK).click()
        self.browser.find_element(*AddResumePageLocators.SALARY).send_keys(TestData.salary_resume)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_CURRENCY).click()
        self.browser.find_element(*AddResumePageLocators.CURRENCY_UAH).click()
        # блок "Желаемая должность"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_SKILLS).click()
        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.skills_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_WORK_EXPERIENCE).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_COMPANY_NAME).send_keys(TestData.company_name_resume)
        self.browser.find_element(*AddResumePageLocators.FIELD_SITE_COMPANY).send_keys(TestData.company_site_resume)
        self.browser.find_element(*AddResumePageLocators.SCOPE_OF_COMPANY_CASINO_STAFF).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_POSITION).send_keys(TestData.position_resume)

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_AUGUST_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_START).click()

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_MARCH_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_FINISH).click()

        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_WORK_EXPERIENCE_2).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_COMPANY_NAME_2).send_keys(TestData.company_name_resume_2)
        self.browser.find_element(*AddResumePageLocators.FIELD_SITE_COMPANY_2).send_keys(TestData.company_site_resume_2)
        self.browser.find_element(*AddResumePageLocators.SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_POSITION_2).send_keys(TestData.position_resume_2)

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_APRIL_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_START_2).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_START_2).click()

        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.WORKING_NOW_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2).click()
        # self.browser.find_element(*AddResumePageLocators.YEAR_WORK_EXPERIENCE_FINISH_2).click()

        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.responsibilities_and_achievements)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Навыки и достижения"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_NAME_OF_INSTITUTION).send_keys(TestData.name_of_institution)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LEVEL_OF_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.HIGHER_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_COUNTRY_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.COUNTRY_UKRAINE_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_CITI_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.CITI_KHARKOV_EDUCATION).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_DEPARTMENT_AND_SPECIALITY).send_keys(TestData.department_and_speciality)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_EDUCATION_START).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_SEPTEMBER_EDUCATION_START).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_EDUCATION_START).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_EDUCATION_START).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_EDUCATION_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_MAY_EDUCATION_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_EDUCATION_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_EDUCATION_FINISH).click()

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_NAME_OF_INSTITUTION_2).send_keys(TestData.name_of_institution_2)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LEVEL_OF_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.SECONDARY_SPECIAL_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_COUNTRY_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.COUNTRY_BELARUS_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_CITI_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.CITI_MINSK_EDUCATION_2).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2).send_keys(TestData.department_and_speciality_2)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_EDUCATION_START_2).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_NOVEMBER_EDUCATION_START_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_EDUCATION_START_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_EDUCATION_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_JANUARY_EDUCATION_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_EDUCATION_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_EDUCATION_FINISH_2).click()
        # блок "Образование"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_COURSES_AND_CERTIFICATES).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE).send_keys(TestData.name_course)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_COURSES_START).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_JUNE_COURSES_START).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_COURSES_START).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_COURSES_START).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_COURSES_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_JUNE_COURSES_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_COURSES_FINISH).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_COURSES_FINISH).click()

        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description)
        self.browser.switch_to.default_content()  # выход из фрейма

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_COURSES_AND_CERTIFICATES_2).click()
        self.browser.find_element(*AddResumePageLocators.FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2).send_keys(TestData.name_course_2)
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_COURSES_START_2).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_OCTOBER_COURSES_START_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_COURSES_START_2).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_COURSES_START_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_MONTH_COURSES_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.MONTH_OCTOBER_COURSES_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_YEAR_COURSES_FINISH_2).click()
        self.browser.find_element(*AddResumePageLocators.YEAR_COURSES_FINISH_2).click()

        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.course_description_2)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Курсы и сертификаты"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_LANGUAGE).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LANGUAGE_1).click()
        self.browser.find_element(*AddResumePageLocators.POLISH_LANGUAGE_1).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_1).click()
        self.browser.find_element(*AddResumePageLocators.HIGH_LEVEL_1).click()

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_LANGUAGE_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LANGUAGE_2).click()
        self.browser.find_element(*AddResumePageLocators.GERMAN_LANGUAGE_2).click()
        self.browser.find_element(*AddResumePageLocators.DROPDOWN_LEVEL_OF_LANGUAGE_2).click()
        self.browser.find_element(*AddResumePageLocators.FREE_LEVEL_2).click()
        # блок "Знание языков"

        radio = self.browser.find_element(*AddResumePageLocators.RADIO_I_DONT_HAVE_DISABILITY)
        radio_checked = radio.get_attribute("checked")
        assert radio_checked is not None, "Не установлено 'У меня нет инвалидности' по умолчанию"
        # блок "Инвалидность"

        self.browser.find_element(*AddResumePageLocators.BUTTON_ADD_ADDITIONAL_INFORMATION).click()

        iframe = self.browser.find_element(*AddResumePageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AddResumePageLocators.CKEDITOR)
        CKEditor.send_keys(TestData.additional_information)
        self.browser.switch_to.default_content()  # выход из фрейма
        # блок "Дополнительная информация"

    def percentage_check_of_resume_completion(self):  # проверка заполнения резюме в процентах
        percent = self.browser.find_element(*AddResumePageLocators.RESUME_COMPLETED_ON).text
        assert percent == '100', 'Не верный процент заполнения резюме'

    def checking_status_level_filling_resume(self, language):  # проверка статуса уровня заполнения резюме
        status_level_filling = self.browser.find_element(*AddResumePageLocators.STATUS_OF_YOUR_RESUME).text
        if language == "/ua":
            assert status_level_filling == 'Професійне', 'Не верный статус уровня заполнения'
        else:
            assert status_level_filling == 'Профессиональное', 'Не верный статус уровня заполнения'

    def submitting_resume_for_publication(self,):  # отправка резюме на публикацию
        self.browser.find_element(*AddResumePageLocators.BUTTON_PUBLISH).click()