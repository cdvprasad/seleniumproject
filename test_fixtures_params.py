from selenium import webdriver
import pytest
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixtures(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.params =="chrome":
        web_driver = webdriver.Chrome()
    if request.params == 'firefox':
        web_driver = web_driver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixture("init_driver")
class BaseTest:
    pass
class Test_google(BaseTest):
    def test_google_title(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title =="google"

