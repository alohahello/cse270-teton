import requests
from unittest.mock import patch


def mock_get(*args, **kwargs):
    class MockResponse:
        def json(self):
            return [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]

        @property
        def status_code(self):
            return 200

    return MockResponse()


@patch("requests.get", side_effect=mock_get)
def test_get_users(mock_requests_get):
    response = requests.get("http://127.0.0.1:8000/users/all")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0