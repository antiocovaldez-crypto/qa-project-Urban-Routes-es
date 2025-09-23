from selenium.webdriver.common.by import By

class LocatorsComfortPage:
    COMFORT_BUTTON = (By.XPATH, "//div[contains(text(), 'Comfort')]")
    COMFORT_SELECTED = (By.XPATH, "//div[contains(@class, 'tcard active') and contains(text(), 'Comfort')]")
    phone_button = (By.CLASS_NAME, "np-text")  # El botón "Número de teléfono"

