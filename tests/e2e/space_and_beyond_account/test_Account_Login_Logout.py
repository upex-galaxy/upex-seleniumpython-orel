from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import os
from tests.e2e.pages.space_and_beyond.loginlogout_page import LoginLogutPage

load_dotenv()

# Story GX3-5635
class Test_Account_Login_Logout:
    
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")    
    
    def test_should_login_successfully_with_valid_credentials(self, driver):
        """TC01: Validate successful login when the credentials are valid."""
        login_page = LoginLogutPage(driver)
        login_page.open_space_and_beyond_page()
        login_page.enter_user_name(self.USERNAME)
        login_page.enter_password(self.PASSWORD)
        login_page.click_submit_button()
        assert "HELLO" in login_page.get_dropdown_text()
        
    def test_should_not_login_with_empty_username(self, driver):
        """TC02: Validate that login cannot be performed when the 'username' field is empty."""
        login_page = LoginLogutPage(driver)
        login_page.open_space_and_beyond_page()
        login_page.enter_user_name("")  
        login_page.enter_password(self.PASSWORD)
        login_page.click_submit_button()
        
        error_message = login_page.driver.find_element(By.CSS_SELECTOR, 'span[class*="hint"] + span[class*="error"]')

        # Verificar el mensaje de error
        
        assert "Password is a required field" not in error_message.text
        assert "Name is a required field" in error_message.text

    def test_should_not_login_with_empty_password(self, driver):
        """TC03: Validate that login cannot be performed when the 'password' field is empty."""
        login_page = LoginLogutPage(driver)
        login_page.open_space_and_beyond_page()
        login_page.enter_user_name(self.USERNAME)
        login_page.enter_password("")  
        login_page.click_submit_button()

        error_message = login_page.driver.find_element(By.CSS_SELECTOR, 'span[class*="hint"] + span[class*="error"]')
        
        # Verificar el mensaje de error
        assert "Name is a required field" not in error_message.text
        assert "Password is a required field" in error_message.text

    def test_should_logout_successfully_when_clicking_logout_button(self, driver):
        """TC04: Validate successful logout when the user clicks the 'Logout' button."""
        login_page = LoginLogutPage(driver)
        login_page.open_space_and_beyond_page()
        login_page.enter_user_name(self.USERNAME)
        login_page.enter_password(self.PASSWORD) 
        login_page.click_submit_button()
        assert "HELLO" in login_page.get_dropdown_text()
        login_page.log_out()
        


