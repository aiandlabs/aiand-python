import base64
import os

import aiand

MODEL_ID = os.environ.get("AIAND_TEST_MODEL", "openai/gpt-oss-120b")
REQUEST_TIMEOUT = (5, 60)
PNG_BYTES = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/p9sAAAAASUVORK5CYII="
)
PDF_BYTES = (
    b"%PDF-1.4\n"
    b"1 0 obj\n"
    b"<< /Type /Catalog >>\n"
    b"endobj\n"
    b"trailer\n"
    b"<< /Root 1 0 R >>\n"
    b"%%EOF\n"
)


def _configuration() -> aiand.Configuration:
    return aiand.Configuration(access_token=os.environ.get("AIAND_API_KEY", "sk-recorded"))


def _cassette(aiand_vcr, require_cassette_or_recording, name: str):
    require_cassette_or_recording(name)
    return aiand_vcr.use_cassette(name)


def test_list_models_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    with aiand.ApiClient(_configuration()) as api_client:
        client = aiand.OpenaiApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "list_models.yaml"):
            response = client.list_models(_request_timeout=REQUEST_TIMEOUT)

    assert response.object == "list"
    assert response.data
    assert response.data[0].id


def test_create_chat_completion_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    request = aiand.CreateChatCompletionRequest.from_dict(
        {
            "model": MODEL_ID,
            "messages": [{"role": "user", "content": "Reply with exactly one short sentence."}],
            "temperature": 0,
            "max_completion_tokens": 12,
        }
    )

    with aiand.ApiClient(_configuration()) as api_client:
        client = aiand.OpenaiApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "chat_completion.yaml"):
            response = client.create_chat_completion(
                request,
                _request_timeout=REQUEST_TIMEOUT,
            )

    assert response.object == "chat.completion"
    assert response.choices
    assert response.choices[0].message.role == "assistant"


def test_create_completion_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    request = aiand.CreateCompletionRequest.from_dict(
        {
            "model": MODEL_ID,
            "prompt": "Write three words about reliable SDKs:",
            "temperature": 0,
            "max_tokens": 8,
        }
    )

    with aiand.ApiClient(_configuration()) as api_client:
        client = aiand.OpenaiApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "completion.yaml"):
            response = client.create_completion(
                request,
                _request_timeout=REQUEST_TIMEOUT,
            )

    assert response.object == "text_completion"
    assert response.choices
    assert response.choices[0].text is not None


def test_create_response_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    request = aiand.CreateResponseRequest(
        model=MODEL_ID,
        input=aiand.ResponseInput("Reply with exactly one short sentence."),
        temperature=0,
        max_output_tokens=12,
        parallel_tool_calls=False,
        truncation="disabled",
    )

    with aiand.ApiClient(_configuration()) as api_client:
        client = aiand.OpenaiApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "response.yaml"):
            response = client.create_response(
                request,
                _request_timeout=REQUEST_TIMEOUT,
            )

    assert response.object == "response"
    assert response.id
    assert response.status in {
        "completed",
        "failed",
        "in_progress",
        "cancelled",
        "queued",
        "incomplete",
    }
    assert response.model
    assert response.output is not None


def test_files_lifecycle_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    with aiand.ApiClient(_configuration()) as api_client:
        files = aiand.FilesApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "files_lifecycle.yaml"):
            uploaded = files.upload_file(
                file=("aiand-vcr-pixel.png", PNG_BYTES),
                purpose="vision",
                _request_timeout=REQUEST_TIMEOUT,
            )
            listed = files.list_files(_request_timeout=REQUEST_TIMEOUT)
            fetched = files.get_file(uploaded.id, _request_timeout=REQUEST_TIMEOUT)
            content = files.get_file_content(uploaded.id, _request_timeout=REQUEST_TIMEOUT)
            deleted = files.delete_file(uploaded.id, _request_timeout=REQUEST_TIMEOUT)

    assert uploaded.object == "file"
    assert uploaded.id.startswith("file-")
    assert listed.object == "list"
    assert fetched.id == uploaded.id
    assert content == PNG_BYTES
    assert deleted.id == uploaded.id
    assert deleted.deleted is True


def test_uploads_complete_lifecycle_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    with aiand.ApiClient(_configuration()) as api_client:
        uploads = aiand.UploadsApi(api_client)
        files = aiand.FilesApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "uploads_complete.yaml"):
            upload = uploads.create_upload(
                aiand.CreateUploadRequest.from_dict(
                    {
                        "filename": "aiand-vcr-upload.png",
                        "purpose": "vision",
                        "bytes": len(PNG_BYTES),
                        "mime_type": "image/png",
                    }
                ),
                _request_timeout=REQUEST_TIMEOUT,
            )
            part = uploads.add_upload_part(
                upload.id,
                data=("aiand-vcr-upload-part.png", PNG_BYTES),
                _request_timeout=REQUEST_TIMEOUT,
            )
            completed = uploads.complete_upload(
                upload.id,
                aiand.CompleteUploadRequest.from_dict({"part_ids": [part.id]}),
                _request_timeout=REQUEST_TIMEOUT,
            )
            deleted = files.delete_file(completed.file.id, _request_timeout=REQUEST_TIMEOUT)

    assert upload.status == "pending"
    assert part.upload_id == upload.id
    assert completed.status == "completed"
    assert completed.file is not None
    assert completed.file.id.startswith("file-")
    assert deleted.id == completed.file.id
    assert deleted.deleted is True


def test_uploads_cancel_with_vcr(aiand_vcr, require_cassette_or_recording) -> None:
    with aiand.ApiClient(_configuration()) as api_client:
        uploads = aiand.UploadsApi(api_client)

        with _cassette(aiand_vcr, require_cassette_or_recording, "uploads_cancel.yaml"):
            upload = uploads.create_upload(
                aiand.CreateUploadRequest.from_dict(
                    {
                        "filename": "aiand-vcr-cancel.pdf",
                        "purpose": "document",
                        "bytes": len(PDF_BYTES),
                        "mime_type": "application/pdf",
                    }
                ),
                _request_timeout=REQUEST_TIMEOUT,
            )
            cancelled = uploads.cancel_upload(upload.id, _request_timeout=REQUEST_TIMEOUT)

    assert upload.status == "pending"
    assert cancelled.id == upload.id
    assert cancelled.status == "cancelled"
