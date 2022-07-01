import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.сonfiguration import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_edit_page import ResumeEditPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage


@pytest.mark.s_r_c
@pytest.mark.job_seeker
def test_editing_resume(browser, language):  # редактирование резюме
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    browser.refresh()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(language, 2)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
    job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

    my_resume_page = MyResumePage(browser, browser.current_url)
    my_resume_page.opening_resume_menu()  # открытие меню резюме
    my_resume_page.go_to_resume_editing_page()  # переход на страницу редактирования резюме

    resume_edit_page = ResumeEditPage(browser, browser.current_url)
    resume_edit_page.change_data_in_all_fields()  # изменение данных во всех полях
    resume_edit_page.percentage_check_of_resume_completion()  # проверка заполнения резюме в процентах
    resume_edit_page.checking_status_level_filling_resume(language)  # проверка статуса уровня заполнения резюме
    resume_edit_page.submitting_resume_change_for_publication()  # отправка изменений резюме на публикацию

    my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
    my_resume_page.confirmation_of_opening_of_page_my_resumes(language)  # подтверждение открытия страницы 'Мои резюме'
    my_resume_page.checking_message_confirming_submission_of_resume_for_moderation(language)  # проверка сообщения о подтверждении отправки резюме на модерацию

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title_after_editing()  # поиск резюме по названию должности после редактирования
    admin_resumes_page.checking_that_resume_status_is_on_moderated()  # проверка что статус резюме 'На модерацию'
    admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме

    admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
    admin_resume_edit_page.change_resume_status_to_published()  # изменение статуса резюме на 'Опубликовано'

    admin_resumes_page.waiting_to_save_status_and_open_resume_page()  # ожидание сохранения статуса и открытия страницы всех рузюме