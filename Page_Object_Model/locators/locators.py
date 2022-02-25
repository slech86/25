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


class VacancyPageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))

class ResumePageLocators():
    H1 = (By.CSS_SELECTOR, ('h1'))


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
    LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваша вакансія вже на сайті"]'))  # письмо после публикации вакансии ua
    LETTER_AFTER_PUBLISHING_RESUME_RU = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме опубликовано"]'))  # письмо после публикации резюме ru
    LETTER_AFTER_PUBLISHING_RESUME_UA = (By.XPATH, ('//tr[contains(@class, "message unread")]//span[text()="Ваше резюме опубліковано"]'))  # письмо после публикации резюме ua

    IFRAME_LETTER = (By.CSS_SELECTOR, ('#messagecontframe'))
    LINK_IN_LETTER = (By.CSS_SELECTOR, ('[rel="noreferrer"]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU = (By.XPATH, ('//div[text()="Ура! Ваш аккаунт прошел модерацию."]'))
    TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA = (By.XPATH, ('//div[text()="Ура! Ваш акаунт пройшов модерацiю."]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_RU = (By.XPATH, ('//div[contains(text(), "Оплата получена, активируйте услугу на ")]'))
    TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_UA = (By.XPATH, ('//div[contains(text(), "Оплата отримана, активуйте послугу на ")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_RU = (By.XPATH, ('//div[text()="Ваша вакансия ' + TestData.job_title_vacancy + ' добавлена на сайт."]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_UA = (By.XPATH, ('//div[text()="Ваша вакансія ' + TestData.job_title_vacancy + ' вже на сайті!"]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_RU = (By.XPATH, ('//div[contains(text(), "Ваше резюме опубликовано на ")]'))
    TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_UA = (By.XPATH, ('//div[contains(text(), "Ваше резюме опубліковано на ")]'))


class SitemapPageLocators():
    SECTIONS = (By.CSS_SELECTOR, ('.folder .folder .opened > span:nth-child(1) + .line > span:nth-child(1) + span'))