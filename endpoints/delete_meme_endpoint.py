import requests
from endpoints.endpoint import Endpoints


class DeleteMeme(Endpoints):
    def delete_a_meme(self, headers, meme_id):
        self.response = requests.delete(f"{self.url}/meme/{meme_id}", headers=headers)
        return self.response
