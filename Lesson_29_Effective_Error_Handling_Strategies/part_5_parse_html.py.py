from bs4 import BeautifulSoup

def parse_data(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # Attempt to find a specific element
        data_element = soup.find('div', class_='data-class')
        if data_element is not None:
            return data_element.text
        else:
            print("Data element not found in the HTML.")
    except Exception as parse_err:
        print(f"Error occurred while parsing HTML: {parse_err}")
    return None
