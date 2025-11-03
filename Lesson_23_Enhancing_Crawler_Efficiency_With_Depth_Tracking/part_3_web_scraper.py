import requests
from bs4 import BeautifulSoup

def scrape(url, depth=0, max_depth=2, visited=None, graph=None):
    if visited is None:
        visited = set()
    if graph is None:
        graph = {}

    if depth > max_depth or url in visited:
        return

    visited.add(url)
    graph[url] = []
    print(f"Scraping URL: {url} at depth: {depth}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a')

    for link in links:
        href = link.get('href')
        if href and (href.startswith('http')):
            graph[url].append(href)  # Update adjacency list
            scrape(href, depth + 1, max_depth, visited, graph)

    return graph

start_url = 'https://example.com'
graph = scrape(start_url)
print("Graph representation of URLs visited:")
print(graph)
