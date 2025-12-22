import requests
from endpoints.endpoint import Endpoints


class DeleteMeme(Endpoints):
	def delete_a_meme(self, meme_id, headers):
		self.response = requests.delete(f'{self.url}/meme/{meme_id}', headers=headers)
		return self.response