import pytest
import time
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.сonfiguration import UrlStartPage
from Page_Object_Model.data_for_testing import contact_display
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.сonfiguration import UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables

# pytest --reruns 1 --html=./reports/report.html -s tests/job_seeker_and_employer/test_4_1_opening_contacts_in_resume.py

user = 'employer'
purchase_id = '850'
# order_id = '806'
resume_id = '1267'
resume_name = 'qa test проверка открытия контактов в резюме'
product_id = '30'


class TestBlockOfContactsOnResumePage:
    # @pytest.mark.skip
    # @pytest.mark.s_r_c
    def test_precondition(self, browser):  # блок контактов на странице резюме
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        time.sleep(0.5)

        admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
        admin_sql_page.open()
        admin_sql_page.sql_change_number_of_contact_views_per_day(purchase_id)  # изменение количества просмотров контактов в день
        admin_sql_page.sql_delete_record_opening_contacts(users_variables[user]["id"], resume_id)  # удаление записи о открытии контакта

    def test_block_of_contacts_on_resume_page(self, browser, language):  # блок контактов на странице резюме
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

        resumes_page = ResumesPage(browser, browser.current_url)

        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя

        resumes_page.search_resume_by_job_title(resume_name)  # поиск резюме по названию
        resumes_page.go_to_resume_page(resume_id)  # нажатие на блок резюме для перехода на его страницу

        resume_page = ResumePage(browser, browser.current_url)
        resume_page.opening_contacts_in_resume()  # открытие контактов в резюме
        resume_page.new_checking_contact_display(contact_display)  # проверка отображения контактов

    def test_checking_reduction_in_number_of_contact_views_in_service_package(self, browser, language):  # проверка уменьшения в пакете услуг количества просмотров контактов
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

        services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
        services_and_prices_page.checking_reduction_in_number_of_contact_views_in_service_package(product_id, purchase_id)  # проверка уменьшения в пакете услуг количества просмотров контактов
