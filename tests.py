import pytest
import requests
from pydantic import BaseModel
import allure

base_url = "https://petstore.swagger.io/v2/"

@allure.feature("User API Testing")
class TestUserAPI:

    @allure.title("GET /user")
    def test_fetch_user(self):
        response_user = requests.get(f"{base_url}user")
        assert response_user.status_code == 200
        with allure.step("Check the response JSON"):
            user_data = response_user.json()
            UserDetail(**user_data)  # Validate the response with Pydantic
        allure.attach(response_user.text, "Response", allure.attachment_type.JSON)

    @allure.title("POST /user")
    def test_create_user(self):
        data = {"id": 1, "username": "new_user", "email": "user@example.com"}
        response_post_user = requests.post(f"{base_url}user", json=data)
        assert response_post_user.status_code == 200
        with allure.step("Check the response JSON"):
            user_data = response_post_user.json()
            UserDetail(**user_data)  # Validate the response with Pydantic
        allure.attach(response_post_user.text, "Response", allure.attachment_type.JSON)

@allure.feature("Store API Testing")
class TestStoreAPI:

    @allure.title("GET /store")
    def test_fetch_store(self):
        response_store = requests.get(f"{base_url}store/inventory")
        assert response_store.status_code == 200
        with allure.step("Check the response JSON"):
            store_data = response_store.json()
        allure.attach(response_store.text, "Response", allure.attachment_type.JSON)

    @allure.title("PUT /store/1")
    def test_update_store(self):
        store_data = {"id": 1, "name": "New Store"}
        response_put_store = requests.put(f"{base_url}store/inventory", json=store_data)
        assert response_put_store.status_code == 200
        with allure.step("Check the response JSON"):
            store_data = response_put_store.json()
        allure.attach(response_put_store.text, "Response", allure.attachment_type.JSON)

class UserDetail(BaseModel):
    id: int
    username: str
    email: str
    phone: str = None

if __name__ == "__main__":
    pytest.main()
