#!/usr/bin/env python3
"""Patch the published OpenAPI document with documented SDK-generation details."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

API_BASE_URL = "https://api.aiand.com"
FILE_PURPOSES = ["vision", "video", "audio", "document"]
BINARY_MULTIPART_FIELDS = {
    "CreateFileRequest": "file",
    "AddUploadPartRequest": "data",
}


def set_file_purposes(schema: dict[str, Any]) -> None:
    purpose = schema.get("properties", {}).get("purpose")
    if not isinstance(purpose, dict):
        return

    purpose["enum"] = FILE_PURPOSES
    purpose["description"] = (
        "One of `vision`, `video`, `audio`, or `document`. Determines size, "
        "MIME limits, and which models can reference the file. Optional for "
        "single-shot file uploads when the API can infer it from MIME type."
    )


def patch_file_purposes(spec: dict[str, Any]) -> None:
    schemas = spec.get("components", {}).get("schemas", {})
    for name in ("CreateFileRequest", "CreateUploadRequest", "FileObject", "UploadObject"):
        schema = schemas.get(name)
        if isinstance(schema, dict):
            set_file_purposes(schema)


def patch_model_prices(spec: dict[str, Any]) -> None:
    model_properties = (
        spec.get("paths", {})
        .get("/v1/models", {})
        .get("get", {})
        .get("responses", {})
        .get("200", {})
        .get("content", {})
        .get("application/json", {})
        .get("schema", {})
        .get("properties", {})
        .get("data", {})
        .get("items", {})
        .get("properties", {})
    )

    if not isinstance(model_properties, dict):
        return

    for field in ("input_per_1m", "output_per_1m"):
        if field in model_properties:
            model_properties[field] = {
                "type": "string",
                "description": "USD per 1 million tokens. Returned as a string for precision.",
            }


def patch_multipart_binary_fields(spec: dict[str, Any]) -> None:
    schemas = spec.get("components", {}).get("schemas", {})
    if not isinstance(schemas, dict):
        return

    for schema_name, property_name in BINARY_MULTIPART_FIELDS.items():
        property_schema = (
            schemas.get(schema_name, {})
            .get("properties", {})
            .get(property_name)
        )
        if not isinstance(property_schema, dict):
            continue

        property_schema["type"] = "string"
        property_schema["format"] = "binary"


def patch_spec(spec: dict[str, Any]) -> dict[str, Any]:
    spec["servers"] = [{"url": API_BASE_URL, "description": "ai& API"}]
    patch_model_prices(spec)
    patch_file_purposes(spec)
    patch_multipart_binary_fields(spec)
    return spec


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: patch_openapi_spec.py INPUT_JSON OUTPUT_JSON", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    spec = json.loads(input_path.read_text())
    output_path.write_text(json.dumps(patch_spec(spec), indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
