from selenium import webdriver
from setuptools.glob import escape

from pages.test_18_04_heroku_pages import Test_18_04_hk

class Test_18_04_herok():

    def test_18_04_herkologin(self,setup):

        self.driver=setup

        obj=Test_18_04_hk(self.driver);

        obj.test_get_url('https://the-internet.herokuapp.com/login') ;

        obj.test_enter_username('tomsmith') ;

        obj.test_enter_password('SuperSecretPassword!') ;

        obj.test_click_login() ;

        if(obj.test_status()==True):
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_04_heroku_pass.png') ;
            print('\n*********LOGIN SUCCESSFUL********') ;

            obj.test_print_login_text();

            obj.test_click_logout();
            self.driver.close() ;

        else:
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_04_heroku_fail.png') ;
            print('\n*********LOGIN UNSUCCESSFUL*********') ;

            self.driver.close() ;