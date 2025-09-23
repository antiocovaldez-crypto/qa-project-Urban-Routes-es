from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Phone.PhonePageLocators import LocatorsPhonePage

class MethodsPhonePage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LocatorsPhonePage()

    def enter_phone_number(self, phone_number):
        # Esperar a que aparezca el campo y escribir el número
        phone_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.phone_input))
        phone_field.clear()

        try:
            phone_field.send_keys(phone_number)
            return True
        except TimeoutException:
            return False

    def click_next_button(self):
        try:
            # Hacer clic en el botón "Siguiente"
            next_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locators.next_button))
            next_btn.click()
            return True
        except TimeoutException:
            return False