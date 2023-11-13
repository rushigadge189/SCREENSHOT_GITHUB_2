import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_009_mouse_over():

    def test_009_over(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get("https://www.google.com") ;

        driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys('vtiger') ;

        driver.find_element(By.XPATH, '(//input[@value="Google Search"])[1]').click();

        driver.find_element(By.XPATH, '(//h3[@class="LC20lb MBeuO DKV0Md"])[1]').click() ;

        action=ActionChains(driver) ;

        resource_tab=driver.find_element(By.XPATH, '//a[contains(text(),"Resources")]') ;
        action.move_to_element(resource_tab).perform() ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_009_mouseover_pass.png");

        driver.find_element(By.XPATH, "//div[@class='col-4 p-lg-5']//a[@class='list-link'][normalize-space()='Contact Us']").click() ;

        contact=driver.find_element(By.XPATH, '(//div[@class="text-reset text-decoration-none"])[1]').text ;

        print('\n*********CONTACT INFO*********') ;
        print(contact) ;

        driver.close() ;


