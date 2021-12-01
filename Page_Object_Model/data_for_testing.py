import time

class UrlStartPage():
    prefix = 'http://preprod.'
    suffix = '.preprod.pw'
    suffix_page = '/vacancy'

    url_start_page = f"{prefix}logincasino.work{suffix}{suffix_page}"

# class UrlStartPageAdmin(BasePage):
#     prefix = 'http://'
#     suffix = '.preprod.pw'
#     suffix_page = '/x'
#
#     url_start_page = f"{prefix}admin-work.pw{suffix}{suffix_page}"

class TestData():
    time_Now = str(int(time.time()))

    login_ru = 'testLogin_' + time_Now
    login_ua = login_ru + 'ua'

    password = 'password' + time_Now

    email = ['test_automation+', '@smileexpo.com.ua']
    email_ru = email[0] + time_Now + email[1]
    email_ua = email[0] + time_Now + 'ua' + email[1]

