import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose lang")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = webdriver.Chrome(executable_path='/Page_Object_Model / drivers / chromedriver')
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        print("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    user_language = request.config.getoption("--language")
    if user_language == "ru":
        language = ''
    elif user_language == "ua":
        language = '/ua'
    yield language
