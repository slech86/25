import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.vacancies_page import VacanciesPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage

# pytest --reruns 1 --html=./reports/report.html -s tests/job_seeker/print_pdf/test_3_2_1_checking_status_of_page_response_to_print_pdf.py

user = 'job_seeker'


# @pytest.mark.s_r_c
# @pytest.mark.job_seeker
# @pytest.mark.skip
def test_checking_status_of_page_response_to_print_pdf(browser, language):  # проверка статуса ответа страницы 'распечатать пдф'
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.go_to_vacancies_page_through_header()  # переход на страницу вакансий через хедер

    vacancies_page = VacanciesPage(browser, browser.current_url)
    vacancies_page.go_to_first_vacancy_page_in_list()  # нажатие на блок первой вакансии в списке для перехода на ее страницу

    vacancy_page = VacancyPage(browser, browser.current_url)
    vacancy_page.checking_status_of_page_response_to_print_pdf()  # проверка статуса ответа страницы 'распечатать пдф'

    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
    job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

    my_resume_page = MyResumePage(browser, browser.current_url)
    my_resume_page.opening_resume_menu()  # открытие меню резюме
    my_resume_page.checking_status_of_page_response_to_print_pdf()  # проверка статуса ответа страницы 'распечатать пдф'
