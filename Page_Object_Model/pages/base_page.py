from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=7):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self, cookie=True):
        if cookie is True and 'logincasino.work' in self.url:
            self.browser.get(self.url + '/?disableAgeModal=true')
            self.browser.add_cookie({'name': 'AgeValidation', 'value': '1'})
            self.browser.get(self.url)
        else:
            self.browser.get(self.url)


    def is_element_present(self, how, what):  # упадет если нет элемента
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):  # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):  # будет ждать указаное время, упадет если элемент не исчезнет.
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
