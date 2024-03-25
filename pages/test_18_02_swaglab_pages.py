from selenium.webdriver.common.by import By


class Test_18_02_swag_lab():

    username_tf=(By.XPATH, '//input[@id="user-name"]') ;
    password_tf=(By.XPATH, '//input[@id="password"]') ;
    login_button=(By.XPATH, '//input[@value="Login"]') ;
    hamburger_icon=(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;
    logout_button=(By.XPATH, '//a[@id="logout_sidebar_link"]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get_url(self,url):
        self.driver.get(url) ;

    def test_enter_username(self, username):
        self.driver.find_element(*Test_18_02_swag_lab.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_02_swag_lab.password_tf).send_keys(password) ;

    def test_click_login(self):
        self.driver.find_element(*Test_18_02_swag_lab.login_button).click() ;

    def test_status(self):
        try:
            self.driver.find_element(*Test_18_02_swag_lab.hamburger_icon) ;
            print('\n*********LOGIN SUCCESSFUL*********') ;
            return True ;

        except :
            print('\n*********LOGIN UNSUCCESSFUL*********') ;
            return False ;

    def test_click_hamburger_icon(self):
        self.driver.find_element(*Test_18_02_swag_lab.hamburger_icon).click() ;

    def test_click_logout_buton(self):
        self.driver.find_element(*Test_18_02_swag_lab.logout_button).click() ;


