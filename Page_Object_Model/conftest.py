import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru', help="Choose lang")


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('chrome')  # 'headless', 'chrome'
    # options.add_argument('--start-maximized')
    options.add_argument('--window-size=1600,1000')
    options.binary_location = "/Applications/Google Chrome Beta.app/Contents/MacOS/Google Chrome Beta"
    return options


@pytest.fixture(scope="function")
def browser(request, chrome_options):
    options = chrome_options
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        s = Service('drivers/chromedriver')
        browser = webdriver.Chrome(service=s, options=options)
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
    elif user_language == "en":
        language = '/en'
    yield language
