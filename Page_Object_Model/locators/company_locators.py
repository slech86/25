from selenium.webdriver.common.by import By
from Page_Object_Model.singleton import Singleton


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
    FIELD_COMPANY_SLUG = (By.CSS_SELECTOR, ('#' + inputPrefix + 'slug'))
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
    FIELD_COMPANY_SLUG = (By.CSS_SELECTOR, ('#' + inputPrefix + 'slug'))
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
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_EN = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="2"]'))  # английский
    # блок "Настройки"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#submit-button'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации


class CompanyPersonalCabinetPageLocators():
    MY_VACANCIES = (By.XPATH, ('//a[contains(@href, "/vacancy/my")]/div[@class="employer-card"]'))
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/company/edit")]/div[@class="employer-card"]'))
    SERVICES_AND_PRICES = (By.XPATH, ('//a[contains(@href, "/prices")]/div[@class="employer-card"]'))


class MyVacanciesPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_ADD_VACANCY = (By.CSS_SELECTOR, ('#add-vacancy'))

    def assembly_of_locators_with_id_vacancies(self):  # сборка локаторов с id вакансии
        singleton = Singleton()
        button_vacancy_menu = (By.CSS_SELECTOR, ('#my-vacancy-' + singleton.id_vacancies + ' .share-btn'))
        button_edit = (By.XPATH, ('//div[@id="my-vacancy-' + singleton.id_vacancies + '"]//a[contains(@href, "/vacancy/' + singleton.id_vacancies + '/edit")]'))
        button_show_responses = (By.XPATH, ('//a[contains(@href, "/vacancy/' + singleton.id_vacancies + '/feedback")]'))
        new_response_icon = (By.CSS_SELECTOR, ('#my-vacancy-' + singleton.id_vacancies + ' .counter.red'))
        locators = [button_vacancy_menu,
                    button_edit,
                    button_show_responses,
                    new_response_icon]
        return locators

    INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после отправки вакансии на модерацию
    CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после отправки вакансии на модерацию


class ResponsesToVacancyPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    MARK_NOT_VIEWED_RESPONSE = (By.CSS_SELECTOR, ('.lc-card:nth-child(1) .lc-card-time > svg'))

    def assembly_of_locators_with_id_resume(self):  # сборка локаторов с id резюме
        singleton = Singleton()
        resume_in_responses_to_vacancy = (By.XPATH, ('//a[contains(@href, "/resume/' + singleton.id_resume + '")]'))
        return resume_in_responses_to_vacancy


class VacancyAddPageLocators:
    inputPrefix = 'vacancyaddform-'

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    CATEGORY_VACANCIES = "document.getElementsByName('VacancyAddForm[category_id][]')[1].click()"
    SUBCATEGORIES = (By.CSS_SELECTOR, ('[for="subcategories_id-29"]'))
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
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-language"]'))
    ENGLISH_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-language [data-original-index="1"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-level"]'))
    MIDDLE_LEVEL_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-level [data-original-index="3"]'))
    BUTTON_ADD_LANGUAGE_2 = (By.CSS_SELECTOR, ('.resume-item-link.js-add-languages'))
    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-language"]'))
    RUSSIAN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-language [data-original-index="37"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-level"]'))
    NATIVE_LEVEL_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-level [data-original-index="7"]'))
    # блок "Знание языков"

    ADD_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#vacancy-description .btn-disabled'))
    IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'description iframe'))
    # блок "Описание вакансии"

    ADD_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#about-company .btn-disabled'))
    IFRAME_CKEDITOR_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'about_company iframe'))
    # блок "О компании"

    ADD_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#working-conditions .btn-disabled'))
    IFRAME_CKEDITOR_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'working_conditions iframe'))
    # блок "Условия работы"

    ADD_TASKS = (By.CSS_SELECTOR, ('#tasks .btn-disabled'))
    IFRAME_CKEDITOR_TASKS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'tasks iframe'))
    # блок "Задачи"

    ADD_REQUIREMENTS = (By.CSS_SELECTOR, ('#requirements-candidate .btn-disabled'))
    IFRAME_CKEDITOR_REQUIREMENTS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'requirements iframe'))
    # блок "Требования к соискателю"

    ADD_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#additional-information .btn-disabled'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'additionally_information iframe'))
    # блок "Дополнительная информация"

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков
    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-publish'))


