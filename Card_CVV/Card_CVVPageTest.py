import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Home.HomePageMethods import MethodsHomePage
from Flash.FlashPageMethods import MethodsFlashPage
from Comfort.ComfortPageMethods import MethodsComfortPage
from Card.CardPageMethods import MethodsCardPage
from Pay_Method.Pay_MethodPageMethods import MethodsPay_MethodPage
from Card_CVV.Card_CVVPageMethods import MethodsCard_CVVPage

from selenium import webdriver
import data

class TestCard_CVVPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.urban_routes_url)

    def test_fill_card_data(self):
        # Flujo completo hasta abrir el modal de agregar tarjeta
        home_page = MethodsHomePage(self.driver)
        home_page.set_route(data.address_from, data.address_to)

        flash_page = MethodsFlashPage(self.driver)
        flash_page.click_flash_button()
        flash_page.click_order_taxi_button()

        comfort_page = MethodsComfortPage(self.driver)
        comfort_page.click_comfort_button()

        pay_method_page = MethodsPay_MethodPage(self.driver)
        pay_method_page.click_card_button()

        add_card_page = MethodsCardPage(self.driver)
        add_card_page.click_add_card_button()

        card_cvv_page = MethodsCard_CVVPage(self.driver)
        card_cvv_page.fill_card_number(data.card_number)
        card_cvv_page.fill_card_code(data.card_code)
        card_cvv_page.click_add_card_confirm_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()