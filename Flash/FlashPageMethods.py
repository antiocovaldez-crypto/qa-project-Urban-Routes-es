from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Flash.FlashPageLocators import LocatorsFlashPage

class MethodsFlashPage:

    def __init__(self, driver):
        self.driver = driver

    def click_flash_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsFlashPage.flash_button))
            self.driver.find_element(*LocatorsFlashPage.flash_button).click()
            return True
        except TimeoutException:
            return False

    def click_order_taxi_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LocatorsFlashPage.order_taxi_button))
            self.driver.find_element(*LocatorsFlashPage.order_taxi_button).click()
            return True
        except TimeoutException:
            return False
