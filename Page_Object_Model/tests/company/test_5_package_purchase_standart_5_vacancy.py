import time
import pytest
from Page_Object_Model.pages.oll_page import OllPage
from Page_Object_Model.pages.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_page import AdminPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.my_vacancies_page import MyVacanciesPage
from Page_Object_Model.pages.add_vacancy_page import AddVacancyPage

def test_package_purchase_standart_and_orders_processing_and_activating_it_on_site(browser, language):  # покупка пакета "Standart: 5 вакансия" и проведение заказа в админке и активация его на сайте
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
    id_product = services_and_prices_page.adding_to_cart_standart_5_vacancy_and_getting_product_id()  # добавление в корзину "Standart: 5 вакансия" и получение id продукта
    services_and_prices_page.click_button_buy_in_basket()  # нажатие кнопки "Курить" в корзине
    services_and_prices_page.verification_of_message_after_purchase()  # проверка сообщения после покупки

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page = MyVacanciesPage(browser, browser.current_url)
    my_vacancies_page.go_to_add_vacancy_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page = AddVacancyPage(browser, browser.current_url)
    add_vacancy_page.absence_of_button_to_publish()  # проверка отсутствия кнопки "Опубликовать"

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_order_page()  # переход на страницу заказов

    if language == "/ua":
        admin_page.search_for_user_orders_by_email_ua()  # поиск заказов пользователя по e-mail ua
    else:
        admin_page.search_for_user_orders_by_email_ru()  # поиск заказов пользователя по e-mail ru

    admin_page.order_processing()  # проведение заказа, изменение статуса заказа с "Новый" на "Проведенный"
    id_order = admin_page.getting_last_order_id_of_user()  # получение последнего id заказа пользователя

    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_user_purchases_page()  # переход на страницу "Покупки пользователей"
    id_purchase = admin_page.getting_id_of_purchase(id_order)  # получение id покупки

    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page.go_to_add_vacancy_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page.absence_of_button_to_publish()  # проверка отсутствия кнопки "Опубликовать"

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

    services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
    # services_and_prices_page.switch_to_tab_Not_activated()  # переход на вкладку "Не активированные"
    services_and_prices_page.availability_of_product_in_not_activated_services(id_product, id_purchase)  # наличие "Standart: 5 вакансия" в не активированных услугах
    services_and_prices_page.product_activation(id_purchase)  # активация продукта
    services_and_prices_page.product_availability_in_activated_services(id_product, id_purchase)  # наличие "Standart: 5 вакансия" в активированных услугах

    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page.go_to_my_vacancies_page()  # переход на страницу "Мои вакансии"

    my_vacancies_page.go_to_add_vacancy_page()  # переход на страницу "Добавить вакансию"

    add_vacancy_page.submitting_vacancy_for_publication()  # проверка наличия кнопки "Опубликовать"

def test_checking_letter_after_order_processing(browser, language):  # проверка письма после проведения заказа
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email

    if language == "/ua":
        email_page.letter_after_order_processing_ua()  # письмо после проведения заказа ua
    else:
        email_page.letter_after_order_processing_ru()  # письмо после проведения заказа ru

def test_complete_deletion_of_user_orders(browser, language):  # полное удаление заказов пользователя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_order_page()  # переход на страницу заказов

    if language == "/ua":
        admin_page.search_for_user_orders_by_email_ua()  # поиск заказов пользователя по e-mail ua
    else:
        admin_page.search_for_user_orders_by_email_ru()  # поиск заказов пользователя по e-mail ru

    admin_page.complete_objects_deletion()  # полное удаление объектов

