import requests
from bs4 import BeautifulSoup

# Your target URL
url = 'http://example.com'

# Send a request to fetch the content of the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract the title of the page
    title = soup.title.string
    print(f'Title of the page is: {title}')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
