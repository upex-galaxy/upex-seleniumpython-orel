from selenium.webdriver.common.action_chains import ActionChains
from tests.e2e.pages.demoqa.buttons_page import ButtonsPage
from selenium.webdriver.common.by import By
import pytest


# Story GX3-5656
class Test_Elements_Button:

    def test_should_display_message_by_left_click(self, driver):
        """TC01: Validate that the message 'You have done a dynamic click' is displayed correctly after clicking the 'Click Me' button"""     
        buttons_page = ButtonsPage(driver)
        buttons_page.open_buttons_page()
        
        buttons_page.helpers.wait_for_element(buttons_page.driver.find_element(By.ID, "doubleClickBtn"))
        
        button = buttons_page.locators.get_by_text("Click Me", True)
        button.click()
        
        # Verificar el mensaje que aparece después del clic
        message = buttons_page.driver.find_element(By.ID, "dynamicClickMessage")
        assert message.text == "You have done a dynamic click", "Incorrect message displayed!"

    def test_right_click(self, driver):
        """TC02: Validate that the message 'You have done a right click' is displayed correctly after right-clicking the 'Right Click Me' button"""
        buttons_page = ButtonsPage(driver)
        buttons_page.open_buttons_page()
        
        buttons_page.helpers.wait_for_element(buttons_page.driver.find_element(By.ID, "rightClickBtn"))
        
        # Localizar el botón para clic derecho
        button = buttons_page.driver.find_element(By.ID, "rightClickBtn")
        import time
        time.sleep(1) 
        buttons_page.web.execute_script("arguments[0].scrollIntoView(true);", button)
        # Hacer clic derecho en el botón
        actions = ActionChains(driver)
        actions.context_click(button).perform()    

        # Verificar el mensaje que aparece después del clic derecho
        message = buttons_page.driver.find_element(By.ID, "rightClickMessage")
        assert message.text == "You have done a right click", "Incorrect message displayed!"

    def test_double_click(self, driver):
        """TC03: Validate that the message 'You have done a double click' is displayed correctly after double-clicking the 'Double Click Me' button"""
        buttons_page = ButtonsPage(driver)
        buttons_page.open_buttons_page()
        
        buttons_page.helpers.wait_for_element(buttons_page.driver.find_element(By.ID, "doubleClickBtn"))

        # Localizar el botón para doble clic
        button = buttons_page.driver.find_element(By.ID, "doubleClickBtn")

        # Hacer doble clic en el botón
        actions = ActionChains(driver)
        actions.double_click(button).perform()

        # Verificar el mensaje que aparece después del doble clic
        message = buttons_page.driver.find_element(By.ID, "doubleClickMessage")
        assert message.text == "You have done a double click", "Incorrect message displayed!"

if __name__ == "__main__":
    pytest.main()
