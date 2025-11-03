import random
import requests
from bs4 import BeautifulSoup

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Linux; Android 10; SM-G950U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36"
]

def fetch_page(url):
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    return response.content

url = 'https://example.com'
page_content = fetch_page(url)
soup = BeautifulSoup(page_content, 'html.parser')
print(soup.title.text)
