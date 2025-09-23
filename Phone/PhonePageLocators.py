from selenium.webdriver.common.by import By


class LocatorsPhonePage:
    # Campo de entrada del número de teléfono
    phone_input = (By.ID, "phone")

    # Botón "Siguiente"
    next_button = (By.XPATH, "//button[contains(text(), 'Siguiente')]")

    # Label del teléfono (por si lo necesitas)
    phone_label = (By.CSS_SELECTOR, "label[for='phone']")