from selenium.webdriver.common.by import By
from Page_Object_Model.singleton import Singleton


class JobSeekerRegistrationEditPageLocators:
    id_language = '1'
    prefix = 'usersnew-'
    input_prefix = prefix + 'descriptions-' + id_language + '-'

    FIELD_LOGIN = (By.CSS_SELECTOR, ('#' + prefix + 'login'))
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#' + prefix + 'email'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#' + prefix + 'password'))
    FIELD_REPEAT_PASSWORD = (By.CSS_SELECTOR, ('#' + prefix + 'repeatpassword'))
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, '[data-target="#change-pass"]')
    CURRENT_PASSWORD = (By.CSS_SELECTOR, '#changepasswordform-password')
    NEW_PASSWORD = (By.CSS_SELECTOR, '#changepasswordform-newpassword')
    NEW_PASSWORD_AGAIN = (By.CSS_SELECTOR, '#changepasswordform-repeatpassword')
    BUTTON_SAVE_CHANGES_PASSWORD = (By.CSS_SELECTOR, '#job-seeker-edit-password-form [type="submit"]')
    INFO_TEXT_AFTER_PASSWORD_CHANGE = (By.CSS_SELECTOR, '#save-pass .text')
    CROSS_IN_POP_UP_AFTER_PASSWORD_CHANGE = (By.CSS_SELECTOR, '#save-pass .close')  # крестик в pop-up окне после измененя пароля
    # блок "Данные для авторизации"

    BUTTON_EDIT_IN_PERSONAL_INFORMATION_BLOCK = (By.CSS_SELECTOR, ('#personal-information .post-resume-title + .btn-edit'))
    FIELD_NAME = (By.CSS_SELECTOR, ('#' + input_prefix + 'name'))
    FIELD_SURNAME = (By.CSS_SELECTOR, ('#' + input_prefix + 'surname'))

    DROPDOWN_YEAR = (By.CSS_SELECTOR, '[data-id="' + input_prefix + '_datey"]')
    YEAR_1999 = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_datey [data-original-index="3"]'))
    YEAR_2001 = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_datey [data-original-index="1"]'))
    DROPDOWN_MONTH = (By.CSS_SELECTOR, '[data-id="' + input_prefix + '_datem"]')
    MONTH_NOVEMBER = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_datem [data-original-index="11"]'))
    MONTH_JANUARY = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_datem [data-original-index="1"]'))
    DROPDOWN_DAY = (By.CSS_SELECTOR, '[data-id="' + input_prefix + '_dated"]')
    DAY_30 = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_dated [data-original-index="30"]'))
    DAY_1 = (By.CSS_SELECTOR, ('#content-' + id_language + ' .field-' + input_prefix + '_dated [data-original-index="1"]'))

    FIELD_GENDER_FEMALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="2"] + .radio-custom'))
    FIELD_GENDER_MALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="1"] + .radio-custom'))
    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country = (By.CSS_SELECTOR, ('.field-' + JobSeekerRegistrationEditPageLocators.input_prefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city = (By.CSS_SELECTOR, ('.field-' + JobSeekerRegistrationEditPageLocators.input_prefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city
    # блок "Личная информация"

    BUTTON_EDIT_IN_SETTINGS_BLOCK = (By.CSS_SELECTOR, ('#other-settings .post-resume-title + .btn-edit'))
    DROPDOWN_LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL = (By.CSS_SELECTOR, ('[data-id="' + prefix + 'mail_language"]'))
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_RU = (By.CSS_SELECTOR, ('.field-' + prefix + 'mail_language [data-original-index="0"]'))  # русский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_UA = (By.CSS_SELECTOR, ('.field-' + prefix + 'mail_language [data-original-index="1"]'))  # украинский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_EN = (By.CSS_SELECTOR, ('.field-' + prefix + 'mail_language [data-original-index="2"]'))  # английский
    LANGUAGE_OF_NOTIFICATIONS_ON_EMAIL_PL = (By.CSS_SELECTOR, ('.field-' + prefix + 'mail_language [data-original-index="3"]'))  # польский
    # блок "Настройки"

    BUTTON_SUBMIT = (By.CSS_SELECTOR, '#button-submit')

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

    def assembly_of_locators_with_id_resume(self, id_resume):  # сборка локаторов с id резюме
        locators = {
            'status_resume': (By.XPATH, '//a[contains(@href, "/resume/' + id_resume + '/edit")]/ancestor::div[5]//div[@class="lc-card-time "]/span'),
            'button_hide': (By.XPATH, '//a[@data-resume-id=' + id_resume + '][@data-status-id="0"]'),
            'button_publish': (By.XPATH, '//a[@data-resume-id=' + id_resume + '][@data-status-id="1"]'),
            'button_delete': (By.CSS_SELECTOR, '.open-delete-modal[data-resume-id="' + id_resume + '"]'),
            'button_edit': (By.XPATH, '//a[contains(@href, "/resume/' + id_resume + '/edit")]'),
            'button_resume_menu': (By.XPATH, '//a[contains(@href, "/resume/' + id_resume + '/edit")]/ancestor::div[4]'),
        }
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
        locators['button_add_block'] = (By.CSS_SELECTOR, '#content-' + ResumeAddEditPageLocators.id_language + ' #' + id_block + ' .icon-plus')
        return locators
    CROSS_IN_COPY_TO_OTHER_LANGUAGES = (By.CSS_SELECTOR, '.copy-languages-toggle-tooltip')
    TAB = (By.CSS_SELECTOR, '[id="' + id_language + '-tab"]')
    FIELD_PHOTO = (By.CSS_SELECTOR, '#resumenew-photo')
    FIELD_NAME = (By.CSS_SELECTOR, '#' + input_prefix + 'name')
    FIELD_SURNAME = (By.CSS_SELECTOR, '#' + input_prefix + 'surname')

    DROPDOWN_YEAR = (By.CSS_SELECTOR, '[data-id="' + input_prefix + 'birthdayy"]')
    YEAR_OF_BIRTH_1981 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayy [data-original-index="21"]'))
    YEAR_OF_BIRTH_1976 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayy [data-original-index="26"]'))
    DROPDOWN_MONTH = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdaym"]'))
    MONTH_SEPTEMBER = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdaym [data-original-index="9"]'))
    MONTH_MARCH = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdaym [data-original-index="3"]'))
    DROPDOWN_DAY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'birthdayd"]'))
    DAY_5 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayd [data-original-index="5"]'))
    DAY_8 = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'birthdayd [data-original-index="8"]'))

    FIELD_GENDER_FEMALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="2"] + .radio-custom'))
    FIELD_GENDER_MALE = (By.CSS_SELECTOR, ('#' + input_prefix + 'gender [value="1"] + .radio-custom'))

    DROPDOWN_COUNTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'country_id"]'))
    COUNTRY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'country_id > option'))

    def assembly_of_locators_with_position_country(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        country = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'country_id [data-original-index="' + singleton.position_object + '"]'))
        return country

    DROPDOWN_CITI = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'city_id"]'))
    CITY_LIST = (By.CSS_SELECTOR, ('#' + input_prefix + 'city_id > option'))

    def assembly_of_locators_with_position_city(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        city = (By.CSS_SELECTOR, ('.field-' + ResumeAddEditPageLocators.input_prefix + 'city_id [data-original-index="' + singleton.position_object + '"]'))
        return city

    DROPDOWN_WILLING_TO_RELOCATE = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'willing_relocate"]'))
    NOT_READY_TO_RELOCATE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'willing_relocate [data-original-index="2"]'))
    READY_TO_RELOCATE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'willing_relocate [data-original-index="1"]'))
    # блок "Личная информация"

    # блок "Контактная информация"
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

    # блок "Желаемая должность"
    FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title'))
    VALIDATION_MESSAGE_FIELD_JOB_TITLE = (By.CSS_SELECTOR, ('#' + input_prefix + 'job_title + p'))

    CATEGORY_RESUME_DESIGN_GRAPHICS_ANIMATION = (By.XPATH, '//div[@id="' + input_prefix + 'category_id"]//div[@class="custom-control checkbox"][8]/label')
    CATEGORY_RESUME_SALES_CUSTOMER_MANAGEMENT = (By.XPATH, '//div[@id="' + input_prefix + 'category_id"]//div[@class="custom-control checkbox"][14]/label')
    SUBCATEGORIES_UX_DESIGNER = (By.XPATH, '//div[@id="' + input_prefix + 'subcategories_id"]//div[@class="custom-control checkbox"][7]/label[contains(@for, "subcategories") and contains(@for, "-70")]')
    SUBCATEGORIES_ACCOUNT_MANAGER = (By.XPATH, '//div[@id="' + input_prefix + 'subcategories_id"]//div[@class="custom-control checkbox"][3]/label[contains(@for, "subcategories") and contains(@for, "-168")]')
    DISTANT_WORK = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment .checkbox:nth-child(3) > label'))  # удаленная работа
    UNDEREMPLOYMENT = (By.CSS_SELECTOR, ('#' + input_prefix + 'employment .checkbox:nth-child(2) > label'))  # Неполная занятость
    SALARY = (By.CSS_SELECTOR, '#' + input_prefix + 'salary')
    DROPDOWN_CURRENCY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'currency"]'))
    CURRENCY_UAH = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'currency [data-original-index="1"]'))
    CURRENCY_USD = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'currency [data-original-index="2"]'))
    # блок "Желаемая должность"

    IFRAME_CKEDITOR_SKILLS_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, ('#cke_' + input_prefix + 'skills iframe'))
    # блок "Навыки и достижения"

    # блок "Опыт работы"
    FIELD_COMPANY_NAME = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-company')
    FIELD_SITE_COMPANY = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-web_site')
    SCOPE_OF_COMPANY_CASINO_STAFF = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-0-category"]//div[@class="custom-control checkbox"][3]/label')
    SCOPE_OF_COMPANY_SECURITY_SERVICE = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-0-category"]//div[@class="custom-control checkbox"][5]/label')
    FIELD_POSITION = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-0-position')

    DROPDOWN_MONTH_WORK_EXPERIENCE_START = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_start_m"]')
    MONTH_AUGUST_WORK_EXPERIENCE_START = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_m required")]//li[9]/a')
    MONTH_DECEMBER_WORK_EXPERIENCE_START = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_m required")]//li[13]/a')
    DROPDOWN_YEAR_WORK_EXPERIENCE_START = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_start_y"]')
    YEAR_WORK_EXPERIENCE_START_2018 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_y required")]//li[6]/a')
    YEAR_WORK_EXPERIENCE_START_2010 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_start_y required")]//li[14]/a')

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_end_m"]')
    MONTH_MARCH_WORK_EXPERIENCE_FINISH = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_m required")]//li[5]/a')
    MONTH_JANUARY_WORK_EXPERIENCE_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_m required")]//li[8]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-0-period_end_y"]')
    YEAR_WORK_EXPERIENCE_FINISH_2020 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_y required")]//li[4]/a')
    YEAR_WORK_EXPERIENCE_FINISH_2012 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-0-period_end_y required")]//li[12]/a')

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS = (By.CSS_SELECTOR, '#cke_resumenew-workexperiencenew-' + id_language + '-0-responsibilities iframe')

    BUTTON_ADD_WORK_EXPERIENCE_NUMBER_2 = (By.XPATH, '(//div[@id="content-' + id_language + '"]//div[@id="work-experience"]//button[contains(@class, "js-add-more")])[1]')

    FIELD_COMPANY_NAME_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-company')
    FIELD_SITE_COMPANY_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-web_site')
    SCOPE_OF_COMPANY_MAINTENANCE_OF_SLOTS_2 = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-1-category"]//div[@class="custom-control checkbox"][6]/label')
    SCOPE_OF_COMPANY_WEBSITE_PROMOTION_2 = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-1-category"]//div[@class="custom-control checkbox"][10]/label')
    FIELD_POSITION_2 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-1-position')

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_start_m"]'))
    MONTH_APRIL_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_m required")]//li[5]/a'))
    MONTH_FEBRUARY_WORK_EXPERIENCE_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_m required")]//li[3]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_start_y"]'))
    YEAR_WORK_EXPERIENCE_START_2020_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_y required")]//li[4]/a'))
    YEAR_WORK_EXPERIENCE_START_1993_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_start_y required")]//li[31]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_end_m"]'))
    WORKING_NOW_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_end_m required")]//li[2]/a'))
    MONTH_MARCH_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_end_m required")]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-workexperiencenew-' + id_language + '-1-period_end_y"]')
    YEAR_WORK_EXPERIENCE_FINISH_1996_2 = (By.XPATH, '//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-1-period_end_y required")]//li[28]/a')
    # DROPDOWN_YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//button'))
    # YEAR_WORK_EXPERIENCE_FINISH_2 = (By.XPATH, ('//div[@id="work-experience"]//div[contains(@class, "additional-block-item")][2]//form[contains(@id, "work-experience-form")]/div[5]//div[@class="d-flex"]/div[contains(@class, "search-select")][2]//li[4]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_2 = (By.CSS_SELECTOR, ('#cke_resumenew-workexperiencenew-' + id_language + '-1-responsibilities iframe'))

    BUTTON_ADD_WORK_EXPERIENCE_NUMBER_3 = (By.XPATH, '(//div[@id="content-' + id_language + '"]//div[@id="work-experience"]//button[contains(@class, "js-add-more")])[2]')

    FIELD_COMPANY_NAME_3 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-2-company')
    FIELD_SITE_COMPANY_3 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-2-web_site')
    SCOPE_OF_COMPANY_WEBSITE_PROMOTION_3 = (By.XPATH, '//div[@id="resumenew-workexperiencenew-' + id_language + '-2-category"]//div[@class="custom-control checkbox"][10]/label')
    FIELD_POSITION_3 = (By.CSS_SELECTOR, '#resumenew-workexperiencenew-' + id_language + '-2-position')

    DROPDOWN_MONTH_WORK_EXPERIENCE_START_3 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-2-period_start_m"]'))
    MONTH_APRIL_WORK_EXPERIENCE_START_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-2-period_start_m required")]//li[5]/a'))
    DROPDOWN_YEAR_WORK_EXPERIENCE_START_3 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-2-period_start_y"]'))
    YEAR_WORK_EXPERIENCE_START_2003_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-2-period_start_y required")]//li[21]/a'))

    DROPDOWN_MONTH_WORK_EXPERIENCE_FINISH_3 = (By.CSS_SELECTOR, ('[data-id="resumenew-workexperiencenew-' + id_language + '-2-period_end_m"]'))
    WORKING_NOW_WORK_EXPERIENCE_FINISH_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-workexperiencenew-' + id_language + '-2-period_end_m required")]//li[2]/a'))

    IFRAME_CKEDITOR_RESPONSIBILITIES_AND_ACHIEVEMENTS_3 = (By.CSS_SELECTOR, ('#cke_resumenew-workexperiencenew-' + id_language + '-2-responsibilities iframe'))
    # блок "Опыт работы"

    DROPDOWN_WORK_EXPERIENCE_GAMBLING_INDUSTRY = (By.CSS_SELECTOR, ('[data-id="' + input_prefix + 'gambling_experience"]'))
    WITHOUT_EXPERIENCE = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'gambling_experience [data-original-index="1"]'))
    EXPERIENCE_2_TO_5_YEARS = (By.CSS_SELECTOR, ('.field-' + input_prefix + 'gambling_experience [data-original-index="4"]'))
    # блок "Опыт работы в игорной индустрии"

    # блок "Образование"
    FIELD_NAME_OF_INSTITUTION = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-name_institution'))
    DROPDOWN_LEVEL_OF_EDUCATION = (By.CSS_SELECTOR, ('[data-id="resumenew-educationsnew-' + id_language + '-0-level_education"]'))
    HIGHER_EDUCATION = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-level_education required")]//li[2]/a'))
    INCOMPLETE_HIGHER_EDUCATION = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-level_education required")]//li[3]/a'))

    DROPDOWN_COUNTRY_EDUCATION = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-country_id"]')
    COUNTRY_NOT_SELECTED_EDUCATION = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-country_id")]//li[1]/a'))
    COUNTRY_EDUCATION_LIST = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-country_id > option'))

    def assembly_of_locators_with_position_country_education(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_ukraine_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-0-country_id")]//li[' + str(position_object) + ']/a'))
        return country_ukraine_education

    DROPDOWN_CITI_EDUCATION = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-city_id"]')
    CITI_NOT_SELECTED_EDUCATION = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-city_id")]//li[1]/a'))
    CITY_EDUCATION_LIST = (By.CSS_SELECTOR, '#resumenew-educationsnew-' + id_language + '-0-city_id > option')

    def assembly_of_locators_with_position_city_education(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_kharkov_education = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-0-city_id")]//li[' + str(position_object) + ']/a'))
        return city_kharkov_education

    FIELD_DEPARTMENT_AND_SPECIALITY = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-0-specialty'))

    DROPDOWN_MONTH_EDUCATION_START = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_start_m"]')
    MONTH_SEPTEMBER_EDUCATION_START = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_m")]//li[10]/a')
    MONTH_NOT_SELECTED_EDUCATION_START = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_m")]//li[1]/a')
    DROPDOWN_YEAR_EDUCATION_START = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_start_y"]')
    YEAR_EDUCATION_START_2010 = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_y")]//li[14]/a')
    YEAR_NOT_SELECTED_EDUCATION_START = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_start_y")]//li[1]/a')

    DROPDOWN_MONTH_EDUCATION_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_end_m"]')
    MONTH_MAY_EDUCATION_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_m")]//li[7]/a'))
    MONTH_NOT_SELECTED_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_m")]//li[1]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-0-period_end_y"]')
    YEAR_EDUCATION_FINISH_2015 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_y")]//li[9]/a'))
    YEAR_NOT_SELECTED_EDUCATION_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-0-period_end_y")]//li[1]/a'))

    BUTTON_ADD_EDUCATION_NUMBER_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="education"]//button[contains(@class, "js-add-more")])[1]'))

    FIELD_NAME_OF_INSTITUTION_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-name_institution'))
    DROPDOWN_LEVEL_OF_EDUCATION_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-educationsnew-' + id_language + '-1-level_education"]'))
    SECONDARY_SPECIAL_EDUCATION_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-level_education required")]//li[4]/a'))
    SECONDARY_EDUCATION_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-level_education required")]//li[5]/a'))

    DROPDOWN_COUNTRY_EDUCATION_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-country_id"]')
    COUNTRY_EDUCATION_LIST_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-country_id > option'))

    def assembly_of_locators_with_position_country_education_2(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_education_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-1-country_id")]//li[' + str(position_object) + ']/a'))
        return country_education_2

    DROPDOWN_CITI_EDUCATION_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-city_id"]')
    CITY_EDUCATION_LIST_2 = (By.CSS_SELECTOR, '#resumenew-educationsnew-' + id_language + '-1-city_id > option')

    def assembly_of_locators_with_position_city_education_2(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_education_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-1-city_id")]//li[' + str(position_object) + ']/a'))
        return city_education_2

    FIELD_DEPARTMENT_AND_SPECIALITY_2 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-1-specialty'))

    DROPDOWN_MONTH_EDUCATION_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_start_m"]')
    MONTH_NOVEMBER_EDUCATION_START_2 = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_m")]//li[12]/a')
    MONTH_JUNE_EDUCATION_START_2 = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_m")]//li[7]/a')
    DROPDOWN_YEAR_EDUCATION_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_start_y"]')
    YEAR_EDUCATION_START_2018_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_y")]//li[6]/a'))
    YEAR_EDUCATION_START_2005_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_start_y")]//li[19]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_end_m"]')
    MONTH_JANUARY_EDUCATION_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_m")]//li[3]/a'))
    MONTH_JULY_EDUCATION_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_m")]//li[9]/a'))
    DROPDOWN_YEAR_EDUCATION_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-1-period_end_y"]')
    YEAR_EDUCATION_FINISH_2020_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_y")]//li[4]/a'))
    YEAR_EDUCATION_FINISH_2008_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-1-period_end_y")]//li[16]/a'))

    BUTTON_ADD_EDUCATION_NUMBER_3 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="education"]//button[contains(@class, "js-add-more")])[2]'))

    FIELD_NAME_OF_INSTITUTION_3 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-2-name_institution'))
    DROPDOWN_LEVEL_OF_EDUCATION_3 = (By.CSS_SELECTOR, ('[data-id="resumenew-educationsnew-' + id_language + '-2-level_education"]'))
    HIGHER_EDUCATION_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-2-level_education required")]//li[2]/a'))

    DROPDOWN_COUNTRY_EDUCATION_3 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-2-country_id"]')
    COUNTRY_EDUCATION_LIST_3 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-2-country_id > option'))

    def assembly_of_locators_with_position_country_education_3(self):  # сборка локаторов с позицией страны
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        country_education_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-2-country_id")]//li[' + str(position_object) + ']/a'))
        return country_education_3

    DROPDOWN_CITI_EDUCATION_3 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-2-city_id"]')
    CITY_EDUCATION_LIST_3 = (By.CSS_SELECTOR, '#resumenew-educationsnew-' + id_language + '-2-city_id > option')

    def assembly_of_locators_with_position_city_education_3(self):  # сборка локаторов с позицией города
        singleton = Singleton()
        position_object = int(singleton.position_object) + 1
        city_education_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + ResumeAddEditPageLocators.id_language + '-2-city_id")]//li[' + str(position_object) + ']/a'))
        return city_education_3

    FIELD_DEPARTMENT_AND_SPECIALITY_3 = (By.CSS_SELECTOR, ('#resumenew-educationsnew-' + id_language + '-2-specialty'))

    DROPDOWN_MONTH_EDUCATION_START_3 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-2-period_start_m"]')
    MONTH_AUGUST_EDUCATION_START_3 = (By.XPATH, '//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-2-period_start_m")]//li[9]/a')
    DROPDOWN_YEAR_EDUCATION_START_3 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-2-period_start_y"]')
    YEAR_EDUCATION_START_2020_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-2-period_start_y")]//li[4]/a'))

    DROPDOWN_MONTH_EDUCATION_FINISH_3 = (By.CSS_SELECTOR, '[data-id="resumenew-educationsnew-' + id_language + '-2-period_end_m"]')
    STUDY_NOW_EDUCATION_FINISH_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-educationsnew-' + id_language + '-2-period_end_m")]//li[2]/a'))
    # блок "Образование"

    # блок "Курсы и сертификаты"
    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE = (By.CSS_SELECTOR, ('#resumenew-coursesnew-' + id_language + '-0-name_certificate'))

    DROPDOWN_MONTH_COURSES_START = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_start_m"]')
    MONTH_JUNE_COURSES_START = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_m")]//li[7]/a'))
    MONTH_SEPTEMBER_COURSES_START = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_m")]//li[10]/a'))
    DROPDOWN_YEAR_COURSES_START = (By.CSS_SELECTOR, ('[data-id="resumenew-coursesnew-' + id_language + '-0-period_start_y"]'))
    YEAR_COURSES_START_2020 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_y")]//li[4]/a'))
    YEAR_COURSES_START_2016 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_start_y")]//li[8]/a'))

    DROPDOWN_MONTH_COURSES_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_end_m"]')
    MONTH_JUNE_COURSES_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_m")]//li[8]/a'))
    MONTH_OCTOBER_COURSES_FINISH = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_m")]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_FINISH = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-0-period_end_y"]')
    YEAR_COURSES_FINISH_2021 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_y")]//li[3]/a'))
    YEAR_COURSES_FINISH_2016 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-0-period_end_y")]//li[8]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION = (By.XPATH, ('//div[@id="cke_resumenew-coursesnew-' + id_language + '-0-description"]//iframe'))

    BUTTON_ADD_COURSES_NUMBER_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="courses-and-certificates"]//button[contains(@class, "js-add-more")])[1]'))

    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_2 = (By.CSS_SELECTOR, ('#resumenew-coursesnew-' + id_language + '-1-name_certificate'))

    DROPDOWN_MONTH_COURSES_START_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_start_m"]')
    MONTH_OCTOBER_COURSES_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_m")]//li[11]/a'))
    MONTH_NOVEMBER_COURSES_START_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_m")]//li[12]/a'))
    DROPDOWN_YEAR_COURSES_START_2 = (By.CSS_SELECTOR, ('[data-id="resumenew-coursesnew-' + id_language + '-1-period_start_y"]'))
    YEAR_COURSES_START_2014_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_y")]//li[10]/a'))
    YEAR_COURSES_START_2020_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_start_y")]//li[4]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_end_m"]')
    MONTH_OCTOBER_COURSES_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_m")]//li[12]/a'))
    MONTH_NOVEMBER_COURSES_FINISH_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_m")]//li[13]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_2 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-1-period_end_y"]')
    YEAR_COURSES_FINISH_2015_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_y")]//li[9]/a'))
    YEAR_COURSES_FINISH_2021_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-1-period_end_y")]//li[3]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_2 = (By.XPATH, ('//div[@id="cke_resumenew-coursesnew-' + id_language + '-1-description"]//iframe'))

    BUTTON_ADD_COURSES_NUMBER_3 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="courses-and-certificates"]//button[contains(@class, "js-add-more")])[2]'))

    FIELD_NAME_OF_INSTITUTION_OR_CERTIFICATE_3 = (By.CSS_SELECTOR, ('#resumenew-coursesnew-' + id_language + '-2-name_certificate'))

    DROPDOWN_MONTH_COURSES_START_3 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-2-period_start_m"]')
    MONTH_DECEMBER_COURSES_START_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-2-period_start_m")]//li[13]/a'))
    DROPDOWN_YEAR_COURSES_START_3 = (By.CSS_SELECTOR, ('[data-id="resumenew-coursesnew-' + id_language + '-2-period_start_y"]'))
    YEAR_COURSES_START_2017_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-2-period_start_y")]//li[7]/a'))

    DROPDOWN_MONTH_COURSES_FINISH_3 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-2-period_end_m"]')
    MONTH_JANUARY_COURSES_FINISH_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-2-period_end_m")]//li[3]/a'))
    DROPDOWN_YEAR_COURSES_FINISH_3 = (By.CSS_SELECTOR, '[data-id="resumenew-coursesnew-' + id_language + '-2-period_end_y"]')
    YEAR_COURSES_FINISH_2018_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-coursesnew-' + id_language + '-2-period_end_y")]//li[6]/a'))

    IFRAME_CKEDITOR_COURSE_DESCRIPTION_3 = (By.XPATH, ('//div[@id="cke_resumenew-coursesnew-' + id_language + '-2-description"]//iframe'))
    # блок "Курсы и сертификаты"

    # блок "Знание языков"
    DROPDOWN_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-0-language"]')
    POLISH_LANGUAGE_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-language required")]//li[35]'))
    ENGLISH_LANGUAGE_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-language required")]//li[2]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_1 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-0-level"]')
    HIGH_LEVEL_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-level required")]//li[6]'))
    BASIC_LEVEL_1 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-0-level required")]//li[2]'))

    BUTTON_ADD_LANGUAGE_NUMBER_2 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "js-add-more")])[1]'))

    DROPDOWN_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-1-language"]')
    GERMAN_LANGUAGE_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-language required")]//li[5]'))
    FRENCH_LANGUAGE_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-language required")]//li[6]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_2 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-1-level"]')
    FREE_LEVEL_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-level required")]//li[7]'))
    ABOVE_AVERAGE_LEVEL_2 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-1-level required")]//li[5]'))

    BUTTON_ADD_LANGUAGE_NUMBER_3 = (By.XPATH, ('(//div[@id="content-' + id_language + '"]//div[@id="knowledge-of-languages"]//button[contains(@class, "js-add-more")])[2]'))

    DROPDOWN_LANGUAGE_3 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-2-language"]')
    HEBREW_LANGUAGE_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-2-language required")]//li[21]'))
    DROPDOWN_LEVEL_OF_LANGUAGE_3 = (By.CSS_SELECTOR, '[data-id="resumenew-knowledgeoflanguagesnew-' + id_language + '-2-level"]')
    MIDDLE_LEVEL_3 = (By.XPATH, ('//div[contains(@class, "field-resumenew-knowledgeoflanguagesnew-' + id_language + '-2-level required")]//li[4]'))
    # блок "Знание языков"

    RADIO_I_DONT_HAVE_DISABILITY = (By.XPATH, ('//div[@id="' + input_prefix + 'disability"]//input[@value="1"]'))
    RADIO_I_HAVE_DISABILITY = (By.XPATH, ('//div[@id="' + input_prefix + 'disability"]/label[2]'))
    FIELD_DESCRIPTION_OF_DISABILITY = (By.CSS_SELECTOR, ('#' + input_prefix + 'disability_description'))
    # блок "Инвалидность"

    IFRAME_CKEDITOR_ADDITIONAL_INFORMATION = (By.XPATH, ('//div[@id="cke_' + input_prefix + 'additionally_information"]//iframe'))
    # блок "Дополнительная информация"

    DROPDOWN_JOB_SEARCH_STATUS = (By.CSS_SELECTOR, ('[data-id="resumenew-job_search_status"]'))
    ACTIVELY_LOOKING_FOR_JOB = (By.XPATH, '//div[contains(@class, "field-resumenew-job_search_status required")]//li[3]')
    WORKING_BUT_OPEN_TO_SUGGESTIONS = (By.XPATH, ('//div[contains(@class, "field-resumenew-job_search_status required")]//li[2]'))
    # блок "Статус поиска работы"

    RESUME_COMPLETED_ON = (By.CSS_SELECTOR, ('.post-resume-status span.resume-rate'))
    STATUS_OF_YOUR_RESUME = (By.CSS_SELECTOR, ('.post-resume-status span.small-text.d-block'))

    CKEDITOR = (By.CSS_SELECTOR, ('body.cke_editable'))  # общий для всех блоков

    BUTTON_PUBLISH = (By.CSS_SELECTOR, '#submit-button')
    BUTTON_TO_DRAFTS = (By.CSS_SELECTOR, '#draft-button')
    BUTTON_PREVIEW = (By.CSS_SELECTOR, '[data-click=".preview-button"]')


