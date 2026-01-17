def test_delete_a_meme(delete_meme_endpoint, get_meme_endpoint, headers, meme_id):
    delete_meme_endpoint.delete_a_meme(headers, meme_id)
    delete_meme_endpoint.check_status_code_is_200()
    get_meme_endpoint.get_one_meme(headers, meme_id)
    get_meme_endpoint.check_status_code_is_404()


def test_delete_a_meme_unauthorized(delete_meme_endpoint, meme_id):
    delete_meme_endpoint.delete_a_meme(
        delete_meme_endpoint.unauthorized_headers, meme_id
    )
    delete_meme_endpoint.check_status_code_is_401()


def test_delete_a_non_existent_meme(delete_meme_endpoint, headers):
    delete_meme_endpoint.delete_a_meme(headers, delete_meme_endpoint.not_existing_id)
    delete_meme_endpoint.check_status_code_is_404()
