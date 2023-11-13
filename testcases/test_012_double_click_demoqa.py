from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Test_012_doubleclick_demo_qa():

    def test_012_double_click_demo(self):

        driver=webdriver.Chrome() ;

        driver.maximize_window() ;

        driver.implicitly_wait(5) ;

        driver.get("https://demoqa.com/buttons") ;

        double_click=driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]' ) ;

        action=ActionChains(driver) ;

        action.double_click(double_click).perform() ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_012_demoqa_pass.png") ;

        text1=driver. find_element(By.XPATH, '//p[@id="doubleClickMessage"]').text ;
        print('\n*********TEXT AFTER DOUBLE CLICK*********') ;
        print(text1) ;

        driver.close() ;