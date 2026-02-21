import pytest


@pytest.mark.smoke
def test_get_all_memes(get_meme_endpoint, headers):
    get_meme_endpoint.get_all_memes(headers)
    get_meme_endpoint.check_status_code_is_200()
    get_meme_endpoint.check_body_contains_memes()


@pytest.mark.smoke
def test_get_one_meme(get_meme_endpoint, headers, meme_id):
    get_meme_endpoint.get_one_meme(headers, meme_id)
    get_meme_endpoint.check_status_code_is_200()
    get_meme_endpoint.check_body_contains_one_meme()


@pytest.mark.extended
def test_get_one_meme_not_found(get_meme_endpoint, headers):
    get_meme_endpoint.get_one_meme(headers, get_meme_endpoint.not_existing_id)
    get_meme_endpoint.check_status_code_is_404()


@pytest.mark.regression
def test_get_all_memes_unauthorized(get_meme_endpoint):
    get_meme_endpoint.get_all_memes(get_meme_endpoint.unauthorized_headers)
    get_meme_endpoint.check_status_code_is_401()


@pytest.mark.regression
def test_get_one_meme_unauthorized(get_meme_endpoint, meme_id):
    get_meme_endpoint.get_one_meme(get_meme_endpoint.unauthorized_headers, meme_id)
    get_meme_endpoint.check_status_code_is_401()
