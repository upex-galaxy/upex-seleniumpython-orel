import requests
import os
from dotenv import load_dotenv, set_key

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

class Api:

    def __init__(self):
        self.base_url = 'https://demoqa.com'
        self.api = requests
        # Diccionario con los endpoints disponibles en la API
        self.endpoints = {
            'create_user': '/Account/v1/User',           # Crear usuario
            'authorized_user': '/Account/v1/Authorized', # Verificar autorización
            'delete_user': '/Account/v1/User',           # Eliminar usuario
            'generate_token': '/Account/v1/GenerateToken', # Generar token de acceso
            'books_from_library': '/BookStore/v1/Books', # Obtener lista de libros
            'books_by_isbn': '/BookStore/v1/Book',        # Obtener libro por ISBN
            'delete_all_books': '/BookStore/v1/Books'
        }

    def create_new_user(self, username, password):
        """
        Crea un nuevo usuario en la API, actualiza las credenciales y genera un token de acceso.
        
        """
        url = self.base_url + self.endpoints['create_user']
        request_data = {
            'userName': username, 
            'password': password
        }
        response = self.api.post(url, json=request_data)
        body = response.json()

        if response.status_code == 201:
            user_id = body['userID']
            # Guardar las credenciales y el ID del usuario en el archivo .env
            set_key('.env', 'GX2-29004_USERNAME', username)
            set_key('.env', 'GX2-29004_PASSWORD', password)
            set_key('.env', 'GX2-29004_USERID', user_id)
            # Generar y guardar el token de acceso en el archivo .env
            token = self.set_access_token(username, password)
            set_key('.env', 'GX2-29004_TOKEN', token)
            # Actualizar también las variables de entorno cargadas en memoria
            os.environ['GX2-29004_USERNAME'] = username
            os.environ['GX2-29004_PASSWORD'] = password
            os.environ['GX2-29004_USERID'] = user_id
            os.environ['GX2-29004_TOKEN'] = token
            # Recargar las variables de entorno para asegurarse de que están actualizadas
            load_dotenv()
        return (response)
    
    def set_access_token(self, username, password):
        """
        Genera un token de acceso utilizando las credenciales del usuario.
        
        """
        url = self.base_url + self.endpoints['generate_token']
        request = {
            'userName': username, 
            'password': password
        }
        response = self.api.post(url, json=request)
        token_json = response.json()
        token = token_json['token']
        assert response.status_code == 200, f'Error al obtener el token: {response.status_code}'
        return token
    
    def authorize_user(self, username, password):
        """
        Verifica si un usuario está autorizado utilizando sus credenciales.
        
        """
        url = self.base_url + self.endpoints['authorized_user']
        username = os.getenv('GX2-29004_USERNAME')
        password = os.getenv('GX2-29004_PASSWORD')
        request = {
            'userName': username, 
            'password': password
        }
        response = self.api.post(url, json=request)
        return response
    
    def delete_user(self, user_id):
        """
        Elimina un usuario específico de la API utilizando su ID.
        
        """
        url = f"{self.base_url}{self.endpoints['delete_user']}/{user_id}"
        token = os.getenv('GX2-29004_TOKEN')
        # Incluir el token en los encabezados de la solicitud para autenticación
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = self.api.delete(url, headers=headers)
        return response
    def get_all_books_from_library(self):
        """
        Obtiene una lista de todos los libros disponibles en la biblioteca.
        
        """
        url = self.base_url + self.endpoints['books_from_library']
        response = self.api.get(url)
        # Convertir la respuesta a formato JSON
        body = response.json()
        assert response.status_code == 200, f'Error al obtener la lista de libros: {response.status_code}'
        return body

    def get_books_by_isbn(self, number_isbn):
        """
        Obtiene información de un libro específico utilizando su ISBN.
        
        """
        url = f"{self.base_url}{self.endpoints['books_by_isbn']}?ISBN={number_isbn}"
        # Realizar la solicitud GET al endpoint para obtener el libro
        response = self.api.get(url)
        return response

    def add_book_to_collection(self, user_id, number_isbn, token):
        """
        Agrega un libro a la colección de un usuario.
        
        """
        url = self.base_url + self.endpoints['books_from_library']
        # Crear el cuerpo de la solicitud con el userId y los libros a añadir (usando ISBN)
        request = {
            'userId': user_id,  
            'collectionOfIsbns': [{'isbn': number_isbn}]
        }
        
        # Incluir el token en los encabezados de la solicitud para autenticación
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = self.api.post(url, json=request, headers=headers)
        return response
    
    def delete_all_books_by_userid(self, user_id):
        """
        Elimina todos los libros agregados a la libreria del usuario.
        
        """
        url = f"{self.base_url}{self.endpoints['delete_all_books']}?UserId={user_id}"
        token = os.getenv('GX2-29004_TOKEN')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = self.api.delete(url, headers=headers)
        assert response.status_code == 204
        return response
        
        
