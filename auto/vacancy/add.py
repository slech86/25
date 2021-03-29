from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

inputPrefix = 'vacancyaddform-'
login = 'admincompany'
email = ['test.p.verbenec+', '@gmail.com']
urlPage = "http://logincasino-work/"

try:
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(urlPage)

    driver.find_element(By.CSS_SELECTOR,('.login.flex-row')).click()
    driver.find_element(By.CSS_SELECTOR,('#loginform-emaillogin')).send_keys(login);
    driver.find_element(By.CSS_SELECTOR,('#loginform-password')).send_keys(login);
    driver.find_element(By.CSS_SELECTOR,('#login-form > [type="submit"].btn.btn-blue')).click();
    driver.find_element(By.CSS_SELECTOR,('a[href="/vacancy/my"] > .employer-card')).click();
    driver.find_element(By.CSS_SELECTOR,('.btn[href="/vacancy/add"]')).click();

    driver.execute_script("document.getElementsByName('VacancyAddForm[category_id][]')[4].click()");
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'country_id>option:nth-child(2)')).click();
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'country_id>option:nth-child(2)')).click();
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'job_title')).send_keys(login + '_job_title');
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'street')).send_keys('street');
    driver.execute_script("document.getElementsByName('VacancyAddForm[employment][]')[2].click()");
    driver.execute_script("document.getElementsByName('VacancyAddForm[work_experience]')[3].click()");

    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'description')).send_keys('description description');
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'about_company')).send_keys('about_company about_company');
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'working_conditions')).send_keys('working_conditions');
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'tasks')).send_keys('tasks tasks tasks');
    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'requirements')).send_keys('requirements requirements');

    driver.find_element(By.CSS_SELECTOR,('#' + inputPrefix + 'city_id>option:nth-child(2)')).click();
    driver.execute_script("document.getElementsByName('VacancyAddForm[subcategories_id][]')[2].click()");
    time.sleep(3)

    button = driver.find_element(By.CSS_SELECTOR,('.buttons-group.d-flex > #submit-button'))
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(5)
    driver.quit()
