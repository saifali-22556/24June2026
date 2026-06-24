import os
import json
import pytest
from playwright.sync_api import Playwright


@pytest.mark.skipif(not os.getenv("GITHUB_TOKEN"), reason="Set GITHUB_TOKEN to run this test")
def test_api_key_auth(playwright: Playwright):
    api_key = os.getenv("GITHUB_TOKEN")
    request = playwright.request.new_context()
    response = request.get(
        "https://api.github.com/user/repos",
        headers={"Authorization": f"Bearer {api_key}"},
    )
    assert response.status == 200
    print(json.dumps(response.json(), indent=4))
    request.dispose()
