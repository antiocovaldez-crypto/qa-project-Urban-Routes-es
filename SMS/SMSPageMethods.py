from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SMS.SMSPageLocators import LocatorsSMSPage


class MethodsSMSPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def retrieve_phone_code(self) -> str:
        import json
        import time
        from selenium.common import WebDriverException
        code = None

        for i in range(10):
            print(f"Intento {i + 1} de 10...")
            try:
                logs = [log["message"] for log in self.driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]

                print(f"Encontré {len(logs)} logs con 'api/v1/number?number'")

                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = self.driver.execute_cdp_cmd('Network.getResponseBody',
                                                       {'requestId': message_data["params"]["requestId"]})
                    print(f"Cuerpo de respuesta: {body['body']}")
                    code = ''.join([x for x in body['body'] if x.isdigit()])
                    print(f"Código extraído: {code}")
            except WebDriverException as e:
                print(f"Error: {e}")
                time.sleep(1)
                continue

            if code:
                break
            time.sleep(1)

        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono...")

        return code

    def enter_sms_code_and_confirm(self):
        """Obtiene el código SMS automáticamente y lo introduce en el campo, luego confirma"""
        try:
            # Obtener el código SMS
            sms_code = self.retrieve_phone_code()

            # Esperar a que aparezca el campo de código SMS
            sms_input = self.wait.until(EC.element_to_be_clickable(LocatorsSMSPage.sms_code_input))

            # Introducir el código SMS
            sms_input.send_keys(sms_code)

            # Hacer clic en el botón Confirmar
            confirm_btn = self.wait.until(EC.element_to_be_clickable(LocatorsSMSPage.confirm_button))
            confirm_btn.click()
            return True  # Proceso SMS completado exitosamente

        except TimeoutException:
            return False  # Falló al encontrar elementos

        except Exception:
            return False  # Falló en cualquier otro paso (retrieve_phone_code, etc.)

