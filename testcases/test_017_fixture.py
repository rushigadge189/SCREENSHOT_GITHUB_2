import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_017_fixture_demo():

    def test_017_01_title(self,setup):

        self.driver=setup ;

        self.driver.get("https://magento.softwaretestingboard.com/") ;

        if(self.driver.title=="Home Page") :
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_017_title_pass.png") ;
            print('\n**********YOU ARE AT THE RIGHT PAGE*********');

            self.driver.close() ;
            assert True ;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_017_title_fail.png");
            print('\n**********SORRY, INVALID URL*********');

            self.driver.close();
            assert False ;


    def test_017_02_login(self,setup):

        self.driver=setup ;

        self.driver.get("https://magento.softwaretestingboard.com/") ;

        self.driver.find_element(By.XPATH, '(//a[contains(text(),"Sign In ")])[1]').click();

        self.driver.find_element(By.XPATH, '//input[@name="login[username]"]').send_keys('rushigadge189@gmail.com') ;

        self.driver.find_element(By.XPATH, '(//input[@type="password"])[1]').send_keys('@#Rushi@181297') ;

        self.driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click() ;

        try:
            self.driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]') ;

            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_017_login_pass.png");

            print('\n**********LOGIN SUCCESSFUL********' ) ;

            info=self.driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]').text ;
            print(info) ;

            self.driver.close();
            assert True ;

        except:
            self.driver.save_screenshot("D:\\PYTHON CT15\REVISION\\screenshots\\test_017_login_fail.png");

            print("\n**********SORRY,LOGIN UNSUCCESSFUL*********") ;

            self.driver.find_element(By.XPATH, '(//button[@class="action switch"])[1]').click();

            self.driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click() ;

            self.driver.close();
            assert False ;


    def test_017_03_details(self,setup):

        self.driver=setup ;

        self.driver.get("https://magento.softwaretestingboard.com/");

        self.driver.find_element(By.XPATH, '(//a[contains(text(),"Sign In ")])[1]').click();

        self.driver.find_element(By.XPATH, '//input[@name="login[username]"]').send_keys('rushigadge189@gmail.com');

        self.driver.find_element(By.XPATH, '(//input[@type="password"])[1]').send_keys('@#Rushi@181297');

        self.driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click();

        self.driver.find_element(By.XPATH, '(//button[@class="action switch"])[1]').click();

        self.driver.find_element(By.XPATH, '(//a[text()="My Account"])[1]').click();

        if(self.driver.title=="My Account") :
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_017_details_pass.png") ;

            print("\n**********DETAILS PRINTED SUCCESSFULLY*******") ;

            details=self.driver.find_element(By.XPATH, '(//div[@class="box-content"])[2]').text ;
            print(details) ;

            self.driver.find_element(By.XPATH, '(//button[@class="action switch"])[1]').click();

            self.driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click() ;

            self.driver.close();
            assert True;

        else:
            self.driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_017_details_fail.png") ;

            print("\n*********SORRY, UNABLE TO PRINT DETAILS*******");

            self.driver.close();
            assert False ;







