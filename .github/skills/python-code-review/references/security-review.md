# Security Review

> Reference for the `python-code-review` skill. Load for any review of production code that handles input, secrets, auth, files, processes, or serialization.
> Related: [fastapi-review.md](./fastapi-review.md), [config-observability-review.md](./config-observability-review.md), [dependencies-uv-review.md](./dependencies-uv-review.md).

Treat security as a first-class review category.

Check for:

## Secrets

Look for:

- Hard-coded credentials
- API keys
- Tokens
- Passwords
- Private keys
- Secrets committed to source

Configuration should normally come from appropriate secret/configuration mechanisms.

Never reproduce an exposed secret in the review output.

If an actual secret is found, refer to it generically and recommend rotation/remediation.

## Injection

Check:

- SQL injection
- Command injection
- Shell execution
- Template injection
- LDAP injection
- Path traversal
- Expression injection
- Unsafe dynamic evaluation

Pay special attention to:

```python
eval(...)
exec(...)
os.system(...)
subprocess(..., shell=True)
```

These are not automatically vulnerabilities; determine whether untrusted input can reach them.

## Deserialization

Review:

- `pickle`
- Unsafe YAML loading
- Dynamic imports
- Arbitrary object reconstruction

Treat untrusted deserialization as high risk.

## Web/API security

Check:

- Authentication
- Authorization
- CORS
- CSRF where applicable
- Rate limiting
- Input validation
- File upload handling
- SSRF
- Sensitive information disclosure
- Security headers where applicable

## Logging

Ensure sensitive values are not logged:

- Passwords
- Tokens
- Session identifiers
- Authorization headers
- Secrets
- Sensitive personal information

## Severity guidance

- Authentication/authorization bypass, remote code execution, untrusted deserialization, and exposed production secrets are normally **CRITICAL**.
- Injection paths where untrusted input demonstrably reaches a sink are normally **HIGH** or **CRITICAL**.
- A risky construct (`shell=True`, `eval`) with no demonstrable path from untrusted input should be reported as lower severity, with the assumption stated explicitly.
