from selenium.webdriver.common.by import By


class LocatorsSMSPage:
    # Campo de entrada del código SMS
    sms_code_input = (By.ID, "code")

    # Botón Confirmar
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")

    # Botón "Vuelve a enviar el código"
    resend_code_button = (By.XPATH, "//button[text()='Vuelve a enviar el código']")

    # Botón cerrar modal (X)
    close_button = (By.CSS_SELECTOR, "button.close-button")