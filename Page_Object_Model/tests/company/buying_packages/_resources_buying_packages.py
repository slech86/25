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


def get_subject_letter(language):
    subject = None
    if language == "":
        subject = 'Оплата прошла успешно! Скорее размещайте вакансии на сайте!'
    elif language == "/ua":
        subject = 'Оплата пройшла успішно! Мерщій розміщуйте вакансії на сайті.'
    elif language == "/en":
        subject = 'The payment was successful! Hurry up to place vacancies on the website!'
    elif language == "/pl":
        subject = 'Płatność powiodła się! Proszę zamieszczać oferty pracy na stronie!'
    return subject


def get_expected_text_letter(language):
    expected_text = None
    if language == "":
        expected_text = 'Оплата прошла успешно. Чтобы продолжить работу, перейдите в личный кабинет на'
    elif language == "/ua":
        expected_text = 'Оплата пройшла успішно. Щоб продовжити роботу перейдіть в особистий кабінет на'
    elif language == "/en":
        expected_text = 'The payment was successful! Hurry up to place vacancies on the'
    elif language == "/pl":
        expected_text = 'Płatność powiodła się. Aby kontynuować pracę, przejdź do swojego'
    return expected_text
