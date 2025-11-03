import robotparser

def can_fetch(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(url + '/robots.txt')
    rp.read()
    return rp.can_fetch('*', url)  # Check if allowed to crawl

print(can_fetch('http://example.com'))
