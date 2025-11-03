import requests

api_url = 'https://www.example.com/api/products'
response = requests.get(api_url)

if response.status_code == 200:
    product_data = response.json()
    print(product_data)
else:
    print(f"API error: {response.status_code}")
