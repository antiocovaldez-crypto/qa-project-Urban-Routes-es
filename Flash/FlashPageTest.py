import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Home.HomePageMethods import MethodsHomePage

from selenium import webdriver
from FlashPageMethods import MethodsFlashPage
from FlashPageLocators import LocatorsFlashPage
import pytest
import data


class TestFlashPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_flash_functionality(self):
        # Usar los métodos de Home para configurar la ruta
        home_page = MethodsHomePage(self.driver)
        home_page.set_route(data.address_from, data.address_to)

        # Ahora usar los métodos de Flash
        flash_page = MethodsFlashPage(self.driver)
        flash_page.click_flash_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
