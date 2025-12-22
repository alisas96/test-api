import requests
from endpoints.endpoint import Endpoints


class CreateMeme(Endpoints):
    def post_a_meme(self, body, headers):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=headers)
        print("Status:", self.response.status_code)
        print("Headers:", self.response.headers)
        print("Body:", self.response.text)
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json["id"]
        else:
            self.json = {}
            self.meme_id = None 
        return self.response


