from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Comfort.ComfortPageLocators import LocatorsComfortPage  # ← AQUÍ está la conexión

class MethodsComfortPage:
    def __init__(self, driver):
        self.driver = driver

    def click_comfort_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            comfort_button = wait.until(EC.element_to_be_clickable(LocatorsComfortPage.COMFORT_BUTTON))
            comfort_button.click()
            return True  # Modal apareció correctamente
        except TimeoutException:
            return False  # Modal no apareció

    def click_phone_button(self):
        try:
            # Hacer clic en la celda "Número de teléfono"
            wait = WebDriverWait(self.driver, 10)
            phone_button = wait.until(EC.element_to_be_clickable(LocatorsComfortPage.phone_button))
            phone_button.click()
            return True
        except TimeoutException:
            return False


