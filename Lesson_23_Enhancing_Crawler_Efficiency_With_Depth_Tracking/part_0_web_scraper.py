import requests
from bs4 import BeautifulSoup

def scrape(url, depth=0, max_depth=2):
    if depth > max_depth:
        return
    
    print(f"Scraping URL: {url} at depth: {depth}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all anchor tags
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if href and (href.startswith('http')):
            scrape(href, depth + 1, max_depth)

# Starting point of the web crawler
start_url = 'https://example.com'
scrape(start_url)
