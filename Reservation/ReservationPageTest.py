import sys
import os



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Reservation.ReservationPageLocators import LocatorsReservationPage
from Home.HomePageMethods import MethodsHomePage
from Flash.FlashPageMethods import MethodsFlashPage
from Comfort.ComfortPageMethods import MethodsComfortPage
from Phone.PhonePageMethods import MethodsPhonePage
from SMS.SMSPageMethods import MethodsSMSPage
from Card.CardPageMethods import MethodsCardPage
from Pay_Method.Pay_MethodPageMethods import MethodsPay_MethodPage
from Card_CVV.Card_CVVPageMethods import MethodsCard_CVVPage
from Message.MessagePageMethods import MethodsMessagePage
from Blanket_Tissues.BTPageMethods import MethodsBTPage

from Reservation.ReservationPageMethods import MethodsReservationPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import data

class TestReservationPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # Configurar opciones de Chrome para habilitar logs
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--enable-logging")
        chrome_options.add_argument("--log-level=0")
        chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.locators = LocatorsReservationPage()


    def test_complete_flow(self):
        # Ejecutar todos los tests en orden
        # Primero ejecuta la configuración de ruta
        self.driver.get(data.urban_routes_url)
        routes_page = MethodsHomePage(self.driver)  # ⬅️ Usa TU driver
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

        flash_page = MethodsFlashPage(self.driver)
        assert flash_page.click_flash_button()
        assert flash_page.click_order_taxi_button()

        comfort_page = MethodsComfortPage(self.driver)
        assert comfort_page.click_comfort_button()
        assert comfort_page.click_phone_button()

        phone_page = MethodsPhonePage(self.driver)
        assert phone_page.enter_phone_number(data.phone_number)
        assert phone_page.click_next_button()

        sms_page = MethodsSMSPage(self.driver)
        #sms_page.retrieve_phone_code()
        assert sms_page.enter_sms_code_and_confirm()

        pay_method_page = MethodsPay_MethodPage(self.driver)
        assert pay_method_page.click_card_button()

        add_card_page = MethodsCardPage(self.driver)
        assert add_card_page.click_add_card_button()

        card_cvv_page = MethodsCard_CVVPage(self.driver)
        assert card_cvv_page.fill_card_number(data.card_number)
        assert card_cvv_page.fill_card_code(data.card_code)  # Ahora el campo CVV debería estar disponible
        assert card_cvv_page.click_add_card_confirm_button()

        reservation_page = MethodsReservationPage(self.driver)
        assert reservation_page.pay_method_add_card_exit_button()

        message_page = MethodsMessagePage(self.driver)
        assert message_page.fill_message(data.message_for_driver)

        bt_page = MethodsBTPage(self.driver)
        assert bt_page.click_blanket_and_tissues_toggle()

        ice_cream_page = MethodsBTPage(self.driver)
        assert ice_cream_page.click_ice_cream_button_twice()

        reservation_page = MethodsReservationPage(self.driver)
        assert reservation_page.test_reservation_modal()

        driver_arrival_page = MethodsReservationPage(self.driver)
        assert driver_arrival_page.wait_for_driver_info_modal()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
