# aiand-python

Python で ai& API を使用します。

このパッケージは、公開されている ai& OpenAPI spec から
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) を使って生成されています。現在 spec に含まれている
OpenAI 互換エンドポイントである models、chat completions、legacy completions、
responses、files、chunked uploads をカバーしています。

ai& は [docs.aiand.com](https://docs.aiand.com) でもドキュメントを公開しています。SDK 更新
スクリプトは公開 OpenAPI spec から再生成し、その後 Python generator のエッジケース向けに
小さな生成後互換レイヤーを適用します。

## Installation

このチェックアウトからインストールする場合:

```sh
cd aiand-python
python -m pip install -e .
```

`uv` を使う場合:

```sh
cd aiand-python
uv sync --extra test --extra dev
```

このパッケージが公開されたら、次のようにインストールします:

```sh
python -m pip install aiand
```

現在の SDK バージョンは `0.1.0` です。リリースノートは [CHANGELOG.md](CHANGELOG.md) を参照してください。

## Usage

API キーを環境変数に設定します:

```sh
export AIAND_API_KEY="sk-..."
```

クライアントを作成します:

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    models = client.list_models()

print(models.data[0].id)
```

生成されたベース URL は `https://api.aiand.com` です。OpenAPI のパスには `/v1` が含まれるため、SDK の
呼び出しは `https://api.aiand.com/v1/models` のような URL に解決されます。

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

## Responses

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

request = aiand.CreateResponseRequest(
    model="openai/gpt-oss-120b",
    input=aiand.ResponseInput("Give me one practical sentence about ai&."),
    temperature=0.2,
    max_output_tokens=64,
    parallel_tool_calls=False,
    truncation="disabled",
)

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    response = client.create_response(request)

print(response.to_dict()["output"])
```

型付きコンストラクタは、設定されていない任意パラメータをリクエスト本文から省略します。

## Models And Pricing

```python
import os

import aiand

configuration = aiand.Configuration(access_token=os.environ["AIAND_API_KEY"])

with aiand.ApiClient(configuration) as api_client:
    client = aiand.OpenaiApi(api_client)
    models = client.list_models()

for model in models.data:
    print(
        model.id,
        model.provider,
        model.context_window,
        model.capabilities,
        model.input_per_1m,
        model.output_per_1m,
    )
```

ドキュメントでは、モデル料金は精密な文字列フィールドとして説明されています。この SDK では
`input_per_1m` と `output_per_1m` を float ではなく文字列として保持します。

## Files

ファイルを一度アップロードし、返された `file_id` を chat completion リクエストから参照します。

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

ファイル purpose の値は `vision`、`video`、`audio`、`document` です。

## Chunked Uploads

より大きなアセットでは、upload を作成し、part を順番に追加してから完了します。

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

生成された各 operation は、OpenAPI Generator の標準的なリクエスト制御を受け付けます:

```python
response = client.list_models(
    _request_timeout=(5, 30),
    _headers={"X-Request-Source": "aiand-python"},
)
```

API キー認証には `Configuration(access_token=...)` を使用します。ドキュメントでは、browser/JWT
auth では `X-Org-ID` が必要になる場合があると説明されています。サーバーサイド API キーでは、organization は
キーから解決されます。

## Errors

生成されたクライアントは、非 2xx レスポンスに対して `aiand.ApiException` を送出します。

```python
import aiand

try:
    client.list_models()
except aiand.ApiException as error:
    print(error.status)
    print(error.body)
```

## Testing

ネットワーク呼び出しなしで unit tests を実行します:

```sh
uv run --extra test pytest
```

hand-maintained code 向けの focused linter を実行します:

```sh
uv run --extra dev ruff check tests scripts
```

`aiand/` 以下の生成コードは意図的に Ruff から除外されています。これは
OpenAPI Generator によって再作成されるため、手で再フォーマットするのではなく、挙動をレビューする必要があります。

## Recording VCR Cassettes

テストでは live API coverage のために [vcrpy](https://vcrpy.readthedocs.io/) を使用します。Cassettes は
`tests/cassettes` に置かれます。

cassettes を記録するには、`.env.test` を作成します:

```sh
AIAND_API_KEY=sk-your-real-aiand-api-key
```

その後、次を実行します:

```sh
./scripts/record-cassettes
```

VCR config は `Authorization` ヘッダーと、一般的な request/organization ヘッダーをフィルタします。
recording script は `AIAND_VCR_RECORD_MODE=once` を設定します。`.env.test` はコミットしないでください。
sanitized cassette files のみをコミットしてください。

VCR suite は、公開 endpoint group ごとに 1 つの compact cassette を記録します:

- `list_models.yaml`
- `chat_completion.yaml`
- `completion.yaml`
- `response.yaml`
- `files_lifecycle.yaml`
- `uploads_complete.yaml`
- `uploads_cancel.yaml`

これらの cassettes を合わせると、現在 OpenAPI spec から生成されるすべての endpoint に到達します:
`GET /v1/models`、`POST /v1/chat/completions`、`POST /v1/completions`、
`POST /v1/responses`、`GET /v1/files`、`POST /v1/files`、`GET /v1/files/{id}`、
`GET /v1/files/{id}/content`、`DELETE /v1/files/{id}`、`POST /v1/uploads`、
`POST /v1/uploads/{id}/parts`、`POST /v1/uploads/{id}/complete`、および
`POST /v1/uploads/{id}/cancel` です。

## Updating The SDK

Prerequisites:

- Java。OpenAPI Generator に必要です。
- Node/npm と `npx`。`@openapitools/openapi-generator-cli@2.34.0` の実行に使用します。
- Python 3.10 以上。
- development と tests 用の `uv`。

最新の公開 spec から再生成します:

```sh
./scripts/update-sdk
```

この script は次を行います:

1. `https://api.aiand.com/openapi.json` を `openapi/openapi.json` にダウンロードします。
2. `openapi-generator-config.yaml` で OpenAPI Generator を実行します。
3. generator-specific Python compatibility のために `scripts/patch_generated_client.py` を適用します。

再生成後:

```sh
uv run --extra test pytest
uv run --extra dev ruff check tests scripts
```

`aiand/`、`docs/`、`openapi/openapi.json` の生成 diff をレビューしてください。公開
spec に endpoint が追加された場合や generator edge case が修正された場合は、
post-generation patch layer が小さく明確なままであるように `scripts/patch_generated_client.py` を更新してください。

npm wrapper は `scripts/update-sdk` で pin されており、OpenAPI Generator version は
`openapitools.json` で pin されています。どちらかを upgrade するには、pin された version を編集し、再生成して、
生成 diff を慎重にレビューしてください。

## Development Notes

ほとんどの SDK ファイルは生成されています。主な hand-maintained files は次のとおりです:

- `README.md`
- `CHANGELOG.md`
- `LICENSE`
- `pyproject.toml`
- `scripts/update-sdk`
- `scripts/patch_generated_client.py`
- `scripts/record-cassettes`
- `tests/`

bug reports と pull requests を歓迎します。

## License

このプロジェクトは [Apache License 2.0](LICENSE) の下でライセンスされています。
