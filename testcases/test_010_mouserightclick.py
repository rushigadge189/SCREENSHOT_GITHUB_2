import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_010_mouse_right_click():

    def test_010_right_click(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window();

        driver.implicitly_wait(5);

        driver.get('https://nxtgenaiacademy.com/mouseevent/') ;

        action=ActionChains(driver) ;

        right_click=driver.find_element(By.XPATH, '//button[@id="rightclick"]') ;

        action.context_click(right_click).perform();

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_009_rightclcik_pass.png") ;

        driver.find_element(By.XPATH, '//a[text()="Registration Form"]').click();

        text=driver.find_element(By.XPATH, '//div[@class="copyright_text"]').text ;
        print('\n***********TEXT AFTER RIGHT CLICK*********') ;
        print(text) ;

        driver.close() ;
