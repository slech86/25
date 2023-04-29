import pytest
import time
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage
from Page_Object_Model.pages.email_page import EmailPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_add_page import ResumeAddPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.singleton import Singleton
from Page_Object_Model.users import Accounts
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.admin_panel.admin_sql_page import AdminSqlPage
from Page_Object_Model.users import users_variables
from Page_Object_Model.tests import _resources_tests
from Page_Object_Model.tests.job_seeker.resume import _resources_resume
from Page_Object_Model.mail.onesec_api import Mailbox

domain_sender_letter = _resources_tests.domain_sender_letter


@pytest.mark.job_seeker
# @pytest.mark.skip
class TestResumeAdd:
    def test_precondition(self, browser, language):
        _resources_tests.admin_authorization(browser)  # авторизация в админку
        _resources_tests.change_language_of_notifications_on_email(browser, language, users_variables[_resources_resume.user_resume]["id"])  # изменение языка уведомлений на email
        admin_sql_page = AdminSqlPage(browser, UrlStartPageAdmin.url_page_admin + '/developer/sql')
        admin_sql_page.open()
        admin_sql_page.sql_deleting_all_user_resume(users_variables[_resources_resume.user_resume]["id"])  # удаление всех резюме пользователя

    def test_adding_resume(self, browser, language):  # добавление резюме
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(_resources_resume.user_resume)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
        job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

        my_resume_page = MyResumePage(browser, browser.current_url)
        number_of_resumes_created = my_resume_page.obtaining_number_of_resumes_to_create()  # получение количества резюме для создания
        my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

        add_resume_page = ResumeAddPage(browser, browser.current_url)
        page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
        add_resume_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
        add_resume_page.filling_in_required_fields(TestData.job_title_resume)  # заполнение обязательных полей
        browser.execute_script("window.scrollBy(0, -4000);")
        add_resume_page.filling_in_optional_fields()  # заполнение не обязательных полей
        # add_resume_page.percentage_check_of_resume_completion()  # проверка заполнения резюме в процентах
        # add_resume_page.checking_status_level_filling_resume(language)  # проверка статуса уровня заполнения резюме
        add_resume_page.submitting_resume_for_publication()  # отправка резюме на публикацию

        my_resume_page.waiting_for_my_resumes_page_to_open(language)  # ожидание открытия страницы 'Мои резюме'
        my_resume_page.confirmation_of_opening_of_page_my_resumes(language)  # подтверждение открытия страницы 'Мои резюме'
        my_resume_page.checking_message_confirming_of_creation_of_resume(language)  # проверка сообщения о создании нового резюме
        my_resume_page.checking_number_of_resumes_to_create(number_of_resumes_created + 1)  # проверка уменьшения количества резюме для создания

        admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
        admin_page.open()
        admin_page.admin_authorization()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу резюме

        admin_resumes_page = AdminResumesPage(browser, browser.current_url)
        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume)  # поиск резюме по названию должности
        singleton = Singleton()
        singleton.id_resume.append(admin_resumes_page.getting_resume_id())  # получение id резюме
        admin_resumes_page.checking_that_resume_status_is_on_moderated()  # проверка что статус резюме 'На модерацию'

        url_resume_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{singleton.id_resume[0]}"
        resume_page = ResumePage(browser, url_resume_page)
        resume_page.open()
        resume_page.checking_opening_of_resume_page_for_moderation(language)  # проверка открытия страницы резюме на модерации

        admin_page.open()
        admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
        admin_page.go_to_resumes_page()  # переход на страницу всех резюме

        admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume)  # поиск резюме по названию должности
        admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме

        admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
        admin_resume_edit_page.change_resume_status_to_published()  # изменение статуса резюме на 'Опубликовано'

        admin_resumes_page.waiting_to_save_status_and_open_resume_page()  # ожидание сохранения статуса и открытия страницы всех рузюме

        url_resume_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}/resume/{singleton.id_resume[0]}"
        resume_page = ResumePage(browser, url_resume_page)
        resume_page.open()
        resume_page.checking_opening_of_page_of_published_resume(TestData.job_title_resume)  # проверка открытия страницы опубликованного резюме

    def test_verification_of_letter_after_publication_of_resume(self, browser, language):  # проверка письма после публикации резюме
        # link = Accounts.url_email
        # email_page = EmailPage(browser, link)
        # email_page.open()
        # # browser.maximize_window()
        # email_page.email_authorization()  # авторизация email
        # email_page.verification_of_letter_after_publication_of_resume(language)  # проверка письма после публикации резюме

        subject = None
        if language == "":
            subject = 'Ваше резюме опубликовано'
        elif language == "/ua":
            subject = 'Ваше резюме опубліковано'
        elif language == "/en":
            subject = 'Your resume is published on the site.'
        elif language == "/pl":
            subject = 'Your resume is published on the site.'

        expected_text = None
        if language == "":
            expected_text = 'Ваше резюме опубликовано на'
        elif language == "/ua":
            expected_text = 'Ваше резюме опубліковано на'
        elif language == "/en":
            expected_text = 'Your resume is published on the'
        elif language == "/pl":
            expected_text = 'Your resume is published on the'

        email = Mailbox(users_variables[_resources_resume.user_resume]['mail_name'])
        letter = _resources_tests.waiting_letter(email, domain_sender_letter, subject)  # ожидание письма
        _resources_tests.checking_content_of_letter(email, letter, expected_text)  # проверка содержания письма
