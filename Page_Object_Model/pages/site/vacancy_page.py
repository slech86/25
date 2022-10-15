import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import VacancyPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from Page_Object_Model.configuration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class VacancyPage(BasePage):
    def confirmation_opening_of_vacancy_page(self, language, vacancy_id):  # подтверждение открытия страницы вакансии
        if language == '/ua':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/vacancy/' + vacancy_id, 'Не правильный URL'
        elif language == '':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/vacancy/' + vacancy_id, 'Не правильный URL'
        elif language == '/en':
            assert self.browser.current_url == f'{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/vacancy/' + vacancy_id, 'Не правильный URL'

    def checking_opening_of_page_of_an_unpublished_vacancy(self, language):  # проверка открытия страницы не опубликованной вакансии
        h1 = self.browser.find_element(*VacancyPageLocators.H1).text
        if language == "/ua":
            assert h1 == 'Пошук завершено', "Не корректный h1"
        if language == "":
            assert h1 == 'Поиск завершен', "Не корректный h1"
        if language == "/en":
            assert h1 == 'Search completed', "Не корректный h1"

    def checking_opening_of_page_of_published_vacancy(self, job_title_vacancy):  # проверка открытия страницы опубликованной вакансии
        h1 = self.browser.find_element(*VacancyPageLocators.H1).text
        assert h1 == job_title_vacancy, "Вакансия не опубликована"

    def checking_status_of_page_response_to_print_pdf(self):  # проверка статуса ответа страницы 'распечатать пдф'
        self.browser.find_element(*VacancyPageLocators.BUTTON_VACANCY_MENU).click()
        WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(VacancyPageLocators.BUTTON_PRINT)).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        response = requests.head(self.browser.current_url)
        assert response.status_code == 200, 'Статус ответа страницы не 200'
        self.browser.switch_to.window(self.browser.window_handles[0])

    def pressing_button_responds_1(self):  # нажатие на кнопку "Откликнуться" # 1
        self.browser.find_element(*VacancyPageLocators.BUTTON_RESPONSE_1).click()

    def presence_of_button_responds_2(self):  # наличие кнопки "Откликнуться" # 2
        assert self.is_element_present(*VacancyPageLocators.BUTTON_RESPONSE_2), 'Нет кнопки "Откликнуться" №2'

    def filling_and_sending_response_with_selected_active_resume(self, resume_id):  # заполнение и отправка отклика с выбранным активным резюме
        resume_locator = VacancyPageLocators()
        resume = resume_locator.assembly_of_locators_with_id_resume(resume_id)
        self.browser.find_element(*resume).click()
        self.browser.find_element(*VacancyPageLocators.BUTTON_ADD_COVER_LETTER).click()
        self.browser.find_element(*VacancyPageLocators.FIELD_COVER_LETTER).send_keys(TestData.cover_letter)
        self.browser.find_element(*VacancyPageLocators.BUTTON_SEND_CV).click()

    def checking_confirmation_message_for_sending_resume_of_company(self, language):  # проверка сообщения о подтверждении отправки резюме компании
        # time.sleep(1)
        info_text = WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(VacancyPageLocators.INFO_TEXT_AFTER_SENDING_RESPONSE_TO_VACANCY)).text
        print(info_text)
        print('info_text')
        if language == "/ua":
            assert "Ваше резюме відправлено роботодавцю!" == info_text, 'Не верное сообщение'
        elif language == "":
            assert "Ваше резюме отправлено работодателю!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your CV has been sent to an employer!" == info_text, 'Не верное сообщение'
        self.browser.find_element(*VacancyPageLocators.CROSS_IN_POP_UP_AFTER_SENDING_RESPONSE_TO_VACANCY).click()
        time.sleep(0.5)


    def presence_of_buttons_resume_posted(self):  # наличие не активных кнопок "Резюме отправлено"
        assert self.is_element_present(*VacancyPageLocators.NOT_ACTIVE_BUTTON_RESUME_POSTED_1), 'Нет  кнопки "Резюме отправлено" №1'
        assert self.is_element_present(*VacancyPageLocators.NOT_ACTIVE_BUTTON_RESUME_POSTED_2), 'Нет  кнопки "Резюме отправлено" №2'
