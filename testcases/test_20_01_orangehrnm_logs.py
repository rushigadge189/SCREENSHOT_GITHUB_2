import logging

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator

class Test_20_log_orange_hrm():

    log=Test_LogGenerator.logger() ;

    def test_20_oange_hrm_logs(self):

        self.log.info("TEST CASE IS STARTED") ;

        self.log.info("OPEN THE BROWSER") ;
        driver=webdriver.Chrome() ;

        self.log.info("MAXIMIZE THE WINDOW") ;
        driver.maximize_window() ;

        self.log.info("IMPLICIT WAIT")
        driver.implicitly_wait(5) ;

        self.log.info("NAVIGATE TO THE ORL") ;
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;

        self.log.info("ENTER THE URL") ;
        driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys('Admin') ;

        self.log.info("ENTER THE PASSWORD") ;
        driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('admin123') ;

        self.log.info("CLICK ON THE LOGIN BUTTON") ;
        driver.find_element(By.XPATH, '//button[text()=" Login "]').click() ;

        try:
            self.log.info("LOOKING FOR AN ELEMENT/PAGE TITLE") ;
            driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']") ;

            logging.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_01_orangehrm_log_pass.png") ;

            self.log.info("PRINTING STATEMENT") ;
            print("\n*******LOGIN SUCCESSFUL*******") ;

            self.log.info("PROCEED FOR LOGOUT") ;
            driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click();
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//a[text()="Logout"]' ) ;
            time.sleep(1) ;

            self.log.info("CLOSE THE BROWSER") ;
            driver.close() ;

            assert True ;

        except:
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_01_orangehrm_log_pass.png");

            print("\n********LOGIN UNSUCCESSFUL********") ;

            self.log.info("CLOSE THE BROWSER") ;
            driver.close() ;
            assert False ;

        self.log.info("TEST CASE IS COMPLETED") ;

