from selenium.webdriver.common.by import By
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.singleton import Singleton


class OllPageLocators:
    BUTTON_YES_WHEN_CHECKING_AGE = (By.CSS_SELECTOR, ".modal-content .btn.btn-blue.age-validation")

    DROPDOWN_LIST_EMPLOYER = (By.CSS_SELECTOR, '.header_nav>.dropdown-nav-link:nth-child(1) .flex-row')  # только при не авторизированом пользователе
    RESUME_IN_HEDER = (By.XPATH, '//div[@class="dropdown-nav-menu"]//a[contains(@href, "/resume")]')
    DROPDOWN_LIST_APPLICANT = (By.CSS_SELECTOR, '.header_nav>.dropdown-nav-link:nth-child(2) .flex-row')  # только при не авторизированом пользователе
    VACANCIES_IN_HEDER = (By.XPATH, '//div[@class="dropdown-nav-menu"]//a[contains(@href, "/vacancy")]')
    BUTTON_POP_UP_FOR_LOGIN = (By.CSS_SELECTOR, ('.login.flex-row'))
    BUTTON_AUTHORIZED_USER = (By.CSS_SELECTOR, ('.logout.flex-row'))
    LINK_PERSONAL_ACCOUNT = (By.XPATH, ('//a[@class="dropdown-item"][contains(@href, "/cabinet")]'))
    BUTTON_LEAVE = (By.CSS_SELECTOR, '[data-target="#log-out-modal"]')
    BUTTON_YES_LOGOUT = (By.XPATH, ('//a[contains(@href, "/site/logout")]'))
    # хедер

    COMPANY_REGISTRATION_LINK = (By.CSS_SELECTOR, ('#employer .fz-13'))
    JOB_SEEKER_REGISTRATION_LINK = (By.CSS_SELECTOR, ('#job-seeker .fz-13'))
    JOB_SEEKER_TAB = (By.CSS_SELECTOR, ('#job-seeker-tab'))
    FIELD_LOGIN = (By.CSS_SELECTOR, ('#loginform-emaillogin'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#loginform-password'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('.field-loginform-summaryerror + [type="submit"]'))
    INFO_TEXT_IN_POP_UP_WINDOW = (By.CSS_SELECTOR, ('#login-form .small-text'))
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, '.forgot-password-link')
    # pop-up окно авторизации

    FIELD_FORGOT_PASSWORD_FORM_EMAIL = (By.CSS_SELECTOR, '#forgotpasswordform-email')
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, '.modal-footer>[type="submit"]')
    INFO_TEXT_AFTER_PASSWORD_RESET_REQUEST = (By.CSS_SELECTOR, '#send-reset-link .text')
    # pop-up окно авторизации "Восстановить пароль"

    RUSSIAN_LANGUAGE_TAB = (By.CSS_SELECTOR, '[id="1-tab"]')
    UKRAINIAN_LANGUAGE_TAB = (By.CSS_SELECTOR, 'id="3-tab"')
    ENGLISH_LANGUAGE_TAB = (By.CSS_SELECTOR, 'id="4-tab"')
    # страницы мультиязычности


class VacanciesPageLocators:
    inputPrefix = 'vacancysortform-'

    H1 = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_TO_SEARCH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    BUTTON_SEARCH = (By.CSS_SELECTOR, '#top-sort-form-btn')
    BUTTON_BOOKMARK = (By.CSS_SELECTOR, '.short-card-bookmarks')

    def assembly_of_locators_with_id_vacancies(self, id_vacancies):  # сборка локаторов с id вакансии
        locator = (By.XPATH, ('//a[contains(@href, "/vacancy/' + id_vacancies + '")]'))
        return locator

    FIRST_VACANCY_IN_LIST = (By.CSS_SELECTOR, ('.lc-card:nth-child(1)'))


class ResumesPageLocators:
    inputPrefix = 'resumesortform-'

    H1 = (By.CSS_SELECTOR, ('h1'))
    FIELD_JOB_TITLE_TO_SEARCH = (By.CSS_SELECTOR, ('#' + inputPrefix + 'job_title'))
    BUTTON_SEARCH = (By.CSS_SELECTOR, ('#top-sort-form-btn'))

    def assembly_of_locators_with_id_resume(self, id_resume):  # сборка локаторов с id резюме
        resume = (By.XPATH, ('//a[contains(@href, "/resume/' + id_resume + '")]'))
        return resume

    FIRST_RESUME_IN_LIST = (By.CSS_SELECTOR, ('.lc-card:nth-child(1)'))


