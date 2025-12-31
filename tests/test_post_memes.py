import pytest


VALID_TEXT_DATA = (
    "We need to talk about your memes",
    "We need to talk about your memes memes"
    "memes memes memes memes memes memes memes memes memes"
    "memes memes memes memes memes memes memes memes memes"
    "memes memes memes memes memes memes memes memes",
)


@pytest.mark.parametrize("text", VALID_TEXT_DATA)
def test_post_a_meme(create_meme_endpoint, headers, text):
    body = {
        "text": text,
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_200()
    create_meme_endpoint.check_text_value_is_valid(body)
    create_meme_endpoint.check_url_value_is_valid(body)
    create_meme_endpoint.check_tags_value_is_valid(body)
    create_meme_endpoint.check_info_value_is_valid(body)


def test_post_a_meme_must_not_be_unauthorized(create_meme_endpoint):
    body = {
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, create_meme_endpoint.unauthorized_headers)
    create_meme_endpoint.check_status_code_is_401()


INVALID_TEXT_URL_DATA = (
    ["cat", "meme", "hands"],
    21,
    {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    None,
)


INVALID_TAGS_DATA = (
    21,
    {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    "We need to talk about your memes memes",
)


INVALID_INFO_DATA = (
    21,
    ["cat", "meme", "hands"],
    "We need to talk about your memes memes",
)


@pytest.mark.parametrize("text", INVALID_TEXT_URL_DATA)
def test_post_a_meme_text_must_be_str(create_meme_endpoint, headers, text):
    body = {
        "text": text,
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("url", INVALID_TEXT_URL_DATA)
def test_post_a_meme_url_must_be_str(create_meme_endpoint, headers, url):
    body = {
        "text": "We need to talk about your memes memes",
        "url": url,
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("tags", INVALID_TAGS_DATA)
def test_post_a_meme_tags_must_be_array(create_meme_endpoint, headers, tags):
    body = {
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": tags,
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("info", INVALID_INFO_DATA)
def test_post_a_meme_info_must_be_obj(create_meme_endpoint, headers, info):
    body = {
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": info,
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_400()


def test_post_a_meme_without_info(create_meme_endpoint, headers):
    body = {
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
    }
    create_meme_endpoint.post_a_meme(body, headers)
    create_meme_endpoint.check_status_code_is_400()
