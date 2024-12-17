from selenium.webdriver.common.by import By
import pytest
from tests.e2e.pages.demoqa.textbox_page import TextBoxPage

# Story GX3-5700
class Test_Elements_Text_Box:
    def test_should_display_inserted_information_after_submit(self, driver):
        """TC01: Validate that when all inputs are filled correctly and "Submit" is pressed, the inserted information is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()
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
        
        # Scroll to the submit button
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        # Esperar a que el campo de correo electrónico esté visible
        text_box_page.helpers.wait_for_element(text_box_page.email_input())
        
        # Validation
        displayed_data = text_box_page.get_displayed_information()
        assert displayed_data["name"] == f"Name:{user_name}"
        assert displayed_data["email"] == f"Email:{is_email_valid}"
        assert displayed_data["current_address"] == f"Current Address :{current_address}"
        assert displayed_data["permanent_address"] == f"Permananet Address :{permanent_address}"


    def test_no_elements_shown_when_inputs_are_empty(self, driver):
        """TC02: Validate that NOTHING is displayed when all inputs are left empty and "Submit" is pressed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()        
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        stored_name = text_box_page.web.find_elements(By.ID, "name")
        stored_email = text_box_page.web.find_elements(By.ID, "email")
        stored_current_address = text_box_page.web.find_elements(By.CSS_SELECTOR, "p#currentAddress")
        stored_permanent_address = text_box_page.web.find_elements(By.CSS_SELECTOR, "p#permanentAddress")
        
        assert len(stored_name) == 0
        assert len(stored_email) == 0
        assert len(stored_current_address) == 0
        assert len(stored_permanent_address) == 0
        
    def test_email_field_displays_error_for_invalid_email_without_at(self, driver):
        """TC03: Validate that an email without "@" is NOT accepted in the Email field and a red border is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()        
        # Inputs
        user_name = "My Name"
        is_email_invalid = "emailsexample.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        # Validation: Verify that the email input field displays an error
        email_field_class = text_box_page.email_input().get_attribute("class")
        assert "field-error" in email_field_class, "The email field did not display a red border for an invalid email"

        
    def test_email_field_displays_error_for_invalid_email_without_alphanumeric_before_at(self, driver):
        """TC04: Validate that an email without an alphanumeric character before "@" is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()        
        # Inputs
        user_name = "My Name"
        is_email_invalid = "@example.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        # Validation: Verify that the email input field displays an error
        email_field_class = text_box_page.email_input().get_attribute("class")
        assert "field-error" in email_field_class, "The email field did not display a red border for an email without alphanumeric characters before '@'"

        
    def test_email_field_displays_error_for_invalid_email_without_alphanumeric_after_at(self, driver):
        """TC05: Validate that an email without an alphanumeric character after "@" is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()        
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@.com"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        # Validation: Verify that the email input field displays an error
        email_field_class = text_box_page.email_input().get_attribute("class")
        assert "field-error" in email_field_class, "The email field did not display a red border for an email without alphanumeric characters after '@'"
    

    def test_email_field_displays_error_for_invalid_email_without_dot_after_at(self, driver):
        """TC06: Validate that an email without a '.' after '@' is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@examplecom"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        # Validation: Verify that the email input field displays an error
        email_field_class = text_box_page.email_input().get_attribute("class")
        assert "field-error" in email_field_class, "The email field did not display a red border for an email without a dot after '@'"

    def test_email_field_displays_error_for_invalid_email_without_two_characters_after_dot(self, driver):
        """TC07: Validate that an email without two characters after '.' is NOT accepted and a red border is displayed."""
        text_box_page = TextBoxPage(driver)
        text_box_page.open_text_box_page()
        # Inputs
        user_name = "My Name"
        is_email_invalid = "email@example.c"
        current_address = "Mi direccion 23/23"
        permanent_address = "Mi direccion 23/23"
        
        # Interaction
        text_box_page.enter_user_name(user_name)
        text_box_page.enter_email(is_email_invalid)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.web.execute_script("arguments[0].scrollIntoView(true);", text_box_page.submit_button())
        text_box_page.click_submit_button()
        
        # Validation: Verify that the email input field displays an error
        email_field_class = text_box_page.email_input().get_attribute("class")
        assert "field-error" in email_field_class, "The email field did not display a red border for an email without two characters after a dot"


if __name__ == "__main__":
    pytest.main()
