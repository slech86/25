from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import MyVacanciesPageLocators
from Page_Object_Model.сonfiguration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyVacanciesPage(BasePage):
    def go_to_add_vacancy_page(self):  # переход на страницу "Добавить вакансию"
        self.browser.find_element(*MyVacanciesPageLocators.BUTTON_ADD_VACANCY).click()

    def waiting_for_my_vacancies_page_to_open(self, language):  # ожидание открытия страницы 'Мои вакансии'
        if language == "/ua":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мої вакансії'))
        else:
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyVacanciesPageLocators.H1), 'Мои вакансии'))

    def confirmation_of_opening_of_page_my_vacancies(self):  # подтверждение открытия страницы 'Мои вакансии'
        if "/ua" in self.browser.current_url:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/vacancy/my", "Не правильный URL"
        else:
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/vacancy/my", "Не правильный URL"

    def checking_message_confirming_submission_of_vacancy_for_moderation(self):  # проверка сообщения о подтверждении отправки вакансии на модерацию
        infoText = self.browser.find_element(*MyVacanciesPageLocators.INFO_TEXT_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).text
        if "/ua" in self.browser.current_url:
            assert "Створена вами вакансія прийнята і відправлена на модерацію. Вакансія буде доступна на сайті впродовж 24 годин." == infoText, 'Не верное сообщение'
        else:
            assert "Созданная вами вакансия принята и отправлена на модерацию. Вакансия будет доступна на сайте в течение 24 часов." == infoText, 'Не верное сообщение'
        self.browser.find_element(*MyVacanciesPageLocators.CROSS_IN_POP_UP_AFTER_SUBMITTING_VACANCY_FOR_MODERATION).click()
