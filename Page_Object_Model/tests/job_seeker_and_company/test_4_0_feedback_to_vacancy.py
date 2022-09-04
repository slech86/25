import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.pages.site.vacancies_page import VacanciesPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.my_responses_page import MyResponsesPage
from Page_Object_Model.pages.site.responses_to_vacancy_page import ResponsesToVacancyPage
from Page_Object_Model.data_for_testing import TestDataEditing


@pytest.mark.s_r_c
# @pytest.mark.skip
class TestResponseToVacancy:
    def test_response_to_vacancy(self, browser, language):  # отклик на вакансию
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.go_to_vacancies_page_through_header()  # переход на страницу вакансий через хедер

        vacancies_page = VacanciesPage(browser, browser.current_url)
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.new_user_authorization(language, 2)  # авторизация пользователя
        vacancies_page.search_vacancy_by_job_title()  # поиск вакансии по названию
        vacancies_page.go_to_vacancy_page()  # нажатие на блок вакансии для перехода на ее страницу

        vacancy_page = VacancyPage(browser, browser.current_url)
        vacancy_page.presence_of_button_responds_2()  # наличие кнопки "Откликнуться" # 2
        vacancy_page.pressing_button_responds_1()  # нажатие на кнопку "Откликнуться" # 1
        vacancy_page.filling_and_sending_response_with_selected_active_resume()  # заполнение и отправка отклика с выбранным активным резюме
        vacancy_page.checking_confirmation_message_for_sending_resume_of_company(language)  # проверка сообщения о подтверждении отправки резюме компании
        vacancy_page.presence_of_buttons_resume_posted()  # наличие не активных кнопок "Резюме отправлено"
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_responses_page()  # переход на страницу "Мои отклики"

        my_responses_page = MyResponsesPage(browser, browser.current_url)
        my_responses_page.go_to_vacancy_page_of_response()  # нажатие на блок вакансии отклика для перехода на ее страницу

        vacancy_page.checking_opening_of_page_of_published_vacancy_after_editing()  # проверка открытия страницы опубликованной вакансии после редактирования
        vacancy_page.confirmation_opening_of_vacancy_page(language)  # подтверждение открытия страницы вакансии

    def test_company_response_opening(self, browser, language):  # открытие отклика компанией
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.new_user_authorization(language, 1)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"
        my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
        my_vacancies_page.checking_for_availability_icon_new_response_to_vacancy()  # проверка наличия иконки нового отклика на вакансию
        my_vacancies_page.go_to_responses_to_vacancy_page()  # переход на страницу 'Отклики на вакансию'

        responses_to_vacancy_page = ResponsesToVacancyPage(browser, browser.current_url)
        responses_to_vacancy_page.checking_for_unread_response_flag()  # проверка наличия метки не прочитанного отклика
        responses_to_vacancy_page.go_to_resume_page_of_response()  # нажатие резюме отклика для перехода на его страницу

        resume_page = ResumePage(browser, browser.current_url)
        resume_page.checking_opening_of_page_of_published_resume_after_editing()  # проверка открытия страницы опубликованного резюме после редактирования
        resume_page.confirmation_opening_of_resume_page(language)  # подтверждение открытия страницы резюме
        resume_page.checking_cover_letter_text()  # проверка текста сопроводительного письма
        resume_page.checking_contact_display(TestDataEditing)  # проверка отображения контактов
