import time
from selenium.webdriver.common.by import By

from utilities import XUTils
from selenium import webdriver


class Test_19_02_swaglabs():

    def test_19_02_swag_labs(self,setup):

        self.driver=setup ;

        path='D:\\PYTHON CT15\\REVISION\\testdata\\SWAGLABS_DDT.xlsx' ;

        rows=XUTils.getRowCount(path, 'SWAG_LABS');

        for r in range (2, rows+1):

            self.driver.get('https://www.saucedemo.com/') ;
            time.sleep(1) ;

            username=XUTils.readData(path, 'SWAG_LABS', r, 1) ;
            password=XUTils.readData(path, 'SWAG_LABS', r, 2) ;

            self.driver.find_element(By.XPATH, '//input[@id="user-name"]').send_keys(username) ;
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(password) ;
            time.sleep(1) ;

            self.driver.find_element(By.XPATH, '//input[@id="login-button"]').click() ;
            time.sleep(1) ;

            try:
                self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]');
                time.sleep(1);

                self.driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]').click() ;
                time.sleep(1) ;

                self.driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]').click() ;
                time.sleep(1) ;

                print('\n********LOGIN SUCCESSFUL*********');

                XUTils.writeData(path, 'SWAG_LABS', r, 3, 'PASSED')

            except :
                print('\n********LOGIN UNSUCCESSFUL*******') ;
                XUTils.writeData(path, 'SWAG_LABS', r, 3, 'FAILED') ;

        self.driver.close() ;

