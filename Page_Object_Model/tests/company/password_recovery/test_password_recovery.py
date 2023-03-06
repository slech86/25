import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.pages.site.vacancies_page import VacanciesPage
from Page_Object_Model.pages.site.vacancy_page import VacancyPage
from Page_Object_Model.pages.site.my_responses_page import MyResponsesPage
from Page_Object_Model.pages.site.responses_to_vacancy_page import ResponsesToVacancyPage
from Page_Object_Model.data_for_testing import contact_display_when_response_to_vacancy
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.users import Accounts
from Page_Object_Model.pages.email_page import EmailPage

# pytest --reruns 1 --html=./reports/report.html -s tests/company/password_recovery

user = 'job_seeker_change_password'


@pytest.mark.s_r_c
# @pytest.mark.skip
class TestPasswordRecovery:
    # def test_precondition(self, browser):
    #     admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)

    def test_response_to_vacancy(self, browser, language):  # отклик на вакансию
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.clicking_on_button_forgot_password()  # нажатие на кнопку "Забыли пароль"
        page.submitting_password_recovery_request(language, user)  # отправка запроса на восстановление пароля

