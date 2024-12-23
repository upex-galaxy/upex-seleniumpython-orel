from tests.e2e.pages.demoqa.webtables_page import WebTablesPage

# Story GX3-5779
class Test_Elements_Web_Tables:

    def test_should_add_register_with_valid_inputs(self, driver):
        """TC01: Validate successfully adding a record by entering all inputs with valid data and clicking "Submit"."""
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open_web_tables_page()
        first_name = 'First Name'
        last_name = 'Last Name'
        email = 'orel@example.com'
        age = 5
        salary = 300
        departmant = 'legal'
        initial_element_count = web_tables_page.get_rows_count_in_table()
        web_tables_page.open_registration_form()
        web_tables_page.enter_first_name(first_name)
        web_tables_page.enter_last_name(last_name)
        web_tables_page.enter_email(email)
        web_tables_page.enter_age(age)
        web_tables_page.enter_salary(salary)
        web_tables_page.enter_department(departmant)
        web_tables_page.click_submit_button()
        assert initial_element_count + 1 == web_tables_page.get_rows_count_in_table()


    def test_should_display_results_when_typing_in_search_field(self, driver):
        """TC02: Validate searching for records by entering text in the search field and getting matching results."""
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open_web_tables_page()
        keywords = "alden"
        web_tables_page.enter_search_input(keywords)
        web_tables_page.should_have_value_in_table("alden@example.com")
        

    def test_should_sort_registers_on_column_header_click(self, driver):
        """TC03: Validate sorting records successfully by clicking on column headers."""
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open_web_tables_page()
        employees_unsorted = web_tables_page.get_employee_tabledata()
        web_tables_page.click_first_name_header()
        employees_sorted = web_tables_page.get_employee_tabledata()
        manually_sorted = sorted(employees_unsorted, key=lambda x: x['FirstName'])

        assert manually_sorted == employees_sorted
        
    def test_should_edit_register_and_save_changes(self, driver):
        """TC04: Validate editing an existing record and updating its data after clicking "Submit"."""
        web_tables_page = WebTablesPage(driver)
        web_tables_page.open_web_tables_page()
        
        # full_register_list = web_tables_page.get_employee_tabledata()
        # existing_register = full_register_list["FirstName"]["Cierra"]
        
        # existing_register = web_tables_page.get_edit_button("cierra@example.com")
        # edit_register.click()
        # time.sleep(3)

    def test_should_delete_register_on_delete_button_click(self, driver):
        """TC05: Validate deleting a record from the table by clicking the "Delete" button."""
        pass

    def test_should_change_rows_on_row_option_selection(self, driver):
        """TC06: Validate changing the number of visible records by selecting a row option in pagination."""
        pass

    def test_should_navigate_to_previous_page_on_click(self, driver):
        """TC07: Validate navigating to the previous page using the "Previous" button."""
        pass

    def test_should_navigate_to_next_page_on_click(self, driver):
        """TC08: Validate navigating to the next page using the "Next" button."""
        pass

    def test_should_navigate_to_page_on_number_input(self, driver):
        """TC09: Validate navigating to a specific page using the page number field."""
        pass