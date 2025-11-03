def check_robots_txt(url):
    robots_url = urljoin(url, '/robots.txt')
    response = requests.get(robots_url)
    
    if response.status_code == 200:
        return response.text
    else:
        return None

# Example usage:
robots_txt = check_robots_txt('https://example.com')
if robots_txt:
    print("Robots.txt retrieved.")
    print(robots_txt)
else:
    print("Unable to retrieve robots.txt.")
