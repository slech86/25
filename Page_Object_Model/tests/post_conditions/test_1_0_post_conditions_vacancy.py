from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlPageAdmin


# @pytest.mark.s_r_c
def test_complete_deletion_of_vacancy(browser):  # полное удаление вакансии
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title_after_editing()  # поиск вакансии по названию должности после редактирования
    admin_page.complete_objects_deletion()  # полное удаление вакансии


# удаление пакета к которому была привязана вакансия
def test_complete_deletion_of_user_orders(browser, language):  # полное удаление заказов пользователя
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_order_page()  # переход на страницу заказов
    admin_page.search_for_user_orders_by_email(language, 1)  # поиск заказов пользователя по e-mail
    admin_page.complete_objects_deletion()  # полное удаление объектов

