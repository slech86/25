from Page_Object_Model.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Button:
    @staticmethod
    def button_type_button_click_by_label(browser, text, index=1, root_xpath=''):
        locator = (By.XPATH, f'({root_xpath}//button[contains(@aria-label, "{text}")])[{index}]')
        browser.find_element(*locator).click()

    @staticmethod
    def button_btn_edit_click(browser, root_xpath=''):
        locator = (By.XPATH, f'{root_xpath}//a[contains(@class, "btn-edit")]')
        browser.find_element(*locator).click()
