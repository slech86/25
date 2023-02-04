from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.admin_panel_locators import AdminProductEditPageLocators


class AdminProductEditPage(BasePage):
    def get_auto_activation_checkbox_status(self):  # получить статус чекбокса авто активации
        checkbox_auto_activation = self.browser.find_element(*AdminProductEditPageLocators.CHECKBOX_AUTO_ACTIVATION)
        status_checkbox_auto_activation = checkbox_auto_activation.get_attribute("checked")
        return status_checkbox_auto_activation

