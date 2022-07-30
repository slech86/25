import time

import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.сonfiguration import UrlStartPage


# @pytest.mark.skip
# @pytest.mark.s_r_c
def test_block_of_contacts_on_resume_page(browser, language):  # блок контактов на странице резюме
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

    resumes_page = ResumesPage(browser, browser.current_url)
    resumes_page.go_to_first_resume_page_in_list()  # нажатие на блок первого резюме в списке для перехода на его страницу

    resume_page = ResumePage(browser, browser.current_url)
    resume_page.checking_contact_block_before_authorization(language)  # проверка блока контактов до авторизации
    resume_page.checking_absence_of_contact_block()  # проверка отсутствия блока контактов

    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_authorization(language, 1)  # авторизация пользователя

    resume_page.checking_contact_block_before_buying_package_of_services(language)  # проверка блока контактов до покупки пакета услуг
    resume_page.checking_absence_of_contact_block()  # проверка отсутствия блока контактов
