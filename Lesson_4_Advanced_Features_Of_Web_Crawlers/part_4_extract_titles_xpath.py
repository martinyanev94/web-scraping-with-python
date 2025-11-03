from lxml import html
import requests

response = requests.get('https://example.com')
tree = html.fromstring(response.content)

# Extract titles using XPath
titles = tree.xpath('//h1/text()')
print(titles)
