import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import XUTils

class Test_19_01_heroku():

    def test_19_01_ddt_heroku(self):

        driver=webdriver.Chrome() ;
        time.sleep(1) ;

        driver.maximize_window() ;
        time.sleep(1) ;

        driver.implicitly_wait(10) ;


        path="D:\\PYTHON CT15\\REVISION\\testdata\\HEROKU_DDT.xlsx" ;

        rows=XUTils.getRowCount(path, 'HEROKU') ;

        for r in range (2, rows+1) :

            driver.get('https://the-internet.herokuapp.com/login');
            time.sleep(1) ;

            username=XUTils.readData(path,'HEROKU', r, 1) ;
            password=XUTils.readData(path, 'HEROKU', r, 2) ;

            driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(username) ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password) ;
            time.sleep(1) ;

            driver.find_element(By.XPATH, '//i[text()=" Login"]').click() ;
            time.sleep(1) ;

            try:
                driver.find_element(By.XPATH, '//i[text()=" Logout"]') ;

                print('\n**********TEST IS PASSED********') ;

                XUTils.writeData(path, 'HEROKU', r, 3, 'PASSED') ;

            except:
                print('\n********TEST IS FAILED********') ;

                XUTils.writeData(path, 'HEROKU', r, 3, 'FAILED');

        driver.close();



