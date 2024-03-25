import time
from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig


class Test_21_03_hero_ku_autoconfig():
    USERNAME=ReadConfig.getUserName();
    PASSWORD=ReadConfig.getPassWord() ;

    def test_21_03_heroku_login(self,setup):

        self.driver=setup ;
        time.sleep(1) ;

        self.driver.get("https://the-internet.herokuapp.com/login") ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(self.USERNAME) ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.PASSWORD) ;
        time.sleep(1) ;

        self.driver.find_element(By.XPATH, '//i[text()=" Login"]').click() ;
        time.sleep(1) ;

        try:
            self.driver.find_element(By.XPATH, '//i[contains(text()," Logout")]') ;
            time.sleep(1) ;

            print("\n********LOGIN SUCCESSFUL*******") ;

            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_03_herku_config_pass.png") ;
            text1=self.driver.find_element(By.XPATH, '//h4[@class="subheader"]').text
            print("\n*********TEXT AFTER LOGIN*********") ;
            print(text1) ;

            self.driver.find_element(By.XPATH, '//i[contains(text()," Logout")]').click();
            time.sleep(1) ;

            self.driver.close();
            assert True ;

        except :

            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_03_herku_config_fail.png") ;

            print("\n********LOGIN UNSUCCESSFUL*********") ;

            self.driver.close() ;
            assert False ;