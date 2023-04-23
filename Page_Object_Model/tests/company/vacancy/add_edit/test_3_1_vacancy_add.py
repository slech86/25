import time

import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_add_page import VacancyAddPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.users import Accounts
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.site.vacancy_preview_page import VacancyPreviewPage
from Page_Object_Model.tests.company.vacancy import _resources_vacancy
from Page_Object_Model.mail.onesec_api import Mailbox
from Page_Object_Model.tests import _resources_tests
from Page_Object_Model.users import users_variables

domain_sender_letter = _resources_tests.domain_sender_letter


def test_adding_vacancies(browser, language):  # добавление вакансии
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(_resources_vacancy.user_vacancy)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page = VacancyAddPage(browser, browser.current_url)
    page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
    add_vacancy_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    add_vacancy_page.filling_in_required_fields()  # заполнение обязательных полей

    browser.execute_script("window.scrollBy(0, -1000);")
    add_vacancy_page.filling_in_optional_fields()  # заполнение не обязательных полей
    add_vacancy_page.submitting_vacancy_for_publication()  # отправка вакансии на публикацию

    my_vacancies_page.waiting_for_my_vacancies_page_to_open(language)  # ожидание открытия страницы 'Мои вакансии'
    my_vacancies_page.confirmation_of_opening_of_page_my_vacancies(language)  # подтверждение открытия страницы 'Мои вакансии'
    my_vacancies_page.checking_message_confirming_of_creation_of_vacancy(language)  # проверка сообщения о создании новой вакансии

    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title(TestData.job_title_vacancy)  # поиск вакансии по названию должности

    singleton = Singleton()
    singleton.id_vacancies = admin_page.getting_vacancy_id()  # получение id вакансии
    admin_page.checking_that_vacancy_status_is_on_moderated()  # проверка что статус вакансии 'На модерацию'

    url_Vacancy_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/vacancy/{singleton.id_vacancies}"
    vacancy_page = VacancyPage(browser, url_Vacancy_Page)
    vacancy_page.open()
    vacancy_page.checking_opening_of_page_of_an_unpublished_vacancy(language)  # проверка открытия страницы не опубликованной вакансии

    admin_page.open()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title(TestData.job_title_vacancy)  # поиск вакансии по названию должности
    admin_page.go_to_object_editing_page()  # переход на страницу редактирования вакансии

    admin_vacancy_edit_page = AdminVacancyEditPage(browser, browser.current_url)
    admin_vacancy_edit_page.change_vacancy_status_to_published()  # изменение статуса вакансии на 'Опубликовано'

    admin_page.waiting_to_save_status_and_open_vacancies_page()  # ожидание сохранения статуса и открытия страницы вакансий

    url_Vacancy_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/vacancy/{singleton.id_vacancies}"
    vacancy_page = VacancyPage(browser, url_Vacancy_Page)
    vacancy_page.open()
    vacancy_page.checking_opening_of_page_of_published_vacancy(TestData.job_title_vacancy)  # проверка открытия страницы опубликованной вакансии

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page.absence_of_button_to_publish()  # проверка отсутствия кнопки "Опубликовать"

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)

    services_and_prices_page.checking_decrease_in_number_of_available_vacancies_for_publication_in_service_package()  # проверка уменьшения количества доступных вакансий для публикации в пакете услуг


# @pytest.mark.s_r_c
def test_verification_of_letter_after_publication_of_vacancy(browser, language):  # проверка письма после публикации вакансии
    # link = Accounts.url_email
    # email_page = EmailPage(browser, link)
    # email_page.open()
    # # browser.maximize_window()
    # email_page.email_authorization()  # авторизация email
    # email_page.verification_of_letter_after_publication_of_vacancy(language)  # проверка письма после публикации вакансии

    subject = None
    if language == "":
        subject = 'Ваша вакансия добавлена на сайт'
    elif language == "/ua":
        subject = 'Ваша вакансія вже на сайті'
    elif language == "/en":
        subject = 'Your vacancy is already on the site'

    expected_text = None
    if language == "":
        expected_text = 'Ваша вакансия ' + TestData.job_title_vacancy + ' добавлена на'
    elif language == "/ua":
        expected_text = 'Ваша вакансія ' + TestData.job_title_vacancy + ' вже на'
    elif language == "/en":
        expected_text = 'Your vacancy ' + TestData.job_title_vacancy + ' is already on'

    email = Mailbox(users_variables[_resources_vacancy.user_vacancy]['mail_name'])
    letter = _resources_tests.waiting_letter(email, domain_sender_letter, subject)  # ожидание письма
    _resources_tests.checking_content_of_letter(email, letter, expected_text)  # проверка содержания письма
