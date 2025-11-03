session = requests.Session()
session.headers.update(headers)

response = session.get(url)
print(response.content)

# You can now perform additional requests using session
