import time

from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import MyVacanciesPageLocators
from Page_Object_Model.configuration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class MyVacanciesPage(BasePage):
    def go_to_vacancy_add_page(self):  # переход на страницу "Добавить вакансию"
        self.browser.find_element(*MyVacanciesPageLocators.BUTTON_ADD_VACANCY).click()

    def opening_vacancy_menu(self, vacancy_id):  # открытие меню вакансии
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*locators['button_vacancy_menu']).click()
        time.sleep(0.3)

    def go_to_vacancy_editing_page(self, vacancy_id):  # переход на страницу редактирования вакансии
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*locators['button_edit']).click()

    def hide_vacancy(self, vacancy_id):  # скрыть вакансию
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*locators['button_hide']).click()

    def publish_vacancy(self, vacancy_id):  # опубликовать вакансию
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*locators['button_publish']).click()

    def checking_status_display_is_hidden_in_vacancy_block(self, vacancy_id, language):  # проверка отображения статуса "Cкрыто" в блоке вакансии
        time.sleep(0.5)
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        status_text = self.browser.find_element(*locators['status_vacancy']).text
        if language == "":
            assert "Вакансия скрыта" == status_text, 'Вакансия не скрыта'
        elif language == "/ua":
            assert "Вакансія прихована" == status_text, 'Вакансия не скрыта'
        elif language == "/en":
            assert "Vacancy is hidden" == status_text, 'Вакансия не скрыта'
        elif language == "/pl":
            assert "Wakat ukryty" == status_text, 'Вакансия не скрыта'

    def checking_status_of_page_response_to_print_pdf(self, vacancy_id):  # проверка статуса ответа страницы 'распечатать пдф'
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(locators['button_print'])).click()
        self.browser.switch_to.window(self.browser.window_handles[2])
        response = requests.head(self.browser.current_url)
        assert response.status_code == 200, 'Статус ответа страницы не 200'

    def deletion_vacancy_draft(self, id_vacancies):  # удаление черновика вакансии
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locators = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(id_vacancies)  # сборка локаторов с id вакансии
        self.browser.find_element(*locators['button_delete']).click()
        self.browser.find_element(*MyVacanciesPageLocators.BUTTON_CONFIRMATION_DELETION_DRAFT_VACANCIES).click()

    def checking_message_after_deleting_vacancy(self, language):  # проверка сообщения после удаления вакансии
        info_text = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_DELETING_DRAFT_VACANCY).text
        if language == "":
            assert "Черновик удален." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Чернетка видалена." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Draft deleted" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Wersja robocza została usunięta." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_DELETING_DRAFT_VACANCY).click()

    def checking_for_availability_icon_new_response_to_vacancy(self, vacancy_id):  # проверка наличия иконки нового отклика на вакансию
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locator = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        assert self.is_element_present(*locator['new_response_icon']), 'Нет иконки нового отклика на вакансию'

    def go_to_responses_to_vacancy_page(self, vacancy_id):  # переход на страницу 'Отклики на вакансию'
        locators_with_id_vacancies = MyVacanciesPageLocators()
        locator = locators_with_id_vacancies.assembly_of_locators_with_id_vacancies(vacancy_id)  # сборка локаторов с id вакансии
        self.browser.find_element(*locator['button_show_responses']).click()

    def waiting_for_my_vacancies_page_to_open(self, language):  # ожидание открытия страницы 'Мои вакансии'
        if language == "":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мои вакансии'))
        elif language == "/ua":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мої вакансії'))
        elif language == "/en":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'My vacancies'))
        elif language == "/pl":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'My vacancies'))

    def confirmation_of_opening_of_page_my_vacancies(self, language):  # подтверждение открытия страницы 'Мои вакансии'
        if language == "":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/vacancy/my", "Не правильный URL"
        elif language == "/ua":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/vacancy/my", "Не правильный URL"
        elif language == "/en":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/vacancy/my", "Не правильный URL"
        elif language == "/pl":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/pl/vacancy/my", "Не правильный URL"

    def checking_message_confirming_of_creation_of_vacancy(self, language):  # проверка сообщения о создании новой вакансии
        info_text = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_CREATING_VACANCY).text
        if language == "":
            assert "Созданная вами вакансия принята и отправлена на модерацию. Вакансия будет доступна на сайте в течение 24 часов." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Створена вами вакансія прийнята і відправлена на модерацію. Вакансія буде доступна на сайті впродовж 24 годин." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "The vacancy you have created has been accepted and sent for moderation. The vacancy will be available on the website within 12 hours." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Wolne miejsca pracy będą dostępne na stronie internetowej w ciągu 24 godzin." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_CREATING_VACANCY).click()

    def checking_message_about_adding_vacancy_to_draft(self, language):  # проверка сообщения о добавлении вакансии в черновик
        info_text = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_ADDING_VACANCY_TO_DRAFT).text
        if language == "":
            assert "Ваши изменения были сохранены в черновик" == info_text, f"Не верное сообщение, expected result: 'Ваша вакансия добавлена в черновики', actual result: '{info_text}'"
        elif language == "/ua":
            assert "Ваші зміни були збережені в чернетку" == info_text, f"Не верное сообщение, expected result: 'Ваша вакансія додана до чернеток', actual result: '{info_text}'"
        elif language == "/en":
            assert "Your changes have been saved to draft" == info_text, f"Не верное сообщение, expected result: 'Your vacancy has been added to drafts', actual result: '{info_text}'"
        elif language == "/pl":
            assert "Twoje zmiany zostały zapisane w szkicu" == info_text, f"Не верное сообщение, expected result: 'Your vacancy has been added to drafts', actual result: '{info_text}'"
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_ADDING_VACANCY_TO_DRAFT).click()


    def checking_message_confirming_submission_of_vacancy_for_moderation(self, language):  # проверка сообщения о подтверждении отправки вакансии на модерацию
        info_text = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).text
        if language == "":
            assert "Созданная вами вакансия принята и отправлена на модерацию. Вакансия будет доступна на сайте в течение 24 часов." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Створена вами вакансія прийнята і відправлена на модерацію. Вакансія буде доступна на сайті впродовж 24 годин." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "The vacancy you have created has been accepted and sent for moderation. The vacancy will be available on the website within 12 hours." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Wolne miejsca pracy będą dostępne na stronie internetowej w ciągu 24 godzin." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).click()
