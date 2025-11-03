import requests

url = 'http://example-angularjs-site.com/api/data'
response = requests.get(url)
data = response.json()

print(data)
