from .pages.base_page import BasePage

class UrlStartPage(BasePage):
    prefix = 'http://preprod.'
    suffix = '.preprod.pw'
    suffix_page = '/vacancy'

    url_start_page = f"{prefix}logincasino.work{suffix}{suffix_page}"
