# aiand-python

Use the ai& API with Python.

This package is generated from the public ai& OpenAPI spec with
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator). It covers the
OpenAI-compatible endpoints currently present in the spec: models, chat completions,
legacy completions, files, and chunked uploads.

ai& also publishes docs at [docs.aiand.com](https://docs.aiand.com). The SDK update
script applies a small normalization layer where the docs and generated SDK need the same
shape, such as the default API server, file-purpose enum values, string pricing fields, and
multipart binary uploads.

## Installation

From this checkout:

```sh
cd aiand-python
python -m pip install -e .
```

With `uv`:

```sh
cd aiand-python
uv sync --extra test --extra dev
```

Once this package is published, install it as:

```sh
python -m pip install aiand
```

The current SDK version is `0.1.0`. See [CHANGELOG.md](CHANGELOG.md) for release notes.

## Usage

Set your API key in the environment:

```sh
export AIAND_API_KEY="sk-..."
```

Create a client:

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    models = client.list_models()

print(models.data[0].id)
```

The generated base URL is `https://api.aiand.com`. The OpenAPI paths include `/v1`, so SDK
calls resolve to URLs like `https://api.aiand.com/v1/models`.

## Chat

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

request = aiand.CreateChatCompletionRequest.from_dict(
    {
        "model": "openai/gpt-oss-120b",
        "messages": [
            {"role": "system", "content": "You are concise and practical."},
            {"role": "user", "content": "Give me one sentence about ai&."},
        ],
        "temperature": 0.2,
    }
)

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    response = client.create_chat_completion(request)

print(response.choices[0].message.content)
```

## Completions

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

request = aiand.CreateCompletionRequest.from_dict(
    {
        "model": "openai/gpt-oss-120b",
        "prompt": "Write a short product tagline for ai&:",
        "max_tokens": 32,
    }
)

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    response = client.create_completion(request)

print(response.choices[0].text)
```

## Models And Pricing

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    models = client.list_models()

for model in models.data:
    data = model.to_dict()
    print(model.id, data.get("context_window"), model.input_per_1m, model.output_per_1m)
```

The docs describe model pricing as precise string fields. This SDK keeps
`input_per_1m` and `output_per_1m` as strings instead of floats.

## Files

Upload a file once, then reference the returned `file_id` from chat completion requests.

```python
import os
from pathlib import Path

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])
image_path = Path("diagram.png")

with aiand.ApiClient(configuration) as api_client:
    files = aiand.FilesApi(api_client)
    uploaded = files.upload_file(
        file=(image_path.name, image_path.read_bytes()),
        purpose="vision",
    )

print(uploaded.id)
```

The file purpose values are `vision`, `video`, `audio`, and `document`.

## Chunked Uploads

For larger assets, create an upload, add parts in order, then complete it.

```python
import os
from pathlib import Path

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])
video_path = Path("clip.mp4")
part_bytes = video_path.read_bytes()

with aiand.ApiClient(configuration) as api_client:
    uploads = aiand.UploadsApi(api_client)

    upload = uploads.create_upload(
        aiand.CreateUploadRequest.from_dict(
            {
                "filename": video_path.name,
                "purpose": "video",
                "bytes": len(part_bytes),
                "mime_type": "video/mp4",
            }
        )
    )

    part = uploads.add_upload_part(upload.id, data=("part-1", part_bytes))
    completed = uploads.complete_upload(
        upload.id,
        aiand.CompleteUploadRequest.from_dict({"part_ids": [part.id]}),
    )

print(completed.file.id)
```

## Timeouts And Headers

Every generated operation accepts OpenAPI Generator's standard request controls:

```python
response = client.list_models(
    _request_timeout=(5, 30),
    _headers={"X-Request-Source": "aiand-python"},
)
```

Use `Configuration(access_token=...)` for API-key auth. The docs note that browser/JWT
auth can require `X-Org-ID`; for server-side API keys, the organization is resolved from
the key.

## Errors

The generated client raises `aiand.ApiException` for non-2xx responses.

```python
import aiand

try:
    client.list_models()
except aiand.ApiException as error:
    print(error.status)
    print(error.body)
```

## Testing

Run the unit tests without making network calls:

```sh
uv run --extra test pytest
```

Run the focused linter for hand-maintained code:

```sh
uv run --extra dev ruff check tests scripts
```

Generated code under `aiand/` is intentionally excluded from Ruff. It is recreated by
OpenAPI Generator and should be reviewed for behavior, not reformatted by hand.

## Recording VCR Cassettes

Tests use [vcrpy](https://vcrpy.readthedocs.io/) for live API coverage. Cassettes live in
`tests/cassettes`.

To record cassettes, create `.env.test`:

```sh
AIAND_API_KEY=sk-your-real-aiand-api-key
```

Then run:

```sh
./scripts/record-cassettes
```

The VCR config filters the `Authorization` header and common request/organization headers.
The recording script sets `AIAND_VCR_RECORD_MODE=once`. Do not commit `.env.test`. Only
commit sanitized cassette files.

The VCR suite records one compact cassette per public endpoint group:

- `list_models.yaml`
- `chat_completion.yaml`
- `completion.yaml`
- `files_lifecycle.yaml`
- `uploads_complete.yaml`
- `uploads_cancel.yaml`

Together those cassettes hit every endpoint currently generated from the OpenAPI spec:
`GET /v1/models`, `POST /v1/chat/completions`, `POST /v1/completions`,
`GET /v1/files`, `POST /v1/files`, `GET /v1/files/{id}`,
`GET /v1/files/{id}/content`, `DELETE /v1/files/{id}`, `POST /v1/uploads`,
`POST /v1/uploads/{id}/parts`, `POST /v1/uploads/{id}/complete`, and
`POST /v1/uploads/{id}/cancel`.

## Updating The SDK

Prerequisites:

- Java, required by OpenAPI Generator.
- Node/npm with `npx`, used to run `@openapitools/openapi-generator-cli@2.34.0`.
- Python 3.10 or newer.
- `uv` for development and tests.

Regenerate from the latest published spec:

```sh
./scripts/update-sdk
```

That script:

1. Downloads `https://api.aiand.com/openapi.json`.
2. Applies documented normalization in `scripts/patch_openapi_spec.py`.
3. Writes the patched spec to `openapi/openapi.json`.
4. Runs OpenAPI Generator with `openapi-generator-config.yaml`.

After regenerating:

```sh
uv run --extra test pytest
uv run --extra dev ruff check tests scripts
```

Review the generated diff in `aiand/`, `docs/`, and `openapi/openapi.json`. If the public
spec has gained endpoints or corrected a normalized field, update
`scripts/patch_openapi_spec.py` so the local patch layer remains small and obvious.

The OpenAPI Generator version is pinned in `openapitools.json`. To upgrade the generator,
edit that file, regenerate, and review the generated diff carefully.

## Development Notes

Most SDK files are generated. The main hand-maintained files are:

- `README.md`
- `CHANGELOG.md`
- `LICENSE`
- `pyproject.toml`
- `scripts/update-sdk`
- `scripts/patch_openapi_spec.py`
- `scripts/patch_generated_client.py`
- `scripts/record-cassettes`
- `tests/`

Bug reports and pull requests are welcome.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
