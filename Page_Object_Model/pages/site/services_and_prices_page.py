from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ServicesAndPricesPageLocators
from selenium.webdriver.common.by import By
import time

class ServicesAndPricesPage(BasePage):
    def adding_to_cart_standart_1_vacancy_and_getting_product_id(self):  # добавление в корзину "Standart" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 100);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_STANDART).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.STANDART_IN_BASKET)  # наличие в корзине
        id_product = "1"
        return id_product
    def adding_to_cart_standart_5_vacancy_and_getting_product_id(self):  # добавление в корзину "Standart" и получение id продукта
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_5_VACANCY).click()
        self.browser.execute_script("window.scrollBy(0, 100);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_STANDART).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.STANDART_IN_BASKET)  # наличие в корзине
        id_product = "1"
        return id_product
    # пакеты услуг




    def adding_to_cart_Monthly_free_vacancy(self):  # добавление в корзину "Ежемесячная бесплатная вакансия" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 500);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_MONTHLY_FREE_VACANCY).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.MONTHLY_FREE_VACANCY_IN_BASKET)  # наличие в корзине
        id_product = "25"
        return id_product

    def adding_to_cart_1_vacancy_and_getting_product_id(self):  # добавление в корзину "1 вакансия" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 500);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_1_VACANCY).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.ONE_VACANCY_IN_BASKET)  # наличие в корзине
        id_product = "4"
        return id_product
    # пакеты поштучно




    def click_button_buy_in_basket(self):  # нажатие кнопки "Курить" в корзине
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_BUY).click()
        time.sleep(1)

    def verification_of_message_after_purchase(self):  # проверка сообщения после покупки
        infoText = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_BUTTON_PRESSED_BUY_IN_CART).text
        if "ua" in self.browser.current_url:
            assert "Наш менеджер зв'яжеться з Вами в найкоротший термін. Після узгодження всіх деталей Ви отримаєте доступ до послуги." == infoText, 'Не верное сообщение'
        else:
            assert "Наш менеджер свяжется с Вами в кратчайшие сроки. После согласования всех деталей Вы получите доступ к услуге." == infoText, 'Не верное сообщение'
        self.browser.find_element(*ServicesAndPricesPageLocators.CROSS_IN_POP_UP_AFTER_PRESSING_BUTTON_BUY_IN_BASKET).click()

    def switch_to_tab_Not_activated(self):  # переход на вкладку "Не активированные"
        self.browser.find_element(*ServicesAndPricesPageLocators.TAB_NOT_ACTIVATED_SERVICES).click()

    def availability_of_product_in_not_activated_services(self, id_product, id_purchase):  # наличие продукта в не активированных услугах
        for id in id_purchase:
            self.browser.find_element(By.CSS_SELECTOR, ('.tab-deactivate-servises .packages-wrap[data-product-id="' + id_product + '"][data-purchases-id="' + id + '"]'))

    def product_activation(self, id_purchase):  # активация продукта
        for id in id_purchase:
            self.browser.find_element(*ServicesAndPricesPageLocators.TAB_NOT_ACTIVATED_SERVICES).click() # переход на вкладку "Не активированные"
            self.browser.find_element(By.XPATH, ('//a[contains(@href, "/cart/active?id=' + id + '")]')).click()
            time.sleep(1)

    def product_availability_in_activated_services(self, id_product, id_purchase):  # наличие продукта в активированных услугах
        for id in id_purchase:
            self.browser.find_element(By.CSS_SELECTOR, ('.tab-activated-servises .packages-wrap[data-product-id="' + id_product + '"][data-purchases-id="' + id + '"]'))
