import time
from selenium.webdriver.common.by import By

from utilities import XUTils
from selenium import webdriver


class Test_19_04_pa():

    def test_19_04_pa_ddt(self):

        driver=webdriver.Chrome();
        time.sleep(1) ;

        driver.maximize_window();
        time.sleep(1) ;

        driver.implicitly_wait(10) ;

        path="D:\\PYTHON CT15\\REVISION\\testdata\\PRACTISE_AUTOMATION_ddt.xlsx" ;

        rows=XUTils.getRowCount(path, 'PA') ;

        for r in range (2, rows+1) :

            driver.get("https://practicetestautomation.com/practice-test-login/") ;
            time.sleep(1) ;

            username=XUTils.readData(path, 'PA', r, 1) ;
            password=XUTils.readData(path, 'PA', r, 2) ;

            driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(username) ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password);
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//button[@id="submit"]').click() ;
            time.sleep(1) ;

            try:
                driver.find_element(By.XPATH, '//a[@class="wp-block-button__link has-text-color has-background has-very-dark-gray-background-color"]') ;

                print("\n**********LOGIN SUCCESSFUL*************") ;

                XUTils.writeData(path, 'PA', r, 3, 'PASSED' ) ;

                driver.find_element(By.XPATH, '//a[@class="wp-block-button__link has-text-color has-background has-very-dark-gray-background-color"]').click() ;
                time.sleep(1) ;

            except :

                print("\n**********LOGIN UNSUCCESSFUL********") ;

                XUTils.writeData(path, 'PA', r, 3, 'FAILED') ;


        driver.close() ;



