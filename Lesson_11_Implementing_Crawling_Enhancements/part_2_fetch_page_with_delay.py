import time

def fetch_page_with_delay(url):
    time_delay = random.uniform(1, 5)  # Random delay between 1 to 5 seconds
    time.sleep(time_delay)
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    return response.content

page_content = fetch_page_with_delay(url)
soup = BeautifulSoup(page_content, 'html.parser')
print(soup.title.text)