class VacancyEditPageLocators():
    inputPrefix = 'vacancyeditform-'

    BUTTON_EDIT_IN_BASIC_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#general-information .post-resume-title + .btn-edit'))
    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    CATEGORY_VACANCIES = "document.getElementsByName('VacancyEditForm[category_id][]')[9].click()"
    SUBCATEGORIES = (By.CSS_SELECTOR, ('[for="subcategories_id-90"]'))
    FIELD_MINIMAL_SALARY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'salary_min'))
    FIELD_MAXIMUM_SALARY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'salary_max'))
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'currency"]'))
    CURRENCY_RUB = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'currency [data-original-index="3"]'))
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_UKRAINE = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'country_id [data-original-index="1"]'))
    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITI_DNIPRO = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'city_id [data-original-index="2"]'))
    FIELD_STREET = (By.CSS_SELECTOR, ('#' + inputPrefix + 'street'))
    FIELD_PHONE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'phone'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + inputPrefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + inputPrefix + 'skype'))
    FIELD_CONTACT_PERSON = (By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_person'))
    REMOTE_WORK = (By.CSS_SELECTOR, ('#' + inputPrefix + 'employment > .checkbox:nth-child(3) > label'))
    WORK_EXPERIENCE_2_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'work_experience > .checkbox:nth-child(3) > label'))
    DROPDOWN_EDUCATION = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'education"]'))
    SECONDARY_EDUCATION = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'education [data-original-index="5"]'))
    DROPDOWN_VACANCY_BENEFITS = (By.CSS_SELECTOR, ('[data-id="job-benefits-select"]'))
    FOREIGN_LANGUAGE_COURSES = (By.CSS_SELECTOR, ('#job-benefits [data-original-index="7"]'))
    READY_TO_TAKE_PERSON_WITH_DISABILITY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'additionally > .checkbox:nth-child(2) > label'))
    # блок "Основная информация"

    BUTTON_EDIT_IN_KNOWLEDGE_OF_LANGUAGES_BLOCK = (By.CSS_SELECTOR, ('#knowledge-of-languages [class="btn-edit"]'))
    BUTTON_TO_DELETE_FIRST_LANGUAGE = (By.CSS_SELECTOR, ('#knowledge-of-languages #lang-form-del-0 .del-block-link'))

    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages #lang-form-del-1 [data-id="languageaddform-language"]'))
    ENGLISH_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages #lang-form-del-1 .field-languageaddform-language [data-original-index="1"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages #lang-form-del-1 [data-id="languageaddform-level"]'))
    ABOVE_AVERAGE_LEVEL_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages #lang-form-del-1 .field-languageaddform-level [data-original-index="4"]'))
    # блок "Знание языков"

    BUTTON_EDIT_IN_VACANCY_DESCRIPTION_BLOCK = (By.CSS_SELECTOR, ('#vacancy-description .right .btn-edit'))
    IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'description iframe'))
    # блок "Описание вакансии"

    BUTTON_EDIT_IN_ABOUT_COMPANY_BLOCK = (By.CSS_SELECTOR, ('#about-company .right .btn-edit'))
    IFRAME_CKEDITOR_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'about_company iframe'))
    # блок "О компании"

    BUTTON_EDIT_IN_WORKING_CONDITIONS_BLOCK = (By.CSS_SELECTOR, ('#working-conditions .right .btn-edit'))
    IFRAME_CKEDITOR_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'working_conditions iframe'))
    # блок "Условия работы"

    BUTTON_EDIT_IN_TASKS_BLOCK = (By.CSS_SELECTOR, ('#tasks .right .btn-edit'))
    IFRAME_CKEDITOR_TASKS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'tasks iframe'))
    # блок "Задачи"

    BUTTON_EDIT_IN_REQUIREMENTS_BLOCK = (By.CSS_SELECTOR, ('#requirements-candidate .right .btn-edit'))
    IFRAME_CKEDITOR_REQUIREMENTS = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'requirements iframe'))
    # блок "Требования к соискателю"

    BUTTON_EDIT_IN_ADDITIONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#additional-information .right .btn-edit'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_' + inputPrefix + 'additionally_information iframe'))
    # блок "Дополнительная информация"

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков
    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-publish'))


class ServicesAndPricesPageLocators():
    TAB_ACTIVATED_SERVICES = (By.CSS_SELECTOR, ('.labet-activated-servises'))
    TAB_NOT_ACTIVATED_SERVICES = (By.CSS_SELECTOR, ('.labet-deactivate-servises'))
    # вкладки

    def assembly_of_locators_with_id_product_and_id_purchase(self):  # сборка локаторов с id продукта и id покупок
        singleton = Singleton()
        product_in_non_activated_services = []
        product_in_activated_services = []
        button_product_activation = []
        arrow_for_viewing_options_available_in_package = []
        number_of_vacancies_available = []
        locators = []
        for id in singleton.id_purchase:
            product_in_non_activated_services.append((By.CSS_SELECTOR, ('.tab-deactivate-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"]')))
            product_in_activated_services.append((By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"]')))
            button_product_activation.append((By.XPATH, ('//a[contains(@href, "/cart/active?id=' + id + '")]')))
            arrow_for_viewing_options_available_in_package.append((By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"] .more')))
            number_of_vacancies_available.append((By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"] p.small-text')))
        locators.append(product_in_non_activated_services)
        locators.append(product_in_activated_services)
        locators.append(button_product_activation)
        locators.append(arrow_for_viewing_options_available_in_package)
        locators.append(number_of_vacancies_available)
        return locators

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


class ResumePageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    COVER_LETTER_TEXT = (By.CSS_SELECTOR, ('.covering-letter-description'))