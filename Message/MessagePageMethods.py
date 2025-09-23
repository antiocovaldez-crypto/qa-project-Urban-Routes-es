from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Message.MessagePageLocators import LocatorsMessagePage

class MethodsMessagePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_message(self, message_input):
        wait = WebDriverWait(self.driver, 10)

        try:
            driver_message_input = wait.until(EC.element_to_be_clickable(LocatorsMessagePage.message_for_driver))
            driver_message_input.clear()
            driver_message_input.send_keys(message_input)
            return True
        except TimeoutException:
            return False
