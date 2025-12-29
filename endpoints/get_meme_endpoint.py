import requests
from endpoints.endpoint import Endpoints


class GetMeme(Endpoints):
    def get_all_memes(self, headers):
        self.response = requests.get(f"{self.url}/meme", headers=headers)
        return self.response

    def get_one_meme(self, headers, meme_id):
        self.response = requests.get(f"{self.url}/meme/{meme_id}", headers=headers)
        self.parse_json_if_ok()
        return self.response
