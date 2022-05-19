import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import MyVacanciesPageLocators
from Page_Object_Model.сonfiguration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyVacanciesPage(BasePage):
    def go_to_vacancy_add_page(self):  # переход на страницу "Добавить вакансию"
        self.browser.find_element(*MyVacanciesPageLocators.BUTTON_ADD_VACANCY).click()

    def go_to_vacancy_editing_page(self):  # переход на страницу редактирования вакансии
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies()  # сборка локаторов с id вакансии
        self.browser.find_element(*locators[0]).click()
        time.sleep(0.2)
        self.browser.find_element(*locators[1]).click()

    def checking_for_availability_icon_new_response_to_vacancy(self):  # проверка наличия иконки нового отклика на вакансию
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locator = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies()  # сборка локаторов с id вакансии
        assert self.is_element_present(*locator[3]), 'Нет иконки нового отклика на вакансию'

    def go_to_responses_to_vacancy_page(self):  # переход на страницу 'Отклики на вакансию'
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locator = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies()  # сборка локаторов с id вакансии
        self.browser.find_element(*locator[2]).click()

    def waiting_for_my_vacancies_page_to_open(self, language):  # ожидание открытия страницы 'Мои вакансии'
        if language == "/ua":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мої вакансії'))
        elif language == "":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мои вакансии'))
        elif language == "/en":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'My vacancies'))

    def confirmation_of_opening_of_page_my_vacancies(self, language):  # подтверждение открытия страницы 'Мои вакансии'
        if language == "/ua":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/vacancy/my", "Не правильный URL"
        elif language == "":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/vacancy/my", "Не правильный URL"
        elif language == "/en":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/vacancy/my", "Не правильный URL"

    def checking_message_confirming_of_creation_of_vacancy(self, language):  # проверка сообщения о создании новой вакансии
        infoText = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_CREATING_VACANCY).text
        if language == "/ua":
            assert "Створена вами вакансія прийнята і відправлена на модерацію. Вакансія буде доступна на сайті впродовж 24 годин." == infoText, 'Не верное сообщение'
        elif language == "":
            assert "Созданная вами вакансия принята и отправлена на модерацию. Вакансия будет доступна на сайте в течение 24 часов." == infoText, 'Не верное сообщение'
        elif language == "/en":
            assert "The vacancy you have created has been accepted and sent for moderation. The vacancy will be available on the website within 12 hours." == infoText, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_CREATING_VACANCY).click()

    def checking_message_confirming_submission_of_vacancy_for_moderation(self, language):  # проверка сообщения о подтверждении отправки вакансии на модерацию
        infoText = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).text
        if language == "/ua":
            assert "Створена вами вакансія прийнята і відправлена на модерацію. Вакансія буде доступна на сайті впродовж 24 годин." == infoText, 'Не верное сообщение'
        elif language == "":
            assert "Созданная вами вакансия принята и отправлена на модерацию. Вакансия будет доступна на сайте в течение 24 часов." == infoText, 'Не верное сообщение'
        elif language == "/en":
            assert "The vacancy you have created has been accepted and sent for moderation. The vacancy will be available on the website within 12 hours." == infoText, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).click()
