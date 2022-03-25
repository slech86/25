import time
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import MyResumePageLocators
from Page_Object_Model.сonfiguration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyResumePage(BasePage):
    def go_to_add_resume_page(self):  # переход на страницу "Разместить резюме"
        self.browser.find_element(*MyResumePageLocators.BUTTON_ADD_RESUME).click()

    def go_to_resume_editing_page(self):  # переход на страницу редактирования резюме
        self.browser.find_element(*MyResumePageLocators.BUTTON_RESUME_MENU).click()
        time.sleep(0.2)
        locators_with_id_resume = MyResumePageLocators()
        locator = locators_with_id_resume.assembly_of_locators_with_id_resume()  # сборка локатов с id резюме
        self.browser.find_element(*locator).click()

    def waiting_for_my_resumes_page_to_open(self, language):  # ожидание открытия страницы 'Мои резюме'
        if language == "/ua":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'Мої резюме'))
        elif language == "":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'Мои резюме'))
        elif language == "/en":
            WebDriverWait(self.browser, 15).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'My CVs'))

    def confirmation_of_opening_of_page_my_resumes(self, language):  # подтверждение открытия страницы 'Мои резюме'
        if language == "/ua":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/resume/my", "Не правильный URL"
        elif language == "":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/resume/my", "Не правильный URL"
        elif language == "/en":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/resume/my", "Не правильный URL"

    def checking_message_confirming_submission_of_resume_for_moderation(self, language):  # проверка сообщения о подтверждении отправки резюме на модерацию
        infoText = self.browser.find_element(*MyResumePageLocators.INFO_TEXT_AFTER_SUBMITTING_RESUME_FOR_MODERATION).text
        if language == "/ua":
            assert "Створене вами резюме прийнято і відправлено на модерацію. Резюме буде доступним на сайті протягом 12 годин." == infoText, 'Не верное сообщение'
        elif language == "":
            assert "Созданное вами резюме принято и отправлено на модерацию. Резюме будет доступно на сайте в течение 12 часов." == infoText, 'Не верное сообщение'
        elif language == "/en":
            assert "Your resume has been accepted and sent for moderation. The summary will be available on the site within 12 hours." == infoText, 'Не верное сообщение'
        self.browser.find_element(*MyResumePageLocators.CROSS_IN_POP_UP_AFTER_SUBMITTING_RESUME_FOR_MODERATION).click()
