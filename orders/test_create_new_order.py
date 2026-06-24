from playwright.sync_api import APIRequestContext
import json

file_path = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\global_data.json"


def test_create_new_order(before_each_test: APIRequestContext):
    with open(file_path, "r") as f:
        data = json.load(f)
    accessToken = data["accessToken"]
    cartId = data["cart_id"]
    payload = {"cartId": cartId, "customerName": "John Doe"}
    response = before_each_test.post(
        "/orders",
        headers={"Authorization": f"Bearer {accessToken}", "Content-Type": "application/json"},
        data=payload,
    )

    assert response.status == 201
    response_body = response.json()
    print(json.dumps(response_body, indent=4))
    data["order_id"] = response_body["orderId"]
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
