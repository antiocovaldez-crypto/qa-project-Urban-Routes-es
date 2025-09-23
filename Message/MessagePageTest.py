import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Home.HomePageMethods import MethodsHomePage
from Flash.FlashPageMethods import MethodsFlashPage
from Comfort.ComfortPageMethods import MethodsComfortPage
from Message.MessagePageMethods import MethodsMessagePage

from selenium import webdriver
import data

class TestMessagePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_fill_card_data(self):
        home_page = MethodsHomePage(self.driver)
        home_page.set_route(data.address_from, data.address_to)

        flash_page = MethodsFlashPage(self.driver)
        flash_page.click_flash_button()
        flash_page.click_order_taxi_button()

        comfort_page = MethodsComfortPage(self.driver)
        comfort_page.click_comfort_button()

        message_page = MethodsMessagePage(self.driver)
        message_page.fill_message(data.message_for_driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()