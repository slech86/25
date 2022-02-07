from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminVacancyEditPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing, Accounts
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class AdminVacancyEditPage(BasePage):
    def change_vacancy_status_to_published(self):  # изменение статуса вакансии на 'Опубликовано'
        self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_VACANCY_STATUS).click()
        self.browser.find_element(*AdminVacancyEditPageLocators.STATUS_PUBLISHED).click()
        time.sleep(2)
        self.browser.find_element(*AdminVacancyEditPageLocators.BUTTON_SAVE).click()

    def verification_of_saving_data_entered_by_user_after_vacancy_is_created_ru(self, language):  # проверка сохранения введенных пользователем данных после создания вакансии RU
        user = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_USER)
        user_title = user.get_attribute("title")
        if language == '/ua':
            assert '(' + TestData.login_ua + ')' in user_title, "Поле 'Пользователь' не верно"
        else:
            assert '(' + TestData.login_ru + ')' in user_title, "Поле 'Пользователь' не верно"

        job_title_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_JOB_TITLE)
        job_title_vacancy_value = job_title_vacancy.get_attribute("value")
        assert job_title_vacancy_value == TestData.job_title_vacancy, "Поле 'Название должности' не верно"

        category_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_JOB_CATEGORY)
        category_vacancy_title = category_vacancy.get_attribute("title")
        assert category_vacancy_title == TestData.category_vacancy, "Поле 'Категория вакансии' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminVacancyEditPageLocators.FIELD_JOB_SUBCATEGORIES), TestData.subcategories_vacancy))
        subcategories_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_JOB_SUBCATEGORIES)
        subcategories_vacancy_title = subcategories_vacancy.get_attribute("title")
        assert subcategories_vacancy_title == TestData.subcategories_vacancy, "Поле 'Подкатегории' не верно"

        salary_min = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_SALARY_MIN)
        salary_min_value = salary_min.get_attribute("value")
        assert salary_min_value == TestData.salary_min, "Поле 'Диапазон зарплаты - min' не верно"

        salary_max = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_SALARY_MAX)
        salary_max_value = salary_max.get_attribute("value")
        assert salary_max_value == TestData.salary_max, "Поле 'Диапазон зарплаты - max' не верно"

        currency_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_CURRENCY_VACANCY)
        currency_vacancy_title = currency_vacancy.get_attribute("title")
        assert TestData.currency_vacancy in currency_vacancy_title, "Поле 'Валюта желаемого уровня зар. платы' не верно"

        country_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_COUNTRY_VACANCY)
        country_vacancy_title = country_vacancy.get_attribute("title")
        assert country_vacancy_title == TestData.country_vacancy, "Поле 'Расположение вакансии - country' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminVacancyEditPageLocators.FIELD_CITY_VACANCY), TestData.city_vacancy))
        city_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_CITY_VACANCY)
        city_vacancy_title = city_vacancy.get_attribute("title")
        assert city_vacancy_title == TestData.city_vacancy, "Поле 'Расположение вакансии - city' не верно"

        street_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_STREET_VACANCY)
        street_vacancy_value = street_vacancy.get_attribute("value")
        assert street_vacancy_value == TestData.street_vacancy, "Поле 'Улица' не верно"

        phone_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_PHONE)
        phone_vacancy_value = phone_vacancy.get_attribute("value")
        assert phone_vacancy_value == TestData.phone_vacancy, "Поле 'Телефон' не верно"

        email_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_EMAIL)
        email_vacancy_value = email_vacancy.get_attribute("value")
        assert email_vacancy_value == TestData.email_vacancy, "Поле 'Email' не верно"

        skype_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_SKYPE)
        skype_vacancy_value = skype_vacancy.get_attribute("value")
        assert skype_vacancy_value == TestData.skype_vacancy, "Поле 'Skype' не верно"

        contact_person = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_CONTACT_PERSON)
        contact_person_value = contact_person.get_attribute("value")
        assert contact_person_value == TestData.contact_person, "Поле 'Контактное лицо' не верно"

        employment_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_TYPE_EMPLOYMENT)
        employment_vacancy_title = employment_vacancy.get_attribute("title")
        assert employment_vacancy_title == TestData.employment_type_vacancy, "Поле 'Тип занятости' не верно"

        work_experience_vacancy = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_WORK_EXPERIENCE)
        work_experience_vacancy_title = work_experience_vacancy.get_attribute("title")
        assert work_experience_vacancy_title == TestData.work_experience_vacancy, "Поле 'Опыт работы' не верно"

        education = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_EDUCATION)
        education_title = education.get_attribute("title")
        assert education_title == TestData.education, "Поле 'Образование' не верно"

        benefits = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_BENEFITS)
        benefits_title = benefits.get_attribute("title")
        assert benefits_title == TestData.benefits, "Поле 'Преимущества вакансии' не верно"

        additionally = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_ADDITIONALLY)
        additionally_title = additionally.get_attribute("title")
        assert additionally_title == TestData.additionally, "Поле 'Дополнительно' не верно"

        language_vacancy_1 = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_LANGUAGE_1)
        language_vacancy_1_title = language_vacancy_1.get_attribute("title")
        assert language_vacancy_1_title == TestData.language_vacancy_1, "Поле 'Язык 1' не верно"

        level_language_vacancy_1 = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_LEVEL_LANGUAGE_1)
        level_language_vacancy_1_title = level_language_vacancy_1.get_attribute("title")
        assert level_language_vacancy_1_title == TestData.level_language_vacancy_1, "Поле 'Уровень владения 1' не верно"

        language_vacancy_2 = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_LANGUAGE_2)
        language_vacancy_2_title = language_vacancy_2.get_attribute("title")
        assert language_vacancy_2_title == TestData.language_vacancy_2, "Поле 'Язык 2' не верно"

        level_language_vacancy_2 = self.browser.find_element(*AdminVacancyEditPageLocators.FIELD_LEVEL_LANGUAGE_2)
        level_language_vacancy_2_title = level_language_vacancy_2.get_attribute("title")
        assert level_language_vacancy_2_title == TestData.level_language_vacancy_2, "Поле 'Уровень владения 2' не верно"

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_VACANCY_DESCRIPTION_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.description_vacancy, "Поле 'Описание вакансии' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_ABOUT_COMPANY_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.about_company, "Поле 'О компании' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_WORKING_CONDITIONS_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.working_conditions, "Поле 'Условия работы' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_TASKS_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.tasks, "Поле 'Задачи' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_REQUIREMENTS_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.requirements, "Поле 'Требования к соискателю' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        iframe = self.browser.find_element(*AdminVacancyEditPageLocators.IFRAME_CKEDITOR_ADDITIONALLY_INFORMATION_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminVacancyEditPageLocators.CKEDITOR).text
        assert CKEditor == TestData.additionally_information, "Поле 'Дополнительная информация' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма




