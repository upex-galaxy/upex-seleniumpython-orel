import pytest
from tests.api.api_page import Api


class Test_Books_Api:

    def test_create_new_user_orel(self):
        api = Api()
        username = 'orelroman40'
        password = 'Orel1234!40'
        response_create = api.create_new_user(username, password)
        assert response_create.status_code == 201
        body = response_create.json()
        user_id = body['userID']
        response_delete = api.delete_user(user_id)
        assert response_delete.status_code == 204



if __name__ == "__main__":
    pytest.main()
