import json
from playwright.sync_api import APIRequestContext
import pytest

file_path = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\global_data.json"


@pytest.mark.order(1)
@pytest.mark.dependency(name="create_cart", scope="session")
def test_create_new_cart(before_each_test: APIRequestContext):
    response = before_each_test.post("/carts")
    with open(file_path, "r") as file:
        data = json.load(file)

    assert response.status == 201
    print(json.dumps(response.json(), indent=4))
    data["cart_id"] = response.json()["cartId"]
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    data["item_id"] = []
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
