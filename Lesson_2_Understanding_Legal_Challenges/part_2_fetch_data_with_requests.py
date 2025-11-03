import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

url = 'http://example.com/data-page'

# A simple session to manage requests
with requests.Session() as session:
    session.headers.update(headers)
    
    # Example request
    response = session.get(url)
    if response.status_code == 200:
        # Process your data here
        print("Data fetched successfully.")
    else:
        print(f"Failed to fetch data: {response.status_code}")
    
    # Sleep to respect the server's load
    time.sleep(2)
