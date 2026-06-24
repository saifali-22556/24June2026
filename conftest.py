import json
from playwright.sync_api import Playwright
import pytest

filepath = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\python_files\\test_data.json"


@pytest.fixture(scope="function")
def before_each_test(playwright: Playwright):
    with open(filepath, "r") as file:
        data = json.load(file)
    request = playwright.request.new_context(base_url=data["base_url"])
    yield request
    request.dispose()
