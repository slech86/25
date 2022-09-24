import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.сonfiguration import UrlStartPage

# тест зависим от "opening_contacts_in_resume"

user = 'employer'
resume_name = 'qa test проверка контактного блока после использования возможности открывать контакты'
resume_id = '1268'


class TestContactBlockAfterEndOfViews:
    # @pytest.mark.skip
    # @pytest.mark.s_r_c
    def test_verification_of_contact_block_after_end_of_views(self, browser, language):  # проверка контактного блока после использования возможности открывать контакты
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

        resumes_page = ResumesPage(browser, browser.current_url)

        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.user_authorization(user)  # авторизация пользователя

        resumes_page.search_resume_by_job_title(resume_name)  # поиск резюме по названию
        resumes_page.go_to_resume_page(resume_id)  # нажатие на блок резюме для перехода на его страницу

        resume_page = ResumePage(browser, browser.current_url)
        resume_page.checking_message_about_using_ability_to_open_contacts(language)  # проверка сообщения о использовании возможности открывать контакты
