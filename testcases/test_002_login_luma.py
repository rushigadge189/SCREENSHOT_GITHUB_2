import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_002_loginluma():

    def test_002_lgluma(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.get("https://magento.softwaretestingboard.com/");

        driver.find_element(By.XPATH ,"(//a[contains(text(),'Sign In ')])[1]").click() ;

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('rushigadge189@gmail.com') ;

        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys('@#Rushi@181297') ;

        driver.find_element(By.XPATH, '//span[text()="Sign In"]').click() ;

        if(driver.title=='Home Page') :
            time.sleep(1) ;
            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_002_login_pass.png');
            print('\n********LOGIN SUCCESSFUL********') ;
            text123=driver.find_element(By.XPATH, '//span[@class="logged-in"]').text ;
            print('\nTEXT=',text123) ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, "(//a[contains(text(), 'Sign Out')])[1]").click() ;

            driver.close() ;
            assert True ;

        else:
            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_002_login_fail.png');
            print('\n*********LOGIN UNSUCCESSFUL*******') ;
            driver.close();
            assert False ;