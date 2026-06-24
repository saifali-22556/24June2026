import json
from playwright.sync_api import APIRequestContext


def test_get_all_products(before_each_test: APIRequestContext):
    response = before_each_test.get("/products")
    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
