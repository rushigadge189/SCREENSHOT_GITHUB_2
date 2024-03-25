import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_drop_down():

    def test_008_dropdown(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5);

        driver.get('https://www.careinsurance.com/rhicl/proposalcp/renew/index-care');

        driver.find_element(By.XPATH, '//input[@placeholder="Policy Number"]').send_keys('1234567890') ;

        driver.find_element(By.XPATH, '//input[@placeholder="DOB"]').click();

        month=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-month"]')) ;
        month.select_by_visible_text("Jul") ;

        year=Select(driver.find_element(By.XPATH, '//select[@class="ui-datepicker-year"]')) ;
        year.select_by_value('2023');

        driver.find_element(By.XPATH, '//a[text()="6"]').click() ;

        driver.find_element(By.XPATH, '//input[@placeholder="Contact Number"]').send_keys('123456789') ;

        driver.save_screenshot("D:\PYTHON CT15\REVISION\screenshots\\test_008_dropdown_pass.png") ;

        driver.close() ;