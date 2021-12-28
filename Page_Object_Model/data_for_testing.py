import time

class UrlStartPage():
    prefix = 'https://'  # 'http://preprod.', 'http://master.'. 'https://'
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
    city = '[#710719] Черновцы'   # не используется при заполнении полей, только при проверке заполнения полей в админке
    street = 'street_' + time_Now
    date_of_company_foundation = '2018-12-31'   # не используется при заполнении полей, только при проверке заполнения полей в админке
    birthday = '1998-11-30'  # не используется при заполнении полей, только при проверке заполнения полей в админке
    gender = 'Женский'

    company_site = 'http://company_site_' + time_Now + '.com'
    facebook = 'http://facebook_' + time_Now + '.com'
    linkedin = 'http://linkedin_' + time_Now + '.com'
    instagram = 'http://instagram_' + time_Now + '.com'
    telegram = 'http://telegram_' + time_Now + '.com'
    twitter = 'http://twitter_' + time_Now + '.com'
    vk = 'http://vk_' + time_Now + '.com'
    number_of_company_employees = 'от 100 до 250'  # (Количество сотрудников компании) не используется при заполнении полей, только при проверке заполнения полей в админке
    video_1 = 'https://www.youtube.com/watch?v=-8tBpQi5cto'
    video_2 = 'https://www.youtube.com/watch?v=ZsMKc7EecNs'
    video_3 = 'https://www.youtube.com/watch?v=kCunPyM8AQ0'



class Accounts():
    main_login_admin = 'p.verbenets'
    main_password_admin = 'l6FOt9tvJT'

    main_login_email = 'test_automation@smileexpo.com.ua'
    main_password_email = 'BwX37KJyiw02Cl'