from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData


class AdminPageLocators():
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-username'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('[type="submit"]'))
    # авторизация админки

    DROPDOWN_WORK = (By.CSS_SELECTOR, ('.dropdown:nth-child(4)'))
    USERS = (By.CSS_SELECTOR, ('[href="/x/user"]'))
    VACANCIES = (By.CSS_SELECTOR, ('[href="/x/vacancies"]'))
    RESUMES = (By.CSS_SELECTOR, ('[href="/x/resume"]'))
    ORDERS = (By.CSS_SELECTOR, ('[href="/x/orders"]'))
    USER_PURCHASES = (By.CSS_SELECTOR, ('[href="/x/purchases"]'))
    # шапка

    STATUS = (By.CSS_SELECTOR, ('[data-name="status"]'))
    STATUS_SAVING = (By.CSS_SELECTOR, ('.editable-buttons > [type="submit"]'))
    BUTTON_OBJECT_MENU = (By.CSS_SELECTOR, ('div > .fa.fa-bars'))
    BUTTON_COMPLETE_OBJECT_DELETED = (By.CSS_SELECTOR, ('.table-delete.fa.fa-trash'))
    BUTTON_OBJECT_DELETE_CONFIRMATION = (By.XPATH, ('//button[text()="Да"]'))
    BUTTON_SAVE = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-success'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))
    # общие


    FIELD_EMAIL_SEARCH = (By.CSS_SELECTOR, ('[name="User[email]"]'))
    USER_EMAIL_RU = (By.XPATH, ('//td[text()="' + TestData.email_ru + '"]'))
    USER_EMAIL_UA = (By.XPATH, ('//td[text()="' + TestData.email_ua + '"]'))
    STATUS_ACTIVE = (By.CSS_SELECTOR, ('.form-control.input-sm [value="1"]'))
    STATUS_DELETED = (By.CSS_SELECTOR, ('.form-control.input-sm [value="-1"]'))
    # страница пользователей



    FIELD_USER_LOGIN = (By.CSS_SELECTOR, ('[name="User[login]"]'))
    FIELD_USER_EMAIL = (By.CSS_SELECTOR, ('[name="User[email]"]'))
    FIELD_EMAIL_LANGUAGE = (By.XPATH, ('//span[contains(@id, "select2-user-mail_language-")]'))

    FIELD_NAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][name]"]'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][surname]"]'))
    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, ('[name="User[descriptions][1][company_name]"]'))
    FIELD_DATE_OF_COMPANY_FOUNDATION = (By.CSS_SELECTOR, ('[name="User[descriptions][1][foundation_date]"]'))
    FIELD_BIRTHDAY = (By.CSS_SELECTOR, ('#users-descriptions-1-birthday')) #  ????
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
    FIELD_VIDEO_1 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-0'))
    FIELD_VIDEO_2 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-1'))
    FIELD_VIDEO_3 = (By.CSS_SELECTOR, ('#users-descriptions-1-video-2'))
    FIELD_COUNTRY_RU = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-country_id-container'))
    FIELD_CITY_RU = (By.CSS_SELECTOR, ('#select2-users-descriptions-1-city_id-container'))
    FIELD_STREET_RU = (By.CSS_SELECTOR, ('#users-descriptions-1-street'))
    CHECKBOX_GET_NEWS_RU = (By.CSS_SELECTOR, ('#users-descriptions-1-get_news'))



    FIELD_WITH_ROLE_USER = (By.CSS_SELECTOR, ('[title="[#4] User"]'))  # поле с ролью "User"
    ROLE_SUPER_ADMIN = (By.XPATH, ('//li[text()="[#1] SuperAdmin"]'))
    # страница пользователя

    H1_VACANCIES = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_SEARCH_VACANCIES = (By.CSS_SELECTOR, ('[name="Vacancies[job_title]"]'))
    VACANCY_BY_JOB_TITLE = (By.XPATH, ('//a[text()="' + TestData.job_title_vacancy + '"]'))
    ID_VACANCY = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(2)'))
    VACANCY_STATUS = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(3) > p'))
    # страница вакансий

    FIELD_VACANCY_STATUS = (By.XPATH, ('//span[contains(@id, "select2-vacancies-status-")]'))
    STATUS_PUBLISHED = (By.XPATH, ('//ul[contains(@id, "select2-vacancies-status-")]/li[text()="Опубликовано"]'))
    # страница карточки вакансии

    # SEARCH_STATUS_NEW = (By.CSS_SELECTOR, ('[name="Orders[status]"] > [value="1"]'))
    FIELD_EMAIL_SEARCH_ORDERS = (By.CSS_SELECTOR, ('[name="Orders[userEmail]"]'))
    USER_EMAIL_ORDERS_RU = (By.XPATH, ('//span[text()="' + TestData.email_ru + '"]'))
    USER_EMAIL_ORDERS_UA = (By.XPATH, ('//span[text()="' + TestData.email_ua + '"]'))
    STATUS_COMPLETED = (By.CSS_SELECTOR, ('.form-control.input-sm > [value="3"]'))
    ID_LAST_ORDER = (By.CSS_SELECTOR, ('tbody > tr:nth-child(1) > td:nth-child(2)'))
    # страница заказов

    DROPDOWN_SEARCH_ORDERS = (By.CSS_SELECTOR, ('[data-select2-id="7"]'))
    FIELD_SEARCH_IN_DROPDOWN = (By.CSS_SELECTOR, ('.select2-search__field'))  # общее поле ?
    ITEMS_ID_PURCHASE = (By.CSS_SELECTOR, ('#model-grid tbody tr td:nth-child(2)'))
    # страница 'Покупки пользователей'


class AdminResumesPageLocators():
    H1_RESUMES = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_SEARCH_RESUME = (By.CSS_SELECTOR, ('[name="Resume[job_title]"]'))
    RESUME_BY_JOB_TITLE = (By.XPATH, ('//a[text()="' + TestData.job_title_resume + '"]'))
    ID_RESUME = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(2)'))
    RESUME_STATUS = (By.CSS_SELECTOR, ('#pjax-list-container tbody > tr > td:nth-child(3) > p'))
    BUTTON_OBJECT_MENU = (By.CSS_SELECTOR, ('div > .fa.fa-bars'))
    BUTTON_COMPLETE_OBJECT_DELETED = (By.CSS_SELECTOR, ('.table-delete.fa.fa-trash'))
    BUTTON_OBJECT_DELETE_CONFIRMATION = (By.XPATH, ('//button[text()="Да"]'))


class AdminResumeEditPageLocators():
    H1_RESUME = (By.CSS_SELECTOR, ('h1'))
    FIELD_RESUME_STATUS = (By.XPATH, ('//span[contains(@id, "select2-resume-status-")]'))
    STATUS_PUBLISHED = (By.XPATH, ('//ul[contains(@id, "select2-resume-status-")]/li[text()="Опубликовано"]'))
    BUTTON_SAVE = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-success'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))