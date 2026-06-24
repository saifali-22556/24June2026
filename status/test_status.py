from playwright.sync_api import APIRequestContext
import pytest


@pytest.mark.order(1)
def test_status(before_each_test: APIRequestContext):
    response = before_each_test.get("/status")
    print(f"status code ={response.status}")
    assert response.status == 200
    print(response.json())
    assert response.json()["status"] == "UP"
    print("--------------Headers--------------------------")
    print(response.headers)
    assert response.headers["content-type"] == "application/json"
