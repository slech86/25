import time
import pytest
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage

# pytest --reruns 1 --html=./reports/report.html tests/company/vacancy/hidden

user = 'employer'
vacancy_name = 'qa test скрытие вакансии'
vacancy_id = '3519'


class TestHidingVacancy:
    def test_precondition(self, browser):
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        time.sleep(0.5)

        admin_vacancy_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin + '/vacancies')
        admin_vacancy_page.open()
        admin_vacancy_page.vacancy_search_by_job_title(vacancy_name)  # поиск вакансии по названию должности
        vacancy_status = admin_vacancy_page.get_status_of_vacancy()  # получить статус вакансии
        if vacancy_status == 'Опубликовано':
            pass
        else:
            admin_vacancy_page.go_to_object_editing_page()  # переход на страницу редактирования вакансии
            admin_vacancy_edit_page = AdminVacancyEditPage(browser, browser.current_url)
            admin_vacancy_edit_page.change_vacancy_status_to_published()  # изменение статуса вакансии на 'Опубликовано'
            admin_vacancy_page.waiting_to_save_status_and_open_vacancies_page()  # ожидание сохранения статуса и открытия страницы вакансий

    def test_hiding_and_publication_vacancy(self, browser, language):  # скрытие и публикация вакансии
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        my_vacancies_page = MyVacanciesPage(browser, url_Page + '/vacancy/my')
        my_vacancies_page.open()
        my_vacancies_page.opening_vacancy_menu(vacancy_id)  # открытие меню вакансии
        my_vacancies_page.hide_vacancy(vacancy_id)  # скрыть вакансию
        my_vacancies_page.checking_status_display_is_hidden_in_vacancy_block(vacancy_id, language)  # проверка отображения статуса "Cкрыто" в блоке вакансии

        url_vacancy_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/vacancy/{vacancy_id}"
        vacancy_page = VacancyPage(browser, url_vacancy_page)
        vacancy_page.open()
        vacancy_page.checking_opening_of_page_of_an_unpublished_vacancy(language)  # проверка открытия страницы не опубликованной вакансии

        my_vacancies_page.open()
        my_vacancies_page.opening_vacancy_menu(vacancy_id)  # открытие меню вакансии
        my_vacancies_page.publish_vacancy(vacancy_id)  # опубликовать вакансию
        vacancy_page.open()
        vacancy_page.checking_opening_of_page_of_published_vacancy(vacancy_name)  # проверка открытия страницы опубликованной вакансии
