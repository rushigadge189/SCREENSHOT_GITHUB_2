import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_007__explicitwait():

    def test_007_explicit_wait(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get('https://www.google.com') ;

        driver.find_element(By.XPATH,'//textarea[@class="gLFyf"]').send_keys('My Internet Speed') ;

        driver.find_element(By.XPATH, '(//input[@class="gNO89b"])[1]').click();

        driver.find_element(By.XPATH, '//div[text()="RUN SPEED TEST"]').click();

        try:
            wait=WebDriverWait(driver, 30, poll_frequency=0.5) ;
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//div[text()="TEST AGAIN"]'))) ;

            time.sleep(2) ;
            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_007_expli_pass.png');

            upload_speed=driver.find_element(By.XPATH, '//p[@jsname="Lk0VKd"]').text;
            print('\n**********UPLOAD SPEED*********') ;
            print(upload_speed + " MBPS ") ;

            download_speed = driver.find_element(By.XPATH, '//p[@jsname="dSdcdd"]').text;
            print('\n**********DOWNLOAD SPEED*********');
            print(download_speed + " MBPS ");

            driver.close() ;
            assert True ;

        except:
            print('********SOME ERROR OCCURED, PLEASE TRY AGAIN.....!********');

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\expli_fail.png") ;

            driver.close();
            assert False ;

