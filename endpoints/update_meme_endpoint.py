import requests
from endpoints.endpoint import Endpoints


class UpdateMeme(Endpoints):
    def put_a_meme(self, body, headers, meme_id):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}", json=body, headers=headers
        )
        self.parse_json_if_ok()
        return self.response
