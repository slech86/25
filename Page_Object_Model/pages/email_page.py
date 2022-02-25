from .base_page import BasePage
from Page_Object_Model.locators.locators import EmailPageLocators
from Page_Object_Model.data_for_testing import Accounts
from Page_Object_Model.data_for_testing import TestData


class EmailPage(BasePage):
    def email_authorization(self):  # авторизация email
        self.browser.find_element(*EmailPageLocators.FIELD_EMAIL).send_keys(Accounts.main_login_email)
        self.browser.find_element(*EmailPageLocators.FIELD_PASSWORD).send_keys(Accounts.main_password_email)
        self.browser.find_element(*EmailPageLocators.BUTTON_LOG_IN).click()

    def confirmation_of_company_registration_in_letter_ru(self):  # подтверждение регистрации работодателя в письме RU
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])
    def confirmation_of_company_registration_in_letter_ua(self):  # подтверждение регистрации работодателя в письме UA
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_OF_REGISTRATION_CONFIRMATION_COMPANY_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])

    def letter_after_first_moderation_of_company_ru(self):  # письмо после первой модерации компании ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_RU).text
        assert "Ура! Ваш аккаунт прошел модерацию." == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма
    def letter_after_first_moderation_of_company_ua(self):  # письмо после первой модерации компании ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_FIRST_MODERATION_UA).text
        assert "Ура! Ваш акаунт пройшов модерацiю." == letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма


    def confirmation_of_job_seeker_registration_in_letter_ru(self):  # подтверждение регистрации соискателя в письме ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])
    def confirmation_of_job_seeker_registration_in_letter_ua(self):  # подтверждение регистрации соискателя в письме ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_WELCOME_TO_LCWORK_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        self.browser.find_element(*EmailPageLocators.LINK_IN_LETTER).click()
        self.browser.switch_to.default_content()  # выход из фрейма
        self.browser.switch_to.window(self.browser.window_handles[1])


    def letter_after_order_processing_ru(self):  # письмо после проведения заказа ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_ORDER_PROCESSING_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_RU).text
        assert "Оплата получена, активируйте услугу на " in letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма
    def letter_after_order_processing_ua(self):  # письмо после проведения заказа ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_ORDER_PROCESSING_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_ORDER_PROCESSING_UA).text
        assert "Оплата отримана, активуйте послугу на " in letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма


    def verification_of_letter_after_publication_of_vacancy_ru(self):  # проверка письма после публикации вакансии ru
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_PUBLISHING_VACANCY_RU).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_RU).text
        assert 'Ваша вакансия ' + TestData.job_title_vacancy + ' добавлена на сайт.' in letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма
    def verification_of_letter_after_publication_of_vacancy_ua(self):  # проверка письма после публикации вакансии ua
        # time.sleep(20)
        # self.browser.refresh()

        self.browser.find_element(*EmailPageLocators.LETTER_AFTER_PUBLISHING_VACANCY_UA).click()

        iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_VACANCY_UA).text
        assert 'Ваша вакансія ' + TestData.job_title_vacancy + ' вже на сайті!' in letter_text, 'Не верное сообщение'
        self.browser.switch_to.default_content()  # выход из фрейма

    def verification_of_letter_after_publication_of_resume(self, language):  # проверка письма после публикации резюме
        # time.sleep(20)
        # self.browser.refresh()

        if language == "/ua":
            self.browser.find_element(*EmailPageLocators.LETTER_AFTER_PUBLISHING_RESUME_UA).click()

            iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
            self.browser.switch_to.frame(iframe)  # вход в фрейм
            letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_UA).text
            assert 'Ваше резюме опубліковано на ' in letter_text, 'Не верное сообщение'
            self.browser.switch_to.default_content()  # выход из фрейма
        else:
            self.browser.find_element(*EmailPageLocators.LETTER_AFTER_PUBLISHING_RESUME_RU).click()

            iframe = self.browser.find_element(*EmailPageLocators.IFRAME_LETTER)
            self.browser.switch_to.frame(iframe)  # вход в фреймTEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_RU).text
            letter_text = self.browser.find_element(*EmailPageLocators.TEXT_IN_LETTER_AFTER_PUBLISHING_RESUME_RU).text
            assert 'Ваше резюме опубликовано на ' in letter_text, 'Не верное сообщение'
            self.browser.switch_to.default_content()  # выход из фрейма