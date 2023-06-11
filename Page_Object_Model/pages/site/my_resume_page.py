import time
from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.job_seeker_locators import MyResumePageLocators
from Page_Object_Model.configuration import UrlStartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


class MyResumePage(BasePage):
    def obtaining_number_of_resumes_to_create(self):  # получение количества резюме для создания
        text = self.browser.find_element(*MyResumePageLocators.TEXT_OF_NUMBER_OF_CREATED_RESUMES).text
        index = text.find(' ')
        number_of_resumes_created = int(text[index + 1])
        return number_of_resumes_created

    def checking_number_of_resumes_to_create(self, expected_number_of_resumes_generated):  # проверка количества резюме для создания
        text = self.browser.find_element(*MyResumePageLocators.TEXT_OF_NUMBER_OF_CREATED_RESUMES).text
        index = text.find(' ')
        actual_number_of_resumes_generated = int(text[index + 1])
        assert actual_number_of_resumes_generated == expected_number_of_resumes_generated, f"Отображается не верное количество созданных резюме, expected result: '{expected_number_of_resumes_generated}', actual result: '{actual_number_of_resumes_generated}'"

    def go_to_add_resume_page(self):  # переход на страницу "Разместить резюме"
        self.browser.find_element(*MyResumePageLocators.BUTTON_ADD_RESUME).click()

    def opening_menu_of_first_resume_in_list(self):  # открытие меню первого резюме в списке
        self.browser.find_element(*MyResumePageLocators.BUTTON_RESUME_MENU).click()
        time.sleep(0.3)

    def opening_resume_menu(self, id_resume):  # открытие меню резюме
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локатора с id резюме
        self.browser.find_element(*locators['button_resume_menu']).click()

    def go_to_resume_editing_page(self, id_resume):  # переход на страницу редактирования резюме
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локатора с id резюме
        self.browser.find_element(*locators['button_edit']).click()

    def hide_resume(self, id_resume):  # скрыть резюме
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локаторов с id резюме
        self.browser.find_element(*locators['button_hide']).click()

    def publish_resume(self, id_resume):  # опубликовать резюме
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локаторов с id резюме
        self.browser.find_element(*locators['button_publish']).click()

    def checking_status_display_is_hidden_in_resume_block(self, id_resume, language):  # проверка отображения статуса "Cкрыто" в блоке резюме
        time.sleep(0.5)
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локаторов с id резюме
        status_text = self.browser.find_element(*locators['status_resume']).text
        if language == "":
            assert "Резюме скрыто" == status_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Резюме приховано" == status_text, 'Не верное сообщение'
        elif language == "/en":
            assert "CV is hidden" == status_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Podsumowanie ukryte" == status_text, 'Не верное сообщение'

    def checking_status_of_page_response_to_print_pdf(self):  # проверка статуса ответа страницы 'распечатать пдф'
        WebDriverWait(self.browser, 7).until(EC.visibility_of_element_located(MyResumePageLocators.BUTTON_PRINT)).click()
        self.browser.switch_to.window(self.browser.window_handles[2])
        response = requests.head(self.browser.current_url)
        assert response.status_code == 200, 'Статус ответа страницы не 200'

    def deletion_resume_draft(self, id_resume):  # удаление черновика резюме
        locators_with_id_resume = MyResumePageLocators()
        locators = locators_with_id_resume.assembly_of_locators_with_id_resume(id_resume)  # сборка локатора с id резюме
        self.browser.find_element(*locators['button_delete']).click()
        self.browser.find_element(*MyResumePageLocators.BUTTON_CONFIRMATION_DELETION_DRAFT_RESUME).click()

    def checking_message_after_deleting_resume(self, language):  # проверка сообщения после удаления резюме
        info_text = self.browser.find_element(*MyResumePageLocators.INFO_TEXT_AFTER_DELETING_DRAFT_RESUME).text
        if language == "":
            assert "Черновик удален." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Чернетка видалена." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Draft deleted" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Wersja robocza została usunięta." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyResumePageLocators.CROSS_IN_POP_UP_AFTER_DELETING_DRAFT_RESUME).click()

    def waiting_for_my_resumes_page_to_open(self, language):  # ожидание открытия страницы 'Мои резюме'
        if language == "":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'Мои резюме'))
        elif language == "/ua":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'Мої резюме'))
        elif language == "/en":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'My CVs'))
        elif language == "/pl":
            WebDriverWait(self.browser, 35).until(EC.text_to_be_present_in_element((MyResumePageLocators.H1), 'My CVs'))

    def confirmation_of_opening_of_page_my_resumes(self, language):  # подтверждение открытия страницы 'Мои резюме'
        if language == "":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/resume/my", "Не правильный URL"
        elif language == "/ua":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/ua/resume/my", "Не правильный URL"
        elif language == "/en":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/en/resume/my", "Не правильный URL"
        elif language == "/pl":
            assert self.browser.current_url == f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}/pl/resume/my", "Не правильный URL"

    def checking_message_confirming_of_creation_of_resume(self, language):  # проверка сообщения о создании нового резюме
        info_text = self.browser.find_element(*MyResumePageLocators.INFO_TEXT_AFTER_CREATING_RESUME).text
        if language == "":
            assert "Созданное вами резюме принято и отправлено на модерацию. Резюме будет доступно на сайте в течение 12 часов." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Створене вами резюме прийнято і відправлено на модерацію. Резюме буде доступним на сайті протягом 12 годин." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your resume has been accepted and sent for moderation. The summary will be available on the site within 12 hours." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Stworzone przez Ciebie CV zostało zaakceptowane i wysłane do moderacji. CV będą dostępne na stronie w ciągu 12 godzin." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyResumePageLocators.CROSS_IN_POP_UP_AFTER_CREATING_RESUME).click()

    def checking_message_about_adding_resume_to_draft(self, language):  # проверка сообщения о добавлении резюме в черновик
        info_text = self.browser.find_element(*MyResumePageLocators.INFO_TEXT_AFTER_ADDING_RESUME_TO_DRAFT).text
        if language == "":
            assert "Ваши изменения были сохранены в черновик" == info_text, f"Не верное сообщение, expected result: 'Ваше резюме добавлено в черновики', actual result: '{info_text}'"
        elif language == "/ua":
            assert "Ваші зміни були збережені в чернетку" == info_text, f"Не верное сообщение, expected result: 'Ваше резюме додане до чернеток', actual result: '{info_text}'"
        elif language == "/en":
            assert "Your changes have been saved to draft" == info_text, f"Не верное сообщение, expected result: 'Your CV has been added to drafts', actual result: '{info_text}'"
        elif language == "/pl":
            assert "Twoje zmiany zostały zapisane w szkicu" == info_text, f"Не верное сообщение, expected result: 'Your CV has been added to drafts', actual result: '{info_text}'"
        self.browser.find_element(*MyResumePageLocators.CROSS_IN_POP_UP_AFTER_ADDING_RESUME_TO_DRAFT).click()

    def checking_message_confirming_submission_of_resume_for_moderation(self, language):  # проверка сообщения о подтверждении отправки резюме на модерацию
        info_text = self.browser.find_element(*MyResumePageLocators.INFO_TEXT_AFTER_SUBMITTING_RESUME_FOR_MODERATION).text
        if language == "":
            assert "Созданное вами резюме принято и отправлено на модерацию. Резюме будет доступно на сайте в течение 12 часов." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Створене вами резюме прийнято і відправлено на модерацію. Резюме буде доступним на сайті протягом 12 годин." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Your resume has been accepted and sent for moderation. The summary will be available on the site within 12 hours." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Stworzone przez Ciebie CV zostało zaakceptowane i wysłane do moderacji. CV będą dostępne na stronie w ciągu 12 godzin." == info_text, 'Не верное сообщение'
        self.browser.find_element(*MyResumePageLocators.CROSS_IN_POP_UP_AFTER_SUBMITTING_RESUME_FOR_MODERATION).click()
