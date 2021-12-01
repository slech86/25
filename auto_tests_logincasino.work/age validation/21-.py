from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
urlPage = 'http://preprod.logincasino.work.preprod.pw/'
timeNow = time.time()

driver.implicitly_wait(5)
driver.get(urlPage)

try:
    displayBlock = driver.find_element(By.CSS_SELECTOR, ('#age-validation'))
    time.sleep(5)
    validDisplayBlock = displayBlock.get_attribute("style")
    assert "display: block;" in validDisplayBlock
    # проверка на блокировку сайта без подтевержнения возраста

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content .btn.btn-disabled.age-validation"))).click()
    # подтверждение возраста мение 21 года

    infoText = driver.find_element(By.CSS_SELECTOR, ('div.empty-page > svg + p')).text
    assert "Данный сайт logincasino.work предназначен для аудитории старше 21 года" == infoText
    # проверка на открытие страницы и отображение на ней информации о пользании сайтом аудетории старше 21 года

    driver.find_element(By.CSS_SELECTOR, ('.btn-wrap > .btn.btn-blue.age-validation')).click()
    # нажатие кнопки для повторной верификации возраста

    displayBlock = driver.find_element(By.CSS_SELECTOR, ('#age-validation'))
    time.sleep(5)
    validDisplayBlock = displayBlock.get_attribute("style")
    assert "display: block;" in validDisplayBlock
    # проверка на блокировку сайта без подтевержнения возраста

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content .btn.btn-blue.age-validation"))).click()
    # подтверждение возраста больше 21 года

    displayBlock = driver.find_element(By.CSS_SELECTOR, ('#age-validation'))
    time.sleep(5)
    validDisplayBlock = displayBlock.get_attribute("style")
    assert "display: block;" not in validDisplayBlock
    # проверка на разблокировку сайта после подтевержнения возраста > 21

finally:
    time.sleep(1)
    driver.quit()

