import requests

def identify_website_technologies(api_key, url):
    headers = {
        'x-api-key': api_key
    }
    response = requests.get(f'https://api.wappalyzer.com/lookup/v2/?url={url}', headers=headers)
    return response.json()

api_key = 'your_api_key_here'
tech_stack = identify_website_technologies(api_key, url)
print(tech_stack)
