# test_python_ci

[![CI](https://github.com/vladiant/test_python_ci/actions/workflows/ci.yml/badge.svg)](https://github.com/vladiant/test_python_ci/actions/workflows/ci.yml)
[![Release](https://github.com/vladiant/test_python_ci/actions/workflows/release.yml/badge.svg)](https://github.com/vladiant/test_python_ci/actions/workflows/release.yml)
[![Security](https://github.com/vladiant/test_python_ci/actions/workflows/security.yml/badge.svg)](https://github.com/vladiant/test_python_ci/actions/workflows/security.yml)

A minimal Python package that demonstrates the most important CI/CD features
using **GitHub Actions**.

## Project layout

```
src/calculator/       # source package
tests/                # pytest test suite
.github/workflows/
  ci.yml              # lint, type-check, matrix tests + coverage upload
  release.yml         # build sdist/wheel and publish to PyPI on version tag
  security.yml        # CodeQL static analysis + pip-audit dependency scan
pyproject.toml        # project metadata, tool config (ruff, mypy, pytest, coverage)
```

## CI/CD features demonstrated

| Feature | Tool / Action |
|---|---|
| Linting | [ruff](https://docs.astral.sh/ruff/) |
| Formatting check | `ruff format --check` |
| Static type checking | [mypy](https://mypy.readthedocs.io/) (strict mode) |
| Matrix testing | `actions/setup-python` across Python 3.9 – 3.12 |
| Test coverage | `pytest-cov` → XML → [Codecov](https://codecov.io) |
| Publish to PyPI | `pypa/gh-action-pypi-publish` with OIDC trusted publishing |
| CodeQL analysis | `github/codeql-action` |
| Dependency audit | [pip-audit](https://github.com/pypa/pip-audit) |

## Local development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# run tests
pytest --cov=calculator --cov-report=term-missing

# lint + format
ruff check . && ruff format .

# type check
mypy src/
```

## Releasing a new version

1. Bump `version` in `pyproject.toml` and `src/calculator/__init__.py`.
2. Push a tag: `git tag v0.2.0 && git push --tags`.
3. The `release.yml` workflow builds the package and publishes it to PyPI
   via OIDC (no long-lived token required — configure a trusted publisher
   in your PyPI project settings first).
