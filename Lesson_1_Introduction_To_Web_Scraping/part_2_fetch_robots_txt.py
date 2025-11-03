# Check the robots.txt file
robots_url = 'http://example.com/robots.txt'
robots_response = requests.get(robots_url)

if robots_response.status_code == 200:
    print(robots_response.text)
else:
    print(f'Failed to retrieve the robots.txt. Status code: {robots_response.status_code}')
