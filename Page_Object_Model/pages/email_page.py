import time
from .base_page import BasePage
from Page_Object_Model.locators.locators import EmailPageLocators
from Page_Object_Model.data_for_testing import Accounts
from Page_Object_Model.data_for_testing import TestData


class EmailPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailPageLocators.FIELD_EMAIL).send_keys(Accounts.main_login_email)
        self.browser.find_element(*EmailPageLocators.FIELD_PASSWORD).send_keys(Accounts.main_password_email)
        self.browser.find_element(*EmailPageLocators.BUTTON_LOG_IN).click()

    def confirmation_of_company_registration_in_letter(self, language):  # подтверждение регистрации работодателя в письме
        # time.sleep(20)
        # self.browser.refresh()
        letter_of_registration_confirmation_company = None
        if language == "/ua":
            letter_of_registration_confirmation_company = EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA
        elif language == "":
            letter_of_registration_confirmation_company = EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU
        elif language == "/en":
            letter_of_registration_confirmation_company = EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_EN

        self.browser.find_element(*letter_of_registration_confirmation_company).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def letter_after_first_moderation_of_company(self, language):  # письмо после первой модерации компании
        time.sleep(4)
        self.browser.refresh()

        letter_welcome_to_lcwork, text_in_letter_after_first_moderation, text = None, None, None
        if language == "/ua":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_UA
            text_in_letter_after_first_moderation = EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA
            text = 'Ура! Ваш акаунт пройшов модерацiю.'
        elif language == "":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_RU
            text_in_letter_after_first_moderation = EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU
            text = 'Ура! Ваш аккаунт прошел модерацию.'
        elif language == "/en":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_EN
            text_in_letter_after_first_moderation = EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_EN
            text = 'Your account has been moderated.'

        self.browser.find_element(*letter_welcome_to_lcwork).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*text_in_letter_after_first_moderation).text
        assert text == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def confirmation_of_job_seeker_registration_in_letter(self, language):  # подтверждение регистрации соискателя в письме
        # time.sleep(20)
        # self.browser.refresh()

        letter_welcome_to_lcwork = None
        if language == "/ua":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_UA
        elif language == "":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_RU
        elif language == "/en":
            letter_welcome_to_lcwork = EmailPageLocators.LETTER_WELCOME_TO_LCWORK_EN

        self.browser.find_element(*letter_welcome_to_lcwork).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def letter_after_order_processing(self, language):  # письмо после проведения заказа
        # time.sleep(20)
        # self.browser.refresh()

        letter_after_order_processing, text_in_letter_after_order_processing, expected_email_text = None, None, None
        if language == "/ua":
            letter_after_order_processing = EmailPageLocators.LETTER_AFTER_ORDER_PROCESSING_UA
            text_in_letter_after_order_processing = EmailPageLocators.TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_UA
            expected_email_text = 'Оплата отримана, активуйте послугу на '
        elif language == "":
            letter_after_order_processing = EmailPageLocators.LETTER_AFTER_ORDER_PROCESSING_RU
            text_in_letter_after_order_processing = EmailPageLocators.TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_RU
            expected_email_text = 'Оплата получена, активируйте услугу на '
        elif language == "/en":
            letter_after_order_processing = EmailPageLocators.LETTER_AFTER_ORDER_PROCESSING_EN
            text_in_letter_after_order_processing = EmailPageLocators.TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_EN
            expected_email_text = 'Payment received, activate the service on the '

        self.browser.find_element(*letter_after_order_processing).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        text_of_letter = self.browser.find_element(*text_in_letter_after_order_processing).text
        assert expected_email_text in text_of_letter, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def verification_of_letter_after_publication_of_vacancy(self, language):  # проверка письма после публикации вакансии
        # time.sleep(20)
        # self.browser.refresh()

        letter_after_publishing_vacancy, text_in_letter_after_publishing_vacancy, expected_email_text = None, None, None
        if language == "/ua":
            letter_after_publishing_vacancy = EmailPageLocators.LETTER_AFTER_PUBLISHING_VACANCY_UA
            text_in_letter_after_publishing_vacancy = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_UA
            expected_email_text = ['Ваша вакансія ', ' вже на сайті!']
        elif language == "":
            letter_after_publishing_vacancy = EmailPageLocators.LETTER_AFTER_PUBLISHING_VACANCY_RU
            text_in_letter_after_publishing_vacancy = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_RU
            expected_email_text = ['Ваша вакансия ', ' добавлена на сайт.']
        elif language == "/en":
            letter_after_publishing_vacancy = EmailPageLocators.LETTER_AFTER_PUBLISHING_VACANCY_EN
            text_in_letter_after_publishing_vacancy = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_EN
            expected_email_text = ['Your vacancy ', ' is already on website!']

        self.browser.find_element(*letter_after_publishing_vacancy).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        text_of_letter = self.browser.find_element(*text_in_letter_after_publishing_vacancy).text
        assert expected_email_text[0] + TestData.job_title_vacancy + expected_email_text[1] in text_of_letter, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def verification_of_letter_after_publication_of_resume(self, language):  # проверка письма после публикации резюме
        # time.sleep(20)
        # self.browser.refresh()

        letter_after_publishing_resume, text_in_letter_after_publishing_resume, expected_email_text = None, None, None
        if language == "/ua":
            letter_after_publishing_resume = EmailPageLocators.LETTER_AFTER_PUBLISHING_RESUME_UA
            text_in_letter_after_publishing_resume = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_UA
            expected_email_text = 'Ваше резюме опубліковано на '
        elif language == "":
            letter_after_publishing_resume = EmailPageLocators.LETTER_AFTER_PUBLISHING_RESUME_RU
            text_in_letter_after_publishing_resume = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_RU
            expected_email_text = 'Ваше резюме опубликовано на '
        elif language == "/en":
            letter_after_publishing_resume = EmailPageLocators.LETTER_AFTER_PUBLISHING_RESUME_EN
            text_in_letter_after_publishing_resume = EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_EN
            expected_email_text = 'Your resume is published on the '

        self.browser.find_element(*letter_after_publishing_resume).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*text_in_letter_after_publishing_resume).text
        assert expected_email_text in letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма
