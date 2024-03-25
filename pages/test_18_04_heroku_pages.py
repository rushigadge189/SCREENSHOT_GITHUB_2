from selenium.webdriver.common.by import By


class Test_18_04_hk():
    username_tf=(By.XPATH, '//input[@id="username"]') ;
    password_tf=(By.XPATH, '//input[@id="password"]') ;
    login_button=(By.XPATH, '//i[text()=" Login"]') ;
    login_text=(By.XPATH, '//h4[@class="subheader"]');
    logout_link=(By.XPATH, '//i[contains(text(), " Logout")]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get_url(self,url):
        self.driver.get(url) ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_04_hk.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_04_hk.password_tf).send_keys(password) ;

    def test_click_login(self):
        self.driver.find_element(*Test_18_04_hk.login_button).click() ;

    def test_status(self):
        if (self.driver.title=='The Internet'):
            return True ;

        else:
            return False ;

    def test_print_login_text(self):
        text=self.driver.find_element(*Test_18_04_hk.login_text).text ;
        print('\n*********TEXT AFTER LOGIN********') ;
        print(text) ;

    def test_click_logout(self):
        self.driver.find_element(*Test_18_04_hk.logout_link).click() ;