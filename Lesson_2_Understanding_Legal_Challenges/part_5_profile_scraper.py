url = 'http://example-directory.com/profiles'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    for profile in soup.find_all('div', class_='profile'):
        name = profile.find('h2').get_text(strip=True)
        title = profile.find('span', class_='job-title').get_text(strip=True)
        print(f'Name: {name}, Title: {title}')
else:
    print(f'Failed to retrieve directory: {response.status_code}')
