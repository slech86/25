import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_registration_page import CompanyRegistrationPage
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.company_preview_page import CompanyPreviewPage
from Page_Object_Model.data_for_testing import TestData

# pytest --reruns 1 --html=./reports/report.html -s tests/company/preview_company/test_3_3_0_preview_company_profile_when_registration.py


# @pytest.mark.s_r_c
# @pytest.mark.skip
class TestCompanyRegistration:
    @pytest.mark.s_r_c
    def test_preview_company_profile_when_registration(self, browser, language):  # предпросмотр профиля компании при регистрации
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        print(url_page)
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.go_to_company_registration_page()  # нажатие на кнопку для перехода на страницу регистрации работодателя

        company_registration_page = CompanyRegistrationPage(browser, browser.current_url)
        company_registration_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
        company_registration_page.filling_in_required_fields(language, 1)  # заполнение обязательных полей
        company_registration_page.go_to_preview_page()  # переход на страницу предпросмотра

        company_preview_page = CompanyPreviewPage(browser, browser.current_url)
        company_preview_page.checking_for_preview_page_to_open(TestData.company_name)  # проверка открытия страницы предпросмотра
