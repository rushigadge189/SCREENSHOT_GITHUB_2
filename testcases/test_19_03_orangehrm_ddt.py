import time
from selenium.webdriver.common.by import By

from utilities import XUTils
from selenium import webdriver


class Test_19_03_orangehrm():

    def test_19_03_orange_hrm_ddt(self,setup):

        self.driver=setup ;

        path="D:\\PYTHON CT15\\REVISION\\testdata\\ORANGE_HRM_DDT.xlsx" ;

        rows=XUTils.getRowCount(path, 'ORANGE_HRM') ;

        for r in range(2, rows+1):

            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") ;

            username=XUTils.readData(path, 'ORANGE_HRM', r, 1) ;
            password=XUTils.readData(path, 'ORANGE_HRM', r, 2) ;

            self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys(username) ;

            self.driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(password) ;

            self.driver.find_element(By.XPATH, '//button[@type="submit"]').click() ;

            try:
                self.driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]') ;

                print("\n********LOGIN SUCCESSFUL********");

                XUTils.writeData(path, 'ORANGE_HRM', r, 3, "PASSED");

                self.driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click();

                self.driver.find_element(By.XPATH, '//a[text()="Logout"]').click();

            except:
                print("\n*********LOGIN UNSUCCESSFUL*******");

                XUTils.writeData(path, 'ORANGE_HRM', r, 3, "FAILED") ;

        self.driver.close() ;

