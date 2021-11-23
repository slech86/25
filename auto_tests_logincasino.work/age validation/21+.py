from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
urlPage = 'http://preprod.logincasino.work.preprod.pw/'
timeNow = time.time()
inputPrefix = 'jobseekerregistrationform-'
email = ['test.p.verbenec+', '@gmail.com']

driver.implicitly_wait(5)
driver.get(urlPage)

try:
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

