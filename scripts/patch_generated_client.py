#!/usr/bin/env python3
"""Apply small patches to generated files that OpenAPI Generator cannot express."""

from __future__ import annotations

import sys
from pathlib import Path

OLD_HEADERS = "            headers = response_data.headers,\n"
NEW_HEADERS = "            headers = self._response_headers_to_dict(response_data.headers),\n"
HELPER = '''
    @staticmethod
    def _response_headers_to_dict(headers):
        """Normalize urllib3/vcrpy response headers for ApiResponse validation."""
        if headers is None:
            return None
        if isinstance(headers, dict):
            return headers
        if hasattr(headers, "items"):
            return dict(headers.items())
        return dict(headers)

'''
INSERT_BEFORE = "    def sanitize_for_serialization(self, obj):\n"
OLD_FILE_DELETED_VALIDATOR = """    @field_validator('deleted')
    def deleted_validate_enum(cls, value):
        \"\"\"Validates the enum\"\"\"
        if value not in set(['true']):
            raise ValueError("must be one of enum values ('true')")
        return value
"""
NEW_FILE_DELETED_VALIDATOR = """    @field_validator('deleted')
    def deleted_validate_enum(cls, value):
        \"\"\"Validates the enum\"\"\"
        if value is not True:
            raise ValueError("must be True")
        return value
"""
CHOICE_LOGPROBS_REPLACEMENTS = {
    "create_chat_completion_response_choices_inner.py": (
        "    logprobs: CreateChatCompletionResponseChoicesInnerLogprobs\n",
        "    logprobs: Optional[CreateChatCompletionResponseChoicesInnerLogprobs] = None\n",
    ),
    "create_completion_response_choices_inner.py": (
        "    logprobs: CreateCompletionResponseChoicesInnerLogprobs\n",
        "    logprobs: Optional[CreateCompletionResponseChoicesInnerLogprobs] = None\n",
    ),
}
OLD_SETUP_AUTHOR = '    author="OpenAPI Generator community",\n'
NEW_SETUP_AUTHOR = '    author="ai&",\n'
OLD_SETUP_AUTHOR_EMAIL = '    author_email="team@openapitools.org",\n'
SETUP_LICENSE = '    license="Apache-2.0",\n'
SETUP_INSTALL_REQUIRES = "    install_requires=REQUIRES,\n"
OLD_HTTP_DEBUG = """            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
"""
NEW_HTTP_DEBUG = """            # Keep low-level HTTP debug disabled; it writes raw headers,
            # including Authorization.
            httplib.HTTPConnection.debuglevel = 0
"""


def patch_api_client(path: Path) -> None:
    source = path.read_text()

    if OLD_HEADERS in source:
        source = source.replace(OLD_HEADERS, NEW_HEADERS, 1)

    if "_response_headers_to_dict" not in source:
        source = source.replace(INSERT_BEFORE, HELPER + INSERT_BEFORE, 1)

    path.write_text(source)


def patch_file_deleted(path: Path) -> None:
    source = path.read_text()
    source = source.replace(OLD_FILE_DELETED_VALIDATOR, NEW_FILE_DELETED_VALIDATOR, 1)
    path.write_text(source)


def patch_nullable_choice_logprobs(models_root: Path) -> None:
    for filename, (old, new) in CHOICE_LOGPROBS_REPLACEMENTS.items():
        path = models_root / filename
        source = path.read_text()
        source = source.replace(old, new, 1)
        path.write_text(source)


def patch_setup_metadata(path: Path) -> None:
    source = path.read_text()
    source = source.replace(OLD_SETUP_AUTHOR, NEW_SETUP_AUTHOR, 1)
    source = source.replace(OLD_SETUP_AUTHOR_EMAIL, "", 1)
    source = source.replace(SETUP_LICENSE, "", 1)
    source = source.replace(SETUP_INSTALL_REQUIRES, "", 1)
    path.write_text(source)


def patch_configuration(path: Path) -> None:
    source = path.read_text()
    source = source.replace(OLD_HTTP_DEBUG, NEW_HTTP_DEBUG, 1)
    path.write_text(source)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: patch_generated_client.py SDK_ROOT", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    patch_api_client(root / "aiand" / "api_client.py")
    models_root = root / "aiand" / "models"
    patch_file_deleted(models_root / "file_deleted.py")
    patch_nullable_choice_logprobs(models_root)
    patch_setup_metadata(root / "setup.py")
    patch_configuration(root / "aiand" / "configuration.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
