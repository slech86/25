from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData

class OllPageLocators():
    BUTTON_YES_WHEN_CHECKING_AGE = (By.CSS_SELECTOR, ".modal-content .btn.btn-blue.age-validation")

    BUTTON_POP_UP_FOR_LOGIN = (By.CSS_SELECTOR, ('.login.flex-row'))
    BUTTON_AUTHORIZED_USER = (By.CSS_SELECTOR, ('.logout.flex-row'))
    LINK_PERSONAL_ACCOUNT = (By.XPATH, ('//a[@class="dropdown-item"][contains(@href, "/cabinet")]'))
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
    FIELD_PHONE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    FIELD_CONTACT_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    # блок "Контактная информация"

    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'company_name'))
    FIELD_CODE_COMPANY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'code_company'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(2)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(8)'))
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

    COMPANY_ACTIVITY = "document.getElementsByName('CompanyRegistrationForm[activity][]')[14].click()"  # Сфера деятельности компании
    NUMBER_OF_COMPANY_EMPLOYEES = (By.CSS_SELECTOR, ('#' + inputPrefix + 'count_employees > option:nth-child(5)'))  # Количество сотрудников компании

    IFRAME_CKEDITOR_COMPANY_DESCRIPTION = (By.CSS_SELECTOR, ('iframe.cke_wysiwyg_frame'))
    CKEDITOR_COMPANY_DESCRIPTION = (By.CSS_SELECTOR, ('body.cke_editable'))
    # блок "Информация о компании"

    FIELD_LOGO = (By.CSS_SELECTOR, ('#' + inputPrefix + 'logo'))
    FIELD_COVER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'cover'))

    FIELD_VIDEO_1 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video1'))
    FIELD_VIDEO_2 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video2'))
    BUTTON_VIDEO_ADD = (By.CSS_SELECTOR, ('.js-add-video'))
    FIELD_VIDEO_3 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video3'))
    # заполнение блока "Видео"

    CHECKBOX_GET_NEWS = (By.CSS_SELECTOR, ('#' + inputPrefix + 'get_news'))
    # подписка на новости

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#submit-button'))

class CompanyEditPageLocators():
    inputPrefix = 'companyform-'

    BUTTON_EDIT_IN_CONTACT_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#contact-information .post-resume-title + .btn-edit'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_POSITION = (By.CSS_SELECTOR, ('#' + inputPrefix + 'position'))
    FIELD_PHONE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    FIELD_CONTACT_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    # блок "Контактная информация"

    BUTTON_EDIT_IN_COMPANY_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#company-information .post-resume-title + .btn-edit'))
    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'company_name'))
    FIELD_CODE_COMPANY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'code_company'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(4)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(5)'))
    FIELD_STREET = (By.CSS_SELECTOR, ('#' + inputPrefix + 'street'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatey > option:nth-child(33)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatem > option:nth-child(4)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdated > option:nth-child(18)'))
    FIELD_COMPANY_SITE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'company_site'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'facebook'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('#' + inputPrefix + 'linkedin'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'instagram'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + inputPrefix + 'telegram'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'twitter'))
    FIELD_VK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'vk'))

    COMPANY_ACTIVITY = "document.getElementsByName('CompanyForm[activity][]')[15].click()"  # Сфера деятельности компании
    NUMBER_OF_COMPANY_EMPLOYEES = (By.CSS_SELECTOR, ('#' + inputPrefix + 'count_employees > option:nth-child(4)'))  # Количество сотрудников компании

    IFRAME_CKEDITOR_COMPANY_DESCRIPTION = (By.CSS_SELECTOR, ('iframe.cke_wysiwyg_frame'))
    CKEDITOR_COMPANY_DESCRIPTION = (By.CSS_SELECTOR, ('body.cke_editable'))
    # блок "Информация о компании"

    FIELD_LOGO = (By.CSS_SELECTOR, ('#' + inputPrefix + 'logo'))
    FIELD_COVER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'cover'))

    FIELD_VIDEO_1 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video1'))
    FIELD_VIDEO_2 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video2'))
    BUTTON_VIDEO_ADD = (By.CSS_SELECTOR, ('.js-add-video'))
    FIELD_VIDEO_3 = (By.CSS_SELECTOR, ('#' + inputPrefix + 'video3'))
    # блок "Видео"

    BUTTON_EDIT_IN_SETTINGS_BLOCK = (By.CSS_SELECTOR, ('#other-settings .post-resume-title + .btn-edit'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'mail_language"]'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="0"]'))  # русский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="1"]'))  # украинский
    # блок "Настройки"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#submit-button'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации

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
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(2)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(8)'))
    # блок "Личная информация"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#button-registration'))

