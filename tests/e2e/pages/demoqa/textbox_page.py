from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import SuperPage

class TextBoxPage(SuperPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
        # Usamos lambda para retrasar la búsqueda de los elementos hasta que realmente se necesiten.
        self.user_name_input = lambda: self.web.find_element(By.CSS_SELECTOR, "input#userName")
        self.email_input = lambda: self.web.find_element(By.CSS_SELECTOR, "input#userEmail")
        self.current_address_input = lambda: self.web.find_element(By.CSS_SELECTOR, "textarea#currentAddress")
        self.permanent_address_input = lambda: self.web.find_element(By.CSS_SELECTOR, "textarea#permanentAddress")
        self.submit_button = lambda: self.web.find_element(By.CSS_SELECTOR, "button#submit")
        
    def wait_for_displaying(self):
        assert "text-box" in self.web.current_url
        page_button = self.web.find_element(By.CSS_SELECTOR, ".btn-primary")
        self.wait_for_element(page_button)
        
    def enter_user_name(self, value: str):
        self.user_name_input().send_keys(value)
        
    def enter_email(self, value: str):
        self.email_input().send_keys(value)
        
    def enter_current_address(self, value: str):
        self.current_address_input().send_keys(value)
        
    def enter_permanent_address(self, value: str):
        self.permanent_address_input().send_keys(value)
        
    def click_submit_button(self):
        self.submit_button().click()
        
    def get_displayed_information(self):
        return {
            "name": self.web.find_element(By.ID, "name").text,
            "email": self.web.find_element(By.ID, "email").text,
            "current_address": self.web.find_element(By.CSS_SELECTOR, "p#currentAddress").text,
            "permanent_address": self.web.find_element(By.CSS_SELECTOR, "p#permanentAddress").text,
        }
