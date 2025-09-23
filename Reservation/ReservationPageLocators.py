from selenium.webdriver.common.by import By

class LocatorsReservationPage:
    reservation_button = (By.CLASS_NAME, "smart-button")
    """reservation_button = (By.CSS_SELECTOR, "button.smart-button")
    reservation_button = (By.XPATH, "//button[contains(text(), 'Introducir un número de teléfono y reservar')]")
    reservation_button = (By.XPATH, "//button[@class='smart-button']")"""

    # En tu archivo de localizadores
    """close_modal_button = (By.CLASS_NAME, "close-button")"""
    # O más específico:
    close_modal_button = (By.CSS_SELECTOR, "button.close-button.section-close")
    search_car_modal = (By.XPATH, "//div[contains(text(), 'Buscar automóvil')]")
    arrival_sentence = (By.XPATH, "//div[contains(text(), 'El conductor llegará en')]")












