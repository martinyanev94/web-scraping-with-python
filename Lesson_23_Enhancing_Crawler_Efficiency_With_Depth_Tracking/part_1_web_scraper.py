import requests
from bs4 import BeautifulSoup

def scrape(url, depth=0, max_depth=2, visited=None):
    if visited is None:
        visited = set()

    if depth > max_depth or url in visited:
        return

    print(f"Scraping URL: {url} at depth: {depth}")
    visited.add(url)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if href and (href.startswith('http')):
            scrape(href, depth + 1, max_depth, visited)

start_url = 'https://example.com'
scrape(start_url)
