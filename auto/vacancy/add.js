
const {Builder, By, Key} = require('selenium-webdriver');
let driver = new Builder().forBrowser('chrome').build();
driver.manage().setTimeouts( { implicit: 5000 } );
//const test = require('selenium-webdriver/testing');

let inputPrefix = 'vacancyaddform-';
let login = 'testLogin_';
let email = [
    'test.p.verbenec+',
    '@gmail.com',
];
let time = Math.round(+new Date()/1000);
let urlPage = 'http://logincasino-work/vacancy/add';

try {
    driver.get(urlPage);

    driver.findElement(By.css('.login.flex-row')).click();
    driver.findElement(By.css('#loginform-emaillogin')).sendKeys('admincompany'/*, Key.RETURN*/);
    driver.findElement(By.css('#loginform-password')).sendKeys('admincompany'/*, Key.RETURN*/);
    driver.findElement(By.css('#login-form > [type="submit"].btn.btn-blue')).click();
    driver.findElement(By.css('a[href="/vacancy/my"] > .employer-card')).click();
    driver.findElement(By.css('.btn[href="/vacancy/add"]')).click();


    driver.executeScript("document.getElementsByName('VacancyAddForm[category_id][]')[4].click()");
    driver.findElement(By.css('#' + inputPrefix + 'country_id>option:nth-child(2)')).click();
    driver.findElement(By.css('#' + inputPrefix + 'job_title')).sendKeys(login + 'job_title'/*, Key.RETURN*/);
    driver.findElement(By.css('#' + inputPrefix + 'street')).sendKeys('street'/*, Key.RETURN*/);
    driver.executeScript("document.getElementsByName('VacancyAddForm[employment][]')[2].click()");
    driver.executeScript("document.getElementsByName('VacancyAddForm[work_experience]')[3].click()");


    driver.findElement(By.css('#' + inputPrefix + 'description')).sendKeys('description description'/*, Key.RETURN*/);
    driver.findElement(By.css('#' + inputPrefix + 'about_company')).sendKeys('about_company about_company'/*, Key.RETURN*/);
    driver.findElement(By.css('#' + inputPrefix + 'working_conditions')).sendKeys('working_conditions'/*, Key.RETURN*/);
    driver.findElement(By.css('#' + inputPrefix + 'tasks')).sendKeys('tasks tasks tasks'/*, Key.RETURN*/);
    driver.findElement(By.css('#' + inputPrefix + 'requirements')).sendKeys('requirements requirements'/*, Key.RETURN*/);

    driver.findElement(By.css('#' + inputPrefix + 'city_id>option:nth-child(2)')).click();
    driver.executeScript("document.getElementsByName('VacancyAddForm[subcategories_id][]')[2].click()");

    driver.sleep(5000);
    driver.findElement(By.css('.buttons-group.d-flex > #submit-button')).click();
}
finally {
    driver.sleep(2000);
    //driver.quit();
}

/*

test.describe('vacancy add', function() {
    let driver;
    let inputPrefix = 'vacancyaddform-';
    let login = 'testLogin_';
    let email = [
        'test.p.verbenec+',
        '@gmail.com',
    ];
    let time = Math.round(+new Date()/1000);
    let urlPage = 'http://logincasino-work/vacancy/add';

    test.before(function *() {
        driver = yield new Builder().forBrowser('chrome').build();
        driver.manage().setTimeouts( { implicit: 5000 } );
    });

    test.it('works with generators', function*() {
        try {
            driver.get(urlPage);

            driver.findElement(By.css('.login.flex-row')).click();
            driver.findElement(By.css('#loginform-emaillogin')).sendKeys('admincompany', Key.RETURN);
            driver.findElement(By.css('#loginform-password')).sendKeys('admincompany', Key.RETURN);
            driver.findElement(By.css('#login-form > [type="submit"].btn.btn-blue')).click();
            driver.findElement(By.css('a[href="/vacancy/my"] > .employer-card')).click();
            driver.findElement(By.css('.btn[href="/vacancy/add"]')).click();


            driver.executeScript("document.getElementsByName('VacancyAddForm[category_id][]')[4].click()");
            driver.findElement(By.css('#' + inputPrefix + 'country_id>option:nth-child(2)')).click();
            driver.findElement(By.css('#' + inputPrefix + 'job_title')).sendKeys(login + 'job_title', Key.RETURN);
            driver.findElement(By.css('#' + inputPrefix + 'street')).sendKeys('street', Key.RETURN);
            driver.executeScript("document.getElementsByName('VacancyAddForm[employment][]')[2].click()");
            driver.executeScript("document.getElementsByName('VacancyAddForm[work_experience]')[3].click()");


            driver.findElement(By.css('#' + inputPrefix + 'description')).sendKeys('description description', Key.RETURN);
            driver.findElement(By.css('#' + inputPrefix + 'about_company')).sendKeys('about_company about_company', Key.RETURN);
            driver.findElement(By.css('#' + inputPrefix + 'working_conditions')).sendKeys('working_conditions', Key.RETURN);
            driver.findElement(By.css('#' + inputPrefix + 'tasks')).sendKeys('tasks tasks tasks', Key.RETURN);
            driver.findElement(By.css('#' + inputPrefix + 'requirements')).sendKeys('requirements requirements', Key.RETURN);

            driver.findElement(By.css('#' + inputPrefix + 'city_id>option:nth-child(2)')).click();
            driver.executeScript("document.getElementsByName('VacancyAddForm[subcategories_id][]')[2].click()");

            driver.sleep(5000);
            driver.findElement(By.css('.buttons-group.d-flex > #submit-button')).click();
        }
        finally {
            driver.sleep(2000);
            driver.quit();
        }

    });

});*/
