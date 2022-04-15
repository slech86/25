import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_edit_page import VacancyEditPage
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage


@pytest.mark.s_r_c
def test_editing_vacancies(browser, language):  # редактирование вакансии
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    browser.refresh()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(language, 1)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.go_to_vacancy_editing_page()  # переход на страницу редактирования вакансии

    vacancy_edit_page = VacancyEditPage(browser, browser.current_url)
    vacancy_edit_page.change_data_in_all_fields()  # изменение данных во всех полях
    vacancy_edit_page.submitting_vacancy_change_for_publication()  # отправка изменений вакансии на публикацию
    my_vacancies_page.waiting_for_my_vacancies_page_to_open(language)  # ожидание открытия страницы 'Мои вакансии'
    my_vacancies_page.confirmation_of_opening_of_page_my_vacancies(language)  # подтверждение открытия страницы 'Мои вакансии'
    my_vacancies_page.checking_message_confirming_submission_of_vacancy_for_moderation(language)  # проверка сообщения о подтверждении отправки вакансии на модерацию

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title_after_editing()  # поиск вакансии по названию должности после редактирования
    admin_page.checking_that_vacancy_status_is_on_moderated()  # проверка что статус вакансии 'На модерацию'
    admin_page.go_to_object_editing_page()  # переход на страницу редактирования вакансии

    admin_vacancy_edit_page = AdminVacancyEditPage(browser, browser.current_url)
    admin_vacancy_edit_page.change_vacancy_status_to_published()  # изменение статуса вакансии на 'Опубликовано'

    admin_page.waiting_to_save_status_and_open_vacansies_page()  # ожидание сохранения статуса и открытия страницы вакансий


# # удаление пакета к которому была привязана вакансия
# def test_complete_deletion_of_user_orders(browser, language):  # полное удаление заказов пользователя
#     admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
#     admin_page.open()
#     admin_page.admin_authorization()
#     admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
#     admin_page.go_to_order_page()  # переход на страницу заказов
#     admin_page.search_for_user_orders_by_email(language, 1)  # поиск заказов пользователя по e-mail
#     admin_page.complete_objects_deletion()  # полное удаление объектов
