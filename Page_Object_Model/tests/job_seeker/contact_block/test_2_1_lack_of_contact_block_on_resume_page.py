import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.configuration import UrlStartPage

# pytest --reruns 1 --html=./reports/report.html tests/job_seeker/contact_block/test_2_1_lack_of_contact_block_on_resume_page.py

user = 'job_seeker'


# @pytest.mark.job_seeker
def test_checking_absence_of_block_of_contacts_with_an_authorized_applicant(browser, language):  # проверка отсутствия блока контактов при авторизации как соискатель
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

    resumes_page = ResumesPage(browser, browser.current_url)
    resumes_page.go_to_first_resume_page_in_list()  # нажатие на блок первого резюме в списке для перехода на его страницу

    resume_page = ResumePage(browser, browser.current_url)

    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(user)  # авторизация пользователя

    resume_page.checking_absence_of_contact_block_with_information()  # проверка отсутствия блока контактов c информацией
    resume_page.checking_absence_of_contact_block()  # проверка отсутствия блока контактов
