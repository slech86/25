import pytest
import time

from .base_page import BasePage
from .locators import AddVacancyPageLocators


class AddVacancyPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        assert self.is_not_element_present(*AddVacancyPageLocators.BUTTON_PUBLISH), "Не должно быть кнопки 'Опубликовать'"

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        self.browser.find_element(*AddVacancyPageLocators.BUTTON_PUBLISH).click()
