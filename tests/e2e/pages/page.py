from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from tests.e2e.utils.locators import Locator

class SuperPage(Locator):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
    def wait_for_element(self, element: WebElement, seconds=20): 
        """ Espera a que un elemento esté visible """
        is_visible = lambda: element.is_displayed()
        WebDriverWait(self.web, seconds).until(lambda web: is_visible(), message="El elemento no aparece en el tiempo esperado.")
    

