pip install requests beautifulsoup4
import requests

# Specify the URL of the page you want to crawl
url = 'https://example.com'

# Send a GET request to the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Page content fetched successfully.")
    print(response.text)  # Display the HTML content of the page
else:
    print(f"Error fetching the page: {response.status_code}")
