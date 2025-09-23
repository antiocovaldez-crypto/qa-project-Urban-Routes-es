from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Home.HomePageLocators import LocatorsHomePage
class MethodsHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsHomePage

 #
    def set_route(self, from_address, to_address):
            self.set_from(from_address)
            self.set_to(to_address)

    def set_from(self, from_address):
        wait = WebDriverWait(self.driver, 10)
        from_field = wait.until(EC.presence_of_element_located(self.locators.from_field))
        from_field.clear()
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        wait = WebDriverWait(self.driver, 10)
        to_field = wait.until(EC.presence_of_element_located(self.locators.to_field))
        to_field.clear()
        to_field.send_keys(to_address)

    def get_from(self):
        wait = WebDriverWait(self.driver, 10)
        from_field = wait.until(EC.presence_of_element_located(self.locators.from_field))  # ← Elemento encontrado
        return from_field.get_property('value')  # ← Usa directamente la variable from_field

    def get_to(self):
        wait = WebDriverWait(self.driver, 10)
        to_field = wait.until(EC.presence_of_element_located(self.locators.to_field))
        return to_field.get_property('value')  # ← Usa directamente la variable to_field





