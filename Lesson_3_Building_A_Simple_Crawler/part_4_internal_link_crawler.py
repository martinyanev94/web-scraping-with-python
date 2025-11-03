from urllib.parse import urljoin, urlparse

def is_internal_link(url, base_url):
    return urlparse(url).netloc == urlparse(base_url).netloc

# Let's crawl from a single base URL and gather its links
response = requests.get('https://example.com')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for link in soup.find_all('a', href=True):
        full_url = urljoin('https://example.com', link['href'])  # Create a full URL
        if is_internal_link(full_url, 'https://example.com'):
            print(f"Found internal link: {full_url}")
        else:
            print("Skipped external link.")
