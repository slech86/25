from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ResumePageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from Page_Object_Model.сonfiguration import UrlStartPage
from Page_Object_Model.singleton import Singleton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ResumePage(BasePage):
    def confirmation_opening_of_resume_page(self, language):  # подтверждение открытия страницы резюме
        singleton = Singleton()
        if language == '/ua':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/resume/' + singleton.id_resume[0], 'Не правильный URL'
        elif language == '':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/resume/' + singleton.id_resume[0], 'Не правильный URL'
        elif language == '/en':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/resume/' + singleton.id_resume[0], 'Не правильный URL'

    def checking_opening_of_page_of_an_unpublished_resume(self, language):  # проверка открытия страницы не опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Резюме приховано', "Не корректный h1"
        elif language == "":
            assert h1 == 'Резюме скрыто', "Не корректный h1"
        elif language == "/en":
            assert h1 == 'CV is hidden', "Не корректный h1"

    def checking_opening_of_page_of_published_resume(self, job_title_resume):  # проверка открытия страницы опубликованного резюме
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == job_title_resume, "Резюме не опубликована"

    def checking_opening_of_page_of_published_resume_after_editing(self):  # проверка открытия страницы опубликованного резюме после редактирования
        h1 = self.browser.find_element(*ResumePageLocators.H1).text
        assert h1 == TestDataEditing.job_title_resume, "Резюме не опубликована"

    def checking_cover_letter_text(self):  # проверка текста сопроводительного письма
        cover_letter_text = self.browser.find_element(*ResumePageLocators.COVER_LETTER_TEXT).text
        assert cover_letter_text == TestData.cover_letter, "Сопроводительное письмо не совпадает"

    def checking_contact_block_before_authorization(self, language):  # проверка блока контактов до авторизации
        text_in_contact_block = self.browser.find_element(*ResumePageLocators.TEXT_OF_CONTACT_BLOCK_BEFORE_AUTHORIZATION).text
        if language == "":
            assert text_in_contact_block == 'Зарегистрируйтесь или войдите, чтобы полностью ознакомиться или предложить вакансию.', "Текст в блоке контактов до авторизации, не верный"
        elif language == "/ua":
            assert text_in_contact_block == 'Зареєструйтеся або увійдіть, щоб повністю ознайомитися або запропонувати вакансію.', "Текст в блоке контактов до авторизации, не верный"
        elif language == "/en":
            assert text_in_contact_block == 'Register now or sign in to read all or offer a vacancy.', "Текст в блоке контактов до авторизации, не верный"

    def checking_contact_block_before_buying_package_of_services(self, language):  # проверка блока контактов до покупки пакета услуг
        text_in_contact_block = self.browser.find_element(*ResumePageLocators.TEXT_OF_CONTACT_BLOCK_BEFORE_BUYING_PACKAGE_OF_SERVICES).text
        if language == "":
            assert text_in_contact_block == 'Заинтересовал кандидат? Выберите подходящий пакет услуг.', "Текст в блоке контактов до покупки пакета услуг, не верный"
        elif language == "/ua":
            assert text_in_contact_block == 'Зацікавив кандидат? Виберіть відповідний пакет послуг.', "Текст в блоке контактов до покупки пакета услуг, не верный"
        elif language == "/en":
            assert text_in_contact_block == 'Is the candidate interested? Choose the appropriate service package.', "Текст в блоке контактов до покупки пакета услуг, не верный"

    def checking_absence_of_contact_block_with_information(self):  # проверка отсутствия блока контактов c информацией
        assert self.is_not_element_present(*ResumePageLocators.CONTACT_INFORMATION_BLOCK), "Не должно быть блока контактов с информацией"

    def checking_absence_of_contact_block(self):  # проверка отсутствия блока контактов
        assert self.is_not_element_present(*ResumePageLocators.CONTACT_BLOCK), "Не должно быть блока контактов"

    def opening_contacts_in_resume(self):  # открытие контактов в резюме
        self.browser.find_element(*ResumePageLocators.BUTTON_VIEW_CONTACTS).click()
        WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(ResumePageLocators.BUTTON_OPEN_CONTACT_IN_POP_UP)).click()

    def checking_contact_display(self, test_data):  # проверка отображения контактов
        phone1 = self.browser.find_element(*ResumePageLocators.PHONE_1_IN_CONTACT_INFORMATION).text
        assert phone1 == test_data.phone_1_resume, f"Первый телефон в контактах резюме, expected result: '{test_data.phone_1_resume}', actual result: '{phone1}'"

        phone2 = self.browser.find_element(*ResumePageLocators.PHONE_2_IN_CONTACT_INFORMATION).text
        assert phone2 == test_data.phone_2_resume, f"Второй телефон в контактах резюме, expected result: '{test_data.phone_2_resume}', actual result: '{phone2}'"

        email = self.browser.find_element(*ResumePageLocators.EMAIL_IN_CONTACT_INFORMATION).text
        assert email == test_data.email_resume, f"Email в контактах резюме, expected result: '{test_data.email_resume}', actual result: '{email}'"

        skype = self.browser.find_element(*ResumePageLocators.SKYPE_IN_CONTACT_INFORMATION).text
        assert skype == test_data.skype_resume, f"Skype в контактах резюме, expected result: '{test_data.skype_resume}', actual result: '{skype}'"

        portfolio = self.browser.find_element(*ResumePageLocators.PORTFOLIO_IN_CONTACT_INFORMATION)
        portfolio_href = portfolio.get_attribute("href")
        assert portfolio_href == test_data.portfolio, f"Portfolio в контактах резюме, expected result: '{test_data.portfolio}', actual result: '{portfolio_href}'"

        facebook = self.browser.find_element(*ResumePageLocators.FACEBOOK_IN_CONTACT_INFORMATION)
        facebook_href = facebook.get_attribute("href")
        assert facebook_href == test_data.facebook_resume, f"Facebook в контактах резюме, expected result: '{test_data.facebook_resume}', actual result: '{facebook_href}'"

        linkedin = self.browser.find_element(*ResumePageLocators.LINKEDIN_IN_CONTACT_INFORMATION)
        linkedin_href = linkedin.get_attribute("href")
        assert linkedin_href == test_data.linkedin_resume, f"Linkedin в контактах резюме, expected result: '{test_data.linkedin_resume}', actual result: '{linkedin_href}'"

        instagram = self.browser.find_element(*ResumePageLocators.INSTAGRAM_IN_CONTACT_INFORMATION)
        instagram_href = instagram.get_attribute("href")
        assert instagram_href == test_data.instagram_resume, f"Instagram в контактах резюме, expected result: '{test_data.instagram_resume}', actual result: '{instagram_href}'"

        telegram = self.browser.find_element(*ResumePageLocators.TELEGRAM_IN_CONTACT_INFORMATION)
        telegram_href = telegram.get_attribute("href")
        assert telegram_href == test_data.telegram_resume, f"Telegram в контактах резюме, expected result: '{test_data.telegram_resume}', actual result: '{telegram_href}'"

        twitter = self.browser.find_element(*ResumePageLocators.TWITTER_IN_CONTACT_INFORMATION)
        twitter_href = twitter.get_attribute("href")
        assert twitter_href == test_data.twitter_resume, f"Twitter в контактах резюме, expected result: '{test_data.twitter_resume}', actual result: '{twitter_href}'"

        vk = self.browser.find_element(*ResumePageLocators.VK_IN_CONTACT_INFORMATION)
        vk_href = vk.get_attribute("href")
        assert vk_href == test_data.vk_resume, f"VK в контактах резюме, expected result: '{test_data.vk_resume}', actual result: '{vk_href}'"
