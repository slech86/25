from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminResumeEditPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing, Accounts
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.singleton import Singleton
import time


class AdminResumeEditPage(BasePage):
    def change_resume_status_to_published(self):  # изменение статуса резюме на 'Опубликовано'
        time.sleep(2)
        self.browser.find_element(*AdminResumeEditPageLocators.FIELD_RESUME_STATUS).click()
        self.browser.find_element(*AdminResumeEditPageLocators.STATUS_PUBLISHED).click()
        time.sleep(3)
        self.browser.find_element(*AdminResumeEditPageLocators.BUTTON_SAVE).click()

    def verification_of_saving_data_entered_by_user_after_resume_creation_ru(self, language, uah_rate, key):  # проверка сохранения введенных пользователем данных после создания резюме RU
        user = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_USER)
        user_title = user.get_attribute("title")
        if language == '/ua':
            assert '(' + Singleton.logins_and_mails[key][1][0] + ')' in user_title, "Поле 'Пользователь' не верно"
        elif language == "":
            assert '(' + Singleton.logins_and_mails[key][0][0] + ')' in user_title, "Поле 'Пользователь' не верно"
        elif language == "/en":
            assert '(' + Singleton.logins_and_mails[key][2][0] + ')' in user_title, "Поле 'Пользователь' не верно"

        job_search_status = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_JOB_SEARCH_STATUS)
        job_search_status_title = job_search_status.get_attribute("title")
        assert job_search_status_title == TestData.job_search_status, "Поле 'Статус поиска работы' не верно"

        name_course = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_NAME_COURSE_1)
        name_course_value = name_course.get_attribute("value")
        assert name_course_value == TestData.name_course, "Поле 'Курс или сертификат: Название 1' не верно"

        course_period_start = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COURSE_PERIOD_START_1)
        course_period_start_value = course_period_start.get_attribute("value")
        assert course_period_start_value == TestData.course_period_start, "Поле 'Курс или сертификат: Начало 1' не верно"

        course_period_finish = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COURSE_PERIOD_FINISH_1)
        course_period_finish_value = course_period_finish.get_attribute("value")
        assert course_period_finish_value == TestData.course_period_finish, "Поле 'Курс или сертификат: Окончание 1' не верно"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_1)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.course_description, "Поле 'Курс или сертификат: Описание 1' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        name_course_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_NAME_COURSE_2)
        name_course_2_value = name_course_2.get_attribute("value")
        assert name_course_2_value == TestData.name_course_2, "Поле 'Курс или сертификат: Название 2' не верно"

        course_period_start_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COURSE_PERIOD_START_2)
        course_period_start_2_value = course_period_start_2.get_attribute("value")
        assert course_period_start_2_value == TestData.course_period_start_2, "Поле 'Курс или сертификат: Начало 2' не верно"

        course_period_finish_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COURSE_PERIOD_FINISH_2)
        course_period_finish_2_value = course_period_finish_2.get_attribute("value")
        assert course_period_finish_2_value == TestData.course_period_finish_2, "Поле 'Курс или сертификат: Окончание 2' не верно"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_COURSE_DESCRIPTION_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.course_description_2, "Поле 'Курс или сертификат: Описание 2' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        name_of_institution = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_1)
        name_of_institution_value = name_of_institution.get_attribute("value")
        assert name_of_institution_value == TestData.name_of_institution, "Поле 'Образование: Название учебного заведения 1' не верно"

        level_of_education = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LEVEL_OF_EDUCATION_1)
        level_of_education_title = level_of_education.get_attribute("title")
        assert level_of_education_title == TestData.level_of_education, "Поле 'Образование: Уровень образования 1' не верно"

        country_education = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COUNTRY_EDUCATION_1)
        country_education_title = country_education.get_attribute("title")
        assert country_education_title == TestData.country_education, "Поле 'Образование: Страна 1' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminResumeEditPageLocators.FIELD_CITY_EDUCATION_1), TestData.city_education))
        city_education = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_CITY_EDUCATION_1)
        city_education_title = city_education.get_attribute("title")
        assert city_education_title == TestData.city_education, "Поле 'Образование: Город 1' не верно"

        department_and_speciality = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_1)
        department_and_speciality_value = department_and_speciality.get_attribute("value")
        assert department_and_speciality_value == TestData.department_and_speciality, "Поле 'Образование: Факультет и специальность 1' не верно"

        education_period_start = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EDUCATION_PERIOD_START_1)
        education_period_start_value = education_period_start.get_attribute("value")
        assert education_period_start_value == TestData.education_period_start, "Поле 'Образование: Срок обучения - start 1' не верно"

        education_period_finish = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EDUCATION_PERIOD_FINISH_1)
        education_period_finish_value = education_period_finish.get_attribute("value")
        assert education_period_finish_value == TestData.education_period_finish, "Поле 'Образование: Срок обучения - finish 1' не верно"

        name_of_institution_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_NAME_OF_INSTITUTION_2)
        name_of_institution_2_value = name_of_institution_2.get_attribute("value")
        assert name_of_institution_2_value == TestData.name_of_institution_2, "Поле 'Образование: Название учебного заведения 2' не верно"

        level_of_education_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LEVEL_OF_EDUCATION_2)
        level_of_education_2_title = level_of_education_2.get_attribute("title")
        assert level_of_education_2_title == TestData.level_of_education_2, "Поле 'Образование: Уровень образования 2' не верно"

        country_education_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COUNTRY_EDUCATION_2)
        country_education_2_title = country_education_2.get_attribute("title")
        assert country_education_2_title == TestData.country_education_2, "Поле 'Образование: Страна 2' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminResumeEditPageLocators.FIELD_CITY_EDUCATION_2), TestData.city_education_2))
        city_education_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_CITY_EDUCATION_2)
        city_education_2_title = city_education_2.get_attribute("title")
        assert city_education_2_title == TestData.city_education_2, "Поле 'Образование: Город 2' не верно"

        department_and_speciality_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_DEPARTMENT_AND_SPECIALITY_2)
        department_and_speciality_2_value = department_and_speciality_2.get_attribute("value")
        assert department_and_speciality_2_value == TestData.department_and_speciality_2, "Поле 'Образование: Факультет и специальность 2' не верно"

        education_period_start_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EDUCATION_PERIOD_START_2)
        education_period_start_2_value = education_period_start_2.get_attribute("value")
        assert education_period_start_2_value == TestData.education_period_start_2, "Поле 'Образование: Срок обучения - start 2' не верно"

        education_period_finish_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EDUCATION_PERIOD_FINISH_2)
        education_period_finish_2_value = education_period_finish_2.get_attribute("value")
        assert education_period_finish_2_value == TestData.education_period_finish_2, "Поле 'Образование: Срок обучения - finish 2' не верно"

        company_name_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COMPANY_NAME_RESUME_1)
        company_name_resume_value = company_name_resume.get_attribute("value")
        assert company_name_resume_value == TestData.company_name_resume, "Поле 'Опыт работы: Компания 1' не верно"

        company_site_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COMPANY_SITE_RESUME_1)
        company_site_resume_value = company_site_resume.get_attribute("value")
        assert company_site_resume_value == TestData.company_site_resume, "Поле 'Опыт работы: Сайт компании 1' не верно"

        scope_of_company = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SCOPE_OF_COMPANY_1)
        scope_of_company_title = scope_of_company.get_attribute("title")
        assert scope_of_company_title == TestData.scope_of_company, "Поле 'Опыт работы: Сфера деятельности компании 1' не верно"

        position_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_POSITION_RESUME_1)
        position_resume_value = position_resume.get_attribute("value")
        assert position_resume_value == TestData.position_resume, "Поле 'Опыт работы: Должность 1' не верно"

        work_period_start = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_WORK_PERIOD_START_1)
        work_period_start_value = work_period_start.get_attribute("value")
        assert work_period_start_value == TestData.work_period_start, "Поле 'Опыт работы: Период работы - start 1' не верно"

        work_period_finish = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_WORK_PERIOD_FINISH_1)
        work_period_finish_value = work_period_finish.get_attribute("value")
        assert work_period_finish_value == TestData.work_period_finish, "Поле 'Опыт работы: Период работы - finish 1' не верно"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_1)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.responsibilities_and_achievements, "Поле 'Опыт работы: Обязанности и достижения 1' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        company_name_resume_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COMPANY_NAME_RESUME_2)
        company_name_resume_2_value = company_name_resume_2.get_attribute("value")
        assert company_name_resume_2_value == TestData.company_name_resume_2, "Поле 'Опыт работы: Компания 2' не верно"

        company_site_resume_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COMPANY_SITE_RESUME_2)
        company_site_resume_2_value = company_site_resume_2.get_attribute("value")
        assert company_site_resume_2_value == TestData.company_site_resume_2, "Поле 'Опыт работы: Сайт компании 2' не верно"

        scope_of_company_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SCOPE_OF_COMPANY_2)
        scope_of_company_2_title = scope_of_company_2.get_attribute("title")
        assert scope_of_company_2_title == TestData.scope_of_company_2, "Поле 'Опыт работы: Сфера деятельности компании 2' не верно"

        position_resume_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_POSITION_RESUME_2)
        position_resume_2_value = position_resume_2.get_attribute("value")
        assert position_resume_2_value == TestData.position_resume_2, "Поле 'Опыт работы: Должность 2' не верно"

        work_period_start_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_WORK_PERIOD_START_2)
        work_period_start_2_value = work_period_start_2.get_attribute("value")
        assert work_period_start_2_value == TestData.work_period_start_2, "Поле 'Опыт работы: Период работы - start 2' не верно"

        checkbox_get_news_2 = self.browser.find_element(*AdminResumeEditPageLocators.CHECKBOX_WORK_PERIOD_FINISH_2)
        checkbox_get_news_2_checked = checkbox_get_news_2.get_attribute("checked")
        assert checkbox_get_news_2_checked is not None, "Не установлено 'Опыт работы: По настоящее время 2'"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.responsibilities_and_achievements_2, "Поле 'Опыт работы: Обязанности и достижения 2' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        language_resume_1 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LANGUAGE_RESUME_1)
        language_resume_1_title = language_resume_1.get_attribute("title")
        assert language_resume_1_title == TestData.language_resume_1, "Поле 'Язык 1' не верно"

        level_language_resume_1 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LEVEL_LANGUAGE_RESUME_1)
        level_language_resume_1_title = level_language_resume_1.get_attribute("title")
        assert level_language_resume_1_title == TestData.level_language_resume_1, "Поле 'Уровень владения 1' не верно"

        language_resume_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LANGUAGE_RESUME_2)
        language_resume_2_title = language_resume_2.get_attribute("title")
        assert language_resume_2_title == TestData.language_resume_2, "Поле 'Язык 2' не верно"

        level_language_resume_2 = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LEVEL_LANGUAGE_RESUME_2)
        level_language_resume_2_title = level_language_resume_2.get_attribute("title")
        assert level_language_resume_2_title == TestData.level_language_resume_2, "Поле 'Уровень владения 2' не верно"

        name_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_NAME)
        name_resume_value = name_resume.get_attribute("value")
        assert name_resume_value == TestData.name_resume, "Поле 'Ваше имя' не верно"

        surname_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SURNAME)
        surname_resume_value = surname_resume.get_attribute("value")
        assert surname_resume_value == TestData.surname_resume, "Поле 'Фамилия' не верно"

        birthday_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_BIRTHDAY)
        birthday_resume_value = birthday_resume.get_attribute("value")
        assert birthday_resume_value == TestData.birthday_resume, "Поле 'Дата рождения' не верно"

        gender_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_GENDER)
        gender_resume_title = gender_resume.get_attribute("title")
        assert gender_resume_title == TestData.gender_resume, "Поле 'Пол' не верно"

        country_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_COUNTRY_RESUME)
        country_resume_title = country_resume.get_attribute("title")
        assert country_resume_title == TestData.country_resume, "Поле 'Страна' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminResumeEditPageLocators.FIELD_CITY_RESUME), TestData.city_resume))
        city_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_CITY_RESUME)
        city_resume_title = city_resume.get_attribute("title")
        assert city_resume_title == TestData.city_resume, "Поле 'Город' не верно"

        willing_to_relocate = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_WILLING_TO_RELOCATE)
        willing_to_relocate_title = willing_to_relocate.get_attribute("title")
        assert willing_to_relocate_title == TestData.willing_to_relocate, "Поле 'Готовность к переезду' не верно"

        phone_1_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_PHONE_1)
        phone_1_resume_value = phone_1_resume.get_attribute("value")
        assert phone_1_resume_value == TestData.phone_1_resume, "Поле 'Телефон 1' не верно"

        phone_2_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_PHONE_2)
        phone_2_resume_value = phone_2_resume.get_attribute("value")
        assert phone_2_resume_value == TestData.phone_2_resume, "Поле 'Телефон 2' не верно"

        email_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EMAIL)
        email_resume_value = email_resume.get_attribute("value")
        assert email_resume_value == TestData.email_resume, "Поле 'Email' не верно"

        skype_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SKYPE)
        skype_resume_value = skype_resume.get_attribute("value")
        assert skype_resume_value == TestData.skype_resume, "Поле 'Skype' не верно"

        portfolio = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_PORTFOLIO)
        portfolio_value = portfolio.get_attribute("value")
        assert portfolio_value == TestData.portfolio, "Поле 'Портфолио' не верно"

        facebook_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_FACEBOOK)
        facebook_resume_value = facebook_resume.get_attribute("value")
        assert facebook_resume_value == TestData.facebook_resume, "Поле 'Facebook' не верно"

        linkedin_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_LINKEDIN)
        linkedin_resume_value = linkedin_resume.get_attribute("value")
        assert linkedin_resume_value == TestData.linkedin_resume, "Поле 'Linkedin' не верно"

        instagram_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_INSTAGRAM)
        instagram_resume_value = instagram_resume.get_attribute("value")
        assert instagram_resume_value == TestData.instagram_resume, "Поле 'Instagram' не верно"

        telegram_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_TELEGRAM)
        telegram_resume_value = telegram_resume.get_attribute("value")
        assert telegram_resume_value == TestData.telegram_resume, "Поле 'Telegram' не верно"

        twitter_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_TWITTER)
        twitter_resume_value = twitter_resume.get_attribute("value")
        assert twitter_resume_value == TestData.twitter_resume, "Поле 'Twitter' не верно"

        vk_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_VK)
        vk_resume_value = vk_resume.get_attribute("value")
        assert vk_resume_value == TestData.vk_resume, "Поле 'VK' не верно"

        job_title_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_JOB_TITLE)
        job_title_resume_value = job_title_resume.get_attribute("value")
        assert job_title_resume_value == TestData.job_title_resume, "Поле 'Название должности' не верно"

        category_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_CATEGORY_RESUME)
        category_resume_title = category_resume.get_attribute("title")
        assert category_resume_title == TestData.category_resume, "Поле 'Категория резюме' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminResumeEditPageLocators.FIELD_SUBCATEGORIES_RESUME), TestData.subcategories_resume))
        subcategories_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SUBCATEGORIES_RESUME)
        subcategories_resume_title = subcategories_resume.get_attribute("title")
        assert subcategories_resume_title == TestData.subcategories_resume, "Поле 'Подкатегории' не верно"

        employment_type_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EMPLOYMENT_TYPE_RESUME)
        employment_type_resume_title = employment_type_resume.get_attribute("title")
        assert employment_type_resume_title == TestData.employment_type_resume, "Поле 'Тип занятости' не верно"

        salary_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SALARY_RESUME)
        salary_resume_value = salary_resume.get_attribute("value")
        assert salary_resume_value == TestData.salary_resume, "Поле 'Желаемый уровень заработной' не верно"

        salary_resume_usd = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_SALARY_RESUME_USD)
        salary_resume_usd_value = salary_resume_usd.get_attribute("value")
        assert int(salary_resume_usd_value) == round(int(TestData.salary_resume) / uah_rate), "Поле 'Желаемый уровень заработной (USD)' не верно"

        currency_resume = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_CURRENCY_RESUME)
        currency_resume_title = currency_resume.get_attribute("title")
        assert TestData.currency_resume in currency_resume_title, "Поле 'Валюта желаемого уровня зар. платы' не верно"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.skills_and_achievements, "Поле 'Навыки и достижения' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        disability = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_DISABILITY)
        disability_title = disability.get_attribute("title")
        assert disability_title == TestData.disability, "Поле 'Инвалидность' не верно"

        iframe = self.browser.find_element(*AdminResumeEditPageLocators.IFRAME_CKEDITOR_ADDITIONAL_INFORMATION)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminResumeEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.additional_information, "Поле 'Дополнительная информация' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        experience_in_gambling_industry = self.browser.find_element(*AdminResumeEditPageLocators.FIELD_EXPERIENCE_IN_GAMBLING_INDUSTRY)
        experience_in_gambling_industry_title = experience_in_gambling_industry.get_attribute("title")
        assert experience_in_gambling_industry_title == TestData.experience_in_gambling_industry, "Поле 'Общий опыт работы в игорной индустрии' не верно"
