from HomePageMethods import MethodsHomePage

import data

class TestHomePage:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import Chrome
        from selenium.webdriver.chrome.options import Options
        # Crear opciones de Chrome
        chrome_options = Options()
        # Habilitar logging de performance
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        # Crear el driver con las opciones
        cls.driver = Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = MethodsHomePage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


