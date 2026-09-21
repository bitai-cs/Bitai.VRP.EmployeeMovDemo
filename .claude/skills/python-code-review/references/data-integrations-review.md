# Database, Persistence, and External Service Review

> Reference for the `python-code-review` skill. Load when the code touches a database/ORM, transactions, migrations, or calls external HTTP services.
> Related: [async-concurrency-review.md](./async-concurrency-review.md), [performance-review.md](./performance-review.md), [security-review.md](./security-review.md).

## Database and persistence

When persistence exists, inspect:

- Query correctness
- Transaction boundaries
- Connection lifecycle
- N+1 queries
- Pagination
- Index assumptions
- Concurrency
- Isolation
- Error handling
- Retry behavior
- Idempotency
- Migration compatibility

Do not assume a particular database technology unless the repository establishes it.

## HTTP clients and external services

Check:

- Timeouts
- Retries
- Backoff
- Connection reuse
- Error classification
- Rate limits
- Authentication
- Response validation
- Partial failures
- Idempotency

Retry only operations where retrying is safe or explicitly designed.

Do not blindly retry every exception.
