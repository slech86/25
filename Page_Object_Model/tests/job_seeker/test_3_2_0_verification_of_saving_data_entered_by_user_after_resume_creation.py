import pytest
from Page_Object_Model.сonfiguration import UrlStartPageAdmin
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage
from Page_Object_Model.pages.admin_panel.admin_resumes_page import AdminResumesPage
from Page_Object_Model.pages.admin_panel.admin_resume_edit_page import AdminResumeEditPage
from Page_Object_Model.pages.admin_panel.admin_currency_rates_page import AdminCurrencyRatesPage
from Page_Object_Model.data_for_testing import TestData


@pytest.mark.s_r_c
# @pytest.mark.job_seeker
# @pytest.mark.skip
def test_verification_of_saving_data_entered_by_user_after_resume_creation(browser, language):  # проверка сохранения введенных пользователем данных после создания резюме
    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()

    admin_page.opening_dropdown_list_reference_books()  # открытие выпадающего списка "Справочники"
    admin_page.go_to_currency_rates_page()  # переход на страницу курса валют

    admin_currency_rates_page = AdminCurrencyRatesPage(browser, browser.current_url)
    exchange_rates = admin_currency_rates_page.getting_exchange_rates()  # получение курсов валют

    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_resumes_page()  # переход на страницу резюме

    admin_resumes_page = AdminResumesPage(browser, browser.current_url)
    admin_resumes_page.resume_search_by_job_title(TestData.job_title_resume)  # поиск резюме по названию должности
    admin_resumes_page.go_to_object_editing_page()  # переход на страницу редактирования резюме

    admin_resume_edit_page = AdminResumeEditPage(browser, browser.current_url)
    admin_resume_edit_page.verification_of_saving_data_entered_by_user_after_resume_creation_ru(language, exchange_rates[1], 2)  # проверка сохранения введенных пользователем данных после создания резюме RU
