import time

import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.add_vacancy_page import AddVacancyPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.singleton import Singleton


@pytest.mark.s_r_c
def test_adding_vacancies(browser, language):  # добавление вакансии
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.go_to_add_vacancy_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page = AddVacancyPage(browser, browser.current_url)
    add_vacancy_page.filling_in_required_fields()  # заполнение обязательных полей
    browser.execute_script("window.scrollBy(0, -300);")
    add_vacancy_page.filling_in_optional_fields()  # заполнение не обязательных полей
    add_vacancy_page.submitting_vacancy_for_publication()  # отправка вакансии на публикацию

    my_vacancies_page.waiting_for_my_vacancies_page_to_open(language)  # ожидание открытия страницы 'Мои вакансии'
    my_vacancies_page.confirmation_of_opening_of_page_my_vacancies()  # подтверждение открытия страницы 'Мои вакансии'
    my_vacancies_page.checking_message_confirming_submission_of_vacancy_for_moderation()  # проверка сообщения о подтверждении отправки вакансии на модерацию

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title()  # поиск вакансии по названию должности
    id_vacancies = admin_page.getting_vacancy_id()  # получение id вакансии
    admin_page.checking_that_vacancy_status_is_on_moderated()  # проверка что статус вакансии 'На модерацию'

    url_Vacancy_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/vacancy/{id_vacancies}"
    vacancy_page = VacancyPage(browser, url_Vacancy_Page)
    vacancy_page.open()
    vacancy_page.checking_opening_of_page_of_an_unpublished_vacancy(language)  # проверка открытия страницы не опубликованной вакансии

    admin_page.open()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title()  # поиск вакансии по названию должности
    admin_page.go_to_object_editing_page()  # переход на страницу редактирования вакансии

    admin_vacancy_edit_page = AdminVacancyEditPage(browser, browser.current_url)
    admin_vacancy_edit_page.change_vacancy_status_to_published()  # изменение статуса вакансии на 'Опубликовано'

    admin_page.waiting_to_save_status_and_open_vacansies_page()  # ожидание сохранения статуса и открытия страницы вакансий

    url_Vacancy_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/vacancy/{id_vacancies}"
    vacancy_page = VacancyPage(browser, url_Vacancy_Page)
    vacancy_page.open()
    vacancy_page.checking_opening_of_page_of_published_vacancy()  # проверка открытия страницы опубликованной вакансии

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page.go_to_add_vacancy_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page.absence_of_button_to_publish()  # проверка отсутствия кнопки "Опубликовать"

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
    singleton = Singleton()

    services_and_prices_page.checking_decrease_in_number_of_available_vacancies_for_publication_in_monthly_free_vacancy_package(singleton.id_product, singleton.id_purchase)  # проверка уменьшения количества доступных вакансий для публикации в пакете "Ежемесячная бесплатная вакансия"


def test_verification_of_letter_after_publication_of_vacancy(browser, language):  # проверка письма после публикации вакансии
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email

    if language == "/ua":
        email_page.verification_of_letter_after_publication_of_vacancy_ua()  # проверка письма после публикации вакансии ua
    else:
        email_page.verification_of_letter_after_publication_of_vacancy_ru()  # проверка письма после публикации вакансии ru


# удаление пакета созданного в прошлом тесте
def test_complete_deletion_of_user_orders(browser, language):  # полное удаление заказов пользователя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_order_page()  # переход на страницу заказов

    if language == "/ua":
        admin_page.search_for_user_orders_by_email_ua()  # поиск заказов пользователя по e-mail ua
    else:
        admin_page.search_for_user_orders_by_email_ru()  # поиск заказов пользователя по e-mail ru

    admin_page.complete_objects_deletion()  # полное удаление объектов

