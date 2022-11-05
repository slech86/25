import pytest
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.site.vacancy_add_page import VacancyAddPage
from Page_Object_Model.singleton import Singleton


@pytest.mark.s_r_c
class TestPackagePurchaseHelpRefugeeWithHisWork:
    def test_package_purchase_help_refugee_with_his_work_and_activating_it_on_site(self, browser, language):  # покупка пакета "Помоги беженцу с работой" и активация его на сайте
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_new_authorization(language, 1)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

        services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
        singleton = Singleton()
        singleton.id_product = services_and_prices_page.adding_to_cart_help_refugee_with_his_work_and_getting_product_id()  # добавление в корзину "Помоги беженцу с работой" и получение id продукта
        services_and_prices_page.click_button_buy_in_basket()  # нажатие кнопки "Курить" в корзине
        services_and_prices_page.verification_of_message_after_purchase(language)  # проверка сообщения после покупки

        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

        my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
        my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

        add_vacancy_page = VacancyAddPage(browser, browser.current_url)
        add_vacancy_page.absence_of_button_to_publish()  # проверка отсутствия кнопки "Опубликовать"

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_order_page()  # переход на страницу заказов
        admin_page.search_for_user_orders_by_email(language, 1)  # поиск заказов пользователя по e-mail
        singleton = Singleton()
        singleton.id_order = admin_page.getting_last_order_id_of_user()  # получение последнего id заказа пользователя
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_user_purchases_page()  # переход на страницу "Покупки пользователей"
        singleton.id_purchase = admin_page.getting_id_of_purchase(singleton.id_order)  # получение id покупки

        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

        services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
        # services_and_prices_page.switch_to_tab_not_activated()  # переход на вкладку "Не активированные"
        services_and_prices_page.availability_of_product_in_not_activated_services()  # наличие "Помоги беженцу с работой" в не активированных услугах
        services_and_prices_page.product_activation()  # активация продукта
        services_and_prices_page.product_availability_in_activated_services()  # наличие "Помоги беженцу с работой" в активированных услугах

        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

        my_vacancies_page.go_to_vacancy_add_page()  # переход на страницу "Добавить вакансию"

        add_vacancy_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
        add_vacancy_page.submitting_vacancy_for_publication()  # проверка наличия кнопки "Опубликовать"


# закомментировано здесь чтоб в следующем тесте проверить создание вакансии, после чего там и происходит удаление этого пакета
# def test_complete_deletion_of_user_orders(browser, language):  # полное удаление заказов пользователя
#     admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
#     admin_page.open()
#     admin_page.admin_authorization()
#     admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
#     admin_page.go_to_order_page()  # переход на страницу заказов
#
#     if language == "/ua":
#         admin_page.search_for_user_orders_by_email_ua()  # поиск заказов пользователя по e-mail ua
#     else:
#         admin_page.search_for_user_orders_by_email_ru()  # поиск заказов пользователя по e-mail ru
#
#     admin_page.complete_objects_deletion()  # полное удаление объектов
