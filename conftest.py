import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.page import Page

# ------ Context Fixture --------
def pytest_addoption(parser: pytest.Parser):
    """Define una opción de línea de comandos para activar el modo headless."""
    parser.addoption(
        '--headless', action='store', default='false',
        help='Ejecución de pruebas en modo headless. Activar usando "true"'
    )

@pytest.fixture(scope='session')
def local_headless(request: pytest.FixtureRequest):
    """Activa el modo headless si se especifica en la línea de comandos."""
    return request.config.getoption('--headless') == 'true'

@pytest.fixture
def driver_options(local_headless):
    """Configura las opciones del navegador para pruebas."""
    options = webdriver.ChromeOptions()
    
    # Opciones para compatibilidad en entornos restringidos o virtuales
    options.add_argument('--no-sandbox')  
    options.add_argument('--disable-dev-shm-usage')  
    
    # Desactiva GPU (necesario para Windows en headless)
    options.add_argument('--disable-gpu')  
    
    # Evita banners y mensajes innecesarios    options.add_argument('--disable-infobars')  
    
    # Configuración para headless
    if local_headless:
        options.add_argument('--headless=new')  
        options.add_argument('--window-size=1920,1080')  
    
    return options

@pytest.fixture(scope='function')
def driver(driver_options):
    """Inicializa el navegador y lo cierra al final del caso de prueba."""
    driver = webdriver.Chrome(options=driver_options)
    yield driver
    driver.quit()


