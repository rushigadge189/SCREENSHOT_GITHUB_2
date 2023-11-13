import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_003_luma_details():

    def test_003_account_details(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.get('https://magento.softwaretestingboard.com/');

        driver.find_element(By.XPATH, "(//a[contains(text(),'Sign In')])[1]").click();

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys('rushigadge189@gmail.com');

        driver.find_element(By.XPATH, '(//input[@id="pass"])[1]').send_keys('@#Rushi@181297') ;
        time.sleep(1);

        driver.find_element(By.XPATH, '(//span[text()="Sign In"])[1]').click() ;
        time.sleep(1) ;

        if(driver.title=="Home Page"):
            time.sleep(1);

            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_003_details_pass.png') ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();

            driver.find_element(By.XPATH, '(//a[text()="My Account"])[1]').click();

            info=driver.find_element(By.XPATH, "//p[contains(text(),'Rushikesh Gadge')]").text ;
            print('\n********ACCOUNT DETAILS********');
            print(info);

            address=driver.find_element(By.XPATH, "(//address[contains(text(),'Rushikesh Gadge')])[1]").text ;
            print('\n**********ADDRESS*******');
            print(address) ;

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out ")])[1]').click();

            driver.close();

            assert True ;

        else:
            driver.save_screenshot('D:\\PYTHON CT15\\REVISION\\screenshots\\test_003_details_fail.png');

            driver.close();

            assert False ;