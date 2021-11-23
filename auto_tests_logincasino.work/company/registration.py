from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
urlPage = 'http://preprod.logincasino.work.preprod.pw/'
timeNow = time.time()
inputPrefix = 'companyregistrationform-'
login = 'testLogin_'
email = ['test.p.verbenec+', '@gmail.com']

driver.implicitly_wait(5)
driver.get(urlPage)

try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content .btn.btn-blue.age-validation"))).click()
    # подтверждение возраста больше 21 года

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ('.login.flex-row')).click()
    # нажатие на кнопку для открытия pop-up окна для регистрации или авторизации

    driver.find_element(By.CSS_SELECTOR, ('a[href="/company/registration"]')).click()
    # нажатие на кнопку для перехона на страницу регистрации

    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'login')).send_keys(login + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'email')).send_keys(email[0] + str(int(timeNow)) + email[1])
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'password')).send_keys('password' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'repeatpassword')).send_keys('password' + str(int(timeNow)))
    # заполнение блока "Данные для авторизации"

    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'name')).send_keys('name' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'surname')).send_keys('surname' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'position')).send_keys('position' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'phone')).send_keys('+38(010)000-00-00' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'contact_email')).send_keys('email' + str(int(timeNow)) + email[1])
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'skype')).send_keys('skype' + str(int(timeNow)))
    # заполнение блока "Контактная информация"

    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'company_name')).send_keys('company_name' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'code_company')).send_keys('qы12345678')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'country_id > option:nth-child(2)')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'city_id > option:nth-child(28)')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'street')).send_keys('street' + str(int(timeNow)))
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatey > option:nth-child(5)')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdatem > option:nth-child(13)')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'foundationdated > option:nth-child(32)')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'company_site')).send_keys('http://company_site' + str(int(timeNow)) + '.com')

    driver.execute_script("window.scrollBy(0, 500);")
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="facebookCollapse"]')).click()
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="lnCollapse"]')).click()
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="inCollapse"]')).click()
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="telCollapse"]')).click()
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="twCollapse"]')).click()
    driver.find_element(By.CSS_SELECTOR, ('[aria-controls="vkCollapse"]')).click()

    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'facebook')).send_keys('http://facebook' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'linkedin')).send_keys('http://linkedin' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'instagram')).send_keys('http://instagram' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'telegram')).send_keys('http://telegram' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'twitter')).send_keys('http://twitter' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'vk')).send_keys('http://vk' + str(int(timeNow)) + '.com')

    driver.execute_script("document.getElementsByName('CompanyRegistrationForm[activity][]')[15].click()")  # Сфера деятельности компании
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'count_employees > option:nth-child(8)')).click()  # Количество сотрудников компании

    iframe = driver.find_element(By.CSS_SELECTOR, ('iframe.cke_wysiwyg_frame'))
    driver.switch_to.frame(iframe)  # вход в фрейма
    CKEditor = driver.find_element(By.CSS_SELECTOR, ('body.cke_editable'))
    CKEditor.clear()
    CKEditor.send_keys("CKEditor" + str(int(timeNow)))
    driver.switch_to.default_content()  # выход из фрейма
    # ввод данных в CKEditor
    # заполнение блока "Информация о компании"

    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'video1')).send_keys('http://video1' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'video2')).send_keys('http://video2' + str(int(timeNow)) + '.com')
    driver.find_element(By.CSS_SELECTOR, ('.js-add-video')).click()
    driver.find_element(By.CSS_SELECTOR, ('#' + inputPrefix + 'video3')).send_keys('http://video3' + str(int(timeNow)) + '.com')
    # заполнение блока "Видео"

    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, ('#submit-button')).click()
finally:
    time.sleep(7)
    driver.quit()

