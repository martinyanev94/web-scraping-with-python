import requests
from bs4 import BeautifulSoup

def fetch_website_technologies(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Checking for specific technologies in meta tags
    meta_tags = soup.find_all('meta')
    tech_info = []

    for tag in meta_tags:
        if 'generator' in tag.attrs:
            tech_info.append(('Meta Generator', tag['content']))
    
    return tech_info

url = 'https://example.com'
technologies = fetch_website_technologies(url)
print(technologies)
