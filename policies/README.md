# Policy examples

These examples describe the narrow controls used in my lab. Account and resource identifiers are placeholders. They are not an exported inventory of all effective account permissions.

- `lab-app-trust.json`: permits EC2 to assume the application role.
- `lab-app-permissions.json`: grants `s3:GetObject` on the one configured object. It does not grant `s3:ListBucket`.
- `pass-role-statement.json`: a single statement showing how builder access limited passing the role to EC2. It is not a complete standalone policy document or the full LabBuilder policy.
- `cloudtrail-event-selectors.json`: an advanced-selector array for read-only S3 data events matching the exact object ARN. It does not grant S3 access. It does not restrict `eventName` specifically to `GetObject`.

For a separate deployment, replace the sample bucket and account values consistently. The instance role needs an instance profile, and the trail needs its own configuration and a destination bucket with appropriate delivery permissions. Those additional provisioning steps are explained in the report; this folder is not a one-click deployment system.

The broader human setup permission sets are described in the report rather than represented as exact exports. I have not presented reconstructed administrative policies as original downloaded policies.
