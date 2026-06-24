import json
from playwright.sync_api import APIRequestContext


def test_get_a_product(before_each_test: APIRequestContext):
    response = before_each_test.get("/products/1225")
    print(f"status code ={response.status}")
    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
