from tests.e2e.pages.demoqa.radiobuttons_page import RadioButtonsPage
from selenium.webdriver.common.by import By
import pytest

# Story GX3-5676
class Test_Elements_Radio_Buttons:
    def test_should_display_message_by_selecting_yes_radio_button(self, driver):
        """TC01: Validate that the message "You have selected Yes" is displayed correctly after selecting the "Yes" radio button."""
        radio_buttons_page = RadioButtonsPage(driver)
        radio_buttons_page.open_radio_buttons_page()
        
        label_for_yes_radio = radio_buttons_page.driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
        label_for_yes_radio.click()
        
        message = radio_buttons_page.driver.find_element(By.CSS_SELECTOR, ".mt-3")
        assert message.text == "You have selected Yes"

    def test_should_display_message_by_selecting_impressive_radio_button(self, driver):
        """TC02: Validate that the message "You have selected Impressive" is displayed correctly after selecting the "Impressive" radio button."""
        radio_buttons_page = RadioButtonsPage(driver)
        radio_buttons_page.open_radio_buttons_page()
        label_for_impressive_radio = radio_buttons_page.driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
        label_for_impressive_radio.click()
        
        message = radio_buttons_page.driver.find_element(By.CSS_SELECTOR, ".mt-3")
        assert message.text == "You have selected Impressive"    

    def test_should_not_select_no_radio_button_with_cursor(self, driver):
        """TC03: Validate that the 'No' radio button cannot be selected by the cursor."""
        radio_buttons_page = RadioButtonsPage(driver)
        radio_buttons_page.open_radio_buttons_page()
        no_radio_button = radio_buttons_page.driver.find_element(By.CSS_SELECTOR, "input#noRadio")
        cursor_style = no_radio_button.value_of_css_property("cursor")

        assert cursor_style == "not-allowed"



if __name__ == "__main__":
    pytest.main()