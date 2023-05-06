from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ServicesAndPricesPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ServicesAndPricesPage(BasePage):
    # пакеты услуг
    def adding_to_cart_help_refugee_with_his_work_and_getting_product_id(self):  # добавление в корзину "Помоги беженцу с работой" и получение id продукта
        self.browser.execute_script("window.scrollBy(0, 100);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_HELP_REFUGEE_WITH_HIS_WORK).click()
        self.browser.find_element(*ServicesAndPricesPageLocators.HELP_REFUGEE_WITH_HIS_WORK_IN_BASKET)  # наличие в корзине
        id_product = "15"
        return id_product

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

    # пакеты поштучно
    def adding_to_cart_monthly_free_vacancy_and_getting_product_id(self):  # добавление в корзину "Ежемесячная бесплатная вакансия" и получение id продукта
        button = self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_ORDER_IN_MONTHLY_FREE_VACANCY)
        self.browser.execute_script("return arguments[0].scrollIntoView(false);", button)
        button.click()
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
        # self.browser.execute_script("window.scrollBy(0, 10000);")
        self.browser.find_element(*ServicesAndPricesPageLocators.BUTTON_BUY).click()
        time.sleep(1)

    def checking_message_after_buying_free_package(self, language):  # проверка сообщения после покупки бесплатного пакета
        info_text = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_BUTTON_PRESSED_BUY_IN_CART).text
        if language == "":
            assert "После активации услуги в личном кабинете, вы можете предложить вакансию соискателям!" == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Після активації послуги в особистому кабінеті, ви можете запропонувати вакансію здобувачам!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "You will be able to offer a vacancy to job seekers after activating the service in your account!" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Po aktywacji usługi na koncie osobistym możesz oferować wolne miejsca pracy osobom poszukującym pracy!" == info_text, 'Не верное сообщение'
        self.browser.find_element(*ServicesAndPricesPageLocators.CROSS_IN_POP_UP_AFTER_PRESSING_BUTTON_BUY_IN_BASKET).click()

    def checking_message_after_buying_paid_package(self, language):  # проверка сообщения после покупки платного пакета
        info_text = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_BUTTON_PRESSED_BUY_IN_CART).text
        if language == "":
            assert "Наш менеджер свяжется с Вами в кратчайшие сроки. После согласования всех деталей Вы получите доступ к услуге." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Наш менеджер зв'яжеться з Вами у найкоротші терміни. Після узгодження всіх деталей Ви отримаєте доступ до послуги." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Our manager will contact you as soon as possible. After agreeing on all the details, you will get access to the service." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Nasz menedżer skontaktuje się z Tobą tak szybko, jak to możliwe. Po uzgodnieniu wszystkich szczegółów otrzymasz dostęp do usługi." == info_text, 'Не верное сообщение'
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

    def checking_decrease_in_number_of_available_vacancies_for_publication_in_service_package(self):  # проверка уменьшения количества доступных вакансий для публикации в пакете услуг
        locators_with_id_product_and_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_product_and_id_purchase.assembly_of_locators_with_id_product_and_id_purchase()
        for i in range(len(locators[3])):
            self.browser.find_element(*locators[3][i]).click()
            time.sleep(0.4)
            number_of_vacancies_available = self.browser.find_elements(*locators[4][i])
            if len(number_of_vacancies_available) == 1:
                text = number_of_vacancies_available[0].text
                index = text.find('/')
                assert int(text[index - 2]) + 1 == int(text[index + 2]), 'В пакете осталось не верное количество вакансий'
            else:
                text = number_of_vacancies_available[1].text
                index = text.find('/')
                assert int(text[index - 2]) + 1 == int(text[index + 2]), 'В пакете осталось не верное количество вакансий'

    def checking_reduction_in_number_of_contact_views_in_service_package(self, id_product, id_purchase):  # проверка уменьшения в пакете услуг количества просмотров контактов
        locators_with_id_product_and_id_purchase = ServicesAndPricesPageLocators()
        locators = locators_with_id_product_and_id_purchase.new_assembly_of_locators_with_id_product_and_id_purchase(id_product, id_purchase)
        self.browser.find_element(*locators['arrow_for_viewing_options_available_in_package']).click()
        time.sleep(0.3)
        number_of_vacancies_available = self.browser.find_elements(*locators['number_of_vacancies_available'])
        text = number_of_vacancies_available[0].text
        index = text.find('/')
        assert int(text[index - 2]) + 1 == int(text[index + 2]), 'В пакете осталось не верное количество вакансий'

    def checking_message_about_creating_test_payment(self, language):  # проверка сообщения о создании тестового платежа
        info_text = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_OPERATIONS_IN_INTERKASSA).text
        if language == "":
            assert "Платеж успешно прошел, ожидайте модерации." == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Платіж успішно пройшов, зачекайте на модерацію." == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Payment successfully completed, wait for moderation." == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Płatność się powiodła, proszę czekać na moderację." == info_text, 'Не верное сообщение'
        self.browser.find_element(*ServicesAndPricesPageLocators.CROSS_IN_POP_UP_AFTER_OPERATIONS_IN_INTERKASSA).click()

    def checking_message_about_create_cancel_test_payment(self, language):  # проверка сообщения о создании отмененного тестового платежа
        info_text = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_OPERATIONS_IN_INTERKASSA).text
        if language == "":
            assert "Что-то пошло не так! Попробуйте оплатить снова!" == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Щось пішло не так! Спробуйте сплатити знову!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Something went wrong! Try to pay again!" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Coś poszło nie tak! Spróbuj zapłacić ponownie!" == info_text, 'Не верное сообщение'
        self.browser.find_element(*ServicesAndPricesPageLocators.CROSS_IN_POP_UP_AFTER_OPERATIONS_IN_INTERKASSA).click()

    def checking_message_about_create_pending_payment(self, language):  # проверка сообщения о создании платежа в ожидании
        info_text = self.browser.find_element(*ServicesAndPricesPageLocators.INFO_TEXT_AFTER_OPERATIONS_IN_INTERKASSA).text
        if language == "":
            assert "Платеж находится в обработке!" == info_text, 'Не верное сообщение'
        elif language == "/ua":
            assert "Платіж знаходиться в обробці!" == info_text, 'Не верное сообщение'
        elif language == "/en":
            assert "Payment is being processed!" == info_text, 'Не верное сообщение'
        elif language == "/pl":
            assert "Płatność jest przetwarzana!" == info_text, 'Не верное сообщение'
        self.browser.find_element(
            *ServicesAndPricesPageLocators.CROSS_IN_POP_UP_AFTER_OPERATIONS_IN_INTERKASSA).click()
