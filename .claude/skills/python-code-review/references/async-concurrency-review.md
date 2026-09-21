# Async, Concurrency, and Resource Management Review

> Reference for the `python-code-review` skill. Load when the code uses `async`/`await`, `asyncio`, threads, processes, workers, background tasks, or manages files/sockets/clients/connections.
> Related: [fastapi-review.md](./fastapi-review.md), [data-integrations-review.md](./data-integrations-review.md), [performance-review.md](./performance-review.md).

## Async and concurrency

For `asyncio`, concurrent execution, workers, or background tasks, check:

- Blocking operations
- Missing `await`
- Incorrect task lifecycle
- Unhandled task exceptions
- Cancellation handling
- Race conditions
- Shared mutable state
- Locks
- Semaphores
- Queues
- Timeouts
- Resource cleanup
- Task leaks
- Incorrect assumptions about thread safety

Pay particular attention to:

```python
async def ...
```

that calls CPU-heavy synchronous code.

CPU-bound workloads should generally not be assumed to become concurrent merely because the calling function is asynchronous.

## Resource management

Check deterministic cleanup of:

- Files
- Database connections
- HTTP clients
- Sessions
- Sockets
- Threads
- Processes
- Temporary files
- Locks
- Async tasks

Check for:

- Leaks
- Unbounded resource creation
- Missing timeouts
- Missing connection limits
- Incorrect reuse of clients

For network calls, inspect:

- Timeout configuration
- Retry behavior
- Connection pooling
- Error handling
- Cancellation

Never recommend infinite retries.
