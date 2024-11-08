import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Fixture para abrir el navegador
@pytest.fixture
def web():
    driver = Chrome()
    driver.get('https://demoqa.com/buttons/')

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary"))
    )

    yield driver

    driver.quit()
