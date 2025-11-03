import requests
from bs4 import BeautifulSoup

def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.status_code == 200  # Only continue with valid URLs
    except requests.exceptions.RequestException:
        return False

def scrape(url, depth=0, max_depth=2, visited=None):
    if visited is None:
        visited = set()

    if depth > max_depth or url in visited or not is_valid_url(url):
        return

    visited.add(url)
    print(f"Scraping URL: {url} at depth: {depth}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if href and (href.startswith('http')):
            scrape(href, depth + 1, max_depth, visited)

start_url = 'https://example.com'
scrape(start_url)
