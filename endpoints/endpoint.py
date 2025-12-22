class Endpoints:
    url = "http://memesapi.course.qa-practice.com/"
    name = {"name": "alisa"}
    response = None
    token = None
    body = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    def check_status_code_is_not_200(self):
        assert self.response.status_code != 200

    def check_text_value_is_valid(self, body):
        assert self.response.json()["text"] == body["text"]
