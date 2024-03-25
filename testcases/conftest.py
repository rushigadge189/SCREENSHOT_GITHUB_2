import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser") ;


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser");


@pytest.fixture
def setup(browser):
    if(browser=="chrome") :
        print("\n*********RUNNING THE TEST CASE INTO CHROME BROWSER**********") ;
        driver=webdriver.Chrome();
    elif(browser=="edge"):
        print("\n***********RUNNING THE TEST CASE IN EDGE BROWSER***********")
        driver=webdriver.Edge();
    else:
        print("\n***********RUNNING THE TEST CASE IN HEADLESS MODE*********") ;
        chrome_options=webdriver.ChromeOptions();
        chrome_options.add_argument("headless") ;
        driver=webdriver.Chrome(options=chrome_options) ;

    driver.maximize_window();

    driver.implicitly_wait(10) ;

    return driver ;


def pytest_metadata(metadata):
    metadata["CLASS"]="CREDENCE" ;
    metadata["BATCH"]="CT15" ;
    metadata["URL"]="https://credence.in/" ;
    metadata.pop("Platform", None) ;