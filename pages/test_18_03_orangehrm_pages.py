from selenium.webdriver.common.by import By


class Test_18_ohrm_pages():

    username_tf=(By.XPATH,'//input[@placeholder="Username"]') ;
    password_tf=(By.XPATH, '//input[@name="password"]') ;
    login_button=(By.XPATH, '//button[@type="submit"]') ;
    menu_tab=(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;
    logout_link=(By.XPATH, '//a[text()="Logout"]') ;

    def __init__(self,driver):
        self.driver=driver ;


    def test_get_url(self,url):
        self.driver.get(url) ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_ohrm_pages.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_ohrm_pages.password_tf).send_keys(password) ;

    def test_click_login(self):
        self.driver.find_element(*Test_18_ohrm_pages.login_button).click() ;

    def test_status(self):
        if(self.driver.title=='OrangeHRM') :
            return True ;
        else:
            return False ;

    def test_click_menu(self) :
        self.driver.find_element(*Test_18_ohrm_pages.menu_tab).click() ;

    def test_click_logout(self) :
        self.driver.find_element(*Test_18_ohrm_pages.logout_link).click() ;