class JobSeekerEditPageLocators():
    inputPrefix = 'jobseekereditform-'

    BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#personal-information .post-resume-title + .btn-edit'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayy > option:nth-child(2)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdaym > option:nth-child(2)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayd > option:nth-child(2)'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="1"] + .radio-custom'))
    FIELD_COUNTRY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(4)'))
    FIELD_CITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(5)'))
    # блок "Личная информация"

    BUTTON_EDIT_IN_SETTINGS_BLOCK = (By.CSS_SELECTOR, ('#other-settings .post-resume-title + .btn-edit'))
    DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'mail_language"]'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="0"]'))  # русский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="1"]'))  # украинский
    # блок "Настройки"

    BUTTON_SAVE_CHANGES = (By.CSS_SELECTOR, ('#submit-publish'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации

class CompanyPersonalCabinetPageLocators():
    MY_VACANCIES = (By.XPATH, ('//a[contains(@href, "/vacancy/my")]/div[@class="employer-card"]'))
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/company/edit")]/div[@class="employer-card"]'))
    SERVICES_AND_PRICES = (By.XPATH, ('//a[contains(@href, "/prices")]/div[@class="employer-card"]'))

class JobSeekerPersonalCabinetPageLocators():
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/job-seeker/edit")]/div[@class="employer-card"]'))

class MyVacanciesPageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_ADD_VACANCY = (By.CSS_SELECTOR, ('#add-vacancy'))

    INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после отправки вакансии на модерауии
    CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после отправки вакансии на модерауии


class AddVacancyPageLocators():
    inputPrefix = 'vacancyaddform-'

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    CATEGORY_VACANCIES = "document.getElementsByName('VacancyAddForm[category_id][]')[1].click()"
    SUBCATEGORIES = "document.getElementsByName('VacancyAddForm[subcategories_id][]')[2].click()"
    FIELD_MINIMAL_SALARY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'salary_min'))
    FIELD_MAXIMUM_SALARY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'salary_max'))
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'currency"]'))
    CURRENCY_USD = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'currency [data-original-index="2"]'))
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_RUSSIA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'country_id [data-original-index="2"]'))
    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITI_MOSCOW = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'city_id [data-original-index="25"]'))
    FIELD_STREET = (By.CSS_SELECTOR, ('#' + inputPrefix + 'street'))
    FIELD_PHONE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    FIELD_CONTACT_PERSON = (By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_person'))
    FULL_EMPLOYMENT = (By.CSS_SELECTOR, ('#' + inputPrefix + 'employment > .checkbox:nth-child(1) > label'))
    WORK_EXPERIENCE_1_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'work_experience > .checkbox:nth-child(2) > label'))
    DROPDOWN_EDUCATION = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'education"]'))
    HIGHER_EDUCATION = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'education [data-original-index="2"]'))
    DROPDOWN_VACANCY_BENEFITS = (By.CSS_SELECTOR, ('[data-id="job-benefits-select"]'))
    TRANSPORTATION = (By.CSS_SELECTOR, ('#job-benefits [data-original-index="12"]'))
    READY_TO_TAKE_STUDENT = (By.CSS_SELECTOR, ('#' + inputPrefix + 'additionally > .checkbox:nth-child(1) > label'))
    # блок "Основная информация"

    BUTTON_ADD_LANGUAGE = (By.CSS_SELECTOR, ('#addLanguages'))
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, ('[data-id="languageaddform-language"]'))
    ENGLISH_LANGUAGE_1 = (By.CSS_SELECTOR, ('.field-languageaddform-language [data-original-index="1"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, ('[data-id="languageaddform-level"]'))
    MIDDLE_LEVEL_1 = (By.CSS_SELECTOR, ('.field-languageaddform-level [data-original-index="3"]'))
    ADD_LANGUAGE = (By.CSS_SELECTOR, ('.resume-item-link.js-add-languages'))
    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-language"]'))
    ENGLISH_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-language [data-original-index="37"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-level"]'))
    MIDDLE_LEVEL_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-level [data-original-index="7"]'))
    # блок "Знание языков"

    ADD_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#vacancy-description .btn-disabled'))
    IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#cke_vacancyaddform-description iframe'))
    # блок "Описание вакансии"

    ADD_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#about-company .btn-disabled'))
    IFRAME_CKEDITOR_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#cke_vacancyaddform-about_company iframe'))
    # блок "О компании"

    ADD_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#working-conditions .btn-disabled'))
    IFRAME_CKEDITOR_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#cke_vacancyaddform-working_conditions iframe'))
    # блок "Условия работы"

    ADD_TASKS = (By.CSS_SELECTOR, ('#tasks .btn-disabled'))
    IFRAME_CKEDITOR_TASKS = (By.CSS_SELECTOR, ('#cke_vacancyaddform-tasks iframe'))
    # блок "Задачи"

    ADD_REQUIREMENTS = (By.CSS_SELECTOR, ('#requirements-candidate .btn-disabled'))
    IFRAME_CKEDITOR_REQUIREMENTS = (By.CSS_SELECTOR, ('#cke_vacancyaddform-requirements iframe'))
    # блок "Требования к соискателю"

    ADD_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#additional-information .btn-disabled'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_vacancyaddform-additionally_information iframe'))
    # блок "Дополнительная информация"

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков
    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-publish'))


class VacancyPageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))


class ServicesAndPricesPageLocators():
    TAB_ACTIVATED_SERVICES = (By.CSS_SELECTOR, ('.labet-activated-servises'))
    TAB_NOT_ACTIVATED_SERVICES = (By.CSS_SELECTOR, ('.labet-deactivate-servises'))
    # вкладки



    BUTTON_ORDER_IN_STANDART = (By.CSS_SELECTOR, ('[data-product-id="1"]'))
    BUTTON_5_VACANCY = (By.CSS_SELECTOR, ('[for="vacancies-1-5"]'))
    STANDART_IN_BASKET = (By.CSS_SELECTOR, ('.bascket-list-item > [data-product-id="1"]'))
    # пакеты услуг


    BUTTON_ORDER_IN_MONTHLY_FREE_VACANCY = (By.CSS_SELECTOR, ('[data-product-id="25"]'))
    MONTHLY_FREE_VACANCY_IN_BASKET = (By.CSS_SELECTOR, ('.bascket-list-item > [data-product-id="25"]'))

    BUTTON_ORDER_IN_1_VACANCY = (By.CSS_SELECTOR, ('[data-product-id="4"]'))
    ONE_VACANCY_IN_BASKET = (By.CSS_SELECTOR, ('.bascket-list-item > [data-product-id="4"]'))
    # пакеты поштучно


    BUTTON_BUY = (By.CSS_SELECTOR, ('.js-button .btn.btn-blue'))

    INFO_TEXT_AFTER_BUTTON_PRESSED_BUY_IN_CART = (By.CSS_SELECTOR, ('#to-buy-modal .modal-body'))  # информационный текст после нажаия кнопки "Купить" в корзине
    CROSS_IN_POP_UP_AFTER_PRESSING_BUTTON_BUY_IN_BASKET = (By.CSS_SELECTOR, ('#to-buy-modal .close'))  # крестик в pop-up окне после нажаия кнопки "Купить" в корзине


class MainPageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))
    INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст о подтверждении отправки формы регистрации
    INFO_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION = (By.CSS_SELECTOR, ('#to-publish-modal h2'))  # информационный текст о подтверждении електронной почты работодателя после регистрации


