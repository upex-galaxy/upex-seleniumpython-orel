from time import sleep
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShoppingCart:
    @pytest.fixture
    def web(self):
        web = Chrome()
        web.get('https://www.saucedemo.com/')
        
        # Ingresar credenciales y hacer login
        web.find_element(By.CSS_SELECTOR, '[data-test=username]').send_keys('standard_user')
        web.find_element(By.CSS_SELECTOR, '[data-test=password]').send_keys('secret_sauce')
        web.find_element(By.CSS_SELECTOR, '[data-test=login-button]').click()

        # Esperar explícitamente hasta que la página del inventario esté visible
        WebDriverWait(web, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.inventory_list'))
        )
        
        # Una vez que el inventario esté visible, continuamos con el test
        yield web  
        
    def test_1_should_add_item_to_cart(self, web: WebDriver):
        products_to_add_to_cart = web.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        assert len(products_to_add_to_cart) > 0
        #agregamos la cantidad de productos en una variable
        cart_products_list = len(products_to_add_to_cart)
        #con un for, agregamos cada producto al carrito
        for product in products_to_add_to_cart:
            product.click() # Agregar un producto al carrito
    
        # Encontrar el elemento que contiene el número en el ícono del carrito
        cart_icon_badge = web.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
        
        # Convertir el texto del ícono a un número entero
        cart_item_count = int(cart_icon_badge.text)
        
        # Verificar que el número en el ícono del carrito es igual a la cantidad de productos agregados
        assert cart_item_count == cart_products_list, f"Expected {cart_products_list}, but got {cart_item_count}"
        
        web.find_element(By.CSS_SELECTOR, '[data-test=shopping-cart-link]').click() # Ir al carrito
    
        WebDriverWait(web, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.checkout_button')) #verificar que ya estamos en el carrito
        )
    
        products_in_cart = web.find_elements(By.CSS_SELECTOR, '[data-test^="remove"]')
        #verificamos que la cantidad de productos en el carrito es igual a la cantidad de productos agregados
        assert len(products_in_cart) == cart_products_list

#ahora presentare el codigo de un videojuego el cual pide un numero por pantalla y te dice si haz adivinado el numero que se genera de manera aleatoria y se almacena dentro de una variable que luego se compara.
#importamos random para generar un numero aleatorio
import random

#funcion que genera un numero aleatorio entre 1 y 100
def generate_random_number():
        return random.randint(1, 100)
    
    #funcion que pide un numero al usuario y compara con el numero generado aleatoriamente
    def play_game():
        user_number = int(input("Adivina un número entre 1 y 100: ")