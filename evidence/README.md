# Evidence and sanitization notes

I used screenshots, terminal output, management-event JSON, and a delivered S3 data-event log to verify the lab. The raw screenshots and logs remain private.

## Files

| File | Source | Scope |
| --- | --- | --- |
| `run-instances.sanitized.json` | Downloaded successful RunInstances record | Selected launch settings and the successful instance response. |
| `get-object.sanitized.json` | Downloaded CloudTrail data-event file | The successful application-role read, response status, object size, and TLS version. |
| `management-checks.sanitized.json` | Management-event records pasted during the lab | Selected fields from three dry-run checks and the TCP 8080 ingress change. |

The files contain a `_publication` notice and a `Records` array. This wrapper makes the edited nature explicit. They are evidence excerpts for explanation, not untouched CloudTrail exports or integrity-verifiable log originals.

## Retained facts

I retained event names, event times, the region, success/error outcomes, relevant permissions, metadata settings, and the observed 34-byte object read. The source IP and role relationships use consistent replacements so the distinction between the human action and the application action remains visible.

## Replaced or omitted details

I replaced account IDs, IP addresses, bucket names, instance and security-group IDs, and human session names. I omitted access-key identifiers, internal principal IDs, request IDs, event IDs, identity-store references, unneeded network identifiers, and full user-agent strings. Access-key IDs alone are not secret keys, but they were not needed to explain the results.

Example account numbers are `111111111111` and `222222222222`. Example IPv4 addresses are `198.51.100.10` for the human test source and `203.0.113.10` for the instance's public source. These are not live lab addresses.

## Test observations

- Local `/health` and `/hello` returned HTTP 200.
- The allowed-source browser test returned the expected greeting.
- Reading the exact object from EC2 succeeded.
- Listing the bucket as the application role returned `AccessDenied` for `s3:ListBucket`.
- An unsigned direct object URL returned `AccessDenied`.
- The alternate-connection API test timed out while the allowed-source control test still succeeded. This is consistent with the network restriction, not standalone proof of the timeout's cause.
- The S3 data event recorded a successful `GetObject` by `LabAppRole`, HTTP 200, and 34 bytes returned.

The negative-test observations are documented from the original session. They are not fabricated CloudTrail events. No new live AWS tests were run while preparing this public repository.
