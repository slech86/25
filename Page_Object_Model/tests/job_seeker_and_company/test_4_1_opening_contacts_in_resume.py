import pytest
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.resumes_page import ResumesPage
from Page_Object_Model.pages.site.resume_page import ResumePage
from Page_Object_Model.сonfiguration import UrlStartPage
from Page_Object_Model.data_for_testing import TestData
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.site.services_and_prices_page import ServicesAndPricesPage
from Page_Object_Model.singleton import Singleton


class TestBlockOfContactsOnResumePage:
    # @pytest.mark.skip
    # @pytest.mark.s_r_c
    def test_block_of_contacts_on_resume_page(self, browser, language):  # блок контактов на странице резюме
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.go_to_resume_page_through_header()  # переход на страницу всех резюме через хедер

        resumes_page = ResumesPage(browser, browser.current_url)

        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.new_user_authorization(language, 1)  # авторизация пользователя

        resumes_page.search_resume_by_job_title(TestData.job_title_resume_2)  # поиск резюме по названию
        singleton = Singleton()
        resumes_page.go_to_resume_page(singleton.id_resume[1])  # нажатие на блок резюме для перехода на его страницу

        resume_page = ResumePage(browser, browser.current_url)
        resume_page.opening_contacts_in_resume()  # открытие контактов в резюме
        resume_page.checking_contact_display(TestData)  # проверка отображения контактов

    def test_checking_reduction_in_number_of_contact_views_in_service_package(self, browser, language):  # проверка уменьшения в пакете услуг количества просмотров контактов
        url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
        page = OllPage(browser, url_page)
        # browser.maximize_window()
        page.open()
        page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
        page.new_user_authorization(language, 1)  # авторизация пользователя
        page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
        page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

        company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
        company_personal_cabinet_page.go_to_services_and_prices_page()  # переход на страницу "Услуги и цены"

        services_and_prices_page = ServicesAndPricesPage(browser, browser.current_url)
        services_and_prices_page.checking_reduction_in_number_of_contact_views_in_service_package()  # проверка уменьшения в пакете услуг количества просмотров контактов
