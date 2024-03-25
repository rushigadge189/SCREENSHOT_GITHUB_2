import time
from selenium.webdriver.common.by import By
from utilities.logger import Test_logGeneartor


class Test_20_04_logger_swag():

    log=Test_logGeneartor.logger();

    def test_20_04_lo_swag_labs(self,setup):

        self.driver=setup ;

        self.log.info("TEST CASE IS STARTED") ;

        self.log.info("OPENING THE BROWSER") ;

        self.log.info("MAXIMIZE THE BROWSER") ;

        self.log.info("NAVIGAYTE TO THE URL") ;
        self.driver.get('https://www.saucedemo.com/') ;

        self.log.info("ENTERING THE USERNAME") ;
        self.driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys('standard_user') ;

        self.log.info("ENTERING THE PASSWORD") ;
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('secret_sauce') ;

        self.log.info("CLICK ON THE LOGOUT BUTTON") ;
        self.driver.find_element(By.XPATH, '//input[@id="login-button"]').click() ;

        try:
            self.log.info("VERIFYING THE ELEMENT") ;
            self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;

            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_04_swaglabs_pass.png') ;

            self.log.info("PRINTING THE STATUS") ;
            print("\n*********LOGIN SUCCESSFUL********") ;

            self.log.info("LOGOUT") ;
            self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click() ;

            self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click();

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();
            assert True ;

        except:
            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_04_swaglabs_fail.png') ;

            self.log.info("PRINING THE STATSU") ;
            print('\n*********LOGIN UNSUCCESSFUL*******') ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close() ;
            assert False ;
