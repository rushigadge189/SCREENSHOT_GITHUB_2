from selenium.webdriver.common.by import By


class Test_18_luma_pages():
    signin_button=(By.XPATH, '(//a[contains(text(),"Sign In")])[1]')
    username_tf=(By.XPATH, '//input[@id="email"]') ;
    password_tf=(By.XPATH, '(//input[@id="pass"])[1]');
    login_button=(By.XPATH, '(//span[text()="Sign In"])[1]') ;
    arrow_button=(By.XPATH, '/html[1]/body[1]/div[2]/header[1]/div[1]/div[1]/ul[1]/li[2]/span[1]/button[1]') ;
    logout_button=(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_get_url(self,url):
        self.driver.get(url) ;

    def test_click_signin(self):
        self.driver.find_element(*Test_18_luma_pages.signin_button).click() ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_luma_pages.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_luma_pages.password_tf).send_keys(password) ;

    def test_click_login(self):
        self.driver.find_element(*Test_18_luma_pages.login_button).click() ;

    def test_status(self):
        if(self.driver.title=="Home Page"):
            return True ;
        else:
            return False ;

    def test_click_arrow(self):
        self.driver.find_element(*Test_18_luma_pages.arrow_button).click() ;

    def test_logout_button(self):
        self.driver.find_element(*Test_18_luma_pages.logout_button).click() ;
