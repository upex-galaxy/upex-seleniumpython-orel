from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import Page

class ButtonsPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.web = driver
        
        # Usamos lambda para retrasar la búsqueda de los elementos hasta que realmente se necesiten.
        self.right_click_btn = lambda: self.web.find_element(By.ID, "rightClickBtn")   
        
    def open_buttons_page(self):
        """Carga la página Buttons y espera que uno de los botones sea visible"""
        self.web.get('https://demoqa.com/buttons/')
        self.helpers.wait_for_element(self.right_click_btn())
        assert "buttons" in self.web.current_url, "La URL cargada no es la esperada."
        