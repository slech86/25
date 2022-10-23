import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.my_resume_page import MyResumePage
from Page_Object_Model.pages.site.resume_add_page import ResumeAddPage
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.site.resume_preview_page import ResumePreviewPage

# pytest --reruns 1 --html=./reports/report.html -s tests/job_seeker/resume/preview/test_3_3_0_preview_resume_when_creating.py

user = 'job_seeker'


@pytest.mark.job_seeker
# @pytest.mark.skip
class TestResumeAdd:
    @pytest.mark.s_r_c
    def test_adding_resume(self, browser, language):  # добавление резюме
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
        my_resume_page.go_to_add_resume_page()  # переход на страницу "Разместить резюме"

        add_resume_page = ResumeAddPage(browser, browser.current_url)
        add_resume_page.filling_in_required_fields(TestData.job_title_resume_preview)  # заполнение обязательных полей
        add_resume_page.go_to_preview_page()  # переход на страницу предпросмотра

        resume_preview_page = ResumePreviewPage(browser, browser.current_url)
        resume_preview_page.checking_for_preview_page_to_open(TestData.job_title_resume_preview)  # проверка открытия страницы предпросмотра
