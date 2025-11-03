base_url = 'https://example.com/article/'

# Loop through the first 5 articles
for i in range(1, 6):
    url = f"{base_url}{i}"  # Form the complete URL
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for title in soup.find_all('h1'):
            print(f"Article {i} Title: {title.get_text(strip=True)}")
    else:
        print(f"Failed to fetch article {i}: {response.status_code}")