class EmailPageLocators():
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#rcmloginuser'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#rcmloginpwd'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('#rcmloginsubmit'))
    # авторизация email

    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Регистрация работодателя на LCwork"]'))
    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Реєстрація роботодавця на LCwork"]'))
    LETTER_WELCOME_TO_LCWORK_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Добро пожаловать на LСwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ru
    LETTER_WELCOME_TO_LCWORK_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ласкаво просимо на LCwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ua
    LETTER_AFTER_ORDER_PROCESSING_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Оплата подтверждена, активируйте услугу на сайте"]'))  # письмо после проведения заказа ru
    LETTER_AFTER_ORDER_PROCESSING_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Оплата отримана, активуйте послугу на сайті"]'))  # письмо после проведения заказа ua
    LETTER_AFTER_PUBLISHING_VACANCY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваша вакансия добавлена на сайт"]'))  # письмо после публикации вакансии ru
    LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваша вакансия добавлена на сайт"]'))  # письмо после публикации вакансии ua


    IFRAME_LETTER = (By.CSS_SELECTOR, ('#messagecontframe'))
    LINK_IN_LETTER = (By.CSS_SELECTOR, ('[rel="noreferrer"]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU = (By.XPATH, ('//div[text()="Ура! Ваш аккаунт прошел модерацию."]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA = (By.XPATH, ('//div[text()="Ура! Ваш акаунт пройшов модерацiю."]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_RU = (By.XPATH, ('//div[contains(text(), "Оплата получена, активируйте услугу на ")]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_UA = (By.XPATH, ('//div[contains(text(), "Оплата отримана, активуйте послугу на ")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_RU = (By.XPATH, ('//div[contains(text(), "' + TestData.job_title + ' добавлена на сайт.")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//div[contains(text(), "' + TestData.job_title + ' добавлена на сайт.")]'))

class AdminPageLocators():
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-username'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('[type="submit"]'))
    # авторизация админки

    DROPDOWN_WORK = (By.CSS_SELECTOR, ('.dropdown:nth-child(4)'))
    USERS = (By.CSS_SELECTOR, ('[href="/x/user"]'))
    VACANCIES = (By.CSS_SELECTOR, ('[href="/x/vacancies"]'))
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

    H1 = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_SEARCH_VACANCIES = (By.CSS_SELECTOR, ('[name="Vacancies[job_title]"]'))
    VACANCY_BY_JOB_TITLE = (By.XPATH, ('//a[text()="' + TestData.job_title + '"]'))
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
