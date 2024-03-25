import time
from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig


class Test_21_02_testconfig():
    UserName=ReadConfig.getUserName() ;
    Password=ReadConfig.getPassWord() ;

    def test_21_02_testlogin_config(self,setup):

        self.driver=setup ;

        self.driver.get("https://practicetestautomation.com/practice-test-login/") ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(self.UserName) ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.Password) ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//button[text()="Submit"]').click() ;
        time.sleep(1) ;

        try:

            self.driver.find_element(By.XPATH, '//a[contains(text(), "Log out")]') ;

            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_02_test_practice_pass.png") ;

            print('\n********LOGIN SUCCESSFUL********') ;

            text1=self.driver.find_element(By.XPATH, '//strong[text()="Congratulations student. You successfully logged in!"]').text ;
            print(text1) ;

            self.driver.find_element(By.XPATH, '//a[contains(text(), "Log out")]').click() ;


            self.driver.close() ;
            assert True ;




        except:
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_02_test_practice_fail.png") ;
            print("\n********LOGIN UNSUCCESSFUL********") ;
            self.driver.close() ;
            assert False ;


