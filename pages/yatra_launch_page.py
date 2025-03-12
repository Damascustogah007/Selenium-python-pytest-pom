import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_driver import BaseDriver


class launchPage(BaseDriver):
    def __init__(self, driver, action):
        super().__init__(driver)
        self.driver = driver
        self.action = action

    def departFrom(self, departLocation):
        depart_from = self.wait_for_element_to_be_clickable(By.XPATH, "//p[contains(text(),'DEL, Indira Gandhi International')]")
        self.action.click(depart_from).perform()
        location = self.wait_for_element_to_be_visible(By.XPATH, f"//div[contains(text(), '{departLocation}')]")
        self.action.click(location).perform()
        time.sleep(2)

    def goingTo(self, destinationState):
        going_to= self.wait_for_element_to_be_clickable(By.XPATH, "//p[contains(text(),'BOM, Chhatrapati Shivaji International')]")
        self.action.click(going_to).perform()
        location = self.wait_for_element_to_be_visible(By.XPATH, f"//div[contains(text(), '{destinationState}')]")
        self.action.click(location).perform()
        time.sleep(3)

    def getDate(self, departure_date):
        date = departure_date.replace('/', ' ')
        day = date.split()

        input_field = self.wait_for_presence_of_all_element(By.XPATH, "//span[@class='css-7rxdpg']")
        self.action.click(input_field[0]).perform()
        time.sleep(3)

        cal_container = self.wait_for_presence_of_all_element(By.XPATH, "//div[@class='react-datepicker__month-container'][1]//div[@class='react-datepicker__week']")
        for date in cal_container:
            if day[0] in date.text:
                date.click()
                break
        time.sleep(3)

    def searchFlight(self, button_name):
        search_button = self.wait_for_presence_of_all_element(By.XPATH, "//div[@class=\"MuiBox-root css-0\"]//button")
        for button in search_button:
            if button_name in button.text:
                self.action.click(button).perform()

        origin_destination = self.wait_for_element_to_be_visible(By.XPATH, "//input[@id=\"origin_0\"]")
        assert origin_destination.is_displayed()






