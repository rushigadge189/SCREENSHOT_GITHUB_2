from pages.test_18_02_swaglab_pages import Test_18_02_swag_lab

class Test_18_02_swag_lab_prg():

    def test_18_02_swaglab_prg(self,setup):

        self.driver=setup ;

        obj=Test_18_02_swag_lab(self.driver) ;

        obj.test_get_url("https://www.saucedemo.com/") ;

        obj.test_enter_username('standard_user') ;

        obj.test_enter_password('secret_sauce') ;

        obj.test_click_login();

        if(obj.test_status()==True):
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_02_swaglabs_pass.png') ;

        else:
            self.driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_18_02_swaglabs_fail.png') ;

        obj.test_click_hamburger_icon() ;

        obj.test_click_logout_buton() ;

        self.driver.close() ;

