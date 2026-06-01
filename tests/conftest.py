from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import pytest
import vcr

CASSETTE_LIBRARY_DIR = Path(__file__).parent / "cassettes"
FILTERED_RESPONSE_HEADERS = {
    "authorization",
    "cf-ray",
    "set-cookie",
    "x-aiand-org-id",
    "x-org-id",
    "x-request-id",
    "x-ratelimit-limit-requests",
    "x-ratelimit-remaining-requests",
    "x-ratelimit-reset-requests",
}


def _scrub_response(response: dict[str, Any]) -> dict[str, Any]:
    headers = response.get("headers", {})
    for header in list(headers):
        if header.lower() in FILTERED_RESPONSE_HEADERS:
            headers[header] = ["<filtered>"]
    return response


@pytest.fixture(scope="session")
def aiand_vcr() -> vcr.VCR:
    return vcr.VCR(
        cassette_library_dir=str(CASSETTE_LIBRARY_DIR),
        filter_headers=[("authorization", "Bearer <AIAND_API_KEY>")],
        before_record_response=_scrub_response,
        record_mode=os.environ.get("AIAND_VCR_RECORD_MODE", "none"),
        match_on=["method", "scheme", "host", "port", "path", "query"],
    )


@pytest.fixture(scope="session")
def require_cassette_or_recording():
    def _require(cassette_name: str) -> None:
        cassette_path = CASSETTE_LIBRARY_DIR / cassette_name
        record_mode = os.environ.get("AIAND_VCR_RECORD_MODE", "none").lower()
        has_key = bool(os.environ.get("AIAND_API_KEY"))

        if cassette_path.exists():
            return

        if record_mode != "none" and has_key:
            return

        pytest.skip(
            "No cassette is present. Put AIAND_API_KEY in .env.test and run "
            "scripts/record-cassettes to record VCR fixtures."
        )

    return _require
