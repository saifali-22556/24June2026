from playwright.sync_api import APIRequestContext
import json
import pytest

file_path = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\global_data.json"


@pytest.mark.order(3)
@pytest.mark.dependency(depends=["add_item_to_cart"], scope="session")
def test_delete_an_item_from_cart(before_each_test: APIRequestContext):
    with open(file_path, "r") as file:
        data = json.load(file)
    cart_id = data.get("cart_id")
    item_id_list = data.get("item_id")
    if not item_id_list:
        pytest.skip("No items available to delete.")
    item_id_to_delete = item_id_list.pop(1)
    response = before_each_test.delete(f"/carts/{cart_id}/items/{item_id_to_delete}")
    assert response.status in (200, 204), f"Unexpected status {response.status}: {response.text()}"

    data["item_id"] = item_id_list
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Deleted Item ID: {item_id_to_delete} (status: {response.status})")
