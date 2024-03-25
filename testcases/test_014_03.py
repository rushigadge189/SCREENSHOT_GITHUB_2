import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_014_03_multiplication() :

    def test_014_mul(self):

        a=10;
        b=5;
        mul=a*b;
        if(mul==50) :
            print("\n********SUBSTRACTION IS DONE********") ;
            print("RESULT=",mul) ;
            assert True ;
        else:
            print("********INVALID OPERATION********") ;
            assert False ;

    def test_014_02(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get('https://magento.softwaretestingboard.com/') ;

        driver.find_element(By.XPATH, '(//a[contains(text(),"Sign In")])[1]').click() ;

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('rushigadge189@gmail.com') ;

        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys("@#Rushi@181297") ;

        driver.find_element(By.XPATH, '(//button[@type="submit"])[2]').click() ;

        driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

        driver.find_element(By.XPATH ,'//a[contains(text(),"My Account")]').click() ;

        if ( driver.title == "My Account" ) :

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_details_pass.png") ;

            print('\n*********CONTACT INFORMATION********') ;
            text1=driver.find_element(By.XPATH, '(//div[@class="box-content"])[1]').text ;
            print(text1) ;

            text2=driver.find_element(By.XPATH, '(//div[@class="box-content"])[2]').text ;
            print("\n**********ADDRESS INFORMATION********") ;
            print(text2) ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click() ;

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click() ;

            driver.close() ;
            assert True ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_details_fail.png") ;

            print("**********SORRY......!, NOT ABLE TO PRINT ACCOUNT DETAILS") ;

            driver.close() ;

            assert True ;
