from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Comfort.ComfortPageLocators import LocatorsComfortPage
from Pay_Method.Pay_MethodPageLocators import LocatorsPay_MethodPage

class MethodsPay_MethodPage:
    def __init__(self, driver):
        self.driver = driver

    def click_comfort_button(self):
        wait = WebDriverWait(self.driver, 10)
        comfort_button = wait.until(EC.element_to_be_clickable(LocatorsComfortPage.COMFORT_BUTTON))
        comfort_button.click()

    def click_card_button(self):
        # Hacer clic en la celda "Metodo de pago"
        wait = WebDriverWait(self.driver, 10)

        try:
            card_button = wait.until(EC.element_to_be_clickable(LocatorsPay_MethodPage.card_button))
            card_button.click()
            return True
        except TimeoutException:
            return False