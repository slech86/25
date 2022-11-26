import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_edit_page import VacancyEditPage
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_vacancy_edit_page import AdminVacancyEditPage
from Page_Object_Model.data_for_testing import TestDataEditing
from Page_Object_Model.pages.site.vacancy_preview_page import VacancyPreviewPage
from Page_Object_Model.singleton import Singleton

# pytest --reruns 1 --html=./reports/report.html -s tests/company/vacancy/preview/test_3_3_0_preview_vacancy_when_creating.py

user = 'employer_vacancy'
vacancy_id = '1358'
vacancy_name = 'qa test предпросмотр резюме при редактировании'


@pytest.mark.s_r_c
def test_preview_vacancy_when_editing(browser, language):  # предпросмотр вакансии при редактировании
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
    singleton = Singleton()
    my_vacancies_page.opening_vacancy_menu(singleton.id_vacancies)  # открытие меню вакансии
    my_vacancies_page.go_to_vacancy_editing_page()  # переход на страницу редактирования вакансии

    vacancy_edit_page = VacancyEditPage(browser, browser.current_url)
    vacancy_edit_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    vacancy_edit_page.change_data_in_all_fields()  # изменение данных во всех полях
    vacancy_edit_page.go_to_preview_page()  # переход на страницу предпросмотра

    vacancy_preview_page = VacancyPreviewPage(browser, browser.current_url)
    vacancy_preview_page.checking_for_preview_page_to_open(TestDataEditing.job_title_vacancy)  # проверка открытия страницы предпросмотра

