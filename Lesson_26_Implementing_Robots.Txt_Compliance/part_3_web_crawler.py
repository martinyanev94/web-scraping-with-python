import time

def crawl(url):
    if is_allowed_to_scrape(url, robots_rules, user_agent):
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully scraped {url}")
            time.sleep(1)  # Throttle with a 1-second delay
        else:
            print(f"Failed to scrape {url}: {response.status_code}")
    else:
        print(f"Skipping {url} due to robots.txt compliance.")

# Example URL
crawl("http://example.com/private/data")
