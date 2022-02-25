import time


class Accounts():
    main_login_admin = 'p.verbenets'
    main_password_admin = 'l6FOt9tvJT'

    main_login_email = 'test_automation@smileexpo.com.ua'
    main_password_email = 'BwX37KJyiw02Cl'


class TestData():
    time_Now = str(int(time.time()))

    login_ru = 'testLogin_' + time_Now
    login_ua = login_ru + 'ua'

    password = 'password_' + time_Now

    email = ['test_automation+', '@smileexpo.com.ua']
    email_ru = email[0] + time_Now + email[1]
    email_ua = email[0] + time_Now + 'ua' + email[1]

    email_language_ru = '[#1] Русский'
    email_language_ua = '[#3] Українська'

    name = 'name_' + time_Now
    surname = 'surname_' + time_Now
    position = 'position_' + time_Now
    phone = '+01(010)101-01-01'
    contact_email = 'contact_email_' + time_Now + email[1]
    company_name = 'company_name_' + time_Now
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

    job_title_vacancy = 'test_job_title_vacancy_' + time_Now
    category_vacancy = '[#4] Отдел кадров'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_vacancy = '[#29] HR-менеджер'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_min = '700'
    salary_max = '1000'
    currency_vacancy = '(USD) Доллар'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке
    country_vacancy = '[#185] Россия'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_vacancy = '[#524901] Москва'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street_vacancy = 'street_vacancy_' + time_Now

    phone_vacancy = '+38(101)010-10-10'
    email_vacancy = 'email_vacancy_' + time_Now + email[1]
    skype_vacancy = 'skype_vacancy_' + time_Now
    contact_person = 'contact_person_' + time_Now
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

    name_resume = 'name_resume_' + time_Now
    surname_resume = 'surname_resume_' + time_Now
    birthday_resume = '1981-09-05'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender_resume = 'Женский'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    country_resume = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_resume = '[#698740] Одесса'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    willing_to_relocate = 'Не готов к переезду'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    phone_1_resume = '+77(666)555-44-33'
    phone_2_resume = '+88(999)222-11-00'
    email_resume = 'email_resume_' + time_Now + email[1]
    skype_resume = 'skype_resume_' + time_Now
    portfolio = 'https://portfolio_' + time_Now + '.com'

    facebook_resume = 'https://facebook_resume_' + time_Now + '.com'
    linkedin_resume = 'https://linkedin_resume_' + time_Now + '.com'
    instagram_resume = 'http://instagram_resume_' + time_Now + '.com'
    telegram_resume = 'http://telegram_resume_' + time_Now + '.com'
    twitter_resume = 'http://twitter_resume_' + time_Now + '.com'
    vk_resume = 'http://vk_resume_' + time_Now + '.com'

    job_title_resume = 'test_job_title_resume_' + time_Now
    category_resume = '[#123] Дизайн, графика, анимация'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_resume = '[#70] UX-дизайнер'  # не используется при заполнении полей, только при проверке заполнения полей в админке

    employment_type_resume = 'Удаленная'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_resume = '25123'
    currency_resume = '(UAH) Гривна'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке

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


class TestDataEditing():
    email_language_ru = '[#1] Русский'
    email_language_ua = '[#3] Українська'

    name = TestData.name + '_editing'
    surname = TestData.surname + '_editing'
    position = TestData.position + '_editing'
    phone = '+1(234)567-89-10'
    contact_email = TestData.contact_email + 'editing'
    company_name = TestData.company_name + '_editing'
    code_company = '01111110'
    company_activity = '[#146] Финансы' + '[#188] Гемблинг'  # ??? (Сфера деятельности компании) не используется при заполнении полей, только при проверке заполнения полей в админке
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

    job_title_vacancy = TestData.job_title_vacancy + '_editing'
    category_vacancy = '[#4] Отдел кадров'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    subcategories_vacancy = '[#29] HR-менеджер'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    salary_min = '8000'
    salary_max = '15000'
    currency_vacancy = '(USD) Доллар'  # (нужно искать как часть title) не используется при заполнении полей, только при проверке заполнения полей в админке
    country_vacancy = '[#185] Россия'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city_vacancy = '[#524901] Москва'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street_vacancy = TestData.street_vacancy + '_editing'

    phone_vacancy = '+38(111)213-14-15'
    email_vacancy = TestData.street_vacancy + 'editing'
    skype_vacancy = TestData.street_vacancy + '_editing'
    contact_person = TestData.street_vacancy + '_editing'
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
