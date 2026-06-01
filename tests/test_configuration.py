import aiand


def test_default_host_uses_aiand_api() -> None:
    assert aiand.Configuration().host == "https://api.aiand.com"


def test_bearer_auth_uses_access_token() -> None:
    configuration = aiand.Configuration(access_token="sk-test")

    assert configuration.auth_settings()["bearerAuth"]["value"] == "Bearer sk-test"
