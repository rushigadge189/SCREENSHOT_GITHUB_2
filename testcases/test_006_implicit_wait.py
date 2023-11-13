import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_006_implicitwait():

    def test_006_sync_implicit_wait(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(25) ;

        driver.get('https://www.google.com');

        driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]').send_keys('My Internet Speed') ;

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click() ;

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click() ;
        time.sleep(25) ;

        upload=driver.find_element(By.XPATH, '//p[@jsname="Lk0VKd"]').text ;
        print('\n*********UPLOAD SPEED*********') ;
        print(upload + ' MBPS ') ;

        download=driver.find_element(By.XPATH, '//p[@jsname="dSdcdd"]').text ;
        print('\n*********DOWNLOAD SPEED********') ;
        print(download + ' MBPS ')

        driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_006_impli_pass.png');

        driver.close();