from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class Helpers:
    def __init__(self, driver: WebDriver):
        self.driver = driver  # Aquí guardas el driver

    def wait_for_element(self, element: WebElement, seconds=20):
        """ Espera a que un elemento esté visible """
        is_visible = lambda: element.is_displayed()
        WebDriverWait(self.driver, seconds).until(lambda web: is_visible(), message="El elemento no aparece en el tiempo esperado.")
