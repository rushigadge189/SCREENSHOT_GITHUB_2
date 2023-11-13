import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_014_02_substraction():

    def test_014_02_sub(self):

        a=10;
        b=5;
        sub=a-b;
        if(sub==5) :
            print("\n*********SUBSTRACTION IS DONE*********") ;
            print("RESULT=",sub) ;
            assert True ;
        else:
            print("********INBVALID OPERATION") ;
            assert False ;

    def test_014_02(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window() ;

        driver.implicitly_wait(5) ;

        driver.get("https://magento.softwaretestingboard.com/") ;

        driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]').click() ;

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('rushigadge189@gmail.com') ;

        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys('@#Rushi@181297') ;

        driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click() ;
        time.sleep(1) ;

        try:
            driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]') ;

            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_login_pass.png') ;

            print("\n*********LOGIN SUCCESSFUL*******") ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click() ;

            driver.close();

            assert True ;

        except:
            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_login_fail.png') ;

            print('\n********LOGIN UNSUCCESSFUL********') ;

            driver.close();

            assert False ;


