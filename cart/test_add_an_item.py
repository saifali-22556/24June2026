import json
from playwright.sync_api import APIRequestContext
import pytest

file_path = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\global_data.json"


@pytest.mark.order(2)
@pytest.mark.parametrize("product_id", [1225, 1709, 1710])
@pytest.mark.dependency(depends=["create_cart"], scope="session", name="add_item_to_cart")
def test_add_an_item_to_cart(before_each_test: APIRequestContext, product_id):
    with open(file_path, "r") as file:
        data = json.load(file)
    cart_id = data.get("cart_id")
    payload = {"productId": product_id, "quantity": 2}
    response = before_each_test.post(f"/carts/{cart_id}/items", data=payload)
    assert response.status == 201
    response_json = response.json()
    new_item_id = response_json["itemId"]
    print(json.dumps(response_json, indent=4))
    data["item_id"].append(new_item_id)
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Added Item ID: {new_item_id}")
