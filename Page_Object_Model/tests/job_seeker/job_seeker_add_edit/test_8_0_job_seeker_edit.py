import pytest
from Page_Object_Model.configuration import UrlStartPage
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.job_seeker_edit_page import JobSeekerEditPage
from Page_Object_Model.pages.site.job_seeker_personal_cabinet_page import JobSeekerPersonalCabinetPage
from Page_Object_Model.tests.job_seeker.job_seeker_add_edit import _resources_job_seeker_add_edit


# @pytest.mark.s_r_c
@pytest.mark.job_seeker
def test_changing_all_job_seeker_data(browser, language):  # изменение всех данных соискателя
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_new_authorization(_resources_job_seeker_add_edit.user)  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    job_seeker_personal_cabinet_page = JobSeekerPersonalCabinetPage(browser, browser.current_url)
    job_seeker_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

    job_seeker_edit_page = JobSeekerEditPage(browser, browser.current_url)
    page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
    job_seeker_edit_page.change_data_in_all_fields(language)  # изменение данных во всех полях
    job_seeker_edit_page.saving_data_after_modification()  # сохранение данных после изменений
    job_seeker_edit_page.checking_message_after_saving_changes_to_personal_information(language)  # проверка сообщения после сохранения изменений личной информации