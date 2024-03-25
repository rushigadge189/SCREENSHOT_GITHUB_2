from selenium import webdriver

from pages.test_18_01_luma_pages_login import Test_18_luma_pages

class Test_18_lumalogin():

    def test_18_luma_login(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window() ;

        driver.implicitly_wait(10) ;

        obj=Test_18_luma_pages(driver) ;

        obj.test_get_url("https://magento.softwaretestingboard.com/") ;

        obj.test_click_signin() ;

        obj.test_enter_username("rushigadge189@gmail.com") ;

        obj.test_enter_password("@#Rushi@181297") ;

        obj.test_click_login() ;

        if(obj.test_status()==True) :
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_01_luma_pass.png") ;
            print("\n*********LOGIN SUCCESSFUL********") ;
        else:
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_01_luma_fail.png") ;
            print("\n********LOGIN UNSUCCESSFUL*********") ;

        obj.test_click_arrow() ;

        obj.test_logout_button() ;
        driver.close() ;






