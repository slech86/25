import pytest
import time
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_product_edit_page import AdminProductEditPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.interkassa_page import InterkassaPage
from Page_Object_Model.pages.site.vacancy_add_page import VacancyAddPage
from Page_Object_Model.users import Accounts
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables


user = 'employer_vacancy'


def sql_deleting_all_user_orders(browser):  # удаление всех заказов пользователя
    admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
    admin_sql_page.open()
    admin_sql_page.sql_deleting_all_user_orders(users_variables[user]["id"])  # удаление всех заказов пользователя
    return admin_sql_page
