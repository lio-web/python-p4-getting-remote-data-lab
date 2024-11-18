import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        response.raise_for_status() 
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            # Convert the JSON string to a Python list or dictionary
            return json.loads(response_body)
        except json.JSONDecodeError:
            # Handle the case where the response is not valid JSON
            return None
