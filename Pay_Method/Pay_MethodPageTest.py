import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Home.HomePageMethods import MethodsHomePage
from Flash.FlashPageMethods import MethodsFlashPage
from Comfort.ComfortPageMethods import MethodsComfortPage
from Pay_Method.Pay_MethodPageMethods import MethodsPay_MethodPage

from selenium import webdriver

import data

class TestPay_MethodPage:
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

        # Hacer clic en la celda Metodo de pago
        pay_method_page = MethodsPay_MethodPage(self.driver)
        pay_method_page.click_card_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()