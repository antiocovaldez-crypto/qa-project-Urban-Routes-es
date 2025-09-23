from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Reservation.ReservationPageLocators import LocatorsReservationPage

class MethodsReservationPage:
    def __init__(self, driver):
            self.driver = driver
            self.locators = LocatorsReservationPage()

    def pay_method_add_card_exit_button(self):
        import time
        time.sleep(2)

        selector = (By.CSS_SELECTOR, "button.close-button.section-close")
        elements = self.driver.find_elements(*selector)

        for element in elements:
            if element.is_displayed() and element.is_enabled():
                try:
                    element.click()
                    return True  # ✅ Botón X clickeado exitosamente
                except Exception:
                    continue

        return False  # ❌ No se pudo cerrar el modal

    def test_reservation_modal(self):
        wait = WebDriverWait(self.driver, 20)
        reservation_button = wait.until(EC.element_to_be_clickable(self.locators.reservation_button))
        reservation_button.click()
        try:
            reservation_button = wait.until(EC.visibility_of_element_located(self.locators.reservation_button))
            return True  # Modal apareció correctamente
        except TimeoutException:
            return False  # Modal no apareció

    def wait_for_driver_info_modal(self):
        # Paso 1: Verificar que aparece el modal "Buscar automóvil"
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locators.search_car_modal))

        # Paso 2: Esperar a que desaparezca el modal "Buscar automóvil" (máximo 40 seg)
        WebDriverWait(self.driver, 40).until_not(EC.presence_of_element_located(self.locators.search_car_modal))

        # Paso 3: Verificar que aparece "El conductor llegará en..."
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locators.arrival_sentence))

        # Paso 4: Retornar si el elemento está visible
        return self.driver.find_element(*self.locators.arrival_sentence).is_displayed()



