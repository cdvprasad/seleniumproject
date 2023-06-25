from selenium import webdriver
import time
import pytest

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("---------------------------setup-----------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('http://www.google.com')

    yield
    print("-------------tera down-------------------")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title(init_driver):
    assert driver.title == "Google1"

@pytest.mark.usefixtures("init_driver")
def test_google_url(init_driver):
    assert driver.current_url == 'https://www.google.com/'
