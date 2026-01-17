import pytest


VALID_TEXT_DATA = (
    "We need to talk about your memes",
    "We need to talk about your memes memes"
    "memes memes memes memes memes memes memes memes memes"
    "memes memes memes memes memes memes memes memes memes"
    "memes memes memes memes memes memes memes memes",
)


@pytest.mark.parametrize("text", VALID_TEXT_DATA)
def test_put_a_meme(update_meme_endpoint, headers, meme_id, text):
    body = {
        "id": meme_id,
        "text": text,
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQar4w1Wf2HrjYAy6lOPX81lTLWMfUwi_TlmQ&s",
        "tags": ["dog", "meme", "hands"],
        "info": {"color": ["grey", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_200()
    update_meme_endpoint.check_text_value_is_valid(body)
    update_meme_endpoint.check_url_value_is_valid(body)
    update_meme_endpoint.check_tags_value_is_valid(body)
    update_meme_endpoint.check_info_value_is_valid(body)


def test_put_a_meme_must_not_be_unauthorized(update_meme_endpoint, meme_id):
    body = {
        "id": meme_id,
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQar4w1Wf2HrjYAy6lOPX81lTLWMfUwi_TlmQ&s",
        "tags": ["dog", "meme", "hands"],
        "info": {"color": ["grey", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(
        body, update_meme_endpoint.unauthorized_headers, meme_id
    )
    update_meme_endpoint.check_status_code_is_401()


INVALID_BODY = (
    {
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    },
    {
        "id": "ID_WILL_BE_REPLACED",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    },
)


@pytest.mark.parametrize("body", INVALID_BODY)
def test_put_a_meme_without_some_key(update_meme_endpoint, body, headers, meme_id):
    if "id" in body:
        body["id"] = meme_id
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


INVALID_ID_DATA = (
    999999999999,
    0,
    -1,
    ["cat", "meme", "hands"],
    "three",
    {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    None,
)


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


@pytest.mark.parametrize("id", INVALID_ID_DATA)
def test_id_must_exist_and_be_positive_num(update_meme_endpoint, headers, meme_id, id):
    body = {
        "id": id,
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("text", INVALID_TEXT_URL_DATA)
def test_put_a_meme_text_must_be_str(update_meme_endpoint, headers, text, meme_id):
    body = {
        "id": meme_id,
        "text": text,
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("url", INVALID_TEXT_URL_DATA)
def test_put_a_meme_url_must_be_str(update_meme_endpoint, headers, url, meme_id):
    body = {
        "id": meme_id,
        "text": "We need to talk about your memes memes",
        "url": url,
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("tags", INVALID_TAGS_DATA)
def test_put_a_meme_tags_must_be_array(update_meme_endpoint, headers, tags, meme_id):
    body = {
        "id": meme_id,
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": tags,
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


@pytest.mark.parametrize("info", INVALID_INFO_DATA)
def test_put_a_meme_info_must_be_obj(update_meme_endpoint, headers, info, meme_id):
    body = {
        "id": meme_id,
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": info,
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()


def test_put_a_meme_without_info(update_meme_endpoint, headers, meme_id):
    body = {
        "id": meme_id,
        "text": "We need to talk about your memes memes",
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
    }
    update_meme_endpoint.put_a_meme(body, headers, meme_id)
    update_meme_endpoint.check_status_code_is_400()
