
const {Builder, By, Key, until} = require('selenium-webdriver');
const test = require('selenium-webdriver/testing');


test.describe('company registration', function() {
    let driver;
    let inputPrefix = 'companyregistrationform-';
    let login = 'testLogin_';
    let email = [
        'test.p.verbenec+',
        '@gmail.com',
    ];
    let time = Math.round(+new Date()/1000);
    let urlPage = 'http://logincasino-work/company/registration';

    test.before(function *() {
        driver = yield new Builder().forBrowser('chrome').build();
        driver.manage().setTimeouts( { implicit: 8000 } );
    });

    test.it('works with generators', function*() {

        driver.get(urlPage);

        driver.findElement(By.css('#' + inputPrefix + 'country_id > option:nth-child(2)')).click();
        driver.findElement(By.id(inputPrefix + 'login')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'email')).sendKeys(email[0] + time + email[1], Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'password')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'repeatpassword')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'name')).sendKeys(login, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'surname')).sendKeys(login, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'position')).sendKeys(login + 'position', Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'phone')).sendKeys('+38(098)123-33-44', Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'contact_email')).sendKeys(email[0] + time + email[1], Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'skype')).sendKeys(email[0] + 'skype' + email[1], Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'company_name')).sendKeys(login + 'company_name', Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'code_company')).sendKeys('10000000', Key.RETURN);

        driver.findElement(By.id(inputPrefix + 'documents1')).sendKeys(__dirname+"\\files\\document_1.png");
        driver.findElement(By.id(inputPrefix + 'documents2')).sendKeys(__dirname+"\\files\\document_2.jpg");
        driver.findElement(By.id(inputPrefix + 'documents3')).sendKeys(__dirname+"\\files\\document_3.pdf");

        driver.findElement(By.css('#' + inputPrefix + 'city_id > option:nth-child(2)')).click();
        driver.findElement(By.id(inputPrefix + 'street')).sendKeys(login + 'street', Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'company_site')).sendKeys('http://' + time + '.com', Key.RETURN);
        driver.findElement(By.css('#' + inputPrefix + 'count_employees > option:nth-child(2)')).click();
        driver.findElement(By.id(inputPrefix + 'description_company')).sendKeys(login + 'description_company', Key.RETURN);

        driver.findElement(By.id(inputPrefix + 'logo')).sendKeys(__dirname+"\\files\\logo.png");
        driver.findElement(By.id(inputPrefix + 'cover')).sendKeys(__dirname+"\\files\\cover.png");

        driver.executeScript("document.getElementsByName('CompanyRegistrationForm[get_news]')[0].click()");

        driver.sleep(5000);
        driver.findElement(By.xpath("//button[@class='btn btn-blue']")).click();


    });

});
