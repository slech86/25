import pytest
import time

from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import AddVacancyPageLocators


class AddVacancyPage(BasePage):
    def absence_of_button_to_publish(self):  # проверка отсутствия кнопки "Опубликовать"
        with pytest.raises(NoSuchElementException):
            self.browser.find_element(*AddVacancyPageLocators.BUTTON_PUBLISH)
            pytest.fail("Не должно быть кнопки 'Опубликовать'")

    def submitting_vacancy_for_publication(self):  # отправка вакансии на публикацию
        self.browser.find_element(*AddVacancyPageLocators.BUTTON_PUBLISH).click()