class MainPageLocators:
    H1 = (By.CSS_SELECTOR, ('h1'))
    INFO_TEXT_ABOUT_SENDING_REGISTRATION_FORM = (By.CSS_SELECTOR, ('#lc-popup-registration .text'))  # информационный текст о подтверждении отправки формы регистрации
    INFO_TEXT_ABOUT_CONFIRMATION_OF_COMPANY_EMAIL_AFTER_REGISTRATION = (By.CSS_SELECTOR, ('#to-publish-modal h2'))  # информационный текст о подтверждении електронной почты работодателя после регистрации
    INFO_TEXT_IN_MODAL = (By.CSS_SELECTOR, ('#thanks-modal .text'))  # информационный текст в модальном окне

    # восстановление пароля
    FIELD_PASSWORD_IN_RESET_PASSWORD_FORM = (By.CSS_SELECTOR, '#resetpasswordform-newpassword')
    FIELD_REPEAT_PASSWORD_IN_RESET_PASSWORD_FORM = (By.CSS_SELECTOR, '#resetpasswordform-repeatpassword')
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, '#resetPassword [type="submit"]')
    INFO_TEXT_AFTER_PASSWORD_RECOVERY = (By.CSS_SELECTOR, ('#save-new-password .text'))  # информационный текст после восстановления пароля
    # восстановление пароля


