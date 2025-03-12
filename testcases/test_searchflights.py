import pytest
from pages.search_flight_result_page import SearchFlightResults
from pages.yatra_launch_page import launchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
       # instantiate the class
       launch = launchPage(self.driver, self.action)
       launch.departFrom('Bangalore, (BLR)')
       launch.goingTo('Chennai, (MAA)')
       launch.getDate("27/03/2023")
       launch.searchFlight('Search')
       search = SearchFlightResults(self.driver)
       search.page_scroll()
       search.filter_flight()
       search.search_all_stops('1 Stop')
       print("Test Passed successfully!!!")




