import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator

class Test_20_luma_logger():

    log=Test_LogGenerator.logger();

    def test_20_log_luma(self):

        self.log.info("TEST CASE IS STARTED") ;

        self.log.info("OPENING THE BROWSER") ;
        driver=webdriver.Chrome();

        self.log.info("MAXIMIZE THE WINDOW") ;
        driver.maximize_window() ;

        driver.implicitly_wait(10) ;

        self.log.info("NAVIGATE TO THE URL") ;
        driver.get("https://magento.softwaretestingboard.com/") ;

        self.log.info("CLICK ON THE SIGN IN") ;
        driver.find_element(By.XPATH ,'(//a[contains(text(),"Sign In")])[1]').click();

        self.log.info("ENTERING THE USERNAME") ;
        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('rushigadge189@gmail.com') ;

        self.log.info("ENTERING THE PASSWORD") ;
        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys('@#Rushi@181297') ;

        self.log.info("CLICK ON THE SUBMIT BUTTON") ;
        driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click() ;

        self.log.info("VERIFY THE TITLE") ;
        if (driver.title=="Home Page") :

            self.log.info("LOGIN PASSED") ;
            print("\n*********LOGIN SUCCESSFUl********")

            self.log.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_02_luma_logs_pass.png") ;


            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, '(//a[text()="My Account"])[1]').click() ;

            self.log.info("PRINTING THE ACCOUNT DETAILS") ;

            print("\n*********ACCOUNT DETAILS********") ;
            info1=driver.find_element(By.XPATH, '(//div[@class="box-content"])[2]').text ;
            print(info1) ;

            self.log.info("LOGOUT") ;
            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]') ;

            self.log.info("CLSING THE BROWSER") ;
            driver.close();

            assert True ;
        else:

            self.log.info("LOGIN FAILED")
            print("\n*********LOGIN UNSUCCESSFUL*******") ;

            self.log.info("TAKING THE SCREENSHOT") ;
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_02_luma_logs_pass.png") ;

            self.log.info("CLOSING THE BROWSER")
            driver.close() ;

            assert False ;

        self.log.info("TEST CASE IS COMPLETED") ;





