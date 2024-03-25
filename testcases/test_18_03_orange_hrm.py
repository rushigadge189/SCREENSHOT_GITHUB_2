from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.test_18_03_orangehrm_pages import Test_18_ohrm_pages

class Test_18_02_orangehrm_prg():

    def test_18_02_hrm(self,setup):

        self.driver=setup ;

        self.obj=Test_18_ohrm_pages(self.driver) ;

        self.obj.test_get_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login");

        self.obj.test_enter_username('Admin') ;

        self.obj.test_enter_password('admin123') ;

        self.obj.test_click_login() ;

        self.obj.test_status() ;

        self.wait=WebDriverWait(self.driver, 10, poll_frequency=0.5) ;

        if(self.obj.test_status()==True) :
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//p[@class="oxd-userdropdown-name"]')))
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_03_hrm_pass.png") ;
            print("\n**********LOGIN SUCCESSFUL*********") ;

            self.obj.test_click_menu();

            self.obj.test_click_logout();

            self.driver.close() ;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_03_hrm_fail.png") ;
            print("\n********LOGIN UNSUCCESSFUL*********") ;

            self.driver.close();
