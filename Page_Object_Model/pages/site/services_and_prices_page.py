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

    def adding_to_cart_monthly_free_vacancy(self):  # добавление в корзину "Ежемесячная бесплатная вакансия" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 600);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_MONTHLY_FREE_VACANCY).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.MONTHLY_FREE_VACANCY_IN_BASKET)  # наличие в корзине
        id_product = "25"
        return id_product

    def adding_to_cart_1_vacancy_and_getting_product_id(self):  # добавление в корзину "1 вакансия" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 600);")
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

    def switch_to_tab_not_activated(self):  # переход на вкладку "Не активированные"
        self.browser.find_element(*ServicesAndPricesPageLocators.TAB_NOT_ACTIVATED_SERVICES).click()

    def availability_of_product_in_not_activated_services(self):  # наличие продукта в не активированных услугах
        locators_with_id_product_and_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_product_and_id_purchase.assembly_of_locators_with_id_product_and_id_purchase()
        for locator in locators[0]:
            assert self.is_element_present(*locator), "Продукта нет в не активированных услугах"

    def product_activation(self):  # активация продукта
        locators_with_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_purchase.assembly_of_locators_with_id_product_and_id_purchase()
        for locator in locators[2]:
            self.browser.find_element(*ServicesAndPricesPageLocators.TAB_NOT_ACTIVATED_SERVICES).click()  # переход на вкладку "Не активированные"
            self.browser.find_element(*locator).click()
            time.sleep(1)

    def product_availability_in_activated_services(self):  # наличие продукта в активированных услугах
        locators_with_id_product_and_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_product_and_id_purchase.assembly_of_locators_with_id_product_and_id_purchase()
        for locator in locators[1]:
            assert self.is_element_present(*locator), "Продукта нет в активированных услугах"

    def checking_decrease_in_number_of_available_vacancies_for_publication_in_monthly_free_vacancy_package(self):  # проверка уменьшения количества доступных вакансий для публикации в пакете "Ежемесячная бесплатная вакансия"
        locators_with_id_product_and_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_product_and_id_purchase.assembly_of_locators_with_id_product_and_id_purchase()
        for i in range(len(locators[3])):
            self.browser.find_element(*locators[3][i]).click()
            time.sleep(0.3)
            text = self.browser.find_element(*locators[4][i]).text
            index = text.find('/')
            assert int(text[index - 2]) + 1 == int(text[index + 2]), 'В пакете осталось не верное количество вакансий'
