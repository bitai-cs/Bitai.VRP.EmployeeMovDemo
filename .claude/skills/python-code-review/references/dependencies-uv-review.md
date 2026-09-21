# Dependency and UV Review

> Reference for the `python-code-review` skill. Load when `pyproject.toml`, lock files, or requirements files change, or when the project uses UV.
> Related: [security-review.md](./security-review.md), [config-observability-review.md](./config-observability-review.md).

## Dependencies

Inspect:

- `pyproject.toml`
- Lock files
- Dependency versions
- Runtime vs development dependencies
- Unused dependencies
- Duplicate functionality
- Deprecated packages

Do not recommend dependency changes without understanding the project's Python version and package manager.

For UV projects, respect the project's existing `pyproject.toml` and lock-file workflow.

Do not manually edit generated lock files unless the project's workflow requires it.

## UV

If UV is used, recognize it as the project's package/dependency/environment manager.

Check for:

- Correct `pyproject.toml` configuration
- Reproducible dependency resolution
- Appropriate dependency groups
- Development dependencies
- Python version constraints
- Consistent lock-file usage
- Correct project commands

Prefer the repository's existing UV workflow.

Do not introduce another package manager without a clear requirement.
