import requests
from endpoints.endpoint import Endpoints


class Authorization(Endpoints):
    def authorize(self):
        self.response = requests.post(f"{self.url}/authorize", json=self.name)
        self.response_json = self.response.json()
        self.token = self.response.json()["token"]
        return self.token

    def token_is_valid(self):
        if self.token == None:
            return False
        response = requests.get(f"{self.url}/authorize/{self.token}")
        return response.status_code == 200

    def get_valid_token(self):
        return self.token if self.token_is_valid() else self.authorize()

    def check_token_key_in_response(self):
        assert "token" in self.response_json

    def check_token_value_is_str(self):
        assert isinstance(self.token, str)

    def check_token_value_is_not_empty(self):
        assert len(self.token) > 0
