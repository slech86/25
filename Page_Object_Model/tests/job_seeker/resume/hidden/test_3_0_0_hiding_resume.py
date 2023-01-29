import time
import pytest
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_page import ResumePage

user = 'job_seeker'
resume_name = 'qa test скрытие резюме'
resume_id = '1551'


@pytest.mark.s_r_c
class TestHidingResume:
    def test_precondition(self, browser):
        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        time.sleep(0.5)

        admin_resumes_page = AdminResumesPage(browser, UrlStartPageAdmin.url_page_admin + '/resume')
        admin_resumes_page.open()
        admin_resumes_page.resume_search_by_job_title(resume_name)  # поиск резюме по названию должности
        vacancy_status = admin_resumes_page.get_status_of_resume()  # получить статус резюме
        if vacancy_status == 'Опубликовано':
            pass
        else:
            admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме
            admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
            admin_resume_edit_page.change_resume_status_to_published()  # изменение статуса резюме на 'Опубликовано'
            admin_resumes_page.waiting_to_save_status_and_open_resume_page()  # ожидание сохранения статуса и открытия страницы всех рузюме

    def test_hiding_and_publication_resume(self, browser, language):  # скрытие и публикация резюме
        url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_Page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя
        my_resume_page = MyResumePage(browser, url_Page + '/resume/my')
        my_resume_page.open()
        my_resume_page.opening_resume_menu(resume_id)  # открытие меню резюме
        my_resume_page.hide_resume(resume_id)  # скрыть резюме
        my_resume_page.checking_status_display_is_hidden_in_resume_block(resume_id, language)  # проверка отображения статуса "Cкрыто" в блоке резюме

        url_resume_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{resume_id}"
        resume_page = ResumePage(browser, url_resume_page)
        resume_page.open()
        resume_page.checking_opening_of_resume_page_for_moderation(language)  # проверка открытия страницы резюме на модерации

        my_resume_page.open()
        my_resume_page.opening_resume_menu(resume_id)  # открытие меню резюме
        my_resume_page.publish_resume(resume_id)  # опубликовать резюме
        resume_page.open()
        resume_page.checking_opening_of_page_of_published_resume(resume_name)  # проверка открытия страницы опубликованного резюме
