from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



class Locator:
    def __init__(self, driver: WebDriver):
        """
        Inicializa la instancia de Locator con un controlador web.

        Args:
            driver (WebDriver): Instancia del controlador WebDriver utilizada para interactuar con la página web.
        """
        self.web = driver
    def get_by_text(self, text: str, exact=False):
        """
        Localiza elementos en la página web cuyo texto coincida total o parcialmente.

        Args:
            text (str): Texto a buscar en los elementos.
            exact (bool, opcional): Indica si la búsqueda debe ser exacta (True) o parcial (False). Por defecto es False.

        Returns:
            WebElement | list[WebElement] | None: 
                - Un único elemento si hay una coincidencia.
                - Una lista si hay múltiples coincidencias.
                - None si no se encuentran elementos.
        """
        elements = None
        if exact:
            elements = self.web.find_elements(By.XPATH, f'//*[text()="{text}"]')
        else:
            elements = self.web.find_elements(By.XPATH, f'//*[contains(text(),"{text}")]')
        size = len(elements)
        if size >= 2:
            return elements
        elif size == 1:
            return elements[0]
        else:
            return None
#--------------------------------------------------------------------------------------------------------------
    def get_parent_by_text(self, value: str):
        """
    Encuentra el padre de un elemento localizado por su texto.

    Args:
        value (str): Texto contenido en el elemento hijo.

    Returns:
        WebElement: El elemento padre del hijo localizado.
    """
        elemento_hijo = self.get_by_text(value)
        self.wait_for_element(elemento_hijo)
        return elemento_hijo.find_element(By.XPATH, './/parent::*')
#--------------------------------------------------------------------------------------------------------------
    def get_children_by_text(self, value: str):
        """
    Encuentra los hijos de un elemento localizado por su texto.

    Args:
        value (str): Texto contenido en el elemento padre.

    Returns:
        list[WebElement]: Lista de elementos hijos del padre localizado.
    """
        elemento_padre = self.get_by_text(value)
        self.wait_for_element(elemento_padre)
        return elemento_padre.find_elements(By.XPATH, './/child::*')
#--------------------------------------------------------------------------------------------------------------
    def get_children(self, parent_element: WebElement):
        """
    Obtiene todos los elementos hijos de un elemento padre especificado.

    Args:
        parent_element (WebElement): El elemento padre del cual se quieren obtener los hijos.

    Returns:
        list[WebElement]: Lista de elementos hijos del padre especificado.
    """
        return parent_element.find_elements(By.XPATH, './/child::*')
#--------------------------------------------------------------------------------------------------------------
    def get_table_data(self, parent_table: WebElement)-> list[list[str]]: 
        """
        Extrae toda la información visible de una tabla HTML.

        Args:
            table_class (str): La clase CSS contenedora de las filas y columnas de la tabla.

        Returns:
            list: Una lista de listas que contiene los datos de la tabla que son visibles.
        """

        # Localizar la tabla mediante la clase
        table = parent_table.find_element(By.CSS_SELECTOR, "[role=grid]")

        # Obtener todas las filas dentro de la tabla
        rows = table.find_elements(By.CSS_SELECTOR, "[role=rowgrup] [role=row]:not(.-padRow)")

        table_data = []
        for row in rows:
            
            if row.is_displayed():
                # Obtener todas las celdas de la fila actual (td o th)
                cells = row.find_elements(By.CSS_SELECTOR, "[role=gridcell]")
                
                # Extraer el texto de cada celda
                row_data = [cell.text.strip() for cell in cells]
                table_data.append(row_data)

        return table_data
#--------------------------------------------------------------------------------------------------------------