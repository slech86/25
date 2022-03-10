from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.сonfiguration import UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage



# @pytest.mark.s_r_c
def test_complete_deletion_of_resume(browser):  # полное удаление резюме
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу всех резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title_after_editing()  # поиск резюме по названию должности после редактирования
    admin_resumes_page.complete_objects_deletion()  # полное удаление резюме
