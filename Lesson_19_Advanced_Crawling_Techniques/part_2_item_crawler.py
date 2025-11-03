import requests
import itertools

def crawl_items(base_url):
    for item_id in itertools.count(1):
        url = f"{base_url}/view/item-{item_id}"
        html = download(url)
        if html is None:
            break  # Assume we hit the end when we get None

def download(url):
    print(f"Downloading: {url}")
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

crawl_items('http://example.com')
