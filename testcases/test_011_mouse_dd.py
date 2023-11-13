from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_011_dd():

    def test_011_mousedd(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get('https://demoqa.com/droppable/');

        wait=WebDriverWait(driver, 40, poll_frequency=0.5) ;
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//img[@src="/images/Toolsqa.jpg"]'))) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_011_beforedd.png") ;

        action=ActionChains(driver) ;

        src=driver.find_element(By.XPATH, '//div[@id="draggable"]') ;

        dest=driver.find_element(By.XPATH, '(//div[@id="droppable"])[1]') ;

        action.drag_and_drop(src,dest).perform() ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_011_afterdd.png") ;

        driver.close() ;
