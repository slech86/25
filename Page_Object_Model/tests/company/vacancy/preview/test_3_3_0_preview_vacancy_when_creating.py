import time

import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_add_page import VacancyAddPage
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.site.vacancy_preview_page import VacancyPreviewPage

# pytest --reruns 1 --html=./reports/report.html -s tests/company/vacancy/preview/test_3_3_0_preview_vacancy_when_creating.py

user = 'employer'


@pytest.mark.s_r_c
def test_preview_vacancy_when_creating(browser, language):  # предпросмотр вакансии при создании
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page = VacancyAddPage(browser, browser.current_url)
    add_vacancy_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    add_vacancy_page.filling_in_required_fields()  # заполнение обязательных полей
    add_vacancy_page.browser.execute_script("window.scrollBy(0, 2500);")
    add_vacancy_page.go_to_preview_page()  # переход на страницу предпросмотра

    vacancy_preview_page = VacancyPreviewPage(browser, browser.current_url)
    vacancy_preview_page.checking_for_preview_page_to_open(TestData.job_title_vacancy)  # проверка открытия страницы предпросмотра
