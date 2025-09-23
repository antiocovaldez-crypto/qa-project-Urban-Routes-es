from selenium.webdriver.common.by import By

class LocatorsCard_CVVPage:
    card_number_input = (By.ID, "number")
    card_code_input = (By.CSS_SELECTOR, 'input[placeholder="12"]')
    add_card_confirm_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")





