import pytest
from Page_Object_Model.configuration import UrlStartPage, UrlStartPageAdmin
from Page_Object_Model.pages.site.oll_page import OllPage
from Page_Object_Model.pages.site.company_edit_page import CompanyEditPage
from Page_Object_Model.pages.site.company_personal_cabinet_page import CompanyPersonalCabinetPage
from Page_Object_Model.pages.admin_panel.admin_page import AdminPage


@pytest.mark.s_r_c
def test_changing_all_company_data(browser, language):  # изменение всех данных компании
    url_page = f"{UrlStartPage.prefix}logincasino.work{UrlStartPage.suffix}{language}{UrlStartPage.suffix_page}"
    page = OllPage(browser, url_page)
    # browser.maximize_window()
    page.open()
    page.opening_pop_up_for_login()  # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации
    page.user_new_authorization(language, 'company')  # авторизация пользователя
    page.opening_authorized_user_menu()  # нажатие на кнопку для открытия меню авторизированного пользователя
    page.go_to_personal_cabinet_page()  # нажатие на кнопку для перехода на страницу личного кабинета

    company_personal_cabinet_page = CompanyPersonalCabinetPage(browser, browser.current_url)
    company_personal_cabinet_page.go_to_personal_data_page()  # переход на страницу "Личные данные"

    company_edit_page = CompanyEditPage(browser, browser.current_url)
    page.choice_of_russian_language_in_multi_language_forms()  # выбор русского языка в мультиязычных формах
    company_edit_page.hiding_copy_to_other_languages()  # скрытие кнопки "Скопировать на другие языки"
    company_edit_page.change_data_in_all_fields(language)  # изменение данных во всех полях

    company_edit_page.submitting_form_for_moderation_after_changing_data()  # отправка формы на модерацию после изменения данных
    company_edit_page.checking_message_after_saving_changes_to_personal_information(language)  # проверка сообщения после сохранения изменений личной информации

    admin_page = AdminPage(browser, UrlStartPageAdmin.url_page_admin)
    admin_page.open()
    admin_page.admin_authorization()
    admin_page.opening_dropdown_list_work()  # открытие выпадающего списка "Work"
    admin_page.go_to_users_page()  # переход на страницу пользователей
    admin_page.new_user_search_by_email(language, 'company')  # поиск пользователя по e-mail
    admin_page.check_that_user_has_status_data_editing()  # проверка что пользователь имеет статус "Редактирование данных"
