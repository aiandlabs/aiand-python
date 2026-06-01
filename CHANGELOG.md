# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning before `1.0`, where minor versions may include
breaking changes while the SDK surface is still settling.

## [0.1.0] - 2026-05-31

Initial public Python SDK release for the ai& API.

### Added

- Generated `aiand` Python package from the public ai& OpenAPI spec.
- OpenAI-compatible API coverage for models, chat completions, legacy completions, files,
  and chunked uploads.
- Pydantic model exports for generated request and response types.
- API-key authentication through `aiand.Configuration(access_token=...)`.
- Default API server support for `https://api.aiand.com`.
- Package metadata for Python 3.10 through Python 3.13.
- Comprehensive README with installation, usage, cassette recording, testing, and SDK
  regeneration instructions.
- `scripts/update-sdk` for downloading the latest spec, applying local normalization, and
  regenerating the client with OpenAPI Generator.
- `scripts/patch_openapi_spec.py` for documented spec normalization while upstream schema
  fixes are pending.
- `scripts/patch_generated_client.py` for small generated-client compatibility patches.
- vcrpy test coverage for every generated public endpoint:
  - `GET /v1/models`
  - `POST /v1/chat/completions`
  - `POST /v1/completions`
  - `GET /v1/files`
  - `POST /v1/files`
  - `GET /v1/files/{id}`
  - `GET /v1/files/{id}/content`
  - `DELETE /v1/files/{id}`
  - `POST /v1/uploads`
  - `POST /v1/uploads/{id}/parts`
  - `POST /v1/uploads/{id}/complete`
  - `POST /v1/uploads/{id}/cancel`
- Sanitized VCR cassette fixtures with API-key and request-header redaction.
- Apache License 2.0.

### Implementation Notes

- Includes a small documented normalization layer for generation from the current public
  OpenAPI spec.
- Aligns file purpose enum values with the public docs: `vision`, `video`, `audio`, and
  `document`.
- Treats model pricing fields as strings to preserve decimal precision.
- Marks multipart upload fields as binary file bodies before generation.
- Normalizes VCR/urllib3 response headers before generated `ApiResponse` validation.
- Accepts boolean `true` for `FileDeleted.deleted`.
- Allows nullable `logprobs` values returned by completion and chat completion choices.
