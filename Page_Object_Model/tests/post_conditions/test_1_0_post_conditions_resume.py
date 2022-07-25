import pytest
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.data_for_testing import TestData


@pytest.fixture(scope="function", autouse=True)
def authorization_in_admin(browser):  # авторизация в админку
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу всех резюме


class TestPostConditionsResume:

    # @pytest.mark.s_r_c
    def test_complete_deletion_of_resume_1(self, browser):  # полное удаление первого резюме
        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title_after_editing()  # поиск резюме по названию должности после редактирования
        admin_resumes_page.complete_objects_deletion()  # полное удаление резюме

    def test_complete_deletion_of_resume_2(self, browser):  # полное удаление второго резюме
        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_2)  # поиск резюме по названию должности
        admin_resumes_page.complete_objects_deletion()  # полное удаление резюме

    def test_complete_deletion_of_resume_3(self, browser):  # полное удаление третьего резюме
        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_3)  # поиск резюме по названию должности
        admin_resumes_page.complete_objects_deletion()  # полное удаление резюме

    # def test_complete_deletion_of_draft_resume(self, browser):  # полное удаление черновика резюме
    #     admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    #     admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume_for_draft)  # поиск резюме по названию должности
    #     admin_resumes_page.complete_objects_deletion()  # полное удаление резюме
