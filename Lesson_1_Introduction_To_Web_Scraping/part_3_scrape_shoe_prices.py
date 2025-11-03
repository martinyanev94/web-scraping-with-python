import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    'http://competitorsite.com/shoe1',
    'http://competitorsite.com/shoe2',
]

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', class_='price').text
        print(f'Price for {url} is {price}')
    else:
        print(f'Failed to retrieve {url}. Status code: {response.status_code}')
