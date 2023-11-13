import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_005_mul_window():

    def test_005_multiple_window_handles(self):

        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.get('https://nxtgenaiacademy.com/multiplewindows/') ;

        driver.implicitly_wait(5);

        parenttext = driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]') .text;
        print('\n**********PARENT TAB TEXT*********');
        print(parenttext);

        driver.find_element(By.XPATH, '//button[@name="145newbrowsertab234"]').click();

        select_window=driver.window_handles ;

        driver.switch_to.window(select_window[1]);

        childtext=driver.find_element(By.XPATH, '(//h2[@class="elementor-heading-title elementor-size-default"])[1]').text;
        print('\n**********CHILD TAB TEXT*********');
        print(childtext) ;

        driver.close() ;

        driver.switch_to.window(select_window[0]) ;

        parenttext = driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').text;
        print('\n**********PARENT TAB TEXT*********');
        print(parenttext);

        driver.close() ;

    def test_005_mul_windiw_tab(self):
        driver=webdriver.Chrome();

        driver.maximize_window();

        driver.implicitly_wait(5) ;

        driver.get('https://nxtgenaiacademy.com/multiplewindows/');

        print('\n********PARENT WINDOW TITLE********');
        parenttitle=driver.title;
        print(parenttitle);


        parenttext2 = driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').text;
        print('\n**********PARENT WINDOW TEXT*********');
        print(parenttext2);

        parent_window=driver.current_window_handle;

        driver.find_element(By.XPATH, '//button[@name="newbrowserwindow123"]').click() ;

        select_window2=driver.window_handles ;

        for w in select_window2:
            driver.switch_to.window(w) ;
            if (driver.title=='NxtGen A.I Academy – Automate Intelligently') :

                print('\n********CHILD WINDOW TITLE********');
                childtitle=driver.title ;
                print(childtitle);

                print('\n***********CHILD WINDOW TEXT*********');
                childtext3 = driver.find_element(By.XPATH, '(//h2[@class="elementor-heading-title elementor-size-default"])[1]').text;
                print(childtext3);

                driver.close() ;
                break ;

        driver.switch_to.window(parent_window) ;

        print('\n********PARENT WINDOW TITLE********');
        parenttitle2 = driver.title;
        print(parenttitle2);

        parenttext3 = driver.find_element(By.XPATH, '//h1[@class="elementor-heading-title elementor-size-default"]').text;
        print('\n**********PARENT WINDOW TEXT*********');
        print(parenttext3);

        #driver.close();
        driver.quit() ;





