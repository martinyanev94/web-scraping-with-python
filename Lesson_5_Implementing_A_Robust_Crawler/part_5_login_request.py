import requests

def login(url, user, password):
    session = requests.Session()
    login_payload = {'username': user, 'password': password}
    session.post(url, data=login_payload)
    return session
