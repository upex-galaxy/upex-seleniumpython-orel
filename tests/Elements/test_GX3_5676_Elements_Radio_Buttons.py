from tests.Elements.utils.imports import *


class Test_GX3_5676_Elements_Radio_Buttons:
    
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
    
    def test_left_click(self, web):
        """TC01: Validate that the message 'You have done a dynamic click' is displayed correctly after clicking the 'Click Me' button"""
 