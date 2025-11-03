def crawl_site(start_url, depth=2):
    if depth == 0:
        return
    page_content = fetch_page_with_delay(start_url)
    soup = BeautifulSoup(page_content, 'html.parser')
    print(f"Crawling: {start_url} - Title: {soup.title.text}")

    for link in soup.find_all('a', href=True):
        next_url = link['href']
        if next_url.startswith('/'):
            next_url = start_url + next_url  # Handle relative URLs
        crawl_site(next_url, depth - 1)

crawl_site(url, depth=2)
