import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage

# pytest --reruns 1 --html=./reports/report.html -s tests/company/print_pdf/test_3_2_1_checking_status_of_page_response_to_print_pdf.py

user = 'employer'
vacancy_id = '1979'


# @pytest.mark.s_r_c
def test_checking_status_of_page_response_to_print_pdf(browser, language):  # проверка статуса ответа страницы 'распечатать пдф'
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

    resumes_page = ResumesPage(browser, browser.current_url)
    resumes_page.go_to_first_resume_page_in_list()  # нажатие на блок первого резюме в списке для перехода на его страницу

    resume_page = ResumePage(browser, browser.current_url)
    resume_page.checking_status_of_page_response_to_print_pdf()  # проверка статуса ответа страницы 'распечатать пдф'

    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.opening_vacancy_menu(vacancy_id)  # открытие меню вакансии
    my_vacancies_page.checking_status_of_page_response_to_print_pdf(vacancy_id)  # проверка статуса ответа страницы 'распечатать пдф'
