def fetch_server_info(url):
    response = requests.head(url)
    headers = response.headers
    return headers.get('Server', 'No server info detected')

server_info = fetch_server_info(url)
print(f'Server Information: {server_info}')
