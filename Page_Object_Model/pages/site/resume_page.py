from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ResumePageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from Page_Object_Model.сonfiguration import UrlStartPage
from Page_Object_Model.singleton import Singleton


class ResumePage(BasePage):
    def confirmation_opening_of_vacancy_page(self, language):  # подтверждение открытия страницы вакансии
        singleton = Singleton()
        if language == '/ua':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/resume/' + singleton.id_resume, 'Не правильный URL'
        elif language == '':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/resume/' + singleton.id_resume, 'Не правильный URL'
        elif language == '/en':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/resume/' + singleton.id_resume, 'Не правильный URL'

    def checking_opening_of_page_of_an_unpublished_resume(self, language):  # проверка открытия страницы не опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Резюме приховано', "Не корректный h1"
        elif language == "":
            assert h1 == 'Резюме скрыто', "Не корректный h1"
        elif language == "/en":
            assert h1 == 'CV is hidden', "Не корректный h1"

    def checking_opening_of_page_of_published_resume(self):  # проверка открытия страницы опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == TestData.job_title_resume, "Резюме не опубликована"

    def checking_opening_of_page_of_published_resume_after_editing(self):  # проверка открытия страницы опубликованного резюме после редактирования
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == TestDataEditing.job_title_resume, "Резюме не опубликована"

    def checking_cover_letter_text(self):  # проверка текста сопроводительного письма
        cover_letter_text = self.browser.find_element(*ResumePageLocators.COVER_LETTER_TEXT).text
        assert cover_letter_text == TestData.cover_letter, "Сопроводительное письмо не совпадает"

    def checking_contact_display(self):  # проверка отображения контактов
        phone1 = self.browser.find_element(*ResumePageLocators.PHONE_1_IN_CONTACT_INFORMATION).text
        assert phone1 == TestDataEditing.phone_1_resume, f"Первый телефон в контактах резюме, expected result: '{TestDataEditing.phone_1_resume}', actual result: '{phone1}'"

        phone2 = self.browser.find_element(*ResumePageLocators.PHONE_2_IN_CONTACT_INFORMATION).text
        assert phone2 == TestDataEditing.phone_2_resume, f"Второй телефон в контактах резюме, expected result: '{TestDataEditing.phone_2_resume}', actual result: '{phone2}'"

        email = self.browser.find_element(*ResumePageLocators.EMAIL_IN_CONTACT_INFORMATION).text
        assert email == TestDataEditing.email_resume, f"Email в контактах резюме, expected result: '{TestDataEditing.email_resume}', actual result: '{email}'"

        skype = self.browser.find_element(*ResumePageLocators.SKYPE_IN_CONTACT_INFORMATION).text
        assert skype == TestDataEditing.skype_resume, f"Skype в контактах резюме, expected result: '{TestDataEditing.skype_resume}', actual result: '{skype}'"

        portfolio = self.browser.find_element(*ResumePageLocators.PORTFOLIO_IN_CONTACT_INFORMATION)
        portfolio_href = portfolio.get_attribute("href")
        assert portfolio_href == TestDataEditing.portfolio, f"Portfolio в контактах резюме, expected result: '{TestDataEditing.portfolio}', actual result: '{portfolio_href}'"

        facebook = self.browser.find_element(*ResumePageLocators.FACEBOOK_IN_CONTACT_INFORMATION)
        facebook_href = facebook.get_attribute("href")
        assert facebook_href == TestDataEditing.facebook_resume, f"Facebook в контактах резюме, expected result: '{TestDataEditing.facebook_resume}', actual result: '{facebook_href}'"

        linkedin = self.browser.find_element(*ResumePageLocators.LINKEDIN_IN_CONTACT_INFORMATION)
        linkedin_href = linkedin.get_attribute("href")
        assert linkedin_href == TestDataEditing.linkedin_resume, f"Linkedin в контактах резюме, expected result: '{TestDataEditing.linkedin_resume}', actual result: '{linkedin_href}'"

        instagram = self.browser.find_element(*ResumePageLocators.INSTAGRAM_IN_CONTACT_INFORMATION)
        instagram_href = instagram.get_attribute("href")
        assert instagram_href == TestDataEditing.instagram_resume, f"Instagram в контактах резюме, expected result: '{TestDataEditing.instagram_resume}', actual result: '{instagram_href}'"

        telegram = self.browser.find_element(*ResumePageLocators.TELEGRAM_IN_CONTACT_INFORMATION)
        telegram_href = telegram.get_attribute("href")
        assert telegram_href == TestDataEditing.telegram_resume, f"Telegram в контактах резюме, expected result: '{TestDataEditing.telegram_resume}', actual result: '{telegram_href}'"

        twitter = self.browser.find_element(*ResumePageLocators.TWITTER_IN_CONTACT_INFORMATION)
        twitter_href = twitter.get_attribute("href")
        assert twitter_href == TestDataEditing.twitter_resume, f"Twitter в контактах резюме, expected result: '{TestDataEditing.twitter_resume}', actual result: '{twitter_href}'"

        vk = self.browser.find_element(*ResumePageLocators.VK_IN_CONTACT_INFORMATION)
        vk_href = vk.get_attribute("href")
        assert vk_href == TestDataEditing.vk_resume, f"VK в контактах резюме, expected result: '{TestDataEditing.vk_resume}', actual result: '{vk_href}'"
