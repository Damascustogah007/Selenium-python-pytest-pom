import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    action = ActionChains(driver)
    # wait = WebDriverWait(driver, 10)

    driver.maximize_window()
    driver.get('https://www.yatra.com/')

    request.cls.driver = driver
    # request.cls.wait = wait
    request.cls.action = action

    yield
    driver.quit()