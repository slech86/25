import time
from Page_Object_Model.singleton import Singleton


class Accounts():
    main_login_admin = 'p.verbenets'
    main_password_admin = 'l6FOt9tvJT'

    url_email = 'https://mail.qazz.pw/'  # "https://mail.smileexpo.com.ua/?_task=mail&_mbox=INBOX"
    main_login_email = 'test_automation@qazz.pw'
    main_password_email = 'VzbxybY0Q7yOzwKDibTUdPli'

    # main_login_email = 'test_automation@smileexpo.com.ua'
    # main_password_email = 'BwX37KJyiw02Cl'


class TestData:
    time_Now = str(int(time.time()))
    email = ['test_automation+', '@qazz.pw']
    password = 'password_' + time_Now

    # пользователи
    def login_and_mail_generation(self, key):
        time_now = str(int(time.time()))
        login_ru = 'testLogin_' + time_now
        login_ua = login_ru + 'ua'
        login_en = login_ru + 'en'

        email_ru = TestData.email[0] + time_now + TestData.email[1]
        email_ua = TestData.email[0] + time_now + 'ua' + TestData.email[1]
        email_en = TestData.email[0] + time_now + 'en' + TestData.email[1]

        singleton = Singleton()
        singleton.logins_and_mails[key] = [
            [login_ru, email_ru],
            [login_ua, email_ua],
            [login_en, email_en]
        ]

    email_language_ru = '[#1] Русский'
    email_language_ua = '[#3] Українська'
    email_language_en = '[#4] English'

    name = 'name_' + time_Now
    surname = 'surname_' + time_Now
    position = 'position_' + time_Now
    phone = '+420(737)222-333'
    contact_email = 'contact_email_' + time_Now + email[1]
    company_name = 'company_name_' + time_Now
    company_slug = 'company_slug_' + time_Now
    code_company = 'qы10000001'
    company_activity = '[#146] Финансы'  # (Сфера деятельности компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    ckeditor_company_description = "CKEditor_company_description_" + time_Now
    skype = 'skype' + time_Now
    country = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city = '[#703448] Киев'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street = 'street_' + time_Now
    date_of_company_foundation = '2019-12-31'   # не используется при заполнении полей, только при проверке заполнения полей в админке
    birthday = '1999-11-30'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender = 'Женский'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    company_site = 'https://company_site_' + time_Now + '.com'
    facebook = 'https://facebook_' + time_Now + '.com'
    linkedin = 'http://linkedin_' + time_Now + '.com'
    instagram = 'http://instagram_' + time_Now + '.com'
    telegram = 'http://telegram_' + time_Now + '.com'
    twitter = 'https://twitter_' + time_Now + '.com'
    vk = 'http://vk_' + time_Now + '.com'
    number_of_company_employees = 'от 100 до 250'  # (Количество сотрудников компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    video_1 = 'https://www.youtube.com/watch?v=6OBg9Iz7dD0'
    video_2 = 'https://www.youtube.com/watch?v=ZsMKc7EecNs'
    video_3 = 'https://www.youtube.com/watch?v=kCunPyM8AQ0'
    # пользователи

    # вакансия
    job_title_vacancy = 'test_job_title_vacancy_' + time_Now
    job_title_vacancy_for_draft = 'test_job_title_vacancy for_draft_' + time_Now
    category_vacancy = '[#4] Отдел кадров'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_vacancy = '[#29] HR-менеджер'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_min = '700'
    salary_max = '1000'
    currency_vacancy = '(USD) USD'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке
    country_vacancy = '[#79] Грузия'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_vacancy = '[#9000009] Батуми'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street_vacancy = 'street_vacancy_' + time_Now

    phone_vacancy = '+7(777)999-9999'
    email_vacancy = 'email_vacancy_' + time_Now + email[1]
    skype_vacancy = 'skype_vacancy_' + time_Now
    contact_person = 'contact_person_' + time_Now
    telegram_vacancy = 'https://telegram_vacancy' + time_Now + '.com/'
    employment_type_vacancy = 'Полная'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_experience_vacancy = 'от 1 года'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education = 'Высшее'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    benefits = 'Развозка'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    additionally = 'Готовы взять студента'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_vacancy_1 = 'Английский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_vacancy_1 = 'Средний'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_vacancy_2 = 'Русский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_vacancy_2 = 'Родной'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    description_vacancy = 'description_vacancy_' + time_Now
    about_company = 'about_company_' + time_Now
    working_conditions = 'working_conditions_' + time_Now
    tasks = 'tasks_' + time_Now
    requirements = 'requirements_' + time_Now
    additionally_information = 'additionally_information' + time_Now
    # вакансия

    # резюме
    name_resume = 'name_resume_' + time_Now
    surname_resume = 'surname_resume_' + time_Now
    birthday_resume = '1981-09-05'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender_resume = 'Женский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_resume = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_resume = '[#698740] Одесса'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    willing_to_relocate = 'Не готов к переезду'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    phone_1_resume = '+380(67)000-0000'
    phone_2_resume = '+48(509)111-222'
    email_resume = 'email_resume_' + time_Now + email[1]
    skype_resume = 'skype_resume_' + time_Now
    portfolio = 'https://portfolio_' + time_Now + '.com/'

    facebook_resume = 'https://facebook_resume_' + time_Now + '.com/'
    linkedin_resume = 'https://linkedin_resume_' + time_Now + '.com/'
    instagram_resume = 'http://instagram_resume_' + time_Now + '.com/'
    telegram_resume = 'http://telegram_resume_' + time_Now + '.com/'
    twitter_resume = 'http://twitter_resume_' + time_Now + '.com/'
    vk_resume = 'http://vk_resume_' + time_Now + '.com/'

    job_title_resume = 'test_job_title_resume ' + time_Now
    job_title_resume_2 = 'test_job_title_resume_2 ' + time_Now
    job_title_resume_3 = 'test_job_title_resume_3 ' + time_Now
    job_title_resume_for_draft = 'test_job_title_resume for_draft_' + time_Now
    category_resume = '[#123] Дизайн, графика, анимация'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_resume = '[#70] UX-дизайнер'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    employment_type_resume = 'Удаленная'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_resume = '25123'
    currency_resume = '(UAH) UAH'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке

    skills_and_achievements = 'skills_and_achievements_' + time_Now

    company_name_resume = 'company_name_resume_' + time_Now
    company_site_resume = 'https://company_site_resume_' + time_Now + '.com'
    scope_of_company = '[#6] Персонал казино'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    position_resume = 'position_resume_' + time_Now
    work_period_start = '01.08.2018'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_period_finish = '01.03.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    responsibilities_and_achievements = 'responsibilities_and_achievements_' + time_Now

    company_name_resume_2 = 'company_name_resume_2_' + time_Now
    company_site_resume_2 = 'https://company_site_resume_2_' + time_Now + '.com'
    scope_of_company_2 = '[#8] Обслуживание автоматов'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    position_resume_2 = 'position_resume_2_' + time_Now
    work_period_start_2 = '01.04.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_period_finish_2 = None  # проверка наличия атрибута "checked" в следующем поле, так как было выбрано "По насоящее время", не используется при заполнении полей, только при проверке заполнения полей в админке
    responsibilities_and_achievements_2 = 'responsibilities_and_achievements_2_' + time_Now

    experience_in_gambling_industry = 'Без опыта'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_of_institution = 'name_of_institution_' + time_Now
    level_of_education = 'Высшее'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_education = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_education = '[#706483] Харьков'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    department_and_speciality = 'department_and_speciality_' + time_Now
    education_period_start = '01.09.2010'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education_period_finish = '01.05.2015'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_of_institution_2 = 'name_of_institution_2_' + time_Now
    level_of_education_2 = 'Среднее специальное'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_education_2 = '[#36] Беларусь'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_education_2 = '[#625144] Минск'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    department_and_speciality_2 = 'department_and_speciality_2_' + time_Now
    education_period_start_2 = '01.11.2018'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education_period_finish_2 = '01.01.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_course = 'name_course_' + time_Now
    course_period_start = '01.06.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_period_finish = '01.06.2021'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_description = 'course_description_' + time_Now

    name_course_2 = 'name_course_2_' + time_Now
    course_period_start_2 = '01.10.2014'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_period_finish_2 = '01.10.2015'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_description_2 = 'course_description_2_' + time_Now

    language_resume_1 = 'Польский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_resume_1 = 'Продвинутый'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_resume_2 = 'Немецкий'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_resume_2 = 'Свободно'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    disability = 'У меня нет инвалидности'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    additional_information = 'additional_information_' + time_Now

    job_search_status = 'Активно ищу работу'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    # резюме

    cover_letter = 'cover_letter_' + time_Now


class TestDataEditing:
    # пользователи
    email_language_ru = '[#1] Русский'
    email_language_ua = '[#3] Українська'
    email_language_en = '[#4] English'

    name = TestData.name + '_editing'
    surname = TestData.surname + '_editing'
    position = TestData.position + '_editing'
    phone = '+357(96)000000'
    contact_email = TestData.contact_email + 'editing'
    company_name = TestData.company_name + '_editing'
    company_slug = TestData.company_slug + '_edit'
    code_company = '01111110'
    company_activity = '[#146] Финансы' + '[#188] Гемблинг'  # ?!? (Сфера деятельности компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    ckeditor_company_description = "editing_" + TestData.ckeditor_company_description
    skype = TestData.skype + '_editing'
    country = '[#122] Казахстан'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city = '[#609655] Караганда'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street = TestData.street + '_editing'
    date_of_company_foundation = '1991-03-17'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    birthday = '2001-01-01'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender = 'Мужской'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    company_site = TestData.company_site + '_editing'
    facebook = TestData.facebook + '_editing'
    linkedin = TestData.linkedin + '_editing'
    instagram = TestData.instagram + '_editing'
    telegram = TestData.telegram + '_editing'
    twitter = TestData.twitter + '_editing'
    vk = TestData.vk + '_editing'
    number_of_company_employees = 'от 50 до 100'  # (Количество сотрудников компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    video_1 = 'https://www.youtube.com/watch?v=jLwvMlvkBv0'
    video_2 = 'https://www.youtube.com/watch?v=j0F8PXnP9yY'
    video_3 = 'https://www.youtube.com/watch?v=-DKCkibqulU'
    # пользователи

    # вакансия
    job_title_vacancy = TestData.job_title_vacancy + '_editing'
    category_vacancy = '[#4] Отдел кадров'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_vacancy = '[#29] HR-менеджер'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_min = '8000'
    salary_max = '15000'
    currency_vacancy = '(USD) USD'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке
    country_vacancy = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_vacancy = '[#709930] Днепр'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street_vacancy = TestData.street_vacancy + '_editing'

    phone_vacancy = '+380(99)999-9999'
    email_vacancy = TestData.email_vacancy + 'editing'
    skype_vacancy = TestData.skype_vacancy + '_editing'
    contact_person = TestData.contact_person + '_editing'
    telegram_vacancy = TestData.telegram_vacancy + '_editing'
    employment_type_vacancy = 'Полная'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_experience_vacancy = 'от 1 года'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education = 'Высшее'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    benefits = 'Развозка'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    additionally = 'Готовы взять студента'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_vacancy_1 = 'Английский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_vacancy_1 = 'Средний'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_vacancy_2 = 'Русский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_vacancy_2 = 'Родной'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    description_vacancy = "editing_" + TestData.description_vacancy
    about_company = "editing_" + TestData.about_company
    working_conditions = "editing_" + TestData.working_conditions
    tasks = "editing_" + TestData.tasks
    requirements = "editing_" + TestData.requirements
    additionally_information = "editing_" + TestData.additionally_information
    # вакансия

    # резюме
    name_resume = TestData.name_resume + '_editing'
    surname_resume = TestData.surname_resume + '_edit'
    birthday_resume = '1976-03-08'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender_resume = 'Мужской'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_resume = '[#174] Польша'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_resume = '[#3088171] Познань'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    willing_to_relocate = 'Готов к переезду'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    phone_1_resume = '+380(63)123-4567'
    phone_2_resume = '+380(50)505-0505'
    email_resume = TestData.email_resume + 'editing'
    skype_resume = TestData.skype_resume + '_editing'
    portfolio = TestData.portfolio + '_editing/'

    facebook_resume = TestData.facebook_resume + '_editing/'
    linkedin_resume = TestData.linkedin_resume + '_editing/'
    instagram_resume = TestData.instagram_resume + '_editing/'
    telegram_resume = TestData.telegram_resume + '_editing/'
    twitter_resume = TestData.twitter_resume + '_editing/'
    vk_resume = TestData.vk_resume + '_editing/'

    job_title_resume = TestData.job_title_resume + '_editing'
    category_resume = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_resume = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    employment_type_resume = 'Удаленная?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_resume = '1200'
    currency_resume = '(USD) USD'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке

    skills_and_achievements = 'editing_' + TestData.skills_and_achievements

    company_name_resume = TestData.company_name_resume + '_editing'
    company_site_resume = TestData.company_site_resume + '_editing'
    scope_of_company = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    position_resume = TestData.position_resume + '_editing'
    work_period_start = '?!?01.08.2018'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_period_finish = '?!?01.03.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    responsibilities_and_achievements = "editing_" + TestData.responsibilities_and_achievements

    company_name_resume_2 = TestData.company_name_resume_2 + '_editing'
    company_site_resume_2 = TestData.company_site_resume_2 + '_editing'
    scope_of_company_2 = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    position_resume_2 = TestData.position_resume_2 + '_editing'
    work_period_start_2 = '?!?01.04.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_period_finish_2 = '?!?01.03.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    responsibilities_and_achievements_2 = 'editing_' + TestData.responsibilities_and_achievements_2

    company_name_resume_3 = 'company_name_resume_3 ' + TestData.time_Now + '_editing'
    company_site_resume_3 = 'https://company_site_resume_3_' + TestData.time_Now + '.com' + '_editing'
    scope_of_company_3 = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    position_resume_3 = 'position_resume_3 ' + TestData.time_Now + '_editing'
    work_period_start_3 = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    work_period_finish_3 = None  # проверка наличия атрибута "checked" в следующем поле, так как было выбрано "По насоящее время", не используется при заполнении полей, только при проверке заполнения полей в админке
    responsibilities_and_achievements_3 = 'editing_' + 'responsibilities_and_achievements_3 ' + TestData.time_Now

    experience_in_gambling_industry = 'от 2 до 5 лет'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_of_institution = TestData.name_of_institution + '_editing'
    level_of_education = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_education = '- Выбрать -'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_education = '- Выбрать -'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    department_and_speciality = TestData.department_and_speciality + '_editing'
    education_period_start = '?!?01.09.2010'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education_period_finish = '?!?01.05.2015'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_of_institution_2 = TestData.name_of_institution_2 + '_editing'
    level_of_education_2 = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_education_2 = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_education_2 = '[#710791] Черкассы'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    department_and_speciality_2 = TestData.department_and_speciality_2 + '_editing'
    education_period_start_2 = '?!?01.11.2018'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education_period_finish_2 = '?!?01.01.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_of_institution_3 = 'name_of_institution_3 ' + TestData.time_Now + '_editing'
    level_of_education_3 = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_education_3 = '[#54] Кипр'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_education_3 = '[#146384] Лимасол'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    department_and_speciality_3 = 'department_and_speciality_3 ' + TestData.time_Now + '_editing'
    education_period_start_3 = '?!?01.11.2018'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    education_period_finish_3 = '?!?01.01.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    name_course = TestData.name_course + '_editing'
    course_period_start = '?!?01.06.2020'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_period_finish = '?!?01.06.2021'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_description = 'editing_' + TestData.course_description

    name_course_2 = TestData.name_course_2 + '_editing'
    course_period_start_2 = '?!?01.10.2014'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_period_finish_2 = '?!?01.10.2015'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_description_2 = 'editing_' + TestData.course_description_2

    name_course_3 = 'name_course_3 ' + TestData.time_Now + '_editing'
    course_period_start_3 = '?!?01.10.2014'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_period_finish_3 = '?!?01.10.2015'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    course_description_3 = 'editing_' + 'course_description_3 ' + TestData.time_Now

    language_resume_1 = '?!?Польский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_resume_1 = '?!?Продвинутый'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_resume_2 = '?!?Немецкий'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_resume_2 = '?!?Свободно'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    language_resume_3 = '?!?Немецкий'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    level_language_resume_3 = '?!?Свободно'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    disability = '?!?У меня нет инвалидности'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    description_of_disability = 'description_of_disability ' + TestData.time_Now + '_editing'

    additional_information = 'editing_' + TestData.additional_information

    job_search_status = '?!?'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    # резюме
