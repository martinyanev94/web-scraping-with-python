robots_url = 'https://www.example.com/robots.txt'
robots_response = requests.get(robots_url)

if robots_response.status_code == 200:
    print("Robots.txt Content:")
    print(robots_response.text)
else:
    print(f"Failed to retrieve robots.txt: {robots_response.status_code}")
