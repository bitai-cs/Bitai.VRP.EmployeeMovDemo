# Testing Review

> Reference for the `python-code-review` skill. Load when reviewing tests, assessing test gaps in a change, or evaluating mocks/fixtures.
> Related: [security-review.md](./security-review.md), [async-concurrency-review.md](./async-concurrency-review.md).

## Test coverage of important behavior

Check whether important behavior is covered by tests.

Review:

- Unit tests
- Integration tests
- API tests
- Error paths
- Boundary conditions
- Security-sensitive behavior
- Concurrency behavior
- External integration failures

Good tests should generally be:

- Deterministic
- Isolated
- Readable
- Focused
- Repeatable

Look for brittle tests based on:

- Timing
- Random values without controlled seeds
- External services
- Machine-specific paths
- Global mutable state

Do not equate code coverage percentage with test quality.

A high coverage number does not prove that important behavior is correctly tested.

## Mocking

Check whether mocks:

- Represent realistic boundaries
- Verify meaningful behavior
- Avoid implementation-detail coupling
- Are not excessive
- Do not make tests pass while production behavior fails

Prefer testing observable behavior over internal implementation details.

Do not mock pure functions or simple data structures without a clear reason.

## Reporting test gaps

Report a test gap only when the untested behavior is critical (security, data integrity, money/business rules, failure handling). Tie the finding to a specific behavior that is unprotected, not to a coverage number.

When a diff changes behavior, check that tests were added or updated for the changed behavior and its error paths.
