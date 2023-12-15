import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self):
        url = f"{self.base_url}/data"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None