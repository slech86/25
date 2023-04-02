import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.pages.site.vacancies_page import VacanciesPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.my_responses_page import MyResponsesPage
from Page_Object_Model.pages.site.responses_to_vacancy_page import ResponsesToVacancyPage
from Page_Object_Model.data_for_testing import contact_display_when_response_to_vacancy
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.users import Accounts
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.tests import _resources_tests

# pytest --reruns 1 --html=./reports/report.html tests/job_seeker_and_employer/test_4_0_response_to_vacancy.py

job_title_vacancy = 'qa test отклик на вакансию'
job_title_resume = 'qa test отклик на вакансию'
resume_id = '1269'
vacancy_id = '1979'
user_employer = 'employer'
user_job_seeker = 'job_seeker'


# @pytest.mark.skip
class TestResponseToVacancy:
    def test_precondition(self, browser, language):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[user_employer]["id"])  # изменение языка уведомлений на email
        _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[user_job_seeker]["id"])  # изменение языка уведомлений на email

        admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
        admin_sql_page.open()
        admin_sql_page.sql_delete_record_response_to_vacancy(users_variables[user_job_seeker]["id"], resume_id, vacancy_id)  # удаление записи отклика на вакансию

    def test_response_to_vacancy(self, browser, language):  # отклик на вакансию
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.go_to_vacancies_page_through_header()  # переход на страницу вакансий через хедер

        vacancies_page = VacanciesPage(browser, browser.current_url)
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user_job_seeker)  # авторизация пользователя
        vacancies_page.search_vacancy_by_job_title(job_title_vacancy)  # поиск вакансии по названию
        vacancies_page.go_to_vacancy_page(vacancy_id)  # нажатие на блок вакансии для перехода на ее страницу

        vacancy_page = VacancyPage(browser, browser.current_url)
        vacancy_page.presence_of_button_responds_2()  # наличие кнопки "Откликнуться" # 2
        vacancy_page.pressing_button_responds_1()  # нажатие на кнопку "Откликнуться" # 1
        vacancy_page.filling_and_sending_response_with_selected_active_resume(resume_id)  # заполнение и отправка отклика с выбранным активным резюме
        vacancy_page.checking_confirmation_message_for_sending_resume_of_company(language)  # проверка сообщения о подтверждении отправки резюме компании
        vacancy_page.presence_of_buttons_resume_posted()  # наличие не активных кнопок "Резюме отправлено"
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_responses_page()  # переход на страницу "Мои отклики"

        my_responses_page = MyResponsesPage(browser, browser.current_url)
        my_responses_page.go_to_vacancy_page_of_response(vacancy_id)  # нажатие на блок вакансии отклика для перехода на ее страницу

        vacancy_page.checking_opening_of_page_of_published_vacancy(job_title_vacancy)  # проверка открытия страницы опубликованной вакансии
        vacancy_page.confirmation_opening_of_vacancy_page(language, vacancy_id)  # подтверждение открытия страницы вакансии

    def test_verification_of_letter_after_receiving_response_to_vacancy(self, browser, language):  # проверка письма после получения отклика на вакансию
        link = Accounts.url_email
        email_page = EmailPage(browser, link)
        email_page.open()
        # browser.maximize_window()
        email_page.email_authorization()  # авторизация email
        email_page.verification_of_letter_after_receiving_response_to_vacancy(language)  # проверка письма после получения отклика на вакансию


    def test_company_response_opening(self, browser, language):  # открытие отклика компанией
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user_employer)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"
        my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
        my_vacancies_page.checking_for_availability_icon_new_response_to_vacancy(vacancy_id)  # проверка наличия иконки нового отклика на вакансию
        my_vacancies_page.go_to_responses_to_vacancy_page(vacancy_id)  # переход на страницу 'Отклики на вакансию'

        responses_to_vacancy_page = ResponsesToVacancyPage(browser, browser.current_url)
        responses_to_vacancy_page.checking_for_unread_response_flag()  # проверка наличия метки не прочитанного отклика
        responses_to_vacancy_page.go_to_resume_page_of_response(resume_id)  # нажатие на резюме отклика для перехода на его страницу

        resume_page = ResumePage(browser, browser.current_url)
        resume_page.checking_opening_of_page_of_published_resume(job_title_resume)  # проверка открытия страницы опубликованного резюме после редактирования
        resume_page.confirmation_opening_of_resume_page(language, resume_id)  # подтверждение открытия страницы резюме
        resume_page.checking_cover_letter_text()  # проверка текста сопроводительного письма
        resume_page.checking_contact_display(contact_display_when_response_to_vacancy)  # проверка отображения контактов

    def test_verification_of_letter_after_viewing_response(self, browser, language):  # проверка письма после просмотра отклика
        link = Accounts.url_email
        email_page = EmailPage(browser, link)
        email_page.open()
        # browser.maximize_window()
        email_page.email_authorization()  # авторизация email
        email_page.verification_of_letter_after_viewing_response(language)  # проверка письма после просмотра отклика

    def test_deleting_response(self, browser, language):  # удаление отклика
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user_employer)  # авторизация пользователя

        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/vacancy/{vacancy_id}/feedback"
        responses_to_vacancy_page = ResponsesToVacancyPage(browser, url_page)
        responses_to_vacancy_page.open()
        responses_to_vacancy_page.deviation_of_response(resume_id, language)  # отклонение отклика
        page.logout()  # выход из учетной записи

        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user_job_seeker)  # авторизация пользователя
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/vacancy/feedback"
        my_responses_page = MyResponsesPage(browser, url_page)
        my_responses_page.open()

        status_in_response_block = None
        if language == "":
            status_in_response_block = 'Ваше резюме отклонено'
        elif language == "/ua":
            status_in_response_block = 'Ваше резюме відхилено'
        elif language == "/en":
            status_in_response_block = 'Your CV has been rejected'

        my_responses_page.checking_status_display_in_response_block(vacancy_id, status_in_response_block)  # проверка отображения статуса в блоке отклика
        my_responses_page.deleting_response(vacancy_id)  # удаление отклика

        page.logout()  # выход из учетной записи
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user_employer)  # авторизация пользователя

        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/vacancy/{vacancy_id}/feedback"
        responses_to_vacancy_page = ResponsesToVacancyPage(browser, url_page)
        responses_to_vacancy_page.open()
        responses_to_vacancy_page.check_for_absence_of_response_block(resume_id)  # проверка отсутствия блока отклика

    def test_verification_of_letter_after_response_deviation(self, browser, language):  # проверка письма после отклонения отклика
        link = Accounts.url_email
        email_page = EmailPage(browser, link)
        email_page.open()
        # browser.maximize_window()
        email_page.email_authorization()  # авторизация email
        email_page.verification_of_letter_after_response_deviation(language)  # проверка письма после отклонения отклика
