import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By


class Test_004_handle_alerts():

    def test_004_simple_alert(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get('https://nxtgenaiacademy.com/alertandpopup/') ;

        driver.find_element(By.XPATH, '//button[text()="Alert Box"]').click();

        simplealert=Alert(driver).text ;
        print('\n*********SIMPLE ALERT TEXT*********') ;
        print(simplealert) ;

        Alert(driver).accept();

        driver.close();

    def test_004_confirmation_alert(self):

        driver2=webdriver.Chrome();

        driver2.maximize_window();

        driver2.implicitly_wait(5);

        driver2.get('https://nxtgenaiacademy.com/alertandpopup/') ;

        driver2.find_element(By.XPATH, '//button[@name="confirmalertbox"]').click();

        confirmalert=Alert(driver2).text ;
        print('\n*********CONFIRMATION ALERT TEXT*********');
        print(confirmalert) ;

        Alert(driver2).accept();

        accepttext=driver2.find_element(By.XPATH, '//p[@id="demo"]').text ;
        print('\n*********CONFIRMATION ALERT TEXT AFTER ACCEPT*********');
        print(accepttext) ;

        driver2.find_element(By.XPATH, '//button[@name="confirmalertbox"]').click();

        Alert(driver2).dismiss()

        accepttext = driver2.find_element(By.XPATH, '//p[@id="demo"]').text;
        print('\n*********CONFIRMATION ALERT TEXT AFTER DISMISS*********');
        print(accepttext);

        driver2.close();

    def test_004_prompt_alert(self):

        driver3=webdriver.Chrome() ;

        driver3.maximize_window();

        driver3.implicitly_wait(5);

        driver3.get('https://nxtgenaiacademy.com/alertandpopup/') ;

        driver3.find_element(By.XPATH, '//button[@name="promptalertbox1234"]').click();

        promptalerttext=Alert(driver3).text ;
        print('\n*********PROMPT ALERT TEXT*********');
        print(promptalerttext);

        Alert(driver3).send_keys('YES');


        Alert(driver3).accept();

        promptaccept=driver3.find_element(By.XPATH, '//p[@id="demoone"]').text ;
        print('\n*********PROMPT ALERT TEXT AFTER ACCEPT*********');
        print(promptaccept) ;

        driver3.close();



