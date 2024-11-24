from tests.e2e.utils.imports import *
from dotenv import load_dotenv
import os
from tests.e2e.pages.loginlogout_page import LoginLogutPage

# Story GX3-5635
class Test_Account_Login_Logout:
    
    @pytest.fixture
    def web(self):
        """Precondition: Navigate to the login page and ensure the user has an existing account on the website."""
        driver = Chrome()
        load_dotenv()
        driver.get('https://demo.testim.io/login')
        login_page = LoginLogutPage(driver)
        login_page.wait_for_displaying()
        USERNAME = os.getenv("USERNAME")
        PASSWORD = os.getenv("PASSWORD")    
        yield driver
        driver.quit()
    def test_should_login_successfully_with_valid_credentials(self, web: WebDriver):
        """TC01: Validate successful login when the credentials are valid."""
        login_page = LoginLogutPage(web)
        login_page.enter_user_name("USERNAME")
        login_page.enter_password("PASSWORD")
        login_page.click_submit_button()
        assert "HELLO" in login_page.get_dropdown_text()
        
    def test_should_not_login_with_empty_username(self, web: WebDriver):
        """TC02: Validate that login cannot be performed when the 'username' field is empty."""
        login_page = LoginLogutPage(web)
        login_page.enter_user_name("")  
        login_page.enter_password("PASSWORD")  
        login_page.click_submit_button()
        
        error_message = web.find_element(By.CSS_SELECTOR, 
            'span.theme__hint___2D9g- + span.theme__error___3ilni')
        # Verificar el mensaje de error
        
        assert "Password is a required field" not in error_message.text
        assert "Name is a required field" in error_message.text

    def test_should_not_login_with_empty_password(self, web: WebDriver):
        """TC03: Validate that login cannot be performed when the 'password' field is empty."""
        login_page = LoginLogutPage(web)
        login_page.enter_user_name("USERNAME") 
        login_page.enter_password("")  
        login_page.click_submit_button()

        error_message = web.find_element(By.CSS_SELECTOR, 
            'span.theme__hint___2D9g- + span.theme__error___3ilni')
        # Verificar el mensaje de error
        assert "Name is a required field" not in error_message.text
        assert "Password is a required field" in error_message.text

    def test_should_logout_successfully_when_clicking_logout_button(self, web: WebDriver):
        """TC04: Validate successful logout when the user clicks the 'Logout' button."""
        login_page = LoginLogutPage(web)
        login_page.enter_user_name("USERNAME")
        login_page.enter_password("PASSWORD")  
        login_page.click_submit_button()
        assert "HELLO" in login_page.get_dropdown_text()
        login_page.log_out()
        


