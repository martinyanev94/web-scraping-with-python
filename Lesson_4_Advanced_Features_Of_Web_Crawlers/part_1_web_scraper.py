import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve {url}")
        return None

def parse_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = [title.get_text(strip=True) for title in soup.find_all('h1')]
    return titles

base_url = 'https://example.com/article/'
urls = [f"{base_url}{i}" for i in range(1, 6)]

with ThreadPoolExecutor(max_workers=5) as executor:
    html_pages = list(executor.map(fetch_page, urls))

titles = []
for html in html_pages:
    if html:
        titles.extend(parse_titles(html))

print(titles)
