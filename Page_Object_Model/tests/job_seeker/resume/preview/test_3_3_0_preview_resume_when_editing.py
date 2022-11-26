import time
import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_edit_page import ResumeEditPage
from Page_Object_Model.pages.site.resume_preview_page import ResumePreviewPage

# pytest --reruns 1 --html=./reports/report.html -s tests/job_seeker/resume/preview/test_3_3_0_preview_resume_when_editing.py

user = 'job_seeker'
resume_id = '1358'
resume_name = 'qa test предпросмотр резюме при редактировании'


@pytest.mark.s_r_c
@pytest.mark.job_seeker
# @pytest.mark.skip
def test_preview_resume_when_editing(browser, language):  # предпросмотр резюме при редактировании
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
    job_seeker_personal_cabinet_page.go_to_my_resume_page()  # переход на страницу "Мои резюме"

    my_resume_page = MyResumePage(browser, browser.current_url)
    my_resume_page.opening_resume_menu()  # открытие меню резюме
    my_resume_page.go_to_resume_editing_page(resume_id)  # переход на страницу редактирования резюме

    resume_edit_page = ResumeEditPage(browser, browser.current_url)
    resume_edit_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    resume_edit_page.go_to_preview_page()  # переход на страницу предпросмотра

    resume_preview_page = ResumePreviewPage(browser, browser.current_url)
    resume_preview_page.checking_for_preview_page_to_open(resume_name)  # проверка открытия страницы предпросмотра
