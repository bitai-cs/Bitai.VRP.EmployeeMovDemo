# Configuration and Observability Review

> Reference for the `python-code-review` skill. Load when the code reads settings/environment variables, or adds/changes logging, metrics, tracing, or error reporting.
> Related: [security-review.md](./security-review.md), [pydantic-review.md](./pydantic-review.md).

## Configuration

Check:

- Environment-specific configuration
- Default values
- Required settings
- Secrets
- Configuration validation
- Type conversion
- Startup failure behavior
- Configuration scattered across modules

Prefer failing early for required invalid configuration.

Avoid silently falling back to unsafe defaults.

## Logging and observability

Check whether important production behavior is observable.

Look for:

- Meaningful log messages
- Appropriate log levels
- Structured logging
- Correlation/request identifiers
- Exception context
- Useful operational metadata
- Sensitive-data filtering

Avoid:

- Logging every line
- Logging sensitive data
- Duplicate exception logging
- Logging without useful context

For distributed applications, consider whether failures can be correlated across service boundaries.
