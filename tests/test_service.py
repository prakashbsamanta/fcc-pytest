import pytest
import requests

import source.service as service
import unittest.mock as mock


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mocked_user_id):
    mocked_user_id.return_value = "Mocked Alice"
    username = service.get_user_from_db(1)
    assert username == "Mocked Alice"


@mock.patch("requests.get")
def test_get_json_placeholder_users(mocked_users):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "william"}
    mocked_users.return_value = mock_response
    data = service.get_json_placeholder_users()

    assert data == {"id": 1, "name": "william"}


@mock.patch("requests.get")
def test_get_json_placeholder_http_error(mocked_user_response):
    mock_response = mock.Mock()
    mock_response.status_code = 401
    mocked_user_response.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_json_placeholder_users()
