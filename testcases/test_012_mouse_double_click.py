import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_012_mouse_double_click():

    def test_012_doubleclick(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5);

        driver.get('https://nxtgenaiacademy.com/mouseevent/') ;

        double_click=driver.find_element(By.XPATH ,'//button[@id="dblclick"]') ;

        action=ActionChains(driver) ;

        action.double_click(double_click).perform() ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_012_rightclick_pass.png") ;

        text1=driver.find_element(By.XPATH, '//p[@id="demo"]').text ;
        print('\n*********TEXT AFTER DOUBLE CLICK*********') ;
        print(text1) ;

        driver.close() ;

