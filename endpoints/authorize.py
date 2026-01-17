import requests
from endpoints.endpoint import Endpoints


class Authorization(Endpoints):
    def authorize(self, name):
        self.response = requests.post(f"{self.url}/authorize", json=name)
        if self.response.status_code == 200:
            self.response_json = self.response.json()
            self.token = self.response_json.get("token")
        else:
            self.response_json = None
            self.token = None
        return self.token

    def token_is_valid(self):
        assert self.token is not None
        response = requests.get(f"{self.url}/authorize/{self.token}")
        assert response.status_code == 200

    def get_valid_token(self, name=None):
        if self.token is None:
            self.authorize(name)
        else:
            self.token_is_valid()
        return self.token
            

    def check_token_key_in_response(self):
        assert "token" in self.response_json

    def check_token_value_is_str(self):
        assert isinstance(self.token, str)

    def check_token_value_is_not_empty(self):
        assert len(self.token) > 0
