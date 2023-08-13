from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from Page_Object_Model.singleton import Singleton


class AdminPageLocators:
    # авторизация админки
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-username'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('[type="submit"]'))
    # авторизация админки

    # шапка
    DROPDOWN_REFERENCE_BOOKS = (By.CSS_SELECTOR, ('.dropdown:nth-child(3)'))
    CURRENCY_RATES = (By.CSS_SELECTOR, ('[href="/x/currency-rates"]'))

    DROPDOWN_WORK = (By.CSS_SELECTOR, ('.dropdown:nth-child(4)'))
    USERS = (By.CSS_SELECTOR, ('[href="/x/user"]'))
    VACANCIES = (By.CSS_SELECTOR, ('[href="/x/vacancies"]'))
    RESUMES = (By.CSS_SELECTOR, ('[href="/x/resume"]'))
    ORDERS = (By.CSS_SELECTOR, ('[href="/x/orders"]'))
    USER_PURCHASES = (By.CSS_SELECTOR, ('[href="/x/purchases"]'))
    # шапка

    # общие
    STATUS = (By.CSS_SELECTOR, ('[data-name="status"]'))
    STATUS_SAVING = (By.CSS_SELECTOR, ('.editable-buttons > [type="submit"]'))
    BUTTON_OBJECT_MENU = (By.CSS_SELECTOR, ('div > .fa.fa-bars'))
    BUTTON_COMPLETE_OBJECT_DELETED = (By.CSS_SELECTOR, ('.table-delete.fa.fa-trash'))
    BUTTON_OBJECT_DELETE_CONFIRMATION = (By.XPATH, ('//button[text()="Да"]'))
    ALERT_CONFIRMATION_OF_OBJECT_DELETION = (By.XPATH, ('//div[@class="feedback"]/div[contains(@id, "alert-")]'))
    BUTTON_SAVE = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-success'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))
    # общие

    # страница пользователей
    H1_USERS = (By.CSS_SELECTOR, 'h1')
    USER_STATUS = (By.XPATH, '//tr[1]/td[4]/p')
    FIELD_ID_SEARCH = (By.CSS_SELECTOR, '[name="User[id]"]')
    FIELD_EMAIL_SEARCH = (By.CSS_SELECTOR, '[name="User[email]"]')

    def assembly_of_locators_with_email(self, value):
        locators = {
            'user_id': (By.XPATH, ('//td[text()="' + value + '"]')),
            'user_email': (By.XPATH, ('//td[text()="' + value + '"]')),
            'user_login': (By.XPATH, ('//td/a[text()="' + value + '"]')),
        }
        return locators
    # страница пользователей

    # страница пользователя
    FIELD_USER_STATUS = (By.XPATH, ('//span[contains(@id, "select2-user-status-")]'))
    STATUS_USER_ACTIVE = (By.XPATH, ('//ul[contains(@id, "select2-user-status-")]/li[text()="Активен"]'))
    STATUS_USER_DELETE = (By.XPATH, ('//ul[contains(@id, "select2-user-status-")]/li[text()="Удалено"]'))
    FIELD_USER_LOGIN = (By.CSS_SELECTOR, ('[name="User[login]"]'))
    FIELD_USER_EMAIL = (By.CSS_SELECTOR, ('[name="User[email]"]'))
    FIELD_USER_PASSWORD = (By.CSS_SELECTOR, '[name="User[toPassword]"]')
    FIELD_EMAIL_LANGUAGE = (By.XPATH, ('//span[contains(@id, "select2-user-mail_language-")]'))
    EMAIL_LANGUAGE_RUSSIAN = (By.XPATH, ('//ul[contains(@id, "select2-user-mail_language-")]/li[text()="[#1] Русский"]'))
    EMAIL_LANGUAGE_UKRAINIAN = (By.XPATH, ('//ul[contains(@id, "select2-user-mail_language-")]/li[text()="[#3] Українська"]'))
    EMAIL_LANGUAGE_ENGLISH = (By.XPATH, ('//ul[contains(@id, "select2-user-mail_language-")]/li[text()="[#4] English"]'))
    EMAIL_LANGUAGE_POLISH = (By.XPATH, ('//ul[contains(@id, "select2-user-mail_language-")]/li[text()="[#5] Polski"]'))

    FIELD_SLUG = (By.CSS_SELECTOR, ('[name="User[slug]"]'))

    FIELD_NAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][name]"]'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][surname]"]'))
    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][company_name]"]'))
    FIELD_DATE_OF_COMPANY_FOUNDATION = (By.CSS_SELECTOR, ('[name="User[descriptions][1][foundation_date]"]'))
    FIELD_BIRTHDAY = (By.CSS_SELECTOR, ('#users-descriptions-1-birthday'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-gender-container'))
    FIELD_POSITION = (By.CSS_SELECTOR, ('[name="User[descriptions][1][position]"]'))
    FIELD_PHONE = (By.CSS_SELECTOR, ('[name="User[descriptions][1][phone]"]'))
    FIELD_CONTACT_EMAIL = (By.CSS_SELECTOR, ('[name="User[descriptions][1][contact_email]"]'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('[name = "User[descriptions][1][skype]"]'))
    FIELD_CODE_COMPANY = (By.CSS_SELECTOR, ('[name="User[descriptions][1][code_company]"]'))
    FIELD_COMPANY_SITE = (By.CSS_SELECTOR, ('[name="User[descriptions][1][company_site]"]'))
    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('[name="User[descriptions][1][facebook]"]'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('[name="User[descriptions][1][linkedin]"]'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('[name="User[descriptions][1][instagram]"]'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('[name="User[descriptions][1][telegram]"]'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('[name="User[descriptions][1][twitter]"]'))
    FIELD_VK = (By.CSS_SELECTOR, ('[name="User[descriptions][1][vk]"]'))
    FIELD_COMPANY_ACTIVITY = (By.CSS_SELECTOR, ('#users-descriptions-1-activity + .select2 .select2-selection__choice'))
    FIELD_NUMBER_OF_COMPANY_EMPLOYEES = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-count_employees-container'))
    IFRAME_CKEDITOR_COMPANY_DESCRIPTION_RU = (By.CSS_SELECTOR, ('#cke_1_contents > iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_COMPANY_DESCRIPTION_UA = (By.CSS_SELECTOR, ('#cke_2_contents > iframe.cke_wysiwyg_frame.cke_reset'))
    CKEDITOR_COMPANY_DESCRIPTION_RU = (By.XPATH, ('//body[contains(@data-title, "users-descriptions-1-description_company")]/p'))
    CKEDITOR_COMPANY_DESCRIPTION_UA = (By.XPATH, ('//body[contains(@data-title, "users-descriptions-3-description_company")]/p'))
    FIELD_VIDEO_1 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-1'))
    FIELD_VIDEO_2 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-2'))
    FIELD_VIDEO_3 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-3'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-country_id-container'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-city_id-container'))
    FIELD_STREET = (By.CSS_SELECTOR, ('#users-descriptions-1-street'))
    CHECKBOX_GET_NEWS = (By.CSS_SELECTOR, ('#users-descriptions-1-get_news'))

    FIELD_WITH_ROLE_USER = (By.CSS_SELECTOR, '[title="[#4] User"]')  # поле с ролью "User"
    ROLE_SUPER_ADMIN = (By.XPATH, '//li[text()="[#1] SuperAdmin"]')
    # страница пользователя

    H1_VACANCIES = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_SEARCH_VACANCIES = (By.CSS_SELECTOR, ('[name="Vacancies[job_title]"]'))
    # VACANCY_BY_JOB_TITLE = (By.XPATH, ('//a[text()="' + TestData.job_title_vacancy + '"]'))

    def assembly_of_locators_with_job_title(self, job_title_vacancy):
        vacancy_by_job_title = (By.XPATH, ('//a[text()="' + job_title_vacancy + '"]'))
        return vacancy_by_job_title

    VACANCY_BY_JOB_TITLE_AFTER_EDITING = (By.XPATH, ('//a[text()="' + TestData.job_title_vacancy + '_editing"]'))
    ID_VACANCY = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(2)'))
    VACANCY_STATUS = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(3) > p'))
    # страница вакансий

    # SEARCH_STATUS_NEW = (By.CSS_SELECTOR, ('[name="Orders[status]"] > [value="1"]'))
    FIELD_EMAIL_SEARCH_ORDERS = (By.CSS_SELECTOR, ('[name="Orders[userEmail]"]'))

    def assembly_of_locators_with_user_email(self, user_email):
        user_email_orders = (By.XPATH, ('//span[text()="' + user_email + '"]'))
        return user_email_orders

    STATUS_COMPLETED = (By.CSS_SELECTOR, ('.form-control.input-sm > [value="3"]'))
    ID_LAST_ORDER = (By.CSS_SELECTOR, ('tbody > tr:nth-child(1) > td:nth-child(2)'))
    # страница заказов

    DROPDOWN_SEARCH_ORDERS = (By.CSS_SELECTOR, ('[data-select2-id="8"]'))
    FIELD_SEARCH_IN_DROPDOWN = (By.CSS_SELECTOR, ('.select2-search__field'))  # общее поле ?

    def assembly_of_locators_with_id_order(self):
        singleton = Singleton()
        found_order = (By.XPATH, ('//li[text()=" Заказ #' + singleton.id_order + '"]'))
        return found_order

    ITEMS_ID_PURCHASE = (By.CSS_SELECTOR, ('#model-grid tbody tr td:nth-child(3)'))
    # страница 'Покупки пользователей'


class AdminCurrencyRatesPageLocators:
    RUB_RATE = (By.CSS_SELECTOR, ('[id="2"] > td:nth-child(6)'))
    UAH_RATE = (By.CSS_SELECTOR, ('[id="1"] > td:nth-child(6)'))


class AdminVacancyEditPageLocators:
    H1_VACANCY = (By.CSS_SELECTOR, ('h1'))
    FIELD_VACANCY_STATUS = (By.XPATH, ('//span[contains(@id, "select2-vacancies-status-")]'))
    STATUS_PUBLISHED = (By.XPATH, ('//ul[contains(@id, "select2-vacancies-status-")]/li[text()="Опубликовано"]'))
    FIELD_USER = (By.XPATH, ('//span[contains(@id, "select2-vacancies-user_id-")]'))

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#vacancies-descriptions-1job_title'))
    FIELD_JOB_CATEGORY = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1-category_id-container'))
    FIELD_JOB_SUBCATEGORIES = (By.CSS_SELECTOR, ('#vacancies-descriptions-1-subcategories_id + span .select2-selection__choice'))
    FIELD_SALARY_MIN = (By.CSS_SELECTOR, ('#vacancies-descriptions-1salary_min'))
    FIELD_SALARY_MIN_USD = (By.CSS_SELECTOR, ('#vacancies-descriptions-1base_salary_min'))
    FIELD_SALARY_MAX = (By.CSS_SELECTOR, ('#vacancies-descriptions-1salary_max'))
    FIELD_SALARY_MAX_USD = (By.CSS_SELECTOR, ('#vacancies-descriptions-1base_salary_max'))
    FIELD_CURRENCY_VACANCY = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1currency-container'))
    FIELD_COUNTRY_VACANCY = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1-country_id-container'))
    FIELD_CITY_VACANCY = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1-city_id-container'))
    FIELD_STREET_VACANCY = (By.CSS_SELECTOR, ('#vacancies-descriptions-1street'))
    FIELD_PHONE = (By.CSS_SELECTOR, '#vacancies-descriptions-1phone')
    FIELD_EMAIL = (By.CSS_SELECTOR, '#vacancies-descriptions-1email')
    FIELD_SKYPE = (By.CSS_SELECTOR, '#vacancies-descriptions-1skype')
    FIELD_TELEGRAM = (By.CSS_SELECTOR, '#vacancies-descriptions-1telegram')
    FIELD_CONTACT_PERSON = (By.CSS_SELECTOR, ('#vacancies-descriptions-1contact_person'))
    FIELD_TYPE_EMPLOYMENT = (By.CSS_SELECTOR, ('#vacancies-descriptions-1employment + span .select2-selection__choice'))
    FIELD_WORK_EXPERIENCE = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1work_experience-container'))
    FIELD_EDUCATION = (By.CSS_SELECTOR, ('#select2-vacancies-descriptions-1education-container'))
    FIELD_BENEFITS = (By.CSS_SELECTOR, ('#vacancies-descriptions-1advantages + span .select2-selection__choice'))
    FIELD_ADDITIONALLY = (By.CSS_SELECTOR, ('#vacancies-descriptions-1additionally + span .select2-selection__choice'))
    FIELD_LANGUAGE_1 = (By.CSS_SELECTOR, '#select2-vacancies-knowledge-of-languages-1-0-language-container')
    FIELD_LEVEL_LANGUAGE_1 = (By.CSS_SELECTOR, '#select2-vacancies-knowledge-of-languages-1-0-level-container')
    FIELD_LANGUAGE_2 = (By.CSS_SELECTOR, '#select2-vacancies-knowledge-of-languages-1-1-language-container')
    FIELD_LEVEL_LANGUAGE_2 = (By.CSS_SELECTOR, '#select2-vacancies-knowledge-of-languages-1-1-level-container')
    IFRAME_CKEDITOR_VACANCY_DESCRIPTION_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1description iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_VACANCY_DESCRIPTION_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3description iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_ABOUT_COMPANY_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1about_company iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_ABOUT_COMPANY_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3about_company iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_WORKING_CONDITIONS_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1working_conditions iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_WORKING_CONDITIONS_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3working_conditions iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_TASKS_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1tasks iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_TASKS_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3tasks iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_REQUIREMENTS_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1requirements iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_REQUIREMENTS_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3requirements iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_ADDITIONALLY_INFORMATION_RU = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-1additionally_information iframe.cke_wysiwyg_frame.cke_reset'))
    IFRAME_CKEDITOR_ADDITIONALLY_INFORMATION_UA = (By.CSS_SELECTOR, ('#cke_vacancies-descriptions-3additionally_information iframe.cke_wysiwyg_frame.cke_reset'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков
    BUTTON_SAVE = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-success'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))


class AdminResumesPageLocators:
    H1_RESUMES = (By.CSS_SELECTOR, 'h1')
    FIELD_JOB_TITLE_SEARCH_RESUME = (By.CSS_SELECTOR, '[name="Resume[job_title]"]')

    def assembly_of_locators_with_job_title_resume(self, job_title):
        resume_by_job_title = (By.XPATH, '//a[text()="' + job_title + '"]')
        return resume_by_job_title

    RESUME_BY_JOB_TITLE_AFTER_EDITING = (By.XPATH, ('//a[text()="' + TestDataEditing.job_title_resume + '"]'))
    ID_RESUME = (By.CSS_SELECTOR, '#pjax-list-container tbody > tr > td:nth-child(2)')
    RESUME_STATUS = (By.CSS_SELECTOR, '#pjax-list-container tbody > tr > td:nth-child(3) > p')
    BUTTON_RESUME_MENU = (By.CSS_SELECTOR, 'div > .fa.fa-bars')
    BUTTON_COMPLETE_RESUME_DELETED = (By.CSS_SELECTOR, '.table-delete.fa.fa-trash')
    BUTTON_RESUME_DELETE_CONFIRMATION = (By.XPATH, '//button[text()="Да"]')
    ALERT_CONFIRMATION_OF_RESUME_DELETION = (By.XPATH, '//div[@class="feedback"]/div[contains(@id, "alert-")]')


class AdminResumeEditPageLocators:
    H1_RESUME_EDIT = (By.CSS_SELECTOR, 'h1')
    FIELD_RESUME_STATUS = (By.XPATH, ('//span[contains(@id, "select2-resume-status-")]'))
    STATUS_PUBLISHED = (By.XPATH, ('//ul[contains(@id, "select2-resume-status-")]/li[text()="Опубликовано"]'))
    FIELD_USER = (By.XPATH, ('//span[contains(@id, "select2-resume-user_id-")]'))
    FIELD_JOB_SEARCH_STATUS = (By.XPATH, ('//span[@id="select2-resume-descriptions-1-job_searching_status-container"]'))

    FIELD_NAME_COURSE_1 = (By.CSS_SELECTOR, '#resume-courses-1-0-name_certificate')
    FIELD_COURSE_PERIOD_START_1 = (By.CSS_SELECTOR, '#resume-courses-1-0-training_period_start')
    FIELD_COURSE_PERIOD_FINISH_1 = (By.CSS_SELECTOR, '#resume-courses-1-0-training_period_finish')
    IFRAME_CKEDITOR_COURSE_DESCRIPTION_1 = (By.XPATH, '//div[@id="cke_resume-courses-1-0-description"]//iframe')

    FIELD_NAME_COURSE_2 = (By.CSS_SELECTOR, '#resume-courses-1-1-name_certificate')
    FIELD_COURSE_PERIOD_START_2 = (By.CSS_SELECTOR, '#resume-courses-1-1-training_period_start')
    FIELD_COURSE_PERIOD_FINISH_2 = (By.CSS_SELECTOR, '#resume-courses-1-1-training_period_finish')
    IFRAME_CKEDITOR_COURSE_DESCRIPTION_2 = (By.XPATH, '//div[@id="cke_resume-courses-1-1-description"]//iframe')

    FIELD_NAME_OF_INSTITUTION_1 = (By.CSS_SELECTOR, '#resume-educations-1-0-name_institution')
    FIELD_LEVEL_OF_EDUCATION_1 = (By.CSS_SELECTOR, '#select2-resume-educations-1-0-level_education-container')
    FIELD_COUNTRY_EDUCATION_1 = (By.CSS_SELECTOR, '#select2-resume-educations-1-0-country_id-container')
    FIELD_CITY_EDUCATION_1 = (By.CSS_SELECTOR, '#select2-resume-educations-1-0-city_id-container')
    FIELD_DEPARTMENT_AND_SPECIALITY_1 = (By.CSS_SELECTOR, '#resume-educations-1-0-specialty')
    FIELD_EDUCATION_PERIOD_START_1 = (By.CSS_SELECTOR, '#resume-educations-1-0-date_start')
    FIELD_EDUCATION_PERIOD_FINISH_1 = (By.CSS_SELECTOR, '#resume-educations-1-0-date_finish')

    FIELD_NAME_OF_INSTITUTION_2 = (By.CSS_SELECTOR, '#resume-educations-1-1-name_institution')
    FIELD_LEVEL_OF_EDUCATION_2 = (By.CSS_SELECTOR, '#select2-resume-educations-1-1-level_education-container')
    FIELD_COUNTRY_EDUCATION_2 = (By.CSS_SELECTOR, '#select2-resume-educations-1-1-country_id-container')
    FIELD_CITY_EDUCATION_2 = (By.CSS_SELECTOR, '#select2-resume-educations-1-1-city_id-container')
    FIELD_DEPARTMENT_AND_SPECIALITY_2 = (By.CSS_SELECTOR, '#resume-educations-1-1-specialty')
    FIELD_EDUCATION_PERIOD_START_2 = (By.CSS_SELECTOR, '#resume-educations-1-1-date_start')
    FIELD_EDUCATION_PERIOD_FINISH_2 = (By.CSS_SELECTOR, '#resume-educations-1-1-date_finish')

    FIELD_COMPANY_NAME_RESUME_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-company')
    FIELD_COMPANY_SITE_RESUME_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-web_site')
    FIELD_SCOPE_OF_COMPANY_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-category + span li.select2-selection__choice')
    FIELD_POSITION_RESUME_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-position')
    FIELD_WORK_PERIOD_START_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-period_employment_start')
    FIELD_WORK_PERIOD_FINISH_1 = (By.CSS_SELECTOR, '#resume-experiences-1-0-period_employment_finish')
    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_1 = (By.XPATH, '//div[@id="cke_resume-experiences-1-0-responsibilities"]//iframe')

    FIELD_COMPANY_NAME_RESUME_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-company')
    FIELD_COMPANY_SITE_RESUME_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-web_site')
    FIELD_SCOPE_OF_COMPANY_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-category + span li.select2-selection__choice')
    FIELD_POSITION_RESUME_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-position')
    FIELD_WORK_PERIOD_START_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-period_employment_start')
    CHECKBOX_WORK_PERIOD_FINISH_2 = (By.CSS_SELECTOR, '#resume-experiences-1-1-untilNow')  # По настоящее время
    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2 = (By.XPATH, '//div[@id="cke_resume-experiences-1-1-responsibilities"]//iframe')

    FIELD_LANGUAGE_RESUME_1 = (By.XPATH, '//span[@id="select2-resume-knowledge-of-languages-1-0-language-container"]')
    FIELD_LEVEL_LANGUAGE_RESUME_1 = (By.XPATH, '//span[@id="select2-resume-knowledge-of-languages-1-0-level-container"]')

    FIELD_LANGUAGE_RESUME_2 = (By.XPATH, '//span[@id="select2-resume-knowledge-of-languages-1-1-language-container"]')
    FIELD_LEVEL_LANGUAGE_RESUME_2 = (By.XPATH, '//span[@id="select2-resume-knowledge-of-languages-1-1-level-container"]')

    FIELD_NAME = (By.CSS_SELECTOR, ('#resume-descriptions-1-name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#resume-descriptions-1-surname'))
    FIELD_BIRTHDAY = (By.CSS_SELECTOR, ('#resume-descriptions-1-birthday'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-gender-container'))
    FIELD_COUNTRY_RESUME = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-country_id-container'))
    FIELD_CITY_RESUME = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-city_id-container'))
    FIELD_WILLING_TO_RELOCATE = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-willing_relocate-container'))
    FIELD_PHONE_1 = (By.CSS_SELECTOR, ('#resume-descriptions-1-phone1'))
    FIELD_PHONE_2 = (By.CSS_SELECTOR, ('#resume-descriptions-1-phone2'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#resume-descriptions-1-email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#resume-descriptions-1-skype'))
    FIELD_PORTFOLIO = (By.CSS_SELECTOR, ('#resume-descriptions-1-portfolio'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][facebook]"]'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][linkedin]"]'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][instagram]"]'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][telegram]"]'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][twitter]"]'))
    FIELD_VK = (By.CSS_SELECTOR, ('[name="Resume[descriptions][1][vk]"]'))

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#resume-descriptions-1-job_title'))
    FIELD_CATEGORY_RESUME = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-category_id-container'))
    FIELD_SUBCATEGORIES_RESUME = (By.CSS_SELECTOR, ('#resume-descriptions-1-subcategories_id + span .select2-selection__choice'))
    FIELD_EMPLOYMENT_TYPE_RESUME = (By.CSS_SELECTOR, ('#resume-descriptions-1-employment + span .select2-selection__choice'))
    FIELD_SALARY_RESUME = (By.CSS_SELECTOR, ('#resume-descriptions-1-salary'))
    FIELD_SALARY_RESUME_USD = (By.CSS_SELECTOR, ('#resume-descriptions-1-base_salary'))
    FIELD_CURRENCY_RESUME = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-currency-container'))
    IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, ('#cke_resume-descriptions-1-skills iframe'))
    FIELD_DISABILITY = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-disability-container'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_resume-descriptions-1-additionally_information iframe'))
    FIELD_EXPERIENCE_IN_GAMBLING_INDUSTRY = (By.CSS_SELECTOR, ('#select2-resume-descriptions-1-gambling_experience-container'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков

    BUTTON_SAVE = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-success'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))


class AdminSqlPageLocators:
    FIELD_SQL = (By.CSS_SELECTOR, '#filter-form textarea')
    BUTTON_EXECUTE = (By.CSS_SELECTOR, '#filter-form [type="submit"]')


class AdminProductEditPageLocators:
    CHECKBOX_AUTO_ACTIVATION = (By.CSS_SELECTOR, '[type="checkbox"][name="Products[activatable]"]')
