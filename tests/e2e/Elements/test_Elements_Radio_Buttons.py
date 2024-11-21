from tests.e2e.utils.imports import *

# Story GX3-5676
class Test_Elements_Radio_Buttons:

    @pytest.fixture
    def web(self):
        """Precondition: open the demo page and wait for the class that stores the text to be seen - Do you like the site? -"""
        driver = Chrome()
        driver.get('https://demoqa.com/radio-button')
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".mb-3"))
        )

        yield driver
        driver.quit()

    def test_should_display_message_by_selecting_yes_radio_button(self, web: WebDriver):
        """TC01: Validate that the message "You have selected Yes" is displayed correctly after selecting the "Yes" radio button."""
        label_for_yes_radio = web.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
        label_for_yes_radio.click()
        
        message = web.find_element(By.CSS_SELECTOR, ".mt-3")
        assert message.text == "You have selected Yes"

    def test_should_display_message_by_selecting_impressive_radio_button(self, web: WebDriver):
        """TC02: Validate that the message "You have selected Impressive" is displayed correctly after selecting the "Impressive" radio button."""
        label_for_impressive_radio = web.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
        label_for_impressive_radio.click()
        
        message = web.find_element(By.CSS_SELECTOR, ".mt-3")
        assert message.text == "You have selected Impressive"    

    def test_should_not_select_no_radio_button_with_cursor(self, web: WebDriver):
        """TC03: Validate that the 'No' radio button cannot be selected by the cursor."""
        no_radio_button = web.find_element(By.CSS_SELECTOR, "input#noRadio")
        cursor_style = no_radio_button.value_of_css_property("cursor")

        assert cursor_style == "not-allowed"



if __name__ == "__main__":
    pytest.main()