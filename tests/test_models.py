import pytest
from pydantic import ValidationError

import aiand


def test_chat_completion_request_serializes_docs_style_messages() -> None:
    request = aiand.CreateChatCompletionRequest.from_dict(
        {
            "model": "openai/gpt-oss-120b",
            "messages": [{"role": "user", "content": "Say hello in one sentence."}],
            "temperature": 0.2,
        }
    )

    assert request.to_dict()["messages"] == [
        {"role": "user", "content": "Say hello in one sentence."}
    ]
    assert request.to_dict()["model"] == "openai/gpt-oss-120b"


def test_model_response_accepts_string_pricing_and_extra_metadata() -> None:
    response = aiand.ListModels200Response.from_dict(
        {
            "object": "list",
            "data": [
                {
                    "id": "openai/gpt-oss-120b",
                    "object": "model",
                    "created": 1775474514,
                    "owned_by": "ai&",
                    "input_per_1m": "0.150000",
                    "output_per_1m": "0.600000",
                    "context_window": 131072,
                    "capabilities": ["reasoning", "tools"],
                }
            ],
        }
    )

    model = response.data[0]

    assert model.input_per_1m == "0.150000"
    assert model.output_per_1m == "0.600000"
    assert model.to_dict()["context_window"] == 131072
    assert model.to_dict()["capabilities"] == ["reasoning", "tools"]


def test_upload_purpose_accepts_document_from_docs() -> None:
    request = aiand.CreateUploadRequest.from_dict(
        {
            "filename": "guide.pdf",
            "purpose": "document",
            "bytes": 1024,
            "mime_type": "application/pdf",
        }
    )

    assert request.purpose == "document"


def test_upload_purpose_rejects_unknown_values() -> None:
    with pytest.raises(ValidationError):
        aiand.CreateUploadRequest.from_dict(
            {
                "filename": "unknown.bin",
                "purpose": "other",
                "bytes": 1024,
                "mime_type": "application/octet-stream",
            }
        )


def test_file_deleted_accepts_boolean_true() -> None:
    deleted = aiand.FileDeleted.from_dict(
        {
            "id": "file-test",
            "object": "file",
            "deleted": True,
        }
    )

    assert deleted.deleted is True


def test_chat_completion_response_accepts_null_logprobs() -> None:
    response = aiand.CreateChatCompletionResponse.from_dict(
        {
            "id": "chatcmpl-test",
            "object": "chat.completion",
            "created": 1775474514,
            "model": "openai/gpt-oss-120b",
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": {"role": "assistant", "content": "Done."},
                    "logprobs": None,
                }
            ],
        }
    )

    assert response.choices[0].logprobs is None


def test_completion_response_accepts_null_logprobs() -> None:
    response = aiand.CreateCompletionResponse.from_dict(
        {
            "id": "cmpl-test",
            "object": "text_completion",
            "created": 1775474514,
            "model": "openai/gpt-oss-120b",
            "choices": [
                {
                    "text": "Done.",
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": "stop",
                }
            ],
        }
    )

    assert response.choices[0].logprobs is None
