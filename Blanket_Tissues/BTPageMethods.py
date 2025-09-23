from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Blanket_Tissues.BTPageLocators import LocatorsBTPage

class MethodsBTPage:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsBTPage()

    def click_blanket_and_tissues_toggle(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            toggle = wait.until(EC.element_to_be_clickable(self.locators.blanket_and_tissues_toggle))
            toggle.click()
            return True
        except TimeoutException:
            return False

    def click_ice_cream_button_twice(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            # Primer helado
            ice_cream_button = wait.until(EC.element_to_be_clickable(self.locators.ice_cream_button))
            ice_cream_button.click()

            # Segundo
            ice_cream_button = wait.until(EC.element_to_be_clickable(self.locators.ice_cream_button))
            ice_cream_button.click()

            return True
        except TimeoutException:
            return False

