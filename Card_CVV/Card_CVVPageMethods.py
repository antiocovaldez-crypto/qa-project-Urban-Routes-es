from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Card_CVV.Card_CVVPageLocators import LocatorsCard_CVVPage

class MethodsCard_CVVPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_card_number(self, card_number):
        wait = WebDriverWait(self.driver, 10)

        try:
            card_input = wait.until(EC.element_to_be_clickable(LocatorsCard_CVVPage.card_number_input))
            card_input.clear()
            card_input.send_keys(card_number)
            card_input.send_keys(Keys.TAB)
            return True  # Número de tarjeta ingresado exitosamente
        except TimeoutException:
            return False  # Falló al ingresar el número de tarjeta

    def fill_card_code(self, card_code):
        wait = WebDriverWait(self.driver, 10)

        try:
            code_input = wait.until(EC.element_to_be_clickable(LocatorsCard_CVVPage.card_code_input))
            code_input.click()  # ← Esta linea activa campo codigo
            code_input.clear()
            code_input.send_keys(card_code)
            code_input.send_keys(Keys.TAB) #Hace que campo CVV pierda enfoque con Tab y pasar a boton "Agregar"
            return True
        except TimeoutException:
            return False

    def click_add_card_confirm_button(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            add_button = wait.until(EC.element_to_be_clickable(LocatorsCard_CVVPage.add_card_confirm_button))
            add_button.click()
            return True
        except TimeoutException:
            return False


