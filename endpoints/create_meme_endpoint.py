import requests
from endpoints.endpoint import Endpoints


class CreateMeme(Endpoints):
    def post_a_meme(self, body, headers):
        self.response = requests.post(f"{self.url}/meme", json=body, headers=headers)
        self.parse_json_if_ok()
        if self.response.status_code == 200:
            self.meme_id = self.json["id"]
        else:
            self.meme_id = None
        return self.response
