import requests

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()  # Parsing the JSON response
        for item in data['items']:
            print(item['title'])  # Adapt this based on your API response structure
    else:
        print(f"Failed to retrieve data: {response.status_code}")

fetch_data_from_api('https://api.example.com/data')
