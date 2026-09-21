# Performance Review

> Reference for the `python-code-review` skill. Load when there is a plausible performance concern (large data, repeated queries/calls, memory-heavy processing).
> Related: [data-integrations-review.md](./data-integrations-review.md), [async-concurrency-review.md](./async-concurrency-review.md), [ortools-review.md](./ortools-review.md).

Look for meaningful performance problems.

Check:

- Algorithmic complexity
- Repeated database queries
- N+1 behavior
- Repeated network calls
- Unnecessary serialization
- Excessive copying
- Unnecessary materialization
- Large memory allocations
- Unbounded collections
- Inefficient loops
- Repeated expensive calculations

Do not label code as a performance problem without a plausible workload or mechanism.

Prefer measurable evidence when performance is important.

Avoid micro-optimizations that reduce readability without meaningful benefit.
