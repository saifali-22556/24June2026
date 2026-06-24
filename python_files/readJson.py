import json

filepath = "C:\\Playwright_Python_Training\\June2026_batch2_playwright_APITesting\\python_files\\test_data.json"

with open(filepath, "r") as file:
    data = json.load(file)
    print(data["base_url"])
    print(data["resource"])
    print(data["token"])
    data["token"] = "qaclick123"
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
