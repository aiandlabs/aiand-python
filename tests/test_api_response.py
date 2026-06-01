from http.client import HTTPMessage

import aiand


class FakeResponse:
    status = 200
    data = b""

    def __init__(self) -> None:
        self.headers = HTTPMessage()
        self.headers.add_header("content-type", "application/json")
        self.headers.add_header("x-request-id", "req_test")


def test_response_deserialize_normalizes_http_message_headers() -> None:
    response = aiand.ApiClient().response_deserialize(
        FakeResponse(),
        response_types_map={"200": None},
    )

    assert response.headers == {
        "content-type": "application/json",
        "x-request-id": "req_test",
    }
