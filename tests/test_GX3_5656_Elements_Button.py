import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_GX3_5656_Elements_Button:
    def test_left_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        buttons = web.find_elements(By.CSS_SELECTOR, ".btn.btn-primary")
        button = None
        for btn in buttons:
            if btn.text == "Click Me":
                button = btn
                break
        button.click()

        # Verifica que el texto del mensaje es correcto y esta en el id dynamicClickMessage
        message = web.find_element(By.ID, "dynamicClickMessage")
        assert message.text == "You have done a dynamic click"
        
        
    def test_right_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        button = web.find_element(By.ID, "rightClickBtn")
        assert button.text == "Right Click Me"
        
        actions = ActionChains(web)
        actions.context_click(button).perform()

        # Verifica que el texto del mensaje es correcto y esta en el id dynamicClickMessage
        message = web.find_element(By.ID, "rightClickMessage")
        assert message.text == "You have done a right click"
        
    def test_double_click(self, web):
        # Encuentra el botón por su texto y haz clic en él
        button = web.find_element(By.ID, "doubleClickBtn")
        assert button.text == "Double Click Me"
        
        actions = ActionChains(web)
        actions.double_click(button).perform()

        # Verifica que el texto del mensaje es correcto y esta en el id dynamicClickMessage
        message = web.find_element(By.ID, "doubleClickMessage")
        assert message.text == "You have done a double click"

if __name__ == "__main__":
    pytest.main()
