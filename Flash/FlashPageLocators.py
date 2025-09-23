from selenium.webdriver.common.by import By

class LocatorsFlashPage:
    flash_button = (By.XPATH, "//div[contains(@class, 'mode') and text()='Flash']")
    order_taxi_button = (By.XPATH, "//button[contains(@class, 'button round') and contains(text(), 'Pedir un taxi')]")

