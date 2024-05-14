import requests

base_url = "https://api.mouser.com/"

api_key = "2c18ba1d-7b17-4d2e-9e0f-34e05a5e674c"

search_endpoint = "api/v2/search/partnumberandmanufacturer?apiKey=2c18ba1d-7b17-4d2e-9e0f-34e05a5e674c"

url = base_url + search_endpoint

payload = {
    "SearchByPartMfrNameRequest": {
        "manufacturerName": "Altech",
        "mouserPartNumber": "845-008M5X20F",
        "partSearchOptions": "Cartridge Fuses Fuse, Miniature, 5x20mm 0.08A, 250V, fast blow"
    }
}

headers = {
    "apiKey": api_key,
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
