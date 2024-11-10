import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_GX3_5656_Elements_Button:
    
    @pytest.fixture
    def web(self):
        driver = Chrome()
        driver.get('https://demoqa.com/buttons/')

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary"))
        )
    
        yield driver
        driver.quit()
    
#__________________Prueba #1_________________________
    def test_left_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        button = web.find_element(By.XPATH, "//button[text()='Click Me']")
        button.click()

        # Verifica que el texto del mensaje es correcto
        message = web.find_element(By.ID, "dynamicClickMessage")
        assert message.text == "You have done a dynamic click"
            
#__________________Prueba #2_________________________
    def test_right_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        button = web.find_element(By.ID, "rightClickBtn")
        assert button.text == "Right Click Me"
        
        actions = ActionChains(web)
        actions.context_click(button).perform()

        # Verifica que el texto del mensaje es correcto
        message = web.find_element(By.ID, "rightClickMessage")
        assert message.text == "You have done a right click"
        
#__________________Prueba #3_________________________
    def test_double_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        button = web.find_element(By.ID, "doubleClickBtn")
        assert button.text == "Double Click Me"
        
        actions = ActionChains(web)
        actions.double_click(button).perform()

        # Verifica que el texto del mensaje es correcto
        message = web.find_element(By.ID, "doubleClickMessage")
        assert message.text == "You have done a double click"

if __name__ == "__main__":
    pytest.main()
