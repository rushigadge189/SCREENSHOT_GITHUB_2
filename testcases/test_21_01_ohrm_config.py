import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class Test_21_01_orangehrm_config():
    UserName=ReadConfig.getUserName();
    PassWord=ReadConfig.getPassWord() ;

    def test_21_01_oranhge(self):
        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(self.UserName) ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(self.PassWord) ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;
        time.sleep(1) ;

        try:
            driver.find_element(By.XPATH, '//span[@class="oxd-userdropdown-tab"]') ;

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_01_ohrm_pass.png");

            print("\n********LOGIN SUCCESSFUL*******") ;

            driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click() ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//a[text()="Logout"]').click();
            time.sleep(1) ;

            driver.close();
            assert True ;

        except:
                driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_21_01_ohrm_pass.png") ;

                print('\n********LOGIN UNSUCCESSFUL*******') ;

                driver.close() ;
                assert False ;

