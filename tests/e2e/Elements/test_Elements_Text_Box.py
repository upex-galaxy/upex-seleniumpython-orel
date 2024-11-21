from tests.e2e.utils.imports import *


class TestElementsTextBox:

    @pytest.fixture
    def web(self):
        """Precondition: Open the "demoqa" page and wait for it to load."""
        driver = Chrome()
        driver.get('https://demoqa.com/text-box')
        text_box_page = TextBoxPage(driver)
        text_box_page.wait_for_displaying()
        yield driver
        driver.quit()

    def test_should_display_inserted_information_after_submit(self, web: WebDriver):
        """TC01: Validate that when all inputs are filled correctly and "Submit" is pressed, the inserted information is displayed."""
        text_box_page = TextBoxPage(web)
        
        # Inputs
        user_name = "My Name"
        is_email_valid = "emails@example.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_valid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation
        displayed_data = text_box_page.get_displayed_information()
        assert displayed_data["name"] == f"Name:{user_name}"
        assert displayed_data["email"] == f"Email:{is_email_valid}"
        assert displayed_data["current_address"] == f"Current Address :{current_address}"
        assert displayed_data["permanent_address"] == f"Permananet Address :{permanent_address}"

    def test_no_elements_shown_when_inputs_are_empty(self, web: WebDriver):
        """TC02: Validate that NOTHING is displayed when all inputs are left empty and "Submit" is pressed."""
        text_box_page = TextBoxPage(web)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        stored_name = web.find_elements(By.ID, "name")
        stored_email = web.find_elements(By.ID, "email")
        stored_current_address = web.find_elements(By.CSS_SELECTOR, "p#currentAddress")
        stored_permanent_address = web.find_elements(By.CSS_SELECTOR, "p#permanentAddress")
        
        assert len(stored_name) == 0
        assert len(stored_email) == 0
        assert len(stored_current_address) == 0
        assert len(stored_permanent_address) == 0
        
    def test_email_field_displays_error_for_invalid_email_without_at(self, web: WebDriver):
        """TC03: Validate that an email without "@" is NOT accepted in the Email field and a red border is displayed."""
        text_box_page = TextBoxPage(web)
        # Inputs
        user_name = "My Name"
        is_email_invalid = "emailsexample.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid )
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify the border color of the email field
        email_field = web.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control")
        for _ in range(10): 
            border_color = email_field.value_of_css_property("border-color")  # Obtiene el color del borde
            if border_color == "rgb(255, 0, 0)":  # Si el color es rojo, salimos del bucle
                break
            time.sleep(0.2) 
        assert "rgb(255, 0, 0)" == border_color or "#ff0000" == border_color
        
    def test_email_field_displays_error_for_invalid_email_without_alphanumeric_before_at(self, web: WebDriver):
        """TC04: Validate that an email without an alphanumeric character before "@" is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(web)
        # Inputs
        user_name = "My Name"
        is_email_invalid = "@example.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid )
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify the border color of the email field
        email_field = web.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control")
        for _ in range(10): 
            border_color = email_field.value_of_css_property("border-color")  # Obtiene el color del borde
            if border_color == "rgb(255, 0, 0)":  # Si el color es rojo, salimos del bucle
                break
            time.sleep(0.2) 
        assert "rgb(255, 0, 0)" == border_color or "#ff0000" == border_color
        
    def test_email_field_displays_error_for_invalid_email_without_alphanumeric_after_at(self, web: WebDriver):
        """TC05: Validate that an email without an alphanumeric character after "@" is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(web)
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid )
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify the border color of the email field
        email_field = web.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control")
        for _ in range(10): 
            border_color = email_field.value_of_css_property("border-color")  # Obtiene el color del borde
            if border_color == "rgb(255, 0, 0)":  # Si el color es rojo, salimos del bucle
                break
            time.sleep(0.2) 
        assert "rgb(255, 0, 0)" == border_color or "#ff0000" == border_color        

    def test_email_field_displays_error_for_invalid_email_without_dot_after_at(self, web: WebDriver):
        """TC06: Validate that an email without a "." after "@" is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(web)
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@examplecom"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid )
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify the border color of the email field
        email_field = web.find_element(By.CSS_SELECTOR, "input#userEmail.mr-sm-2.field-error.form-control")
        for _ in range(10): 
            border_color = email_field.value_of_css_property("border-color")  # Obtiene el color del borde
            if border_color == "rgb(255, 0, 0)":  # Si el color es rojo, salimos del bucle
                break
            time.sleep(0.2) 
        assert "rgb(255, 0, 0)" == border_color or "#ff0000" == border_color        

    def test_email_field_displays_error_for_invalid_email_without_two_characters_after_dot(self, web: WebDriver):
        """TC07: Validate that an email without two characters after "." is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(web)
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@example.c"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid )
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify the border color of the email field
        field_state = text_box_page.email_input().get_attribute("class")
        assert "field-error" in field_state

if __name__ == "__main__":
    pytest.main()
