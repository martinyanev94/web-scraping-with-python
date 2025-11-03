import requests
import xml.etree.ElementTree as ET

class SitemapCrawler:
    def __init__(self, sitemap_url):
        self.sitemap_url = sitemap_url

    def parse_sitemap(self):
        response = requests.get(self.sitemap_url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            urls = [url_elem.text for url_elem in root.findall(".//loc")]
            print("Found URLs in Sitemap:")
            for url in urls:
                print(url)
        else:
            print("Failed to retrieve sitemap.")

# Create an instance with the sitemap URL
sitemap_crawler = SitemapCrawler("https://example.com/sitemap.xml")
sitemap_crawler.parse_sitemap()
