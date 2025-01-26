import os
import pytest
from tests.api.api_page import Api
from dotenv import load_dotenv


class Test_Elements_Book_Store:
    
    

    @pytest.fixture(scope="class", autouse=True)
    def demoqa_authenticated_user(self):
        """
        Precondición: 
        * El usuario debe estar registrado y autenticado con éxito. 
        * No tiene ningun libro agregado a su libreria. 

        - Crea un nuevo usuario, actualiza las credenciales y genera un token de acceso.
        - Elimina todos los libros agregados, para evitar errores en caso el usuario ya estaba creado.
        """
        api = Api()
        username = 'OrelPrueba'
        password = 'OrelPrueba1234!'
        response_create = api.create_new_user(username, password)
        assert response_create.status_code == 201
        user_id = response_create.json()['userID']  # Obtener el ID del usuario
        api.delete_all_books_by_userid(user_id)
        
        yield api
        
        response_delete = api.delete_user(user_id)  # Eliminar el usuario
        assert response_delete.status_code == 204, f"Error al eliminar el usuario: {response_delete.status_code}"
        
    def test_should_access_book_information_successfully(self, demoqa_authenticated_user: Api):
        """TC01: Validate successfully accessing book information (GET => Status 200)."""
        api = demoqa_authenticated_user
        # Almacenar la lista de libros en la web
        books_from_library = api.get_all_books_from_library()
        # Sacar el isbn del primer libro de la lista
        first_book = books_from_library['books'][0]
        isbn_number = first_book['isbn']
        response = api.get_books_by_isbn(isbn_number)
        assert response.status_code == 200

    def test_should_not_access_book_information_if_isbn_is_empty(self, demoqa_authenticated_user: Api):
        """TC02: Validate failing to access book information when the ISBN is empty (GET => Status 400)."""
        api = demoqa_authenticated_user
        # hacemos la solicitud con un isbn vacio.
        response = api.get_books_by_isbn('')
        assert response.status_code == 400

    def test_should_not_access_book_information_if_isbn_is_incorrect(self, demoqa_authenticated_user: Api):
        """TC03: Validate failing to access book information when the ISBN is incorrect (GET => Status 400)."""
        api = demoqa_authenticated_user
        # hacemos la solicitud con un isbn vacio.
        response = api.get_books_by_isbn('6666666666666')
        assert response.status_code == 400

    def test_should_add_book_to_collection_successfully(self, demoqa_authenticated_user: Api):
        """TC04: Validate successfully adding a book to the collection (POST => Status 200)."""
        api = demoqa_authenticated_user
        user_id = os.getenv('GX2-29004_USERID')
        token = os.getenv('GX2-29004_TOKEN')
        books_from_library = api.get_all_books_from_library()
        isbn_number = books_from_library['books'][0]['isbn']
        response = api.add_book_to_collection(user_id, isbn_number, token)
        assert response.status_code == 201

    def test_should_not_add_book_to_collection_if_userid_is_empty(self, demoqa_authenticated_user: Api):
        """TC05: Validate failing to add a book to the collection when the userId is empty (POST => Status 401)."""
        api = demoqa_authenticated_user
        books_from_library = api.get_all_books_from_library()
        token = os.getenv('GX2-29004_TOKEN')
        isbn_number = books_from_library['books'][0]['isbn']
        response = api.add_book_to_collection('', isbn_number, token)
        assert response.status_code == 401 # El userID proporcionado esta incorrecto o vacio.
        
    def test_should_not_add_book_to_collection_if_userid_is_incorrect(self, demoqa_authenticated_user: Api):
        """TC06: Validate failing to add a book to the collection when the userId is incorrect (POST => Status 401)."""
        api = demoqa_authenticated_user
        books_from_library = api.get_all_books_from_library()
        token = os.getenv('GX2-29004_TOKEN')
        isbn_number = books_from_library['books'][0]['isbn']
        response = api.add_book_to_collection('f000f000-00z0-z000-z000-z00000000000', isbn_number, token)
        assert response.status_code == 401 # El userID proporcionado esta incorrecto o vacio.

    def test_should_not_add_book_to_collection_if_isbn_is_empty(self, demoqa_authenticated_user: Api):
        """TC07: Validate failing to add a book to the collection when the ISBN is empty (POST => Status 400)."""
        api = demoqa_authenticated_user
        user_id = os.getenv('GX2-29004_USERID')
        token = os.getenv('GX2-29004_TOKEN')
        response = api.add_book_to_collection(user_id, '', token)
        assert response.status_code == 400 # ISBN supplied is not available in Books Collection!

    def test_should_not_add_book_to_collection_if_isbn_is_incorrect(self, demoqa_authenticated_user: Api):
        """TC08: Validate failing to add a book to the collection when the ISBN is incorrect (POST => Status 400)."""
        api = demoqa_authenticated_user
        user_id = os.getenv('GX2-29004_USERID')
        token = os.getenv('GX2-29004_TOKEN')
        response = api.add_book_to_collection(user_id, '0101010101010', token)
        assert response.status_code == 400 # ISBN supplied is not available in Books Collection!

    def test_should_not_add_book_to_collection_if_user_is_not_authorized(self, demoqa_authenticated_user: Api):
        """TC9: Validate failing to add a book to the collection when the user is not authorized (POST => Status 401)."""
        api = demoqa_authenticated_user
        user_id = os.getenv('GX2-29004_USERID')
        books_from_library = api.get_all_books_from_library()
        isbn_number = books_from_library['books'][0]['isbn']
        response = api.add_book_to_collection(user_id, isbn_number, '')
        assert response.status_code == 401 # No existe una autorizacion (Falta el token)
            
    def test_should_not_add_duplicate_book_to_collection(self, demoqa_authenticated_user: Api):
        """TC10: Validate failing to add a book that is already in the collection (POST => Status 400)."""
        api = demoqa_authenticated_user
        user_id = os.getenv('GX2-29004_USERID')
        token = os.getenv('GX2-29004_TOKEN')
        api.delete_all_books_by_userid(user_id)

        books_from_library = api.get_all_books_from_library()
        isbn_number = books_from_library['books'][0]['isbn']
        # Agregar el libro a la colección por primera vez
        initial_response = api.add_book_to_collection(user_id, isbn_number, token)
        assert initial_response.status_code == 201  # Validar que se agregó exitosamente

        duplicate_response = api.add_book_to_collection(user_id, isbn_number, token)
        assert duplicate_response.status_code == 400  # Validar que no se puede agregar duplicado


if __name__ == "__main__":
    pytest.main()
