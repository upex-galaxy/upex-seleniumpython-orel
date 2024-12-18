from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import Page

class RadioButtonsPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.web = driver
        
        # Usamos lambda para retrasar la búsqueda de los elementos hasta que realmente se necesiten.
        self.question = lambda: self.web.find_element(By.CSS_SELECTOR, ".mb-3")   
        
    def open_radio_buttons_page(self):
        """Carga la página Buttons y que el texto 'Do you like the site?' sea visible"""
        self.web.get('https://demoqa.com/radio-button')
        self.helpers.wait_for_element(self.question())
        assert "radio-button" in self.web.current_url, "La URL cargada no es la esperada."