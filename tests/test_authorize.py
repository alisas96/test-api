import pytest
from endpoints.authorize import Authorization


@pytest.mark.smoke
def test_authorize_valid_name(authorize_endpoint):
    authorize_endpoint.check_status_code_is_200()
    authorize_endpoint.check_token_key_in_response()
    authorize_endpoint.check_token_value_is_not_empty()
    authorize_endpoint.check_token_value_is_str()


@pytest.mark.smoke
def test_token_is_valid(authorize_endpoint):
    authorize_endpoint.token_is_valid()


INVALID_AUTHORIZATION_NAME = (
    {"name": 1234},
    {"name": ""},
    {"name": None},
    {"name": {"color": ["white", "grey"], "objects": ["cat", "text", "hands"]}},
    {"name": ["alisa"]},
)


@pytest.mark.extended
@pytest.mark.parametrize("name", INVALID_AUTHORIZATION_NAME)
def test_authorize_invalid_name(name):
    authorize_endpoint_invalid = Authorization()
    authorize_endpoint_invalid.authorize(name)
    authorize_endpoint_invalid.check_status_code_is_400()
