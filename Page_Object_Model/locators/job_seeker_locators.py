from selenium.webdriver.common.by import By
from Page_Object_Model.singleton import Singleton


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
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_ukraine = (By.CSS_SELECTOR, ('.field-' + JobSeekerRegistrationPageLocators.inputPrefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_ukraine

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_kyiv = (By.CSS_SELECTOR, ('.field-' + JobSeekerRegistrationPageLocators.inputPrefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_kyiv
    # блок "Личная информация"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, ('#button-registration'))


class JobSeekerEditPageLocators:
    inputPrefix = 'jobseekereditform-'

    BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#personal-information .post-resume-title + .btn-edit'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + inputPrefix + 'surname'))
    FIELD_YEAR = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayy > option:nth-child(2)'))
    FIELD_MONTH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdaym > option:nth-child(2)'))
    FIELD_DAY = (By.CSS_SELECTOR, ('#' + inputPrefix + 'birthdayd > option:nth-child(2)'))
    FIELD_GENDER = (By.CSS_SELECTOR, ('#' + inputPrefix + 'gender [value="1"] + .radio-custom'))
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_kazakhstan = (By.CSS_SELECTOR, ('.field-' + JobSeekerEditPageLocators.inputPrefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_kazakhstan

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_karaganda = (By.CSS_SELECTOR, ('.field-' + JobSeekerEditPageLocators.inputPrefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_karaganda
    # блок "Личная информация"

    BUTTON_EDIT_IN_SETTINGS_BLOCK = (By.CSS_SELECTOR, ('#other-settings .post-resume-title + .btn-edit'))
    DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL = (By.CSS_SELECTOR, ('[data-id="' + inputPrefix + 'mail_language"]'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="0"]'))  # русский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="1"]'))  # украинский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_EN = (By.CSS_SELECTOR, ('.field-' + inputPrefix + 'mail_language [data-original-index="2"]'))  # украинский
    # блок "Настройки"

    BUTTON_SAVE_CHANGES = (By.CSS_SELECTOR, ('#submit-publish'))

    INFO_TEXT_AFTER_SAVING_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст после сохранения изменений личной информации
    CROSS_IN_POP_UP_AFTER_SAVING_CHANGES_TO_PERSONAL_INFORMATION = (By.CSS_SELECTOR, ('#thanks-modal .close'))  # крестик в pop-up окне после сохранения изменений личной информации


class JobSeekerPersonalCabinetPageLocators:
    MY_RESUME = (By.XPATH, ('//a[contains(@href, "/resume/my")]/div[@class="employer-card"]'))
    MY_RESPONSES = (By.XPATH, ('//a[contains(@href, "/vacancy/feedback")]/div[@class="employer-card"]'))
    PERSONAL_DATA = (By.XPATH, ('//a[contains(@href, "/job-seeker/edit")]/div[@class="employer-card"]'))


class MyResumePageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    TEXT_OF_NUMBER_OF_CREATED_RESUMES = (By.CSS_SELECTOR, ('.page-title p'))
    BUTTON_ADD_RESUME = (By.CSS_SELECTOR, ('.btn-wrap > .btn.btn-blue'))

    BUTTON_RESUME_MENU = (By.CSS_SELECTOR, ('.lc-card.my-cv-card:nth-child(1) .lc-card-bookmarks'))  # первый в списке

    def assembly_of_locators_with_id_resume(self, index):  # сборка локаторов с id резюме
        singleton = Singleton()
        button_edit = (By.XPATH, '//a[contains(@href, "/resume/' + singleton.id_resume[index] + '/edit")]')
        button_delete = (By.CSS_SELECTOR, '.open-delete-modal[data-resume-id="' + singleton.id_resume[index] + '"]')
        locators = [button_edit,
                    button_delete]
        return locators

    BUTTON_PRINT = (By.XPATH, '//a[contains(@href, "/print")]')  # работает для первого резюме в списке
    BUTTON_CONFIRMATION_DELETION_DRAFT_RESUME = (By.CSS_SELECTOR, ('[class="btn btn-blue btn-apply update-status"]'))

    INFO_TEXT_AFTER_CREATING_RESUME = (By.CSS_SELECTOR, '#lc-popup-resume-new .text')  # информационный текст после создания резюме
    CROSS_IN_POP_UP_AFTER_CREATING_RESUME = (By.CSS_SELECTOR, ('#lc-popup-resume-new .close'))  # крестик в pop-up окне после создания резюме

    INFO_TEXT_AFTER_ADDING_RESUME_TO_DRAFT = (By.CSS_SELECTOR, ('#lc-popup-resume-draft h2'))  # информационный текст после добавления вакансии в черновик
    CROSS_IN_POP_UP_AFTER_ADDING_RESUME_TO_DRAFT = (By.CSS_SELECTOR, ('#lc-popup-resume-draft .close'))  # крестик в pop-up окне после добавления вакансии в черновик

    INFO_TEXT_AFTER_DELETING_DRAFT_RESUME = (By.CSS_SELECTOR, '#thanks-modal h2')  # информационный текст после удаления вакансии
    CROSS_IN_POP_UP_AFTER_DELETING_DRAFT_RESUME = (By.CSS_SELECTOR, '#thanks-modal .close')  # крестик в pop-up окне после удаления вакансии

    INFO_TEXT_AFTER_SUBMITTING_RESUME_FOR_MODERATION = (By.CSS_SELECTOR, ('#lc-popup-resume-moderation .text'))  # информационный текст после отправки резюме на модерацию
    CROSS_IN_POP_UP_AFTER_SUBMITTING_RESUME_FOR_MODERATION = (By.CSS_SELECTOR, ('#lc-popup-resume-moderation .close'))  # крестик в pop-up окне после отправки резюме на модерацию


class ResumeAddEditPageLocators:
    id_language = '1'
    input_prefix = 'resumenew-descriptions-' + id_language + '-'

    def assembly_of_locators_from_id_block(self, id_block):  # сборка локаторов с id блока
        locators = {}
        locators['button_add_block'] = (By.CSS_SELECTOR, '#' + id_block + ' .icon-plus')
        return locators

    TAB = (By.CSS_SELECTOR, '[id="' + id_language + '-tab"]')
    FIELD_PHOTO = (By.CSS_SELECTOR, '#resumenew-photo')
    FIELD_NAME = (By.CSS_SELECTOR, '#' + input_prefix + 'name')
    FIELD_SURNAME = (By.CSS_SELECTOR, '#' + input_prefix + 'surname')

    DROPDOWN_YEAR = (By.CSS_SELECTOR, '[data-id="' + input_prefix + 'birthdayy"]')
    YEAR_OF_BIRTH_1981 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayy [data-original-index="21"]'))
    DROPDOWN_MONTH = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdaym"]'))
    MONTH_SEPTEMBER = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdaym [data-original-index="9"]'))
    DROPDOWN_DAY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdayd"]'))
    DAY_5 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayd [data-original-index="5"]'))

    FIELD_GENDER_FEMALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="2"] + .radio-custom'))

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_ukraine = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_ukraine

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_odessa = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_odessa

    DROPDOWN_WILLING_TO_RELOCATE = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'willing_relocate"]'))
    NOT_READY_TO_RELOCATE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'willing_relocate [data-original-index="2"]'))
    # блок "Личная информация"

    FIELD_PHONE_1 = (By.CSS_SELECTOR, ('[name="ResumeNew[descriptions][' + id_language + '][phone]"]'))
    BUTTON_ADD_PHONE = (By.XPATH, ('(//div[@id = "content-' + id_language + '"]//div[@id = "contact-information"]//button[contains(@class, "addPhone")])[1]'))
    FIELD_PHONE_2 = (By.CSS_SELECTOR, ('[name="ResumeNew[descriptions][' + id_language + '][phone2]"]'))

    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + input_prefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + input_prefix + 'skype'))
    FIELD_PORTFOLIO = (By.CSS_SELECTOR, ('#' + input_prefix + 'portfolio'))

    BUTTON_FACEBOOK = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="facebookCollapse"]'))
    BUTTON_LINKEDIN = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="lnCollapse"]'))
    BUTTON_INSTAGRAM = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="inCollapse"]'))
    BUTTON_TELEGRAM = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="telCollapse"]'))
    BUTTON_TWITTER = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="twCollapse"]'))
    BUTTON_VK = (By.CSS_SELECTOR, ('#content-' + id_language + ' [aria-controls="vkCollapse"]'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('#' + input_prefix + 'facebook'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('#' + input_prefix + 'linkedin'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('#' + input_prefix + 'instagram'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + input_prefix + 'telegram'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('#' + input_prefix + 'twitter'))
    FIELD_VK = (By.CSS_SELECTOR, ('#' + input_prefix + 'vk'))
    # блок "Контактная информация"

    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title'))
    VALIDATION_MESSAGE_FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title + p'))

    CATEGORY_RESUME = (By.XPATH, '//div[@id="resumenew-descriptions-' + id_language + '-category_id"]//div[@class="custom-control checkbox"][8]/label')
    SUBCATEGORIES = (By.XPATH, '//div[@id="resumenew-descriptions-' + id_language + '-subcategories_id"]//div[@class="custom-control checkbox"][7]/label[contains(@for, "subcategories") and contains(@for, "-70")]')
    DISTANT_WORK = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment .checkbox:nth-child(3) > label'))  # удаленная работа
    SALARY = (By.CSS_SELECTOR, '#' + input_prefix + 'salary')
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'currency"]'))
    CURRENCY_UAH = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'currency [data-original-index="1"]'))
    # блок "Желаемая должность"

    IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'skills iframe'))
    # блок "Навыки и достижения"

    # блок "Опыт работы"
    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-company')
    FIELD_SITE_COMPANY = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-web_site')
    SCOPE_OF_COMPANY_CASINO_STAFF = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-0-category"]//div[@class="custom-control checkbox"][3]/label')
    FIELD_POSITION = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-position')

    DROPDOWN_MONTH_WORK_EXPERIENCE_START = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_start_m"]')
    MONTH_AUGUST_WORK_EXPERIENCE_START = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_m required")]//li[9]/a')
    DROPDOWN_YEAR_WORK_EXPERIENCE_START = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_start_y"]')
    YEAR_WORK_EXPERIENCE_START_2018 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_y required")]//li[6]/a')

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_end_m"]')
    MONTH_MARCH_WORK_EXPERIENCE_FINISH = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_m required")]//li[5]/a')
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_end_y"]')
    YEAR_WORK_EXPERIENCE_FINISH_2020 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_y required")]//li[4]/a')

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, '#cke_resumenew-workexperiencenew-' + id_language + '-0-responsibilities iframe')

    BUTTON_ADD_WORK_EXPERIENCE_2 = (By.XPATH, '(//div[@id="content-' + id_language + '"]//div[@id="work-experience"]//button[contains(@class, "js-add-more")])[1]')

    FIELD_COMPANY_NAME_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-company')
    FIELD_SITE_COMPANY_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-web_site')
    SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2 = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-1-category"]//div[@class="custom-control checkbox"][6]/label')
    FIELD_POSITION_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-position')

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_start_m"]'))
    MONTH_APRIL_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_m required")]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_start_y"]'))
    YEAR_WORK_EXPERIENCE_START_2020_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_y required")]//li[4]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_end_m"]'))
    WORKING_NOW_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_end_m required")]//li[2]/a'))
    # DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    # YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2 = (By.CSS_SELECTOR, ('#cke_resumenew-workexperiencenew-' + id_language + '-1-responsibilities iframe'))
    # блок "Опыт работы"

    DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'gambling_experience"]'))
    WITHOUT_EXPERIENCE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'gambling_experience [data-original-index="1"]'))
    # блок "Опыт работы в игорной индустрии"

    # блок "Образование"
    FIELD_NAME_OF_INSTITUTION = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-name_institution'))
    DROPDOWN_LEVEL_OF_EDUCATION = (By.CSS_SELECTOR, ('[data-id="resumenew-educationsnew-' + id_language + '-0-level_education"]'))
    HIGHER_EDUCATION = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-level_education required")]//li[2]/a'))

    DROPDOWN_COUNTRY_EDUCATION = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-country_id"]')
    COUNTRY_EDUCATION_LIST = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-country_id > option'))

    def assembly_of_locators_with_position_country_education(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_ukraine_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-0-country_id")]//li[' + str(position_object) + ']/a'))
        return country_ukraine_education

    DROPDOWN_CITI_EDUCATION = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-city_id"]')
    CITY_EDUCATION_LIST = (By.CSS_SELECTOR, '#resumenew-educationsnew-' + id_language + '-0-city_id > option')

    def assembly_of_locators_with_position_city_education(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_kharkov_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-0-city_id")]//li[' + str(position_object) + ']/a'))
        return city_kharkov_education

    FIELD_DEPARTMENT_AND_SPECIALITY = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-specialty'))

    DROPDOWN_MONTH_EDUCATION_START = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_start_m"]')
    MONTH_SEPTEMBER_EDUCATION_START = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_m")]//li[10]/a')
    DROPDOWN_YEAR_EDUCATION_START = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_start_y"]')
    YEAR_EDUCATION_START_2010 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_y")]//li[14]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_end_m"]')
    MONTH_MAY_EDUCATION_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_m")]//li[7]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_end_y"]')
    YEAR_EDUCATION_FINISH_2015 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_y")]//li[9]/a'))

    BUTTON_ADD_EDUCATION_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="education"]//button[contains(@class, "js-add-more")])[1]'))

    FIELD_NAME_OF_INSTITUTION_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-name_institution'))
    DROPDOWN_LEVEL_OF_EDUCATION_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-educationsnew-' + id_language + '-1-level_education"]'))
    SECONDARY_SPECIAL_EDUCATION_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-level_education required")]//li[4]/a'))

    DROPDOWN_COUNTRY_EDUCATION_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-country_id"]')
    COUNTRY_EDUCATION_LIST_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-country_id > option'))

    def assembly_of_locators_with_position_country_education_2(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_belarus_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-1-country_id")]//li[' + str(position_object) + ']/a'))
        return country_belarus_education

    DROPDOWN_CITI_EDUCATION_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-city_id"]')
    CITY_EDUCATION_LIST_2 = (By.CSS_SELECTOR, '#resumenew-educationsnew-' + id_language + '-1-city_id > option')

    def assembly_of_locators_with_position_city_education_2(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_minsk_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-1-city_id")]//li[' + str(position_object) + ']/a'))
        return city_minsk_education

    FIELD_DEPARTMENT_AND_SPECIALITY_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-specialty'))

    DROPDOWN_MONTH_EDUCATION_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_start_m"]')
    MONTH_NOVEMBER_EDUCATION_START_2 = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_m")]//li[12]/a')
    DROPDOWN_YEAR_EDUCATION_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_start_y"]')
    YEAR_EDUCATION_START_2018_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_y")]//li[6]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_end_m"]')
    MONTH_JANUARY_EDUCATION_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_m")]//li[3]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_end_y"]')
    YEAR_EDUCATION_FINISH_2020_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_y")]//li[4]/a'))
    # блок "Образование"

    # блок "Курсы и сертификаты"
    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE = (By.CSS_SELECTOR, ('#resumenew-coursesnew-' + id_language + '-0-name_certificate'))

    DROPDOWN_MONTH_COURSES_START = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_start_m"]')
    MONTH_JUNE_COURSES_START = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_m")]//li[7]/a'))
    DROPDOWN_YEAR_COURSES_START = (By.CSS_SELECTOR, ('[data-id="resumenew-coursesnew-' + id_language + '-0-period_start_y"]'))
    YEAR_COURSES_START_2020 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_y")]//li[4]/a'))

    DROPDOWN_MONTH_COURSES_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_end_m"]')
    MONTH_JUNE_COURSES_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_m")]//li[8]/a'))
    DROPDOWN_YEAR_COURSES_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_end_y"]')
    YEAR_COURSES_FINISH_2021 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_y")]//li[3]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION = (By.XPATH, ('//div[@id="cke_resumenew-coursesnew-' + id_language + '-0-description"]//iframe'))

    BUTTON_ADD_COURSES_AND_CERTIFICATES_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="courses-and-certificates"]//button[contains(@class, "js-add-more")])[1]'))

    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2 = (By.CSS_SELECTOR, ('#resumenew-coursesnew-' + id_language + '-1-name_certificate'))

    DROPDOWN_MONTH_COURSES_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_start_m"]')
    MONTH_OCTOBER_COURSES_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_m")]//li[11]/a'))
    DROPDOWN_YEAR_COURSES_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-coursesnew-' + id_language + '-1-period_start_y"]'))
    YEAR_COURSES_START_2014_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_y")]//li[10]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_end_m"]')
    MONTH_OCTOBER_COURSES_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_m")]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_end_y"]')
    YEAR_COURSES_FINISH_2015_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_y")]//li[9]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_2 = (By.XPATH, ('//div[@id="cke_resumenew-coursesnew-' + id_language + '-1-description"]//iframe'))
    # блок "Курсы и сертификаты"

    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-0-language"]')
    POLISH_LANGUAGE_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-language required")]//li[35]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-0-level"]')
    HIGH_LEVEL_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-level required")]//li[6]'))

    BUTTON_ADD_LANGUAGE_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "js-add-more")])[1]'))

    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-1-language"]')
    GERMAN_LANGUAGE_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-language required")]//li[5]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-1-level"]')
    FREE_LEVEL_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-level required")]//li[7]'))
    # блок "Знание языков"

    RADIO_I_DONT_HAVE_DISABILITY = (By.XPATH, ('//div[@id="resumenew-descriptions-' + id_language + '-disability"]//input[@value="1"]'))
    I_HAVE_DISABILITY = (By.CSS_SELECTOR, ('//div[@id="resumenew-descriptions-' + id_language + '-disability"]//input[@value="2"]'))
    # блок "Инвалидность"

    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.XPATH, ('//div[@id="cke_resumenew-descriptions-' + id_language + '-additionally_information"]//iframe'))
    # блок "Дополнительная информация"

    DROPDOWN_JOB_SEARCH_STATUS = (By.CSS_SELECTOR, ('[data-id="resumenew-job_search_status"]'))
    ACTIVELY_LOOKING_FOR_JOB = (By.XPATH, '//div[@class=" field-resumenew-job_search_status required"]//li[3]')
    # блок "Статус поиска работы"

    RESUME_COMPLETED_ON = (By.CSS_SELECTOR, ('.post-resume-status span.resume-rate'))
    STATUS_OF_YOUR_RESUME = (By.CSS_SELECTOR, ('.post-resume-status span.small-text.d-block'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков

    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-button'))
    BUTTON_TO_DRAFTS = (By.CSS_SELECTOR, ('#draft-button'))


class ResumeAddEditPageLocators():
    input_prefix = 'resumeeditform-'

    BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#personal-information .post-resume-title + .btn-edit'))
    FIELD_PHOTO = (By.CSS_SELECTOR, ('#' + input_prefix + 'photo'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + input_prefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + input_prefix + 'surname'))

    DROPDOWN_YEAR = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdayy"]'))
    YEAR_OF_BIRTH_1976 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayy [data-original-index="26"]'))
    DROPDOWN_MONTH = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdaym"]'))
    MONTH_MARCH = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdaym [data-original-index="3"]'))
    DROPDOWN_DAY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdayd"]'))
    DAY_8 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayd [data-original-index="8"]'))

    FIELD_GENDER_MALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="1"] + .radio-custom'))

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country_poland = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country_poland

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city_poznan = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city_poznan

    DROPDOWN_WILLING_TO_RELOCATE = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'willing_relocate"]'))
    READY_TO_RELOCATE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'willing_relocate [data-original-index="1"]'))
    # блок "Личная информация"

    BUTTON_EDIT_IN_CONTACT_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#contact-information .post-resume-title + .btn-edit'))
    FIELD_PHONE_1 = (By.CSS_SELECTOR, ('#' + input_prefix + 'phone'))
    FIELD_PHONE_2 = (By.CSS_SELECTOR, ('#resume-phone-add1'))

    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + input_prefix + 'email'))
    FIELD_SKYPE = (By.CSS_SELECTOR, ('#' + input_prefix + 'skype'))
    FIELD_PORTFOLIO = (By.CSS_SELECTOR, ('#' + input_prefix + 'portfolio'))

    FIELD_FACEBOOK = (By.CSS_SELECTOR, ('#' + input_prefix + 'facebook'))
    FIELD_LINKEDIN = (By.CSS_SELECTOR, ('#' + input_prefix + 'linkedin'))
    FIELD_INSTAGRAM = (By.CSS_SELECTOR, ('#' + input_prefix + 'instagram'))
    FIELD_TELEGRAM = (By.CSS_SELECTOR, ('#' + input_prefix + 'telegram'))
    FIELD_TWITTER = (By.CSS_SELECTOR, ('#' + input_prefix + 'twitter'))
    FIELD_VK = (By.CSS_SELECTOR, ('#' + input_prefix + 'vk'))
    # блок "Контактная информация"

    BUTTON_EDIT_IN_POSITION_DESIRED_BLOCK = (By.CSS_SELECTOR, ('#desired-job-title .post-resume-title + .btn-edit'))
    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title'))
    CATEGORY_RESUME = "document.getElementsByName('ResumeEditForm[category_id][]')[13].click()"
    SUBCATEGORIES = (By.CSS_SELECTOR, ('[for="subcategories_id-168"]'))
    UNDEREMPLOYMENT = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment > .checkbox:nth-child(2) > label'))  # Неполная занятость
    SALARY = (By.CSS_SELECTOR, ('#' + input_prefix + 'salary'))
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'currency"]'))
    CURRENCY_USD = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'currency [data-original-index="2"]'))
    # блок "Желаемая должность"

    BUTTON_EDIT_IN_SKILLS_AND_ACHIEVEMENTS_BLOCK = (By.CSS_SELECTOR, ('#skills-and-achievements .post-resume-title + .right .btn-edit'))
    IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'skills iframe'))
    # блок "Навыки и достижения"

    BUTTON_EDIT_IN_WORK_EXPERIENCE_BLOCK = (By.CSS_SELECTOR, ('#work-experience .post-resume-title + .btn-edit'))
    FIELD_COMPANY_NAME = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[1]//input[contains(@id, "resumeworkexperienceform")]'))
    FIELD_SITE_COMPANY = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[2]//input[contains(@id, "resumeworkexperienceform")]'))
    SCOPE_OF_COMPANY_SECURITY_SERVICE = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//div[contains(@id, "resumeworkexperienceform")]//div[@class="custom-control checkbox"][5]/label'))
    FIELD_POSITION = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[4]//input[contains(@id, "resumeworkexperienceform")]'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_DECEMBER_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[13]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_START = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[14]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JANUARY_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[3]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[12]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "work-experience-form")]/div[6]//iframe'))

    FIELD_COMPANY_NAME_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[1]//input[contains(@id, "resumeworkexperienceform")]'))
    FIELD_SITE_COMPANY_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[2]//input[contains(@id, "resumeworkexperienceform")]'))
    SCOPE_OF_COMPANY_WEBSITE_PROMOTION_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//div[contains(@id, "resumeworkexperienceform")]//div[@class="custom-control checkbox"][10]/label'))
    FIELD_POSITION_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[4]//input[contains(@id, "resumeworkexperienceform")]'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_FEBRUARY_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[3]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[31]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_MARCH_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[28]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[6]//iframe'))

    BUTTON_ADD_WORK_EXPERIENCE_NUMBER_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[7]//button[contains(@class, "resume-item-link js-add-work-place")]'))

    FIELD_COMPANY_NAME_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[1]//input[contains(@id, "resumeworkexperienceform")]'))
    FIELD_SITE_COMPANY_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[2]//input[contains(@id, "resumeworkexperienceform")]'))
    SCOPE_OF_COMPANY_WEBSITE_PROMOTION_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//div[contains(@id, "resumeworkexperienceform")]//div[@class="custom-control checkbox"][10]/label'))
    FIELD_POSITION_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[4]//input[contains(@id, "resumeworkexperienceform")]'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_APRIL_WORK_EXPERIENCE_START_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_WORK_EXPERIENCE_START_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[21]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    WORKING_NOW_WORK_EXPERIENCE_FINISH_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[2]/a'))
    # DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    # YEAR_WORK_EXPERIENCE_FINISH_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[28]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_3 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "work-experience-form")]/div[6]//iframe'))
    # блок "Опыт работы"

    DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'gambling_experience"]'))
    EXPERIENCE_2_TO_5_YEARS = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'gambling_experience [data-original-index="4"]'))
    # блок "Опыт работы в игорной идустрии"

    BUTTON_EDIT_IN_EDUCATION_BLOCK = (By.CSS_SELECTOR, ('#education .post-resume-title + .close-form-card-top-btn-wrap > .btn-edit'))
    FIELD_NAME_OF_INSTITUTION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[1]//input[contains(@id, "resumeeducationform")]'))
    DROPDOWN_LEVEL_OF_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[2]//button'))
    UNFINISHED_HIGHER_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[2]//li[3]/a'))

    DROPDOWN_COUNTRY_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[3]//button'))
    COUNTRY_NOT_SELECTED_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[3]//li[1]/a'))
    DROPDOWN_CITI_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[4]//button'))
    CITI_NOT_SELECTED_EDUCATION = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[4]//li[1]/a'))

    FIELD_DEPARTMENT_AND_SPECIALITY = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[5]//input[contains(@id, "resumeeducationform")]'))

    DROPDOWN_MONTH_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_NOT_SELECTED_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[1]/a'))
    DROPDOWN_YEAR_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_NOT_SELECTED_EDUCATION_START = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[1]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_NOT_SELECTED_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[1]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_NOT_SELECTED_EDUCATION_FINISH = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[1]/a'))

    FIELD_NAME_OF_INSTITUTION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[1]//input[contains(@id, "resumeeducationform")]'))
    DROPDOWN_LEVEL_OF_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[2]//button'))
    SECONDARY_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[2]//li[5]/a'))

    DROPDOWN_COUNTRY_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[3]//button'))
    COUNTRY_EDUCATION_LIST_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[3]//option'))

    def assembly_of_locators_with_position_country_education_2(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_ukraine_education = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[3]//li[' + str(position_object) + ']/a'))
        return country_ukraine_education

    DROPDOWN_CITI_EDUCATION_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[4]//button'))
    CITY_EDUCATION_LIST_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[4]//option'))

    def assembly_of_locators_with_position_city_education_2(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_cherkasy_education = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[4]//li[' + str(position_object) + ']/a'))
        return city_cherkasy_education

    FIELD_DEPARTMENT_AND_SPECIALITY_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[5]//input[contains(@id, "resumeeducationform")]'))

    DROPDOWN_MONTH_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JUNE_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[7]/a'))
    DROPDOWN_YEAR_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_START_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[19]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JULY_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[9]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_FINISH_2 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[16]/a'))

    BUTTON_ADD_EDUCATION_NUMBER_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "education-form")]/div[7]//button[contains(@class, "resume-item-link js-add-education")]'))

    FIELD_NAME_OF_INSTITUTION_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[1]//input[contains(@id, "resumeeducationform")]'))
    DROPDOWN_LEVEL_OF_EDUCATION_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[2]//button'))
    HIGHER_EDUCATION_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[2]//li[2]/a'))

    DROPDOWN_COUNTRY_EDUCATION_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[3]//button'))
    COUNTRY_EDUCATION_LIST_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[3]//option'))

    def assembly_of_locators_with_position_country_education_3(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_cyprus_education = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[3]//li[' + str(position_object) + ']/a'))
        return country_cyprus_education

    DROPDOWN_CITI_EDUCATION_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[4]//button'))
    CITY_EDUCATION_LIST_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[4]//option'))

    def assembly_of_locators_with_position_city_education_3(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_limassol_education = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[4]//li[' + str(position_object) + ']/a'))
        return city_limassol_education

    FIELD_DEPARTMENT_AND_SPECIALITY_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[5]//input[contains(@id, "resumeeducationform")]'))

    DROPDOWN_MONTH_EDUCATION_START_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_AUGUST_EDUCATION_START_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[9]/a'))
    DROPDOWN_YEAR_EDUCATION_START_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_EDUCATION_START_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    STUDY_NOW_EDUCATION_FINISH_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[2]/a'))
    # DROPDOWN_YEAR_EDUCATION_FINISH_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    # YEAR_EDUCATION_FINISH_3 = (By.XPATH, ('//div[@id="education"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "education-form")]/div[6]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[16]/a'))
    # блок "Образование"

    BUTTON_EDIT_IN_COURSES_AND_CERTIFICATES_BLOCK = (By.CSS_SELECTOR, ('#courses-and-certificates .post-resume-title + .close-form-card-top-btn-wrap > .btn-edit'))
    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[1]//input[contains(@id, "resumecourseform")]'))

    DROPDOWN_MONTH_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_SEPTEMBER_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[10]/a'))
    DROPDOWN_YEAR_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_START = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[8]/a'))

    DROPDOWN_MONTH_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_OCTOBER_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_FINISH = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[8]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][1]//form[contains(@id, "course-form")]/div[3]//iframe'))

    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[1]//input[contains(@id, "resumecourseform")]'))

    DROPDOWN_MONTH_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_NOVEMBER_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_START_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_NOVEMBER_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[13]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_FINISH_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[3]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_2 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[3]//iframe'))

    BUTTON_ADD_COURSES_NUMBER_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "course-form")]/div[4]//button[contains(@class, "resume-item-link js-add-courses")]'))

    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[1]//input[contains(@id, "resumecourseform")]'))

    DROPDOWN_MONTH_COURSES_START_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_DECEMBER_COURSES_START_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][1]//li[13]/a'))
    DROPDOWN_YEAR_COURSES_START_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_START_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex width"]/div[contains(@class, "search-select")][2]//li[7]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//button'))
    MONTH_JANUARY_COURSES_FINISH_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][1]//li[3]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    YEAR_COURSES_FINISH_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[2]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[6]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_3 = (By.XPATH, ('//div[@id="courses-and-certificates"]//div[contains(@class, "additional-block-item")][3]//form[contains(@id, "course-form")]/div[3]//iframe'))
    # блок "Курсы и сертификаты"

    BUTTON_EDIT_IN_KNOWLEDGE_OF_LANGUAGES_BLOCK = (By.CSS_SELECTOR, ('#knowledge-of-languages .post-resume-title + .btn-edit'))
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-language"]'))
    ENGLISH_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-language [data-original-index="1"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) [data-id="languageaddform-level"]'))
    BASIC_LEVEL_1 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(3) .field-languageaddform-level [data-original-index="1"]'))

    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-language"]'))
    FRENCH_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-language [data-original-index="5"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) [data-id="languageaddform-level"]'))
    ABOVE_AVERAGE_LEVEL_2 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .field-languageaddform-level [data-original-index="4"]'))

    BUTTON_ADD_LANGUAGE_NUMBER_3 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(4) .resume-item-link.js-add-languages'))

    DROPDOWN_LANGUAGE_3 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(5) [data-id="languageaddform-language"]'))
    HEBREW_LANGUAGE_3 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(5) .field-languageaddform-language [data-original-index="20"]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_3 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(5) [data-id="languageaddform-level"]'))
    MIDDLE_LEVEL_3 = (By.CSS_SELECTOR, ('#knowledge-of-languages .additional-block-item:nth-child(5) .field-languageaddform-level [data-original-index="3"]'))
    # блок "Знание языков"

    I_HAVE_DISABILITY = (By.CSS_SELECTOR, ('#disability #' + input_prefix + 'disability > label:nth-child(2)'))
    FIELD_DESCRIPTION_OF_DISABILITY = (By.CSS_SELECTOR, ('#is-disability'))
    # блок "Инвалидность"

    BUTTON_EDIT_IN_ADDITIONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#additional-information .post-resume-title + .right .btn-edit'))
    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'additionally_information iframe'))
    # блок "Дополнительная информация"

    DROPDOWN_JOB_SEARCH_STATUS = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'job_search_status"]'))
    WORKING_BUT_OPEN_TO_SUGGESTIONS = (By.CSS_SELECTOR, ('#resume-visibility-settings li[data-original-index="1"] > a'))
    # блок "Статус поиска работы"

    RESUME_COMPLETED_ON = (By.CSS_SELECTOR, ('.post-resume-status span.resume-rate'))
    STATUS_OF_YOUR_RESUME = (By.CSS_SELECTOR, ('.post-resume-status span.small-text.d-block'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков

    BUTTON_PUBLISH = (By.CSS_SELECTOR, ('#submit-button'))


class MyResponsesPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))

    def assembly_of_locators_with_id_vacancies(self):  # сборка локаторов с id вакансии
        singleton = Singleton()
        vacancy = (By.XPATH, ('//a[contains(@href, "/vacancy/' + singleton.id_vacancies + '")]'))
        return vacancy


class VacancyPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_VACANCY_MENU = (By.CSS_SELECTOR, '.share-btn')
    BUTTON_PRINT = (By.XPATH, '//a[contains(@href, "/print")]')
    BUTTON_RESPONSE_1 = (By.CSS_SELECTOR, ('.company-respond > #response'))
    BUTTON_RESPONSE_2 = (By.CSS_SELECTOR, ('.btn-wrap > #response'))
    NOT_ACTIVE_BUTTON_RESUME_POSTED_1 = (By.CSS_SELECTOR, ('.company-respond > [data-target="#respond-modal"][disabled="disabled"]'))
    NOT_ACTIVE_BUTTON_RESUME_POSTED_2 = (By.CSS_SELECTOR, ('.btn-wrap > [data-target="#respond-modal"][disabled="disabled"]'))

    def assembly_of_locators_with_id_resume(self):  # сборка локаторов с id резюме
        singleton = Singleton()
        resume_in_response_popup_window = (By.CSS_SELECTOR, ('label[for="resume-' + singleton.id_resume[0] + '"]'))
        return resume_in_response_popup_window

    BUTTON_ADD_COVER_LETTER = (By.CSS_SELECTOR, ('.required + .form-group > .cover-letter-btn'))
    FIELD_COVER_LETTER = (By.CSS_SELECTOR, ('.required + .form-group #response-description'))
    BUTTON_SEND_CV = (By.CSS_SELECTOR, ('.field-responses-resume_id + .form-group [type="submit"]'))
    # pop-up окно отклика на вакансию

    INFO_TEXT_AFTER_SENDING_RESPONSE_TO_VACANCY = (By.CSS_SELECTOR, ('#to-publish-modal div>h2'))  # информационный текст после отправки отклика на вакансию
    CROSS_IN_POP_UP_AFTER_SENDING_RESPONSE_TO_VACANCY = (By.CSS_SELECTOR, ('#to-publish-modal .close'))  # крестик в pop-up окне после отправки отклика на вакансию

