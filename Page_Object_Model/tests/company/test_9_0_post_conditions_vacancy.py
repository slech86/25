from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin


def test_complete_deletion_of_vacancy(browser):  # полное удаление вакансии
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_vacancies_page()  # переход на страницу вакансий
    admin_page.vacancy_search_by_job_title()  # поиск вакансии по названию должности
    admin_page.complete_objects_deletion()  # полное удаление вакансии