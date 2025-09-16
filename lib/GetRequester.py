import requests


class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # returns the raw body

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # returns Python list/dict from JSON