class ResumePreviewPageLocators:
    H1 = (By.CSS_SELECTOR, 'h1')


class MyResponsesPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))

    def assembly_of_locators_with_id_vacancies(self, id_vacancies):  # сборка локаторов с id вакансии
        block_vacancy = '//a[contains(@href, "/vacancy/' + id_vacancies + '")]'
        locators = {
            'block_vacancy': (By.XPATH, block_vacancy),
            'status_response': (By.XPATH, f'{block_vacancy}//div[@class="lc-card-time"]/span'),
            'button_delete': (By.XPATH, f'{block_vacancy}//button[contains(@class, "del-lc-card")]'),
        }
        return locators


class VacancyPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    BUTTON_VACANCY_MENU = (By.CSS_SELECTOR, '.share-btn')
    BUTTON_PRINT = (By.XPATH, '//a[contains(@href, "/print")]')
    BUTTON_RESPONSE_1 = (By.CSS_SELECTOR, ('.company-respond > .btn-response'))
    BUTTON_RESPONSE_2 = (By.CSS_SELECTOR, ('.btn-wrap > .btn-response'))
    NOT_ACTIVE_BUTTON_RESUME_POSTED_1 = (By.CSS_SELECTOR, ('.company-respond > [data-target="#respond-modal"][disabled="disabled"]'))
    NOT_ACTIVE_BUTTON_RESUME_POSTED_2 = (By.CSS_SELECTOR, ('.btn-wrap > [data-target="#respond-modal"][disabled="disabled"]'))

    def assembly_of_locators_with_id_resume(self, id_resume):  # сборка локаторов с id резюме
        locators = {
            'resume_in_response_popup_window': (By.CSS_SELECTOR, ('label[for="resume-' + id_resume + '"]')),
            'resume_in_response_popup_window_input': (By.CSS_SELECTOR, ('label[for="resume-' + id_resume + '"] input'))
        }
        return locators

    BUTTON_ADD_COVER_LETTER = (By.CSS_SELECTOR, ('.required + .form-group > .cover-letter-btn'))
    FIELD_COVER_LETTER = (By.CSS_SELECTOR, ('.required + .form-group #response-description'))
    BUTTON_SEND_CV = (By.CSS_SELECTOR, ('.field-responses-resume_id + .form-group [type="submit"]'))
    # pop-up окно отклика на вакансию

    INFO_TEXT_AFTER_SENDING_RESPONSE_TO_VACANCY = (By.CSS_SELECTOR, ('#to-publish-modal div>h2'))  # информационный текст после отправки отклика на вакансию
    CROSS_IN_POP_UP_AFTER_SENDING_RESPONSE_TO_VACANCY = (By.CSS_SELECTOR, ('#to-publish-modal .close'))  # крестик в pop-up окне после отправки отклика на вакансию

