# tests/e2e/utils/assertions.py

class Assertions:
    def __init__(self, driver):
        self.driver = driver

    # Ejemplo de aserción
    def verify_element_text(self, locator, expected_text):
        element = self.driver.find_element(*locator)
        assert element.text == expected_text, f"Expected text '{expected_text}', but got '{element.text}'"
