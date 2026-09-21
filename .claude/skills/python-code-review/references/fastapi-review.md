# FastAPI Review

> Reference for the `python-code-review` skill. Load when FastAPI (or Starlette-based routing) is present.
> Related: [pydantic-review.md](./pydantic-review.md), [security-review.md](./security-review.md), [async-concurrency-review.md](./async-concurrency-review.md).

If FastAPI is present, additionally inspect:

## API boundaries

Check:

- Request models
- Response models
- HTTP status codes
- Validation
- Error responses
- Dependency injection
- Authentication/authorization
- Route organization
- OpenAPI behavior

## Async correctness

Determine whether an endpoint is:

- `async def`
- synchronous `def`

Do not automatically convert everything to `async def`.

Check for blocking operations inside async execution, including:

- Blocking filesystem operations
- Blocking HTTP clients
- Blocking database clients
- CPU-intensive work
- Synchronous libraries

A blocking operation inside an async event loop can reduce concurrency and cause latency problems.

## Dependency injection

Check:

- Appropriate use of `Depends`
- Dependency lifetime
- Resource cleanup
- Request-scoped resources
- Avoidance of hidden global mutable state

## Error handling

Check that internal exceptions are not accidentally exposed through HTTP responses.

Ensure error handling preserves:

- Appropriate HTTP status
- Useful client-safe message
- Diagnostic information in logs
- Correlation/request context where applicable

## Example finding

```text
[HIGH] Blocking database call inside async endpoint

Location:
src/api/routes/users.py:42

Problem:
The async endpoint calls the synchronous database client directly.

Why it matters:
The blocking call can occupy the event-loop thread while waiting for I/O,
reducing concurrency and increasing latency under load.

Recommendation:
Use the project's async database client or execute the blocking operation
through an appropriate worker mechanism.
```
