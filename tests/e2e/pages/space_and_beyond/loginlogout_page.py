from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import Page

class LoginLogutPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.web = driver
        
        # localizamos los inputs
        self.user_name_input = lambda: self.web.find_element(By.CSS_SELECTOR, "input[tabindex='1']")
        self.password_input = lambda: self.web.find_element(By.CSS_SELECTOR, "input[tabindex='2']")
        # Localizamos el elemento para hacer click y enviar login
        self.submit_button = lambda: self.web.find_element(By.CSS_SELECTOR, "button[form='login']")
        # Localizamos el dropdown que contiene el mensaje de bienvenida y el nombre
        self.welcome_dropdown = lambda: self.web.find_element(By.CSS_SELECTOR, ".mui-dropdown")
        # Localizamos el mensaje de error del input Username y Password
        self.login_menu = lambda: self.web.find_element(By.CSS_SELECTOR, ".mui-btn--primary")
        self.dropdown_open_logout = lambda: self.web.find_element(By.CSS_SELECTOR, ".mui--is-open")
        

    def open_space_and_beyond_page(self):
        """Carga la página y espera que el botón de submit esté disponible."""
        self.web.get('https://demo.testim.io/login')
        self.helpers.wait_for_element(self.submit_button())
        assert "login" in self.web.current_url, "La URL cargada no es la esperada."
    
    def enter_user_name(self, value: str): # Introducimos el usuario
        self.user_name_input().send_keys(value)
        
    def enter_password(self, value: str): # Introducimos la contraseña
        self.password_input().send_keys(value)
        
    def click_submit_button(self): # Hacemos click en el boton login
        self.submit_button().click()
        
    def get_dropdown_text(self): # Retornamos el texto que tiene almacenado el dropdown
        dropdown = self.welcome_dropdown()
        return dropdown.text
    
    def log_out(self): # Hacemos click en el dropdown button de login y luego hacemos click en el boton logout
        self.login_menu().click()
        log_out = self.dropdown_open_logout()
        self.helpers.wait_for_element(log_out)
        log_out.click()