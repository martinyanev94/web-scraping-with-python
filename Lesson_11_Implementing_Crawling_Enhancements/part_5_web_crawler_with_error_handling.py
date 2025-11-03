def fetch_page_with_error_handling(url):
    try:
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def crawl_site_with_errors(start_url, depth=2):
    if depth == 0:
        return
    page_content = fetch_page_with_error_handling(start_url)
    if page_content is None:
        return  # Skip the current URL if there was an error
    soup = BeautifulSoup(page_content, 'html.parser')
    print(f"Crawling: {start_url} - Title: {soup.title.text}")

    for link in soup.find_all('a', href=True):
        next_url = link['href']
        if next_url.startswith('/'):
            next_url = start_url + next_url
        crawl_site_with_errors(next_url, depth - 1)

crawl_site_with_errors(url, depth=2)
