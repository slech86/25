import pytest
import time
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.users import Accounts
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.pages.site.interkassa_page import InterkassaPage
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.pages.admin_panel.admin_product_edit_page import AdminProductEditPage
from Page_Object_Model.tests.company.buying_packages import _resources_buying_packages
from Page_Object_Model.tests.company import _resources_company
from Page_Object_Model.tests import _resources_tests

# pytest --reruns 1 --html=./reports/report.html -s tests/company/buying_packages/test_3_0_2_package_purchase_standart_1_vacancy.py


# @pytest.mark.skip
# @pytest.mark.s_r_c
class TestPackagePurchaseStandart1Vacancy:
    def test_precondition(self, browser, language):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        _resources_company.sql_deleting_all_user_orders(browser)  # удаление всех заказов пользователя
        _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[_resources_buying_packages.user]["id"])  # изменение языка уведомлений на email

    def test_package_purchase_standart_and_orders_processing_and_activating_it_on_site(self, browser, language):  # покупка пакета "Standart: 1 вакансия" и проведение заказа в админке и активация его на сайте
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(_resources_buying_packages.user)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

        services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
        singleton = Singleton()
        singleton.id_product = services_and_prices_page.adding_to_cart_standart_1_vacancy_and_getting_product_id()  # добавление в корзину "Standart: 1 вакансия" и получение id продукта
        services_and_prices_page.click_button_buy_in_basket()  # нажатие кнопки "Курить" в корзине

        interkassa_page = InterkassaPage(browser, browser.current_url)
        interkassa_page.transition_to_test_payment_page()  # переход на страницу тестового платежа
        interkassa_page.create_cancel_test_payment()  # Создать отмененный тестовый платеж

        services_and_prices_page.checking_message_about_create_cancel_test_payment(language)  # проверка сообщения о создании отмененного тестового платежа

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_order_page()  # переход на страницу заказов
        admin_page.search_for_user_orders_by_email(users_variables[_resources_buying_packages.user]["mail"])  # поиск заказов пользователя по e-mail
        admin_page.order_processing()  # проведение заказа, изменение статуса заказа с "Новый" на "Проведенный"
        singleton = Singleton()
        singleton.id_order = admin_page.getting_last_order_id_of_user()  # получение последнего id заказа пользователя

        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_user_purchases_page()  # переход на страницу "Покупки пользователей"
        singleton.id_purchase = admin_page.getting_id_of_purchase(singleton.id_order)  # получение id покупки

        admin_product_edit_page = AdminProductEditPage(browser, UrlStartPageAdmin.url_page_admin + '/products/update?pk=1')
        admin_product_edit_page.open()
        status_checkbox_auto_activation = admin_product_edit_page.get_auto_activation_checkbox_status()  # получить статус чекбокса авто активации
        if status_checkbox_auto_activation is not None:
            url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}/prices"
            services_and_prices_page = ServicesAndPricesPage(browser, url_page)
            services_and_prices_page.open()
        if status_checkbox_auto_activation is None:
            url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
            page = OllPage(browser, url_page)
            # browser.maximize_window()
            page.open()
            page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
            page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

            company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
            company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

            services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
            services_and_prices_page.switch_to_tab_not_activated()  # переход на вкладку "Не активированные"
            services_and_prices_page.availability_of_product_in_not_activated_services()  # наличие "Standart: 1 вакансия" в не активированных услугах
            services_and_prices_page.product_activation()  # активация продукта
        services_and_prices_page.product_availability_in_activated_services()  # наличие "Standart: 1 вакансия" в активированных услугах

    def test_checking_letter_after_order_processing(self, browser, language):  # проверка письма после проведения заказа
        link = Accounts.url_email
        email_page = EmailPage(browser, link)
        email_page.open()
        # browser.maximize_window()
        email_page.email_authorization()  # авторизация email
        email_page.letter_after_order_processing(language)  # письмо после проведения заказа

    def test_complete_deletion_of_user_orders(self, browser, language):  # полное удаление заказов пользователя
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_order_page()  # переход на страницу заказов
        admin_page.search_for_user_orders_by_email(users_variables[_resources_buying_packages.user]["mail"])  # поиск заказов пользователя по e-mail
        admin_page.complete_objects_deletion()  # полное удаление объектов
