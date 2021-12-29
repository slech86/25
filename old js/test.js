
const {Builder, By, Key, until} = require('selenium-webdriver');
const test = require('selenium-webdriver/testing');



test.describe('job seeker registration', async function() {
    let driver;
    let inputPrefix = 'jobseekerregistrationform-';
    let login = 'testLogin_';
    let email = [
        'test.p.verbenec+',
        '@gmail.com',
    ];
    let time = Math.round(+new Date()/1000);
    let urlPage = 'http://logincasino-work/job-seeker/registration';

    test.before(function *() {
        driver = yield new Builder().forBrowser('chrome').build();
        driver.manage().setTimeouts( { implicit: 5000 } );
    });
    const documentInitialised = () =>
        driver.executeScript('return initialised');

    test.it('works with generators', function*() {

        driver.get(urlPage);

        /*  driver.findElement(By.className('login flex-row')).click();
          driver.findElement(By.className('footer-link register-link')).click();*/

        driver.findElement(By.id(inputPrefix + 'login')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'email')).sendKeys(email[0] + time + email[1], Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'password')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'repeatpassword')).sendKeys(login + time, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'name')).sendKeys(login, Key.RETURN);
        driver.findElement(By.id(inputPrefix + 'surname')).sendKeys(login, Key.RETURN);

        driver.findElement(By.css('#' + inputPrefix + 'birthdayy>option:nth-child(2)')).click();
        driver.findElement(By.css('#' + inputPrefix + 'birthdaym>option:nth-child(2)')).click();

        await driver.wait(() => documentInitialised(), 10000);
        driver.findElement(By.css('#' + inputPrefix + 'birthdayd>option:nth-child(2)')).click();
        //driver.findElement(By.css('#' + inputPrefix + 'birthdayd>option:nth-child(2)')).click();

        driver.findElement(By.css('label.modal-radio input[value="2"]')).click();
        driver.executeScript("document.getElementsByName('JobSeekerRegistrationForm[get_news]')[0].click()");

        driver.findElement(By.css('#' + inputPrefix + 'country_id>option:nth-child(2)')).click();

        driver.sleep(2000);

        driver.wait(() => documentInitialised(), 10000);
        driver.findElement(By.css('#' + inputPrefix + 'city_id>option:nth-child(2)')).click();
        //driver.findElement(By.css('#' + inputPrefix + 'city_id>option:nth-child(2)')).click();

        driver.findElement(By.css('#button-registration')).click();
        //driver.findElement(By.xpath("//button[@class='btn btn-blue']")).click();


    });

});
