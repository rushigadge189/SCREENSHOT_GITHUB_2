import time
from selenium.webdriver.common.by import By
from utilities.logger import Test_LogGenerator


class Test_20_03_log_heroku():

    log=Test_LogGenerator.logger() ;

    def test_20_03_heroku_logger(self,setup):

        self.log.info("TEST CASE IS STARTED") ;

        print("LOG LEVEL EXAMPLE") ;
        print("******************") ;
        self.log.debug("***THIS IS DEBUG LOG***");
        self.log.info("***THIS IS INFO LOG***");
        self.log.warning("***THIS IS WARNING LOG***") ;
        self.log.error("***THIS IS ERROR LOG***") ;
        self.log.critical("***THIS IS CRITICAL LOG***") ;
        print("******************") ;

        self.driver=setup ;

        self.log.info("OPEN THE BROWSER") ;

        self.log.info("MAXIMIZE THE BROWSER") ;

        self.log.info("NAVIGATION TOWARDS THE URL") ;

        self.driver.get("https://the-internet.herokuapp.com/login") ;

        self.log.info("ENTERIN THE USERNAME") ;
        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith') ;

        self.log.info("ENETRING THE PASSWORD") ;
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!') ;

        self.log.info("CLICK ON THE LOGIN BUTTON") ;
        self.driver.find_element(By.XPATH, '//i[contains(text(), " Login")]').click() ;

        self.log.info("LOOKING FOER AN ELEMENT") ;
        try:
            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]') ;

            self.log.info("PRINTING THE STATUS") ;
            print("\n********LOGIN SUCCESSFUL*******") ;

            self.log.info("TAKING HE SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_03_herku_pass.png") ;

            self.log.info("PRINTING THE WELCOME TEXT") ;
            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text
            print('\n********TEXT AFTER LOGIN********') ;
            print(text1) ;

            self.log.info("CLICK ON LOGOUT BUTTON") ;
            self.driver.find_element(By.XPATH, '//i[text()=" Logout"]').click() ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();

            assert True ;

        except:
            self.log.info("PRINTING THE STATUS") ;
            print("\n********LOGIN UNSUCCESSFUL*******") ;

            self.log.info("TAKING THE SCREENSHOT") ;
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_20_03_herku_fail.png") ;

            self.log.info("CLOSING THE BROWSER") ;
            self.driver.close();

            assert False ;

        self.log.info("TEST CASE IS COMPLETED") ;