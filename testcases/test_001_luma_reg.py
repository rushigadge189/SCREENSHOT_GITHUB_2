import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001_lumareg():

    def test_001_luma_regestration(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.get("https://magento.softwaretestingboard.com/") ;

        driver.find_element(By.XPATH,'(//a[text()="Create an Account"])[1]').click();

        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys('Rushikesh') ;

        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys('Gadge') ;

        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys('rushigadge189@gmail.com') ;

        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('@#Rushi@181297') ;

        driver.find_element(By.XPATH, '//input[@id="password-confirmation"]').send_keys('@#Rushi@181297') ;

        driver.find_element(By.XPATH, '(//span[contains(text(), "Create an Account")])[1]').click();

        if(driver.title=="My Account") :
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_001_luma_pass.png") ;
            print('\n*********REGESTRATION SUCCESSFUL*********');
            assert True ;
            driver.close() ;

        else :
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_001_luma_fail.png") ;
            print('\n********SOME ERROR OCCURED*******') ;
            assert False ;
            driver.close() ;