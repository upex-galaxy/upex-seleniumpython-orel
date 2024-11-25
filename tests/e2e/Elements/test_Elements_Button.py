from tests.e2e.utils.imports import *

# Story GX3-5656
class Test_Elements_Button:
    
    @pytest.fixture
    def web(self):
        """Precondition: Open the demo page and wait for primary button visibility"""
        driver = Chrome()
        driver.get('https://demoqa.com/buttons/')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary"))
        )
    
        yield driver
        driver.quit()
    
    def test_should_display_message_by_left_click(self, web: WebDriver):
        """TC01: Validate that the message 'You have done a dynamic click' is displayed correctly after clicking the 'Click Me' button"""
        button = WebDriverWait(web, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Click Me']"))
        )
        button.click()
        
        message = web.find_element(By.ID, "dynamicClickMessage")
        assert message.text == "You have done a dynamic click"
            
    def test_right_click(self, web: WebDriver):
        """TC02: Validate that the message 'You have done a right click' is displayed correctly after right-clicking the 'Right Click Me' button"""
        button = WebDriverWait(web, 10).until(
            EC.visibility_of_element_located((By.ID, "rightClickBtn"))
        )
        
        actions = ActionChains(web)
        actions.context_click(button).perform()

        message = web.find_element(By.ID, "rightClickMessage")
        assert message.text == "You have done a right click"
        
    def test_double_click(self, web: WebDriver):
        """TC03: Validate that the message 'You have done a double click' is displayed correctly after double-clicking the 'Double Click Me' button"""
        button = WebDriverWait(web, 10).until(
            EC.visibility_of_element_located((By.ID, "doubleClickBtn"))
        )
        
        actions = ActionChains(web)
        actions.double_click(button).perform()

        message = web.find_element(By.ID, "doubleClickMessage")
        assert message.text == "You have done a double click"
        
if __name__ == "__main__":
    pytest.main()