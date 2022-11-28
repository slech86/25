from selenium.webdriver.common.by import By
from Page_Object_Model.singleton import Singleton


class CompanyRegistrationPageLocators:
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

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_ukraine = (By.CSS_SELECTOR, ('.field-' + CompanyRegistrationPageLocators.inputPrefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_ukraine

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_kyiv = (By.CSS_SELECTOR, ('.field-' + CompanyRegistrationPageLocators.inputPrefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_kyiv

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
    BUTTON_PREVIEW = (By.CSS_SELECTOR, ('#' + inputPrefix + 'preview'))


class CompanyPreviewPageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')


class CompanyEditPageLocators:
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

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_kazakhstan = (By.CSS_SELECTOR, ('.field-' + CompanyEditPageLocators.inputPrefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_kazakhstan

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_karaganda = (By.CSS_SELECTOR, ('.field-' + CompanyEditPageLocators.inputPrefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_karaganda

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
    BUTTON_PREVIEW = (By.CSS_SELECTOR, ('#' + inputPrefix + 'preview'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации


class CompanyPersonalCabinetPageLocators():
    MY_VACANCIES = (By.XPATH, ('//a[contains(@href, "/vacancy/my")]/div[@class="employer-card"]'))
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/company/edit")]/div[@class="employer-card"]'))
    SERVICES_AND_PRICES = (By.XPATH, ('//a[contains(@href, "/prices")]/div[@class="employer-card"]'))


class MyVacanciesPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_ADD_VACANCY = (By.CSS_SELECTOR, ('#add-vacancy'))

    def assembly_of_locators_with_id_vacancies(self, id_vacancies):  # сборка локаторов с id вакансии
        locators_with_id_vacancies = {
            'button_vacancy_menu': (By.CSS_SELECTOR, ('#my-vacancy-' + id_vacancies + ' .share-btn')),
            'button_edit': (By.XPATH, ('//div[@id="my-vacancy-' + id_vacancies + '"]//a[contains(@href, "/vacancy/' + id_vacancies + '/edit")]')),
            'new_response_icon': (By.CSS_SELECTOR, '#my-vacancy-' + id_vacancies + ' .counter.red'),
            'button_show_responses': (By.XPATH, ('//a[contains(@href, "/vacancy/' + id_vacancies + '/feedback")]')),
            'button_print': (By.XPATH, '//a[@href="/vacancy/' + id_vacancies + '/print"]'),
            'button_delete': (By.CSS_SELECTOR, ('#my-vacancy-' + id_vacancies + ' .open-delete-modal'))
        }
        return locators_with_id_vacancies

    BUTTON_CONFIRMATION_DELETION_DRAFT_VACANCIES = (By.CSS_SELECTOR, ('[class="btn btn-blue btn-apply update-status"]'))

    INFO_TEXT_AFTER_CREATING_VACANCY = (By.CSS_SELECTOR, ('#lc-popup-vacancy-new .text'))  # информационный текст после создания вакансии
    CROSS_IN_POP_UP_AFTER_CREATING_VACANCY = (By.CSS_SELECTOR, ('#lc-popup-vacancy-new .close'))  # крестик в pop-up окне после создания вакансии

    INFO_TEXT_AFTER_ADDING_VACANCY_TO_DRAFT = (By.CSS_SELECTOR, ('#lc-popup-vacancy-draft h2'))  # информационный текст после добавления вакансии в черновик
    CROSS_IN_POP_UP_AFTER_ADDING_VACANCY_TO_DRAFT = (By.CSS_SELECTOR, ('#lc-popup-vacancy-draft .close'))  # крестик в pop-up окне после добавления вакансии в черновик

    INFO_TEXT_AFTER_DELETING_DRAFT_VACANCY = (By.CSS_SELECTOR, '#thanks-modal h2')  # информационный текст после удаления вакансии
    CROSS_IN_POP_UP_AFTER_DELETING_DRAFT_VACANCY = (By.CSS_SELECTOR, '#thanks-modal .close')  # крестик в pop-up окне после удаления вакансии

    INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#lc-popup-vacancy-moderation .text'))  # информационный текст после отправки вакансии на модерацию
    CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION = (By.CSS_SELECTOR, ('#lc-popup-vacancy-moderation .close'))  # крестик в pop-up окне после отправки вакансии на модерацию


class ResponsesToVacancyPageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')
    MARK_NOT_VIEWED_RESPONSE = (By.CSS_SELECTOR, ('.lc-card:nth-child(1) .lc-card-time > svg'))

    def assembly_of_locators_with_id_resume(self, id_resume):  # сборка локаторов с id резюме
        resume_in_responses_to_vacancy = (By.XPATH, ('//a[contains(@href, "/resume/' + id_resume + '")]'))
        return resume_in_responses_to_vacancy


class VacancyAddEditPageLocators:
    id_language = '1'
    input_prefix = 'vacancynew-descriptions-' + id_language + '-'

    def assembly_of_locators_from_id_block(self, id_block):  # сборка локаторов с id блока
        locators = {}
        locators['button_add_block'] = (By.CSS_SELECTOR, '#content-' + VacancyAddEditPageLocators.id_language + ' #' + id_block + ' .icon-plus')
        return locators

    CROSS_IN_COPY_TO_OTHER_LANGUAGES = (By.CSS_SELECTOR, '.copy-languages-toggle-tooltip')
    TAB = (By.CSS_SELECTOR, '[id="' + id_language + '-tab"]')
    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title'))
    VALIDATION_MESSAGE_FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title + p'))

    CATEGORY_VACANCIES_HUMAN_RESOURCES_DEPARTMENT = (By.XPATH, '//div[@id="' + input_prefix + 'category_id"]//div[@class="custom-control checkbox"][2]/label')
    CATEGORY_VACANCIES_SITE_PROMOTION = (By.XPATH, '//div[@id="' + input_prefix + 'category_id"]//div[@class="custom-control checkbox"][10]/label')
    SUBCATEGORIES_HR_MANAGER = (By.XPATH, '//div[@id="' + input_prefix + 'subcategories_id"]//div[@class="custom-control checkbox"][3]/label[contains(@for, "subcategories") and contains(@for, "-29")]')
    SUBCATEGORIES_SEO_SPECIALIST = (By.XPATH, '//div[@id="' + input_prefix + 'subcategories_id"]//div[@class="custom-control checkbox"][1]/label[contains(@for, "subcategories") and contains(@for, "-90")]')

    FIELD_MINIMAL_SALARY = (By.CSS_SELECTOR, '#' + input_prefix + 'salary_min')
    FIELD_MAXIMUM_SALARY = (By.CSS_SELECTOR, '#' + input_prefix + 'salary_max')
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, '[data-id="' + input_prefix + 'currency"]')
    CURRENCY_USD = (By.CSS_SELECTOR, '.field-' + input_prefix + 'currency [data-original-index="2"]')
    CURRENCY_UAH = (By.CSS_SELECTOR, '.field-' + input_prefix + 'currency [data-original-index="1"]')
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, '[data-id="' + input_prefix + 'country_id"]')
    COUNTRY_LIST = (By.CSS_SELECTOR, '#' + input_prefix + 'country_id > option')

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country = (By.CSS_SELECTOR, ('.field-' + VacancyAddEditPageLocators.input_prefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city = (By.CSS_SELECTOR, ('.field-' + VacancyAddEditPageLocators.input_prefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city

    FIELD_STREET = (By.CSS_SELECTOR, ('#' + input_prefix + 'street'))
    FIELD_PHONE = (By.CSS_SELECTOR, ('#' + input_prefix + 'phone'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + input_prefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + input_prefix + 'skype'))
    FIELD_CONTACT_PERSON = (By.CSS_SELECTOR, ('#' + input_prefix + 'contact_person'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + input_prefix + 'telegram'))
    FULL_EMPLOYMENT = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment > .checkbox:nth-child(1) > label'))
    REMOTE_WORK = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment > .checkbox:nth-child(3) > label'))
    WORK_EXPERIENCE_1_YEAR = (By.CSS_SELECTOR, '#' + input_prefix + 'work_experience > .checkbox:nth-child(2) > label')
    WORK_EXPERIENCE_2_YEAR = (By.CSS_SELECTOR, ('#' + input_prefix + 'work_experience > .checkbox:nth-child(3) > label'))
    DROPDOWN_EDUCATION = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'education"]'))
    HIGHER_EDUCATION = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'education [data-original-index="2"]'))
    SECONDARY_EDUCATION = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'education [data-original-index="5"]'))
    DROPDOWN_VACANCY_BENEFITS = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'advantages"]'))
    TRANSPORTATION = (By.CSS_SELECTOR, ('#content-' + id_language + ' #job-benefits [data-original-index="12"]'))
    FOREIGN_LANGUAGE_COURSES = (By.CSS_SELECTOR, ('#content-' + id_language + ' #job-benefits [data-original-index="7"]'))
    READY_TO_TAKE_STUDENT = (By.CSS_SELECTOR, ('#' + input_prefix + 'additionally > .checkbox:nth-child(1) > label'))
    READY_TO_TAKE_PERSON_WITH_DISABILITY = (By.CSS_SELECTOR, ('#' + input_prefix + 'additionally > .checkbox:nth-child(2) > label'))
    # блок "Основная информация"

    BUTTON_TO_DELETE_FIRST_LANGUAGE = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "del-block-link")])[1]'))
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-0-language"]')
    ENGLISH_LANGUAGE_1 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-0-language required")]//li[2]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-0-level"]')
    MIDDLE_LEVEL_1 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-0-level required")]//li[4]'))

    BUTTON_ADD_LANGUAGE_NUMBER_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "js-add-more")])[1]'))

    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-language"]')
    RUSSIAN_LANGUAGE_2 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-language required")]//li[38]'))
    ENGLISH_LANGUAGE_2 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-language required")]//li[2]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-level"]')
    NATIVE_LEVEL_2 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-level required")]//li[8]'))
    ABOVE_AVERAGE_LEVEL_2 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-1-level required")]//li[4]'))

    # BUTTON_ADD_LANGUAGE_NUMBER_3 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "js-add-more")])[2]'))
    #
    # DROPDOWN_LANGUAGE_3 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-2-language"]')
    # HEBREW_LANGUAGE_3 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-2-language required")]//li[21]'))
    # DROPDOWN_LEVEL_OF_LANGUAGE_3 = (By.CSS_SELECTOR, '[data-id="vacancynew-knowledgeoflanguagesnew-' + id_language + '-2-level"]')
    # MIDDLE_LEVEL_3 = (By.XPATH, ('//div[contains(@class, "field-vacancynew-knowledgeoflanguagesnew-' + id_language + '-2-level required")]//li[4]'))
    # блок "Знание языков"

    IFRAME_CKEDITOR_DESCRIPTION_OF_VACANCIES = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'description iframe'))
    # блок "Описание вакансии"

    IFRAME_CKEDITOR_ABOUT_COMPANY = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'about_company iframe'))
    # блок "О компании"

    IFRAME_CKEDITOR_WORKING_CONDITIONS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'working_conditions iframe'))
    # блок "Условия работы"

    IFRAME_CKEDITOR_TASKS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'tasks iframe'))
    # блок "Задачи"

    IFRAME_CKEDITOR_REQUIREMENTS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'requirements iframe'))
    # блок "Требования к соискателю"

    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'additionally_information iframe'))
    # блок "Дополнительная информация"

    CKEDITOR = (By.CSS_SELECTOR, 'body.cke_editable')  # общий для всех блоков
    BUTTON_PUBLISH = (By.CSS_SELECTOR, '#submit-button')
    BUTTON_TO_DRAFTS = (By.CSS_SELECTOR, '#draft-button')
    BUTTON_PREVIEW = (By.CSS_SELECTOR, '#vacancyform-preview')


class VacancyPreviewPageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')


class ServicesAndPricesPageLocators:
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
        for id in singleton.id_purchase:
            product_in_non_activated_services.append((By.CSS_SELECTOR, ('.tab-deactivate-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"]')))
            product_in_activated_services.append((By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"]')))
            button_product_activation.append((By.XPATH, ('//a[contains(@href, "/cart/active?id=' + id + '")]')))
            arrow_for_viewing_options_available_in_package.append((By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"] .more')))
            number_of_vacancies_available.append((By.CSS_SELECTOR, '.tab-activated-servises .packages-wrap[data-product-id="' + singleton.id_product + '"][data-purchases-id="' + id + '"] p.small-text'))

        locators = [product_in_non_activated_services,
                    product_in_activated_services,
                    button_product_activation,
                    arrow_for_viewing_options_available_in_package,
                    number_of_vacancies_available]
        return locators

    def new_assembly_of_locators_with_id_product_and_id_purchase(self, id_product, id_purchase):  # сборка локаторов с id продукта и id покупок
        locators_with_id_product_and_id_purchase = {
            'arrow_for_viewing_options_available_in_package': (By.CSS_SELECTOR, '.tab-activated-servises .packages-wrap[data-product-id="' + id_product + '"][data-purchases-id="' + id_purchase + '"] .more'),
            'number_of_vacancies_available': (By.CSS_SELECTOR, '.tab-activated-servises .packages-wrap[data-product-id="' + id_product + '"][data-purchases-id="' + id_purchase + '"] p.small-text')
        }
        return locators_with_id_product_and_id_purchase

    BUTTON_ORDER_IN_HELP_REFUGEE_WITH_HIS_WORK = (By.CSS_SELECTOR, ('[data-product-id="15"]'))
    HELP_REFUGEE_WITH_HIS_WORK_IN_BASKET = (By.CSS_SELECTOR, ('.bascket-list-item > [data-product-id="15"]'))

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
    INFO_TEXT_AFTER_OPERATIONS_IN_INTERKASSA = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после операций в interkassa
    CROSS_IN_POP_UP_AFTER_OPERATIONS_IN_INTERKASSA = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после операций в interkassa


class ResumePageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')
    COVER_LETTER_TEXT = (By.CSS_SELECTOR, '.covering-letter-description')
    BUTTON_RESUME_MENU = (By.CSS_SELECTOR, '.share-btn')
    BUTTON_PRINT = (By.XPATH, '//a[contains(@href, "/print")]')

    CONTACT_INFORMATION_BLOCK = (By.CSS_SELECTOR, '.cv-card .danger')
    CONTACT_BLOCK = (By.CSS_SELECTOR, '.contacts-block')
    BUTTON_VIEW_CONTACTS = (By.CSS_SELECTOR, '.contacts-block [data-target="#open-contacts"]')
    BUTTON_OPEN_CONTACT_IN_POP_UP = (By.CSS_SELECTOR, '#open-contacts .open-contact')
    TEXT_OF_CONTACT_BLOCK_BEFORE_AUTHORIZATION = (By.CSS_SELECTOR, '.cv-card .danger p')
    TEXT_OF_CONTACT_BLOCK = (By.CSS_SELECTOR, '.cv-card .danger h4')

    PHONE_1_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.contacts-block-items > .item:nth-child(1) span')  # очередность сохраняется при условии наличия всех контактов
    PHONE_2_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.contacts-block-items > .item:nth-child(2) span')  # очередность сохраняется при условии наличия всех контактов
    EMAIL_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.contacts-block-items > .item:nth-child(3) span')  # очередность сохраняется при условии наличия всех контактов
    SKYPE_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.contacts-block-items > .item:nth-child(4) span')  # очередность сохраняется при условии наличия всех контактов
    PORTFOLIO_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .site')  # очередность сохраняется при условии наличия всех контактов
    FACEBOOK_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .fb')  # очередность сохраняется при условии наличия всех контактов
    LINKEDIN_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .in')  # очередность сохраняется при условии наличия всех контактов
    INSTAGRAM_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .inst')  # очередность сохраняется при условии наличия всех контактов
    TELEGRAM_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .tel')  # очередность сохраняется при условии наличия всех контактов
    TWITTER_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .twit')  # очередность сохраняется при условии наличия всех контактов
    VK_IN_CONTACT_INFORMATION = (By.CSS_SELECTOR, '.socials-list .vk')  # очередность сохраняется при условии наличия всех контактов


class InterkassaPageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')

    BUTTON_TEST_PAYSYSTEM = (By.CSS_SELECTOR, '[class="paysystems-category"] [href="#/paysystem/test"]')
    CHECKBOX_CONSENT_WITH_INTERKASSA_RULES = (By.CSS_SELECTOR, '#agreement')
    BUTTON_PAY = (By.CSS_SELECTOR, '.pay-button')
    BUTTON_CREATE_TEST_PAYMENT = (By.CSS_SELECTOR, '.controls > :nth-child(1)[type="submit"]')
    BUTTON_CREATE_CANCEL_TEST_PAYMENT = (By.CSS_SELECTOR, '.controls > :nth-child(2)[type="submit"]')
    BUTTON_PENDING = (By.CSS_SELECTOR, '.controls > :nth-child(4)[type="submit"]')
