from urllib.robotparser import RobotFileParser

class RobotsChecker:
    def __init__(self, base_url):
        self.base_url = base_url
        self.robot_parser = RobotFileParser()

    def fetch_robots(self):
        self.robot_parser.set_url(f"{self.base_url}/robots.txt")
        self.robot_parser.read()

    def can_crawl(self, url):
        return self.robot_parser.can_fetch("*", url)

# Using the RobotsChecker class
checker = RobotsChecker("https://example.com")
checker.fetch_robots()

url_to_check = "https://example.com/some-page"
if checker.can_crawl(url_to_check):
    print(f"Can crawl: {url_to_check}")
else:
    print(f"Cannot crawl: {url_to_check}")
