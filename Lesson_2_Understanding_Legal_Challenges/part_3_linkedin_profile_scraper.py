import requests
from bs4 import BeautifulSoup

# Assume you have the URL for public LinkedIn profiles.
url = 'https://www.linkedin.com/in/sample-profile'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # For example, scraping the job title from the profile
    title = soup.find('h1', class_='text-heading-xlarge').get_text(strip=True)
    print(f'Job Title: {title}')
else:
    print(f'Error retrieving profile: {response.status_code}')
