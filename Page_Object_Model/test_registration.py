import pytest
from .pages.oll_page import OllPage
from .pages.registration_page import RegistrationPage

@pytest.mark.parametrize('language', ["", "ua"])
def test_guest_can_go_to_login_page(browser, language):
    urlPage = f"http://preprod.logincasino.work.preprod.pw/{language}"
    page = OllPage(browser, urlPage)
    page.open()
    page.age_confirmation()
    page.opening_pop_up_for_login()
    page.go_to_registration_page()
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.filling_in_required_fields()

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

