from bs4 import BeautifulSoup

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find and print all <h1> tags on the page
for title in soup.find_all('h1'):
    print(title.get_text(strip=True))
