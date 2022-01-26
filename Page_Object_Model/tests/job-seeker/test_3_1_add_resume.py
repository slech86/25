import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.data_for_testing import UrlStartPage, UrlPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.add_resume_page import AddResumePage
from Page_Object_Model.pages.site.resume_page import ResumePage


@pytest.mark.s_r_c
def test_adding_resume(browser, language):  # добавление резюме
    url_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_Page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization()  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
    job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

    my_resume_page = MyResumePage(browser, browser.current_url)
    my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

    add_resume_page = AddResumePage(browser, browser.current_url)
    add_resume_page.filling_in_required_fields()  # заполнение обязательных полей
    browser.execute_script("window.scrollBy(0, -4000);")
    add_resume_page.filling_in_optional_fields()  # заполнение не обязательных полей
    add_resume_page.submitting_resume_for_publication()  # отправка резюме на публикацию

    my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
    my_resume_page.confirmation_of_opening_of_page_my_resumes()  # подтверждение открытия страницы 'Мои резюме'
    my_resume_page.checking_message_confirming_submission_of_resume_for_moderation()  # проверка сообщения о подтверждении отправки резюме на модерацию

    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title()  # поиск резюме по названию должности
    id_resume = admin_resumes_page.getting_resume_id()  # получение id резюме
    admin_resumes_page.checking_that_resume_status_is_on_moderated()  # проверка что статус резюме 'На модерацию'

    url_Resume_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{id_resume}"
    resume_page = ResumePage(browser, url_Resume_Page)
    resume_page.open()
    resume_page.checking_opening_of_page_of_an_unpublished_resume(language)  # проверка открытия страницы не опубликованного резюме

    admin_page.open()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу всех резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title()  # поиск резюме по названию должности
    admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме

    admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
    admin_resume_edit_page.change_resume_status_to_published()  # изменение статуса резюме на 'Опубликовано'

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.waiting_to_save_status_and_open_resume_page()  # ожидание сохранения статуса и открытия страницы рузюме

    url_Resume_Page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{id_resume}"
    resume_page = ResumePage(browser, url_Resume_Page)
    resume_page.open()
    resume_page.checking_opening_of_page_of_published_resume()  # проверка открытия страницы опубликованного резюме

@pytest.mark.s_r_c
def test_verification_of_letter_after_publication_of_resume(browser, language):  # проверка письма после публикации резюме
    link = "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    email_page = EmailPage(browser, link)
    email_page.open()
    # browser.maximize_window()
    email_page.email_authorization()  # авторизация email
    email_page.verification_of_letter_after_publication_of_resume(language)  # проверка письма после публикации резюме


@pytest.mark.s_r_c
def test_complete_deletion_of_resume(browser):  # полное удаление резюме
    admin_page = AdminPage(browser, UrlPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_Work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу всех резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title()  # поиск резюме по названию должности
    admin_resumes_page.complete_objects_deletion()  # полное удаление резюме



