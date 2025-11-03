import urllib.robotparser

def check_robots(seed_url, user_agent):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urlparse(seed_url).scheme + "://" + urlparse(seed_url).netloc + "/robots.txt")
    rp.read()
    return rp.can_fetch(user_agent, seed_url)
