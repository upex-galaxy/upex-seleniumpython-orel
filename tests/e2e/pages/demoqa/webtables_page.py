from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import SuperPage

class WebTablesPage(SuperPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        
        # STATIC lOCATORS
        # ----------------------------------------------------------------
        # ----------------------------------------------------------------
        # Ubica el id del boton "add" utilizado para agregar registros a la tabla
        self.add_button = lambda: self.web.find_element(By.ID, "addNewRecordButton")
        
        # Localizadores fijos para el formulario de registro
        self.first_name_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="First Name"]')
        self.last_name_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
        self.email_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="name@example.com"]')
        self.age_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="Age"]')
        self.salary_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="Salary"]')
        self.department_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'input[placeholder="Department"]')
        # ----------------------------------------------------------------
        # Ubica el id del boton "Submit" insertar el nuevo registro en la tabla
        self.submit_button = lambda: self.web.find_element(By.ID, 'submit')
        
        # Localizador fijo para la barra de busqueda
        self.search_input = lambda: self.web.find_element(By.ID, 'searchBox')
        
        # Localizador de la tabla completa
        self.employee_table = lambda: self.web.find_element(By.XPATH, '//*[contains(@class,"col-12")][*[text()="Web Tables"]]')
        
            
        # Localizadores dinamicos para los encabezados de las columnas de la tabla

        self.first_name_header = lambda: self.get_by_text('First Name')
        self.last_name_header = lambda: self.get_by_text('Last Name')
        self.age_header = lambda: self.get_by_text('Age')
        self.email_header = lambda: self.get_by_text('Email')
        self.salary_header = lambda: self.get_by_text('Salary')
        self.department_header = lambda: self.get_by_text('Department')
        
    # DYNAMIC lOCATORS
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # Ubica el boton edit de un registro especifico en la tabla
    def get_edit_button(self, value: str):
        edit_button = self.get_parent_by_text(value)
        return edit_button.find_element(By.CSS_SELECTOR, 'span[id*="edit-record"]')
        
    # Localizadores dinamicos para los elementos de la paginacion de la tabla
        
        # self.previous_button 
        # self.next_button 
        # self.jump_to_page_input 
        # self.rows_per_page_select 
        
    # ACTIONS
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def get_employee_tabledata(self)-> list[dict]:
        
        table_data = self.get_table_data(self.employee_table())
        employee_tabledata = []
        for row in table_data:
            employee_row_data = {}
            employee_row_data['FirstName'] = row[0]
            employee_row_data['LastName'] = row[1]
            employee_row_data['Age'] = row[2]
            employee_row_data['Email'] = row[3]
            employee_row_data['Salary'] = row[4]
            employee_row_data['Department'] = row[5]
            employee_tabledata.append(employee_row_data)
        return employee_tabledata


    def wait_for_webtables_page(self):
        """
        Espera a que la página de 'webtables' esté cargada y encuentra el botón principal de la página.
        Raises:
            AssertionError: Si la URL actual no contiene 'webtables'.
            NoSuchElementException: Si el botón principal no está presente en la página.
        """
        assert "webtables" in self.web.current_url, "La página actual no es la esperada ('webtables')."
        page_button = self.web.find_element(By.CSS_SELECTOR, ".btn-primary")
        self.wait_for_element(page_button)
    # ----------------------------------------------------------------
    
    # Proporciona un numero entero que representa el numero registros en la tabla
    def get_rows_count_in_table(self):
        elements = self.get_employee_tabledata()
        return len(elements)
    # ----------------------------------------------------------------
    
    # Abre el formulario para añadir un registro a la tabla
    def open_registration_form(self):
        self.add_button().click()
    # ----------------------------------------------------------------
        
    # Acciones (entrar data en los inputs)
    # # Introducir informacion en el formulario de nuevo registro)
    def enter_first_name(self, value: str):
        self.first_name_input().send_keys(value)
    def enter_last_name(self, value: str):
        self.last_name_input().send_keys(value)
    def enter_email(self, value:str):
        self.email_input().send_keys(value)
    def enter_age(self, value: int):
        self.age_input().send_keys(str(value))
    def enter_salary(self, value: int):
        self.salary_input().send_keys(str(value))
    def enter_department(self, value: str):
        self.department_input().send_keys(value)
    # Acciones (submit del formulario)
    def click_submit_button(self):
        self.submit_button().click()
    # Introducir informacion en el input del filtro por palabra clave)
    def enter_search_input(self, value: str):
        self.search_input().send_keys(value)
        
    def add_new_record(self, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
        self.open_registration_form()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_age(age)
        self.enter_salary(salary)
        self.enter_department(department)
        self.click_submit_button()
    # ----------------------------------------------------------------
        
    # Acciones (click en los encabezados)
    def click_first_name_header(self):
        self.first_name_header().click()
    def click_last_name_header(self):
        self.last_name_header().click()
    def click_age_header(self):
        self.age_header().click()
    def click_email_header(self):
        self.email_header().click()
    def click_salary_header(self):
        self.salary_header().click()
    def click_department_header(self):
        self.department_header().click()
    # ----------------------------------------------------------------

    
    # ASSERTIONS
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # Comprueba si dentro de las celdas de cualquiera de las filas visibles de la tabla, existe el valor que se introduce en el buscador
    def should_have_value_in_table(self, value):
        elements = self.get_table_data('rt-table')
        assert any(value in sublist for sublist in elements)

    # ----------------------------------------------------------------