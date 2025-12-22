import pytest
from endpoints.create_meme_endpoint import CreateMeme
from endpoints.authorize import Authorization
from endpoints.update_meme_endpoint import UpdateMeme
from endpoints.delete_meme_endpoint import DeleteMeme


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def update_meme_endpoint():
    return UpdateMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture(scope="session")
def authorize_endpoint():
    auth = Authorization()
    auth.authorize()
    return auth


@pytest.fixture()
def headers(authorize_endpoint):
    authorize_endpoint.get_valid_token()
    return {"Authorization": authorize_endpoint.token}


@pytest.fixture()
def meme_id(create_meme_endpoint, delete_meme_endpoint, headers):
    body = {
        "text": ("We need to talk about your memes memes"),
        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaH5PTIMq9L3zCL-wsv5Uj6xGw3zestcDB_A&s",
        "tags": ["cat", "meme", "hands"],
        "info": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]},
    }
    create_meme_endpoint.post_a_meme(body, headers)
    meme_id = create_meme_endpoint.meme_id
    yield meme_id
    delete_meme_endpoint.delete_a_meme(meme_id, headers)
