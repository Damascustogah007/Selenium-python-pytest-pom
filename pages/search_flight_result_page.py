import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from utilities.util import verifyOneStop


class SearchFlightResults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def filter_flight(self):
        wait = WebDriverWait(self.driver, 10)
        one_way = wait.until(ec.visibility_of_element_located((By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']")))
        time.sleep(4)
        assert one_way.is_displayed()

    def search_all_stops(self, stop_type):
        all_stops = self.wait_for_presence_of_all_element(By.XPATH, "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        verifyOneStop.getAllStop(all_stops, stop_type)








