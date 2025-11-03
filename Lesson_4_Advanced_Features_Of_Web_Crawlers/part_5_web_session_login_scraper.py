session = requests.Session()

# Replace these with your actual login credentials
payload = {
    'username': 'your_username',
    'password': 'your_password'
}

# Authenticate and create a session
login_url = 'https://example.com/login'
session.post(login_url, data=payload)

# Now you can scrape content from a page that requires authentication
protected_url = 'https://example.com/protected-page'
response = session.get(protected_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.get_text(strip=True) for title in soup.find_all('h1')]
    print(titles)
else:
    print("Failed to retrieve protected page.")
