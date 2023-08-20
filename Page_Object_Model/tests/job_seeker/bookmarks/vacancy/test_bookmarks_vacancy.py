import pytest
import time
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.vacancies_page import VacanciesPage

# pytest --reruns 1 --html=./reports/report.html tests/job_seeker/bookmarks/vacancy/test_bookmarks_vacancy.py
user = 'job_seeker_resume'


@pytest.mark.job_seeker
# @pytest.mark.skip
class TestBookmarksVacancy:
    # def test_precondition(self, browser, language):
    #     _resources_tests.admin_authorization(browser)  # авторизация в админку
    def test_bookmarks_vacancy(self, browser, language):  # закладки вакансий
        url_page = f"{UrlStartPage.url_start_page}{language}/vacancy"
        vacancies_page = VacanciesPage(browser, url_page)
        vacancies_page.open()
        vacancies_page.add_vacancy_to_bookmarks(browser)  # добавить вакансию в закладки (первую в списке)
        page = OllPage(browser, browser.current_url)
        page.user_authorization(user)  # авторизация пользователя
        vacancies_page.go_to_first_vacancy_page_in_list()  # нажатие на блок первой вакансии в списке для перехода на ее страницу
        vacancies_page.add_vacancy_to_bookmarks(browser)  # добавить вакансию в закладки (первую в списке)

        breakpoint()
