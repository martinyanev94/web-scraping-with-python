import logging

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def download(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as err:
        logging.error(f"Error occurred while downloading {url}: {err}")
    return None
