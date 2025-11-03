from urllib.robotparser import RobotFileParser

def can_fetch(url, user_agent):
    robots_url = url + '/robots.txt'
    rp = RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    return rp.can_fetch(user_agent, url)

def crawl_site_with_robots(start_url, depth=2):
    if depth == 0:
        return
    if can_fetch(start_url, random.choice(user_agents)):
        page_content = fetch_page_with_delay(start_url)
        soup = BeautifulSoup(page_content, 'html.parser')
        print(f"Crawling: {start_url} - Title: {soup.title.text}")

        for link in soup.find_all('a', href=True):
            next_url = link['href']
            if next_url.startswith('/'):
                next_url = start_url + next_url
            crawl_site_with_robots(next_url, depth - 1)
    else:
        print(f"Blocked by robots.txt: {start_url}")

crawl_site_with_robots(url, depth=2)
