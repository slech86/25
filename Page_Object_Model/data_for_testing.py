import time

class UrlStartPage():
    prefix = 'http://preprod.'  # 'http://preprod.', 'http://master.'. 'https://'
    if prefix == 'https://':
        suffix = ''
    else:
        suffix = '.preprod.pw'

    suffix_page = ''

    url_start_page = f"{prefix}logincasino.work{suffix}{suffix_page}"

class UrlPageAdmin():
    if UrlStartPage.suffix == '.preprod.pw':
        url_page_admin = "http://admin-work.pw.preprod.pw/x"
    else:
        url_page_admin = "https://admin-work.work/x"


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
    phone_editing = '+1(234)567-89-10'
    contact_email = 'contact_email_' + time_Now + email[1]
    company_name = 'company_name_' + time_Now
    code_company = 'qы10000001'
    code_company_editing = '01111110'
    company_activity = '[#146] Финансы'  # (Сфера деятельности компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    ckeditor_company_description = "CKEditor_company_description_" + time_Now
    skype = 'skype' + time_Now
    country = '[#222] Украина'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    city = '[#703448] Киев'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    street = 'street_' + time_Now
    date_of_company_foundation = '2019-12-31'   # не используется при заполнении полей, только при проверке заполнения полей в админке
    birthday = '1999-11-30'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender = 'Женский'

    company_site = 'http://company_site_' + time_Now + '.com'
    facebook = 'http://facebook_' + time_Now + '.com'
    linkedin = 'http://linkedin_' + time_Now + '.com'
    instagram = 'http://instagram_' + time_Now + '.com'
    telegram = 'http://telegram_' + time_Now + '.com'
    twitter = 'http://twitter_' + time_Now + '.com'
    vk = 'http://vk_' + time_Now + '.com'
    number_of_company_employees = 'от 100 до 250'  # (Количество сотрудников компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    video_1 = 'https://www.youtube.com/watch?v=6OBg9Iz7dD0'
    video_1_editing = 'https://www.youtube.com/watch?v=jLwvMlvkBv0'
    video_2 = 'https://www.youtube.com/watch?v=ZsMKc7EecNs'
    video_2_editing = 'https://www.youtube.com/watch?v=j0F8PXnP9yY'
    video_3 = 'https://www.youtube.com/watch?v=kCunPyM8AQ0'
    video_3_editing = 'https://www.youtube.com/watch?v=-DKCkibqulU'


class Accounts():
    main_login_admin = 'p.verbenets'
    main_password_admin = 'l6FOt9tvJT'

    main_login_email = 'test_automation@smileexpo.com.ua'
    main_password_email = 'BwX37KJyiw02Cl'