import time

class UrlStartPage():
    prefix = 'http://preprod.'  # 'http://preprod.', 'http://master.'. 'https://'
    suffix = '.preprod.pw'  # '.preprod.pw'
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

    password = 'password' + time_Now

    email = ['test_automation+', '@smileexpo.com.ua']
    email_ru = email[0] + time_Now + email[1]
    email_ua = email[0] + time_Now + 'ua' + email[1]


class Accounts():
    main_login_admin = 'p.verbenets'
    main_password_admin = 'l6FOt9tvJT'

    main_login_email = 'test_automation@smileexpo.com.ua'
    main_password_email = 'BwX37KJyiw02Cl'