class EmailPageLocators:
    FIELD_EMAIL = (By.CSS_SELECTOR, ('#rcmloginuser'))
    FIELD_PASSWORD = (By.CSS_SELECTOR, ('#rcmloginpwd'))
    BUTTON_LOG_IN = (By.CSS_SELECTOR, ('#rcmloginsubmit'))
    # авторизация email

    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Регистрация работодателя на LCwork"]'))
    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Реєстрація роботодавця на LCwork"]'))
    LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Employer registration on LCwork"]'))
    LETTER_WELCOME_TO_LCWORK_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Добро пожаловать на LСwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ru
    LETTER_WELCOME_TO_LCWORK_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ласкаво просимо на LCwork"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя ua
    LETTER_WELCOME_TO_LCWORK_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Welcome to LC Work!"]'))  # письмо после первой модерации для работодателя и подтверждение регистрации для соискателя en
    LETTER_AFTER_ORDER_PROCESSING_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Оплата прошла успешно! Скорее размещайте вакансии на сайте!"]'))  # письмо после проведения заказа ru
    LETTER_AFTER_ORDER_PROCESSING_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Оплата пройшла успішно! Мерщій розміщуйте вакансії на сайті."]'))  # письмо после проведения заказа ua
    LETTER_AFTER_ORDER_PROCESSING_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="The payment was successful! Hurry up to place vacancies on the website!"]'))  # письмо после проведения заказа en
    LETTER_AFTER_PUBLISHING_VACANCY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваша вакансия добавлена на сайт"]'))  # письмо после публикации вакансии ru
    LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваша вакансія вже на сайті"]'))  # письмо после публикации вакансии en
    LETTER_AFTER_PUBLISHING_VACANCY_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Your vacancy is already on the site"]'))  # письмо после публикации вакансии en
    LETTER_AFTER_PUBLISHING_RESUME_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме опубликовано"]'))  # письмо после публикации резюме ru
    LETTER_AFTER_PUBLISHING_RESUME_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме опубліковано"]'))  # письмо после публикации резюме ua
    LETTER_AFTER_PUBLISHING_RESUME_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Your resume is published on the site."]'))  # письмо после публикации резюме en
    LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Вы получили отклик на вакансию"]'))  # письмо после получения отклика на вакансию ru
    LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ви отримали відгук на вакансію"]'))  # письмо после получения отклика на вакансию ua
    LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="You have received feedback on the vacancy."]'))  # письмо после получения отклика на вакансию ua
    LETTER_AFTER_VIEWING_RESPONSE_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме было просмотрено"]'))  # письмо после просмотра отклика ru
    LETTER_AFTER_VIEWING_RESPONSE_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме було переглянуто"]'))  # письмо после просмотра отклика ua
    LETTER_AFTER_VIEWING_RESPONSE_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Your resume has been reviewed"]'))  # письмо после просмотра отклика en
    LETTER_AFTER_RESPONSE_OF_RESPONSE_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме было отклонено"]'))  # письмо после отклонения отклика ru
    LETTER_AFTER_RESPONSE_OF_RESPONSE_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме було відхилено"]'))  # письмо после отклонения отклика ua
    LETTER_AFTER_RESPONSE_OF_RESPONSE_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Your resume has been rejected by the company!"]'))  # письмо после отклонения отклика en
    LETTER_PASSWORD_RECOVERY_CONFIRMATION_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Подтверждение восстановления пароля на LCwork"]'))  # письмо Подтверждение восстановления пароля ru
    LETTER_PASSWORD_RECOVERY_CONFIRMATION_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Підтвердження відновлення пароля на LCwork"]'))  # письмо Подтверждение восстановления пароля ua
    LETTER_PASSWORD_RECOVERY_CONFIRMATION_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Confirm password recovery on LC Work"]'))  # письмо Подтверждение восстановления пароля en
    LETTER_CHANGE_PASSWORD_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Смена пароля на LCwork"]'))  # письмо смена пароля ru
    LETTER_CHANGE_PASSWORD_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Зміна пароля на LCwork"]'))  # письмо смена пароля ua
    LETTER_CHANGE_PASSWORD_EN = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Change password on LC Work"]'))  # письмо смена пароля en


    IFRAME_LETTER = (By.CSS_SELECTOR, ('#messagecontframe'))
    LINK_IN_LETTER = (By.CSS_SELECTOR, ('[rel="noreferrer"]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU = (By.XPATH, ('//div[text()="Ура! Ваш аккаунт прошел модерацию."]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA = (By.XPATH, ('//div[text()="Ура! Ваш акаунт пройшов модерацiю."]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_EN = (By.XPATH, ('//div[text()="Your account has been moderated."]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_RU = (By.XPATH, ('//p[contains(text(), "Оплата прошла успешно. Чтобы продолжить работу, перейдите в личный кабинет на")]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_UA = (By.XPATH, ('//p[contains(text(), "Оплата пройшла успішно. Щоб продовжити роботу перейдіть в особистий кабінет на")]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_EN = (By.XPATH, ('//p[contains(text(), "The payment was successful! Hurry up to place vacancies on the")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_RU = (By.XPATH, ('//div[text()="Ваша вакансия ' + TestData.job_title_vacancy + ' добавлена на "]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//div[text()="Ваша вакансія ' + TestData.job_title_vacancy + ' вже на "]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_EN = (By.XPATH, ('//div[text()="Your vacancy ' + TestData.job_title_vacancy + ' is already on website!"]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_RU = (By.XPATH, ('//div[contains(text(), "Ваше резюме опубликовано на ")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_UA = (By.XPATH, ('//div[contains(text(), "Ваше резюме опубліковано на ")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_EN = (By.XPATH, ('//div[contains(text(), "Your resume is published on the ")]'))
    TEXT_IN_LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_RU = (By.XPATH, ('//p[contains(text(), "Вы получили отклик на вакансию ")]'))
    TEXT_IN_LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_UA = (By.XPATH, ('//p[contains(text(), "Ви отримали відгук на вакансію ")]'))
    TEXT_IN_LETTER_AFTER_RECEIVING_RESPONSE_TO_VACANCY_EN = (By.XPATH, ('//p[contains(text(), "You received feedback on vacancy ")]'))
    TEXT_IN_LETTER_AFTER_VIEWING_RESPONSE_RU = (By.XPATH, ('//div[contains(text(), "Ваше резюме было просмотрено компанией ")]'))
    TEXT_IN_LETTER_AFTER_VIEWING_RESPONSE_UA = (By.XPATH, ('//div[contains(text(), "Ваше резюме було переглянуте компанією ")]'))
    TEXT_IN_LETTER_AFTER_VIEWING_RESPONSE_EN = (By.XPATH, ('//div[contains(text(), "Your resume has been reviewed.")]'))
    TEXT_IN_LETTER_AFTER_RESPONSE_OF_RESPONSE_RU = (By.XPATH, ('//div[contains(text(), " отклонила резюме.")]'))
    TEXT_IN_LETTER_AFTER_RESPONSE_OF_RESPONSE_UA = (By.XPATH, ('//div[contains(text(), " вiдхилила ваше резюме.")]'))
    TEXT_IN_LETTER_AFTER_RESPONSE_OF_RESPONSE_EN = (By.XPATH, ('//p[contains(text(), "Your resume has been rejected by the ")]'))


class SitemapPageLocators():
    SECTIONS = (By.CSS_SELECTOR, ('.folder .folder .opened > span:nth-child(1) + .line > span:nth-child(1) + span'))
