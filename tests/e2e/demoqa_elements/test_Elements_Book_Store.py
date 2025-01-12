import pytest


class Test_Elements_Book_Store:
    def test_should_access_book_information_successfully(self, driver):
        """TC01: Validate successfully accessing book information (GET => Status 200)."""
        pass

    def test_should_not_access_book_information_if_isbn_is_empty(self, driver):
        """TC02: Validate failing to access book information when the ISBN is empty (GET => Status 400)."""
        pass

    def test_should_not_access_book_information_if_isbn_is_incorrect(self, driver):
        """TC03: Validate failing to access book information when the ISBN is incorrect (GET => Status 400)."""
        pass

    def test_should_add_book_to_collection_successfully(self, driver):
        """TC04: Validate successfully adding a book to the collection (POST => Status 200)."""
        pass

    def test_should_not_add_book_to_collection_if_userid_is_empty(self, driver):
        """TC05: Validate failing to add a book to the collection when the userId is empty (POST => Status 400)."""
        pass

    def test_should_not_add_book_to_collection_if_userid_is_incorrect(self, driver):
        """TC06: Validate failing to add a book to the collection when the userId is incorrect (POST => Status 401)."""
        pass

    def test_should_not_add_book_to_collection_if_collection_of_isbns_is_empty(self, driver):
        """TC07: Validate failing to add a book to the collection when collectionOfIsbns is empty (POST => Status 400)."""
        pass

    def test_should_not_add_book_to_collection_if_isbn_is_empty(self, driver):
        """TC08: Validate failing to add a book to the collection when the ISBN is empty (POST => Status 400)."""
        pass

    def test_should_not_add_book_to_collection_if_isbn_is_incorrect(self, driver):
        """TC09: Validate failing to add a book to the collection when the ISBN is incorrect (POST => Status 400)."""
        pass


if __name__ == "__main__":
    pytest.main()
