# Release automation for the `aiand` PyPI package.
#
# Day-to-day:   make preflight        # sync + test + lint + build + check
# Verify:       make verify VERSION=0.1.0
# Cut release:  make release VERSION=0.2.0   # bumps tag -> CI publishes via Trusted Publishing
#
# Manual upload (break-glass only; prefer the tag-triggered CI publish):
#   make upload   # requires TWINE_USERNAME=__token__ and TWINE_PASSWORD in the environment
#
# Notes baked in from the 0.1.0 release:
#   - remote is `origin` (not `upstream`)
#   - the verify venv pins Python >=3.10 (system python3 may be too old)
#   - `uv venv` has no pip, so we install with `uv pip`
#   - the import check runs from /tmp so it loads the installed wheel, not local ./aiand

PYTHON_VERSION ?= 3.12
VERIFY_VENV    := /tmp/aiand-verify

.PHONY: help sync test lint clean build check preflight verify upload tag release

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

sync: ## Fast-forward main from origin (with tags)
	git fetch origin main --tags
	git switch main
	git pull --ff-only origin main

test: ## Run the test suite
	uv run --extra test pytest

lint: ## Lint tests and scripts
	uv run --extra dev ruff check tests scripts

clean: ## Remove build artifacts
	rm -rf dist build *.egg-info

build: clean ## Build sdist + wheel
	uv run --extra dev python -m build

check: ## Validate built artifacts with twine
	uv run --extra dev twine check dist/*

preflight: sync test lint build check ## Everything safe and repeatable before a release

verify: ## Clean-room install of VERSION from PyPI and import it (VERSION required)
	@test -n "$(VERSION)" || { echo "VERSION is required, e.g. make verify VERSION=0.1.0"; exit 1; }
	rm -rf $(VERIFY_VENV)
	uv venv --python $(PYTHON_VERSION) $(VERIFY_VENV)
	VIRTUAL_ENV=$(VERIFY_VENV) uv pip install "aiand==$(VERSION)"
	cd /tmp && $(VERIFY_VENV)/bin/python -c "import aiand; print('aiand', aiand.__version__, 'import ok')"

upload: ## Break-glass manual upload (prefer CI). Needs TWINE_* in env
	@test -n "$$TWINE_PASSWORD" || { echo "Set TWINE_USERNAME=__token__ and TWINE_PASSWORD in the environment"; exit 1; }
	uv run --extra dev twine upload dist/*

tag: ## Create and push an annotated release tag (VERSION required)
	@test -n "$(VERSION)" || { echo "VERSION is required, e.g. make tag VERSION=0.2.0"; exit 1; }
	git tag -a v$(VERSION) -m "Release $(VERSION)"
	git push origin v$(VERSION)

release: preflight tag ## Run preflight, then push the tag to trigger CI publish (VERSION required)
	@echo "Pushed v$(VERSION). GitHub Actions will build and publish to PyPI via Trusted Publishing."
	@echo "After it lands: make verify VERSION=$(VERSION)"
