import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_008_facebook_dp():

    def test_008_fb_drp_down(self):

        driver=webdriver.Chrome();
        time.sleep(1);

        driver.maximize_window();
        time.sleep(1);

        driver.implicitly_wait(5);
        time.sleep(1) ;

        driver.get('https://www.facebook.com') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//a[@rel="async"]').click() ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@aria-label="First name"]').send_keys('Roman') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Reigns') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@aria-label="Mobile number or email address"]').send_keys('abc123@gmail.com') ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@aria-label="Re-enter email address"]').send_keys('abc123@gmail.com')
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@id="password_step_input"]').send_keys('@#Rushi@181297') ;
        time.sleep(1) ;

        day=Select(driver.find_element(By.XPATH, '//select[@aria-label="Day"]')) ;
        day.select_by_value('5') ;
        time.sleep(1) ;

        month=Select(driver.find_element(By.XPATH, '//select[@aria-label="Month"]')) ;
        month.select_by_index(2) ;
        time.sleep(1) ;

        year=Select(driver.find_element(By.XPATH, '//select[@aria-label="Year"]')) ;
        year.select_by_visible_text("2010") ;
        time.sleep(1) ;

        driver.find_element(By.XPATH, '//input[@value="2"]').click();
        time.sleep(1) ;

        driver.save_screenshot("D:\\PYTHON CT15\\REVISION\\screenshots\\test_008_fb_dropdown_pass.png") ;
        time.sleep(1) ;

        driver.close();