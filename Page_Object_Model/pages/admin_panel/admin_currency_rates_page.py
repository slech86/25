from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminCurrencyRatesPageLocators


class AdminCurrencyRatesPage(BasePage):
    def getting_exchange_rates(self):  # получение курсов валют
        exchange_rates = []
        rub_rate = self.browser.find_element(*AdminCurrencyRatesPageLocators.RUB_RATE).text
        exchange_rates.append(float(rub_rate))
        uah_rate = self.browser.find_element(*AdminCurrencyRatesPageLocators.UAH_RATE).text
        exchange_rates.append(float(uah_rate))
        return exchange_rates
