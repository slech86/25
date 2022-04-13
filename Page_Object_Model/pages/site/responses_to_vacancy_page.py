from Page_Object_Model.pages.base_page import BasePage
from Page_Object_Model.locators.company_locators import ResponsesToVacancyPageLocators


class ResponsesToVacancyPage(BasePage):
    def checking_for_unread_response_flag(self):  # проверка наличия метки не прочитанного отклика
        assert self.is_element_present(*ResponsesToVacancyPageLocators.MARK_NOT_VIEWED_RESPONSE), "Нет метки не прочитанного отклика"

    def go_to_resume_page_of_response(self):  # нажатие резюме отклика для перехода на его страницу
        resume_locator = ResponsesToVacancyPageLocators()
        resume = resume_locator.assembly_of_locators_with_id_resume()
        self.browser.find_element(*resume).click()
        self.browser.switch_to.window(self.browser.window_handles[1])
