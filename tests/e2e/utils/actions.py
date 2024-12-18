# tests/e2e/utils/actions.py

class Actions:
    def __init__(self, driver):
        self.driver = driver

    # Aquí puedes agregar métodos que interactúan con el driver, como hacer clic, escribir, etc.
    def click_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()
