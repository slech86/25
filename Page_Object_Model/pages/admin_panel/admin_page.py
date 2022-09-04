from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminPageLocators
from Page_Object_Model.data_for_testing import TestData, TestDataEditing
from Page_Object_Model.users import Accounts
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_Object_Model.singleton import Singleton
import random
import time


class AdminPage(BasePage):
    def admin_authorization(self):  # авторизация админки
        self.browser.find_element(*AdminPageLocators.FIELD_LOGIN).send_keys(Accounts.main_login_admin)
        self.browser.find_element(*AdminPageLocators.FIELD_PASSWORD).send_keys(Accounts.main_password_admin)
        self.browser.find_element(*AdminPageLocators.BUTTON_LOG_IN).click()
    # авторизация админки

    def opening_dropdown_list_reference_books(self):  # открытие выпадающего списка "Справочники"
        self.browser.find_element(*AdminPageLocators.DROPDOWN_REFERENCE_BOOKS).click()

    def go_to_currency_rates_page(self):  # переход на страницу курса валют
        self.browser.find_element(*AdminPageLocators.CURRENCY_RATES).click()

    def opening_dropdown_list_work(self):  # открытие выпадающего списка "Work"
        self.browser.find_element(*AdminPageLocators.DROPDOWN_WORK).click()

    def go_to_users_page(self):  # переход на страницу пользователей
        self.browser.find_element(*AdminPageLocators.USERS).click()

    def go_to_vacancies_page(self):  # переход на страницу вакансий
        self.browser.find_element(*AdminPageLocators.VACANCIES).click()

    def go_to_resumes_page(self):  # переход на страницу всех резюме
        self.browser.find_element(*AdminPageLocators.RESUMES).click()

    def go_to_order_page(self):  # переход на страницу заказов
        self.browser.find_element(*AdminPageLocators.ORDERS).click()

    def go_to_user_purchases_page(self):  # переход на страницу "Покупки пользователей"
        self.browser.find_element(*AdminPageLocators.USER_PURCHASES).click()
    # шапка

    def complete_objects_deletion(self):  # полное удаление объектов (кроме пользователя)
        element_to_hover_over = self.browser.find_element(*AdminPageLocators.BUTTON_OBJECT_MENU)
        ActionChains(self.browser).move_to_element(element_to_hover_over).perform()
        self.browser.find_element(*AdminPageLocators.BUTTON_COMPLETE_OBJECT_DELETED).click()
        self.browser.find_element(*AdminPageLocators.BUTTON_OBJECT_DELETE_CONFIRMATION).click()
        assert self.is_element_present(*AdminPageLocators.ALERT_CONFIRMATION_OF_OBJECT_DELETION), 'Нет сообщения о удалении объекта'

    def go_to_object_editing_page(self):  # переход на страницу редактирования объекта
        self.browser.find_element(*AdminPageLocators.BUTTON_OBJECT_MENU).click()  # костыль из-за ховер эффекта на кнопке меню пользователя
    # общие

    def search_user_by_email(self, language, key):  # поиск пользователя по e-mail
        user_email_locators = AdminPageLocators()
        locator = user_email_locators.assembly_of_locators_with_email(key)
        email, user_email = None, None
        if language == "/ua":
            email = Singleton.logins_and_mails[key][1][1]
            user_email = locator[1]
        elif language == "":
            email = Singleton.logins_and_mails[key][0][1]
            user_email = locator[0]
        elif language == "/en":
            email = Singleton.logins_and_mails[key][2][1]
            user_email = locator[2]
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH).send_keys(email, Keys.ENTER)
        time.sleep(2)
        assert self.is_element_present(*user_email), 'Пользователь не найден'

    def checking_that_newly_created_user_has_status_disabled(self):  # проверка что новосозданный пользователь имеет статус "Отключено"
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Отключен', 'Статус не "Отключен"'

    def changing_user_status_to_deleted(self):  # изменение статуса пользователя на "Удалено"
        self.browser.find_element(*AdminPageLocators.FIELD_USER_STATUS).click()
        self.browser.find_element(*AdminPageLocators.STATUS_USER_DELETE).click()
        time.sleep(1)

    def check_that_user_has_status_active(self):  # проверка что пользователь имеет статус "Активен"
        self.browser.refresh()
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Активен', 'Статус не "Активен"'

    def check_that_user_has_status_delete(self):  # проверка что пользователь имеет статус "Удалено"
        self.browser.refresh()
        status = self.browser.find_element(*AdminPageLocators.USER_STATUS).text
        assert status == 'Удалено', 'Статус не "Удалено"'
    # страница пользователей

    # страница пользователя
    def change_of_user_status_from_on_moderation_to_active(self):  # изменение статуса пользователя с "На модерации" на "Активен"
        status = self.browser.find_element(*AdminPageLocators.FIELD_USER_STATUS).text
        assert status == 'На модерации', 'Статус не "На модерации"'
        self.browser.find_element(*AdminPageLocators.FIELD_USER_STATUS).click()
        self.browser.find_element(*AdminPageLocators.STATUS_USER_ACTIVE).click()
        time.sleep(1)

    def changing_role_from_user_to_super_admin(self):  # изменение роли с "User" на "SuperAdmin"
        self.browser.find_element(*AdminPageLocators.FIELD_WITH_ROLE_USER).click()
        self.browser.find_element(*AdminPageLocators.ROLE_SUPER_ADMIN).click()

    def adding_unique_values_to_login_and_email_fields(self):  # внесение в поля "Login" и "Электронный адрес" уникальные значения
        self.browser.find_element(*AdminPageLocators.FIELD_USER_LOGIN).send_keys(str(random.random()))
        field_user_email = self.browser.find_element(*AdminPageLocators.FIELD_USER_EMAIL)
        field_user_email.clear()
        field_user_email.send_keys(TestData.time_Now + '@test.com' + str(random.random()))

    def saving_user_card(self):  # сохранение карточки пользователя
        self.browser.find_element(*AdminPageLocators.BUTTON_SAVE).click()

    def waiting_to_save_status_and_open_users_page(self):  # ожидание сохранения статуса и открытия страницы всех пользователей
        WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((AdminPageLocators.H1_USERS), 'Пользователи'))

    def verification_of_saving_data_entered_by_user_after_company_registration_ru(self, language, key):  # проверка сохранения введенных пользователем данных после регистрации компании RU
        login = self.browser.find_element(*AdminPageLocators.FIELD_USER_LOGIN)
        login_value = login.get_attribute("value")
        if language == "/ua":
            assert login_value == Singleton.logins_and_mails[key][1][0], "Поле 'Логин' не верно"
        elif language == "":
            assert login_value == Singleton.logins_and_mails[key][0][0], "Поле 'Логин' не верно"
        elif language == "/en":
            assert login_value == Singleton.logins_and_mails[key][2][0], "Поле 'Логин' не верно"

        email = self.browser.find_element(*AdminPageLocators.FIELD_USER_EMAIL)
        email_value = email.get_attribute("value")
        if language == "/ua":
            assert email_value == Singleton.logins_and_mails[key][1][1], "Поле 'Email' не верно"
        elif language == "":
            assert email_value == Singleton.logins_and_mails[key][0][1], "Поле 'Email' не верно"
        elif language == "/en":
            assert email_value == Singleton.logins_and_mails[key][2][1], "Поле 'Email' не верно"

        email_language = self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_LANGUAGE)
        email_language_title = email_language.get_attribute("title")
        if language == "/ua":
            assert email_language_title == TestData.email_language_ua, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "":
            assert email_language_title == TestData.email_language_ru, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "/en":
            assert email_language_title == TestData.email_language_en, "Поле 'Язык уведомлений на e-mail' не верно"

        slug = self.browser.find_element(*AdminPageLocators.FIELD_SLUG)
        slug_value = slug.get_attribute("value")
        assert slug_value == TestData.company_slug, "Поле 'Slug' не верно"

        name = self.browser.find_element(*AdminPageLocators.FIELD_NAME)
        name_value = name.get_attribute("value")
        assert name_value == TestData.name, "Поле 'Имя' не верно"

        surname = self.browser.find_element(*AdminPageLocators.FIELD_SURNAME)
        surname_value = surname.get_attribute("value")
        assert surname_value == TestData.surname, "Поле 'Фамилия' не верно"

        company_name = self.browser.find_element(*AdminPageLocators.FIELD_COMPANY_NAME)
        company_name_value = company_name.get_attribute("value")
        assert company_name_value == TestData.company_name, "Поле 'Название компании' не верно"

        date_of_company_foundation = self.browser.find_element(*AdminPageLocators.FIELD_DATE_OF_COMPANY_FOUNDATION)
        date_of_company_foundation_value = date_of_company_foundation.get_attribute("value")
        assert date_of_company_foundation_value == TestData.date_of_company_foundation, "Поле 'Дата основания компании' не верно"

        position = self.browser.find_element(*AdminPageLocators.FIELD_POSITION)
        position_value = position.get_attribute("value")
        assert position_value == TestData.position, "Поле 'Должность' не верно"

        phone = self.browser.find_element(*AdminPageLocators.FIELD_PHONE)
        phone_value = phone.get_attribute("value")
        assert phone_value == TestData.phone, "Поле 'Телефон' не верно"

        contact_email = self.browser.find_element(*AdminPageLocators.FIELD_CONTACT_EMAIL)
        contact_email_value = contact_email.get_attribute("value")
        assert contact_email_value == TestData.contact_email, "Поле 'E-mail компании' не верно"

        skype = self.browser.find_element(*AdminPageLocators.FIELD_SKYPE)
        skype_value = skype.get_attribute("value")
        assert skype_value == TestData.skype, "Поле 'Skype' не верно"

        code_company = self.browser.find_element(*AdminPageLocators.FIELD_CODE_COMPANY)
        code_company_value = code_company.get_attribute("value")
        assert code_company_value == TestData.code_company, "Поле 'Код ЕДРПОУ' не верно"

        company_site = self.browser.find_element(*AdminPageLocators.FIELD_COMPANY_SITE)
        company_site_value = company_site.get_attribute("value")
        assert company_site_value == TestData.company_site, "Поле 'Сайт компании' не верно"

        facebook = self.browser.find_element(*AdminPageLocators.FIELD_FACEBOOK)
        facebook_value = facebook.get_attribute("value")
        assert facebook_value == TestData.facebook, "Поле 'Facebook' не верно"

        linkedin = self.browser.find_element(*AdminPageLocators.FIELD_LINKEDIN)
        linkedin_value = linkedin.get_attribute("value")
        assert linkedin_value == TestData.linkedin, "Поле 'Linkedin' не верно"

        instagram = self.browser.find_element(*AdminPageLocators.FIELD_INSTAGRAM)
        instagram_value = instagram.get_attribute("value")
        assert instagram_value == TestData.instagram, "Поле 'Instagram' не верно"

        telegram = self.browser.find_element(*AdminPageLocators.FIELD_TELEGRAM)
        telegram_value = telegram.get_attribute("value")
        assert telegram_value == TestData.telegram, "Поле 'Telegram' не верно"

        twitter = self.browser.find_element(*AdminPageLocators.FIELD_TWITTER)
        twitter_value = twitter.get_attribute("value")
        assert twitter_value == TestData.twitter, "Поле 'Twitter' не верно"

        vk = self.browser.find_element(*AdminPageLocators.FIELD_VK)
        vk_value = vk.get_attribute("value")
        assert vk_value == TestData.vk, "Поле 'VK' не верно"

        company_activity = self.browser.find_element(*AdminPageLocators.FIELD_COMPANY_ACTIVITY)
        company_activity_title = company_activity.get_attribute("title")
        assert company_activity_title == TestData.company_activity, "Поле 'Сфера деятельности компании' не верно"

        number_of_company_employees = self.browser.find_element(*AdminPageLocators.FIELD_NUMBER_OF_COMPANY_EMPLOYEES)
        number_of_company_employees_title = number_of_company_employees.get_attribute("title")
        assert number_of_company_employees_title == TestData.number_of_company_employees, "Поле 'Количество сотрудников' не верно"

        iframe = self.browser.find_element(*AdminPageLocators.IFRAME_CKEDITOR_COMPANY_DESCRIPTION_RU)
        self.browser.switch_to.frame(iframe)  # вход в фрейм
        CKEditor = self.browser.find_element(*AdminPageLocators.CKEDITOR_COMPANY_DESCRIPTION_RU).text
        assert CKEditor == TestData.ckeditor_company_description, "Поле 'Описание компании' не верно"
        self.browser.switch_to.default_content()  # выход из фрейма

        video_1 = self.browser.find_element(*AdminPageLocators.FIELD_VIDEO_1)
        video_1_value = video_1.get_attribute("value")
        assert video_1_value == 'https://www.youtube.com/embed/6OBg9Iz7dD0', "Поле 'Youtube 1' не верно"

        video_2 = self.browser.find_element(*AdminPageLocators.FIELD_VIDEO_2)
        video_2_value = video_2.get_attribute("value")
        assert video_2_value == 'https://www.youtube.com/embed/ZsMKc7EecNs', "Поле 'Youtube 2' не верно"

        video_3 = self.browser.find_element(*AdminPageLocators.FIELD_VIDEO_3)
        video_3_value = video_3.get_attribute("value")
        assert video_3_value == 'https://www.youtube.com/embed/kCunPyM8AQ0', "Поле 'Youtube 3' не верно"

        country = self.browser.find_element(*AdminPageLocators.FIELD_COUNTRY)
        country_title = country.get_attribute("title")
        assert country_title == TestData.country, "Поле 'Страна' не верно"

        WebDriverWait(self.browser, 6).until(EC.text_to_be_present_in_element((AdminPageLocators.FIELD_CITY), TestData.city))
        city = self.browser.find_element(*AdminPageLocators.FIELD_CITY)
        city_title = city.get_attribute("title")
        assert city_title == TestData.city, "Поле 'Город' не верно"

        street = self.browser.find_element(*AdminPageLocators.FIELD_STREET)
        street_value = street.get_attribute("value")
        assert street_value == TestData.street, "Поле 'Улица' не верно"

        checkbox_get_news = self.browser.find_element(*AdminPageLocators.CHECKBOX_GET_NEWS)
        checkbox_get_news_checked = checkbox_get_news.get_attribute("checked")
        assert checkbox_get_news_checked is not None, "Не установлено получение новостей"

    def verification_of_saving_data_entered_by_user_after_job_seeker_registration_ru(self, language, key):  # проверка сохранения введенных пользователем данных после регистрации соискателя RU
        login = self.browser.find_element(*AdminPageLocators.FIELD_USER_LOGIN)
        login_value = login.get_attribute("value")
        if language == "/ua":
            assert login_value == Singleton.logins_and_mails[key][1][0], "Поле 'Логин' не верно"
        elif language == "":
            assert login_value == Singleton.logins_and_mails[key][0][0], "Поле 'Логин' не верно"
        elif language == "/en":
            assert login_value == Singleton.logins_and_mails[key][2][0], "Поле 'Логин' не верно"

        email = self.browser.find_element(*AdminPageLocators.FIELD_USER_EMAIL)
        email_value = email.get_attribute("value")
        if language == "/ua":
            assert email_value == Singleton.logins_and_mails[key][1][1], "Поле 'Email' не верно"
        elif language == "":
            assert email_value == Singleton.logins_and_mails[key][0][1], "Поле 'Email' не верно"
        elif language == "/en":
            assert email_value == Singleton.logins_and_mails[key][2][1], "Поле 'Email' не верно"

        email_language = self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_LANGUAGE)
        email_language_title = email_language.get_attribute("title")
        if language == "/ua":
            assert email_language_title == TestData.email_language_ua, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "":
            assert email_language_title == TestData.email_language_ru, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "/en":
            assert email_language_title == TestData.email_language_en, "Поле 'Язык уведомлений на e-mail' не верно"

        self.verification_of_saving_data_entered_job_seeker(TestData)

    def verification_of_saving_data_entered_by_user_after_job_seeker_edit_ru(self, language):  # проверка сохранения введенных пользователем данных после редактирования соискателя RU
        email_language = self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_LANGUAGE)
        email_language_title = email_language.get_attribute("title")
        if language == "/ua":
            assert email_language_title == TestDataEditing.email_language_ru, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "":
            assert email_language_title == TestDataEditing.email_language_en, "Поле 'Язык уведомлений на e-mail' не верно"
        elif language == "/en":
            assert email_language_title == TestDataEditing.email_language_ua, "Поле 'Язык уведомлений на e-mail' не верно"

        self.verification_of_saving_data_entered_job_seeker(TestDataEditing)

    def verification_of_saving_data_entered_job_seeker(self, test_data):  # проверка сохранения введенных данных соискателя
        name = self.browser.find_element(*AdminPageLocators.FIELD_NAME)
        name_value = name.get_attribute("value")
        assert name_value == test_data.name, "Поле 'Имя' не верно"

        surname = self.browser.find_element(*AdminPageLocators.FIELD_SURNAME)
        surname_value = surname.get_attribute("value")
        assert surname_value == test_data.surname, "Поле 'Фамилия' не верно"

        birthday = self.browser.find_element(*AdminPageLocators.FIELD_BIRTHDAY)
        birthday_value = birthday.get_attribute("value")
        assert birthday_value == test_data.birthday, "Поле 'День рождения' не верно"

        gender = self.browser.find_element(*AdminPageLocators.FIELD_GENDER)
        gender_title = gender.get_attribute("title")
        assert gender_title == test_data.gender, "Поле 'Пол' не верно"

        country = self.browser.find_element(*AdminPageLocators.FIELD_COUNTRY)
        country_title = country.get_attribute("title")
        assert country_title == test_data.country, "Поле 'Страна' не верно"

        WebDriverWait(self.browser, 5).until(EC.text_to_be_present_in_element((AdminPageLocators.FIELD_CITY), test_data.city))
        city = self.browser.find_element(*AdminPageLocators.FIELD_CITY)
        city_title = city.get_attribute("title")
        assert city_title == test_data.city, "Поле 'Город' не верно"

        checkbox_get_news = self.browser.find_element(*AdminPageLocators.CHECKBOX_GET_NEWS)
        checkbox_get_news_checked = checkbox_get_news.get_attribute("checked")
        assert checkbox_get_news_checked is not None, "Не установлено получение новостей"
    # страница пользователя

    # страница вакансий
    def waiting_to_save_status_and_open_vacansies_page(self):  # ожидание сохранения статуса и открытия страницы вакансий
        WebDriverWait(self.browser, 17).until(EC.text_to_be_present_in_element((AdminPageLocators.H1_VACANCIES), 'Вакансии'))

    def vacancy_search_by_job_title(self, job_title_vacancy):  # поиск вакансии по названию должности
        self.browser.find_element(*AdminPageLocators.FIELD_JOB_TITLE_SEARCH_VACANCIES).send_keys(job_title_vacancy, Keys.ENTER)
        time.sleep(2)
        job_title_locators = AdminPageLocators()
        locator = job_title_locators.assembly_of_locators_with_job_title(job_title_vacancy)
        assert self.is_element_present(*locator), 'Вакансия не найдена'

    def vacancy_search_by_job_title_after_editing(self):  # поиск вакансии по названию должности после редактирования
        self.browser.find_element(*AdminPageLocators.FIELD_JOB_TITLE_SEARCH_VACANCIES).send_keys(TestData.job_title_vacancy + '_editing', Keys.ENTER)
        time.sleep(2)
        assert self.is_element_present(*AdminPageLocators.VACANCY_BY_JOB_TITLE_AFTER_EDITING), 'Вакансия не найдена'

    def getting_vacancy_id(self):  # получение id вакансии
        id_vacancies = self.browser.find_element(*AdminPageLocators.ID_VACANCY).text
        return id_vacancies

    def checking_that_vacancy_status_is_on_moderated(self):  # проверка что статус вакансии 'На модерацию'
        status = self.browser.find_element(*AdminPageLocators.VACANCY_STATUS).text
        assert status == 'На модерацию', f"Не верный статус, expected result: 'На модерацию', actual result: '{status}'"

    def checking_that_vacancy_status_is_draft(self):  # проверка что статус вакансии 'Черновик'
        status = self.browser.find_element(*AdminPageLocators.VACANCY_STATUS).text
        assert status == 'Черновик', f"Не верный статус, expected result: 'Черновик', actual result: '{status}'"

    def checking_that_vacancy_status_is_deleted(self):  # проверка что статус вакансии 'Удалено'
        status = self.browser.find_element(*AdminPageLocators.VACANCY_STATUS).text
        assert status == 'Удалено', f"Не верный статус, expected result: 'Удалено', actual result: '{status}'"
    # страница вакансий

    def search_for_user_orders_by_email(self, language, key):  # поиск заказов пользователя по e-mail
        user_email_locators_orders = AdminPageLocators()
        locators = user_email_locators_orders.assembly_of_locators_with_user_email(key)
        email, user_email_orders = None, None
        if language == "/ua":
            email = Singleton.logins_and_mails[key][1][1]
            user_email_orders = locators[1]
        elif language == "":
            email = Singleton.logins_and_mails[key][0][1]
            user_email_orders = locators[0]
        elif language == "/en":
            email = Singleton.logins_and_mails[key][2][1]
            user_email_orders = locators[2]
        self.browser.find_element(*AdminPageLocators.FIELD_EMAIL_SEARCH_ORDERS).send_keys(email, Keys.ENTER)
        time.sleep(2)
        assert self.is_element_present(*user_email_orders), 'Заказ пользователя не найден'

    # def search_for_user_orders_by_status(self):  # поиск заказов пользователя по статусу "Новый"
    #     self.browser.find_element(*AdminPageLocators.SEARCH_STATUS_NEW).click()
    #     time.sleep(1)

    def getting_last_order_id_of_user(self):  # получение последнего id заказа пользователя
        id_order = self.browser.find_element(*AdminPageLocators.ID_LAST_ORDER).text
        return id_order

    def order_processing(self):  # проведение заказа, изменение статуса заказа с "Новый" на "Проведенный"
        status = self.browser.find_element(*AdminPageLocators.STATUS).text
        assert status == 'Новый', 'Статус не "Новый"'
        self.browser.find_element(*AdminPageLocators.STATUS).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_COMPLETED).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_SAVING).click()
        time.sleep(5)
        status = self.browser.find_element(*AdminPageLocators.STATUS).text
        assert status == 'Проведенный', 'Статус не "Проведенный"'

    def order_processing_2(self):  # проведение заказа, изменение статуса заказа с "Оплачено" на "Проведенный"
        status = self.browser.find_element(*AdminPageLocators.STATUS).text
        assert status == 'Оплачено', 'Статус не "Оплачено"'
        self.browser.find_element(*AdminPageLocators.STATUS).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_COMPLETED).click()
        time.sleep(1)
        self.browser.find_element(*AdminPageLocators.STATUS_SAVING).click()
        time.sleep(5)
        status = self.browser.find_element(*AdminPageLocators.STATUS).text
        assert status == 'Проведенный', 'Статус не "Проведенный"'
    # страница заказов

    def getting_id_of_purchase(self, id_order):  # получение id покупки
        self.browser.find_element(*AdminPageLocators.DROPDOWN_SEARCH_ORDERS).click()
        self.browser.find_element(*AdminPageLocators.FIELD_SEARCH_IN_DROPDOWN).send_keys(id_order)
        locators_with_id_order = AdminPageLocators()
        locator = locators_with_id_order.assembly_of_locators_with_id_order()
        WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(locator)).click()
        time.sleep(1)
        items_id_purchase = self.browser.find_elements(*AdminPageLocators.ITEMS_ID_PURCHASE)
        id_purchase = []
        for id in items_id_purchase:
            id_purchase.append(id.text)
        return id_purchase
    # страница "Покупки пользователей"
