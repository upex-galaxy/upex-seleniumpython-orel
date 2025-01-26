from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Locators:
    def __init__(self, driver: WebDriver):
        """
        Inicializa la instancia de Locator con un controlador web.

        Args:
            driver (WebDriver): Instancia del controlador WebDriver utilizada para interactuar con la página web.
        """
        self.web = driver

    def wait_for_element(self, element: WebElement, seconds=20):
        """Espera a que un elemento esté visible"""
        is_visible = lambda: element.is_displayed()
        WebDriverWait(self.web, seconds).until(lambda web: is_visible(), message="El elemento no aparece en el tiempo esperado.")

    def get_by_text(self, text: str, exact=False, timeout=10):
        """
        Localiza elementos en la página web cuyo texto coincida total o parcialmente y espera su visibilidad.

        Args:
            text (str): Texto a buscar en los elementos.
            exact (bool, opcional): Indica si la búsqueda debe ser exacta (True) o parcial (False). Por defecto es False.
            timeout (int, opcional): Tiempo máximo de espera en segundos. Por defecto es 10.

        Returns:
            WebElement | list[WebElement] | None:
                - Un único elemento si hay una coincidencia.
                - Una lista si hay múltiples coincidencias.
                - None si no se encuentran elementos.
        """
        # Construir el XPath según exactitud
        if exact:
            xpath = f'//*[text()="{text}"]'
        else:
            xpath = f'//*[contains(text(), "{text}")]'

        # Crear la espera explícita
        wait = WebDriverWait(self.web, timeout)

        # Esperar a que al menos un elemento sea visible
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            print(f"El elemento no es visible")

        # Buscar elementos visibles
        elements = self.web.find_elements(By.XPATH, xpath)
        return elements

    # --------------------------------------------------------------------------------------------------------------
    def get_parent_by_text(self, value: str):
        """
        Encuentra el padre de un elemento localizado por su texto.

        Args:
            value (str): Texto contenido en el elemento hijo.

        Returns:
            WebElement | None: El elemento padre del hijo localizado, o None si no se encuentra.
        """
        elemento_hijo = self.get_by_text(value)[0]

        # Intentar obtener el elemento padre
        elemento_padre = elemento_hijo.find_element(By.XPATH, './/parent::*')
        return elemento_padre

    # --------------------------------------------------------------------------------------------------------------
    def get_children_by_text(self, value: str):
        """
        Encuentra los hijos de un elemento localizado por su texto.

        Args:
            value (str): Texto contenido en el elemento padre.

        Returns:
            list[WebElement]: Lista de elementos hijos del padre localizado.
        """
        elemento_padre = self.get_by_text(value)[0]
        self.wait_for_element(elemento_padre)
        return elemento_padre.find_elements(By.XPATH, './/child::*')

    # --------------------------------------------------------------------------------------------------------------
    def get_children(self, parent_element: WebElement):
        """
        Obtiene todos los elementos hijos de un elemento padre especificado.

        Args:
            parent_element (WebElement): El elemento padre del cual se quieren obtener los hijos.

        Returns:
            list[WebElement]: Lista de elementos hijos del padre especificado.
        """
        return parent_element.find_elements(By.XPATH, './/child::*')

    # --------------------------------------------------------------------------------------------------------------
    def get_table_data(self, parent_table: WebElement) -> list[list[str]]:
        """
        Extrae toda la información visible de una tabla HTML.

        Args:
            parent_table (WebElement): Elemento padre que contiene la tabla HTML.

        Returns:
            list[list[str]]: Una lista de listas que contiene los datos visibles de la tabla.
        """

        # Localizar la tabla mediante la clase
        table = parent_table.find_element(By.CSS_SELECTOR, "[role=grid]")

        # Obtener todas las filas dentro de la tabla
        rows = table.find_elements(By.CSS_SELECTOR, "[role=rowgroup] [role=row]:not(.-padRow)")

        table_data = []
        for row in rows:

            if row.is_displayed():
                # Obtener todas las celdas de la fila actual (td o th)
                cells = row.find_elements(By.CSS_SELECTOR, "[role=gridcell]")

                # Extraer el texto de cada celda
                row_data = [cell.text.strip() for cell in cells]
                table_data.append(row_data)

        return table_data


# --------------------------------------------------------------------------------------------------------------
