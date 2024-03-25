import time

from selenium import webdriver


class Test_016_ss():

    def test_016_screenshots(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get("https://magento.softwaretestingboard.com/") ;

        if(driver.title=='Home Page'):
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_016_ss_pass.png") ;
            time.sleep(1) ;

            print('\n********YOU ARE AT HOME PAGE*********') ;

            driver.close() ;
            assert True ;

        else:
            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_016_ss_fail.png") ;

            print('\n**********SORRY...! YOU ENTERED WRONG URL*********') ;

            driver.close() ;
            assert False ;

    def test_016_sum(self):

        a=20;
        b=30;
        sum=a+b;
        if(sum==50) :
            print('\n*********TEST IS PASSED********') ;
            print('ADDITION = ',sum) ;
            assert True ;
        else:
            print('\n********TEST IS FAILED*********') ;
            assert False ;