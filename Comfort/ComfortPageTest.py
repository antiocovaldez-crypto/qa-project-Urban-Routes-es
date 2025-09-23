import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Home.HomePageMethods import MethodsHomePage
from Home.HomePageLocators import LocatorsHomePage
from Flash.FlashPageMethods import MethodsFlashPage  # ← Agregar Flash.
from Flash.FlashPageLocators import LocatorsFlashPage  # ← Agregar Flash.
from ComfortPageMethods import MethodsComfortPage  # ← Esta está bien (mismo directorio)
from ComfortPageLocators import LocatorsComfortPage  # ← Esta también

from selenium import webdriver
import pytest
import data


class TestComfortPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_select_comfort_tariff(self):
        # Usar los métodos de Home para configurar la ruta
        home_page = MethodsHomePage(self.driver)
        home_page.set_route(data.address_from, data.address_to)

        # Ahora usar los métodos de Flash
        flash_page = MethodsFlashPage(self.driver)
        flash_page.click_flash_button()

        #Pedir taxi
        flash_page.click_order_taxi_button()

        # Seleccionar la tarifa Comfort
        comfort_page = MethodsComfortPage(self.driver)
        comfort_page.click_comfort_button()

        # Hacer clic en la celda Numero de teléfono
        comfort_page.click_phone_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()