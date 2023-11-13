import time

from selenium import webdriver


class Test_014_01_addition():

    def test_014_01_add(self):

        a=10 ;
        b=5 ;
        add=a+b ;
        if(add==15) :
            print("\n*********ADDITION IS DONE*********");
            print("RESULT=",add) ;
            assert True ;
        else:
            print("********INVALID OPERATION********") ;
            assert False ;

    def test_014_02(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get("https://magento.softwaretestingboard.com/") ;

        if (driver.title=="Home Page") :

            print ("\n*********YOU ARE AT THE HOME PAGE************") ;

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_url_pass.png") ;

            driver.close() ;

            assert True ;

        else :

            driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_014_02_url_fail.png");

            print("\n*********YOU ARE ENTERED IN WRONG URL******** ") ;

            driver.close() ;

            assert False ;
