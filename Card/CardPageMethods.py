from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Card.CardPageLocators import LocatorsCardPage

class MethodsCardPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_card_button(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            add_card_button = wait.until(EC.element_to_be_clickable(LocatorsCardPage.add_card_button))
            add_card_button.click()
            return True
        except TimeoutException:
            return False






