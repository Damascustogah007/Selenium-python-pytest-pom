import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(1)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            if lastCount == pageLength:
                match = True

    def wait_for_presence_of_all_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_all_elements_located((locator_type, locator)))

    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.element_to_be_clickable((locator_type, locator)))

    def wait_for_element_to_be_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((locator_type, locator)))
