import urllib.robotparser

def can_crawl(url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url("http://example.com/robots.txt")
    rp.read()
    return rp.can_fetch("*", url)

while True:
    url_to_crawl = "http://example.com/page"
    if can_crawl(url_to_crawl):
        print(f"Crawling {url_to_crawl}...")
        # Insert actual crawling logic here
    else:
        print(f"Blocked by robots.txt: {url_to_crawl}")
        break
