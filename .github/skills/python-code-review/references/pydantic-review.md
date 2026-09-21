# Pydantic Review

> Reference for the `python-code-review` skill. Load when Pydantic (or `pydantic_settings`) is present.
> Related: [fastapi-review.md](./fastapi-review.md), [config-observability-review.md](./config-observability-review.md).

If Pydantic is present, inspect:

- Input validation
- Output validation
- Model boundaries
- Optional vs required fields
- Default values
- Mutable defaults
- Serialization
- Aliases
- Strictness
- Nested models
- Validation behavior
- Sensitive fields

Do not duplicate validation unnecessarily between Pydantic and business logic.

Distinguish:

- Structural/input validation
- Business-rule validation

Business rules should not be hidden solely inside transport-layer schemas when they belong to the domain/application layer.
