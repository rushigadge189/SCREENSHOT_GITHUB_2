import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_014_04_division():

    def test_014_04_div(self):

        a=10;
        b=5;
        div=a/b ;
        if(div==2):
            print("\n********DIVISION IS COMPLETED********") ;
            print('RESuLT=',div) ;
            assert True ;
        else:
            print("********INVALID OPERATION********") ;
            assert False ;

    def test_014_02_basic_details(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5)

        driver.get('https://magento.softwaretestingboard.com/') ;

        driver.find_element(By.XPATH, '//a[@title="Fusion Backpack"]').click() ;

        if(driver.title=='Fusion Backpack') :
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_14_02_details_pass.png") ;

            text1=driver.find_element(By.XPATH, '(//div[@class="value"])[2]').text ;
            print('\n*********PRODUCT DESCRIPTION********') ;
            print(text1) ;

            driver.close() ;
            assert True ;

        else:

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_14_02_details_fail.png") ;

            print('\n*********SORRY, NOT ABLE TO PROCESS OUR REQUEST**********')
            driver.close() ;

            assert False ;
