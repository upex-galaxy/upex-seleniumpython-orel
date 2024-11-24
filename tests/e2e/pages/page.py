from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class SuperPage:
    def __init__(self, driver: WebDriver):
        self.web = driver
        
    def wait_for_element(self, element: WebElement, seconds=20): # Espera un tiempo determinado a que el element sea visible.
        """ Espera a que un elemento esté visible """
        is_visible = lambda: element.is_displayed()
        WebDriverWait(self.web, seconds).until(lambda web: is_visible(), message="El elemento no aparece en el tiempo esperado.")
    
    def find_element_by_text(self, text: str) -> WebElement: # Busca un elemento que contenga el texto.
        xpath = f"//*[text()='{text}']" 
        return WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
