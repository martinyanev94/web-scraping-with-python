try:
    response = session.get(url)
    response.raise_for_status()  # Raises an error for bad responses
except requests.exceptions.HTTPError as err:
    print(f'HTTP error occurred: {err}')  # e.g. 404 or 500 errors
except Exception as err:
    print(f'An error occurred: {err}')
