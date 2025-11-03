from urllib.robotparser import RobotFileParser

def check_robots(url):
    rp = RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp.can_fetch('*', url)

url = 'https://example.com'
if check_robots(url):
    print("Allowed to scrape this site!")
else:
    print("Crawling is not allowed per 'robots.txt'")
