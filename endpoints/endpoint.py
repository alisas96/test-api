class Endpoints:
    url = "http://memesapi.course.qa-practice.com/"
    not_existing_id = 99999999999
    unauthorized_headers = {"Content-Type": "application/json"}
    response = None
    token = None
    body = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    def check_status_code_is_401(self):
        assert self.response.status_code == 401

    def check_status_code_is_400(self):
        assert self.response.status_code == 400

    def check_status_code_is_404(self):
        assert self.response.status_code == 404

    def check_text_value_is_valid(self, body):
        assert self.response.json()["text"] == body["text"]

    def check_url_value_is_valid(self, body):
        assert self.response.json()["url"] == body["url"]

    def check_tags_value_is_valid(self, body):
        assert self.response.json()["tags"] == body["tags"]

    def check_info_value_is_valid(self, body):
        assert self.response.json()["info"] == body["info"]

    def check_body_contains_memes(self):
        body = self.response.json()
        memes = body.get("data")
        assert isinstance(body, dict)
        for meme in memes:
            assert "id" in meme
            assert "text" in meme
            assert "url" in meme
            assert "tags" in meme
            assert "info" in meme

    def check_body_contains_one_meme(self):
        body = self.response.json()
        assert "id" in body
        assert "text" in body
        assert "url" in body
        assert "tags" in body
        assert "info" in body

    def parse_json_if_ok(self):
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = {}
