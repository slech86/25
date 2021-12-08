from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData

class OllPageLocators():
    BUTTON_YES_WHEN_CHECKING_AGE = (By.CSS_SELECTOR, ".modal-content .btn.btn-blue.age-validation")

    BUTTON_POP_UP_FOR_LOGIN = (By.CSS_SELECTOR, ('.login.flex-row'))
    BUTTON_AUTHORIZED_USER = (By.CSS_SELECTOR, ('.logout.flex-row'))
    # хедер

    COMPANY_REGISTRATION_LINK = (By.CSS_SELECTOR, ('#employer .fz-13'))
    JOB_SEEKER_REGISTRATION_LINK = (By.CSS_SELECTOR, ('#job-seeker .fz-13'))
    JOB_SEEKER_TAB = (By.CSS_SELECTOR, ('#job-seeker-tab'))
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-emaillogin'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('.field-loginform-summaryerror + [type="submit"]'))
    INFO_TEXT_IN_POP_UP_WINDOW = (By.CSS_SELECTOR, ('#login-form .small-text'))
    # pop-up окно авторизации


class CompanyRegistrationPageLocators():
    inputPrefix = 'companyregistrationform-'

    FIELD_LOGIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'login'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'password'))
    FIELD_REPEAT_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'repeatpassword'))
    # блок "Данные для авторизации"

    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_POSITION = (By.CSS_SELECTOR, ('#' + inputPrefix + 'position'))
    FIELD_TELEPHONE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    FIELD_CONTACT_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    # блок "Контактная информация"

    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'company_name'))
    FIELD_CODE_COMPANY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'code_company'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(2)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(28)'))
    FIELD_STREET = (By.CSS_SELECTOR, ('#' + inputPrefix + 'street'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatey > option:nth-child(5)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatem > option:nth-child(13)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdated > option:nth-child(32)'))
    FIELD_COMPANY_SITE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'company_site'))

    BUTTON_FACEBOOK = (By.CSS_SELECTOR, ('[aria-controls="facebookCollapse"]'))
    BUTTON_LINKEDIN = (By.CSS_SELECTOR, ('[aria-controls="lnCollapse"]'))
    BUTTON_INSTAGRAM = (By.CSS_SELECTOR, ('[aria-controls="inCollapse"]'))
    BUTTON_TELEGRAM = (By.CSS_SELECTOR, ('[aria-controls="telCollapse"]'))
    BUTTON_TWITTER = (By.CSS_SELECTOR, ('[aria-controls="twCollapse"]'))
    BUTTON_VK = (By.CSS_SELECTOR, ('[aria-controls="vkCollapse"]'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'facebook'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'linkedin'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'instagram'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'telegram'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'twitter'))
    FIELD_VK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'vk'))

    COMPANY_ACTIVITY = "document.getElementsByName('CompanyRegistrationForm[activity][]')[15].click()"  # Сфера деятельности компании
    NUMBER_OF_COMPANY_EMPLOYEES = (By.CSS_SELECTOR, ('#' + inputPrefix + 'count_employees > option:nth-child(8)'))  # Количество сотрудников компании

    IFRAME_CKEDITOR = (By.CSS_SELECTOR, ('iframe.cke_wysiwyg_frame'))
    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))
    # заполнение блока "Информация о компании"

    FIELD_LOGO = (By.CSS_SELECTOR, ('#' + inputPrefix + 'logo'))
    FIELD_COVER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'cover'))

    FIELD_VIDEO1 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video1'))
    FIELD_VIDEO2 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video2'))
    BUTTON_VIDEO_ADD = (By.CSS_SELECTOR, ('.js-add-video'))
    FIELD_VIDEO3 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video3'))
    # заполнение блока "Видео"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#submit-button'))

class JobSeekerRegistrationPageLocators():
    inputPrefix = 'jobseekerregistrationform-'

    FIELD_LOGIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'login'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'password'))
    FIELD_REPEAT_PASSWORD = (By.CSS_SELECTOR, ('#' + inputPrefix + 'repeatpassword'))
    # блок "Данные для авторизации"

    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayy > option:nth-child(4)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdaym > option:nth-child(12)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayd > option:nth-child(31)'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="2"] + .radio-custom'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(3)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(7)'))
    # блок "Личная информация"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#button-registration'))


class MainPageLocators():
    INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст о подтверждении отправки формы регистрации
    INFORMATION_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION = (By.CSS_SELECTOR, ('#to-publish-modal h2'))  # информационный текст о подтверждении електронной почты работодателя после регистрации

    INFORMATION_TEXT_ABOUT_CONFIRMATION_OF_JOB_SEEKER_EMAIL_AFTER_REGISTRATION = (By.CSS_SELECTOR, (''))  # информационный текст о подтверждении електронной почты соискателя после регистрации


class EmailPageLocators():
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#rcmloginuser'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#rcmloginpwd'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('#rcmloginsubmit'))
    # авторизация email

    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Регистрация работодателя на LCwork"]'))
    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Реєстрація роботодавця на LCwork"]'))
    LETTER_WELCOME_TO_LCWORK_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Добро пожаловать на LСwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ru
    LETTER_WELCOME_TO_LCWORK_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ласкаво просимо на LCwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ua

    IFRAME_LETTER = (By.CSS_SELECTOR, ('#messagecontframe'))
    LINK_IN_LETTER = (By.CSS_SELECTOR, ('[rel="noreferrer"]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU = (By.XPATH, ('//div[text()="Ура! Ваш аккаунт прошел модерацию."]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA = (By.XPATH, ('//div[text()="Ура! Ваш акаунт пройшов модерацiю."]'))

class AdminPageLocators():
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-username'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('[type="submit"]'))
    # авторизация админки

    DROPDOWN_WORK = (By.CSS_SELECTOR, ('.dropdown:nth-child(4)'))
    USERS = (By.CSS_SELECTOR, ('[href="/x/user"]'))
    # шапка

    FIELD_EMAIL_SEARCH = (By.CSS_SELECTOR, ('[name="User[email]"]'))
    USER_EMAIL_RU = (By.XPATH, ('//td[text()="' + TestData.email_ru + '"]'))
    USER_EMAIL_UA = (By.XPATH, ('//td[text()="' + TestData.email_ua + '"]'))
    USER_STATUS = (By.CSS_SELECTOR, ('[data-name="status"]'))
    STATUS_ACTIVE = (By.CSS_SELECTOR, ('.form-control.input-sm [value="1"]'))
    STATUS_DELETED = (By.CSS_SELECTOR, ('.form-control.input-sm [value="-1"]'))
    STATUS_SAVING = (By.CSS_SELECTOR, ('.editable-buttons > [type="submit"]'))
    BUTTON_USER_EDIT = (By.CSS_SELECTOR, ('div > .fa.fa-bars'))  # костыль из-за ховер эффекта на кнопке меню пользователя
    # страница пользователей

    FIELD_USER_LOGIN = (By.CSS_SELECTOR, ('[name="User[login]"]'))
    FIELD_USER_EMAIL = (By.CSS_SELECTOR, ('[name="User[email]"]'))

    FIELD_WITH_ROLE_USER = (By.CSS_SELECTOR, ('[title="[#4] User"]'))  # поле с ролью "User"
    ROLE_SUPER_ADMIN = (By.XPATH, ('//li[text()="[#1] SuperAdmin"]'))
    BUTTON_SAVE_AND_EDIT = (By.CSS_SELECTOR, ('[type="submit"].btn.btn-primary'))
    # страница пользователя





