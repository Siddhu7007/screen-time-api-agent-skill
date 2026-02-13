# 17 Hardening Checklist Bug Prevention

## Purpose
Provide a prevention-first checklist to reduce production bugs in Screen Time API apps.

## Canonical API Surface
- Authorization state APIs (FamilyControls)
- Monitoring errors (DeviceActivity)
- Store reset APIs (ManagedSettings)
- Shield action responses (ManagedSettings)

## Implementation Pattern
- Use a single policy evaluation function shared by app and extension.
- Gate every apply path on authorization + selection + feature-toggle state.
- Validate monitor intervals and activity count before calling `startMonitoring`.
- Keep clear-all emergency reset in settings/debug paths.
- Add deterministic logging keys for monitor/store/action lifecycle.

## Failure Modes
- Stale restrictions after crashes/restarts.
- Hidden auth revocation causing “blocking stopped” confusion.
- Timezone shift creating schedule surprises.
- Overly granular schedules causing monitor registration failures.

## Validation Checklist
- [ ] Authorization revoke test case exists.
- [ ] App-group mismatch test case exists.
- [ ] Monitor error handling is user-visible and telemetry-visible.
- [ ] Named store inventory is finite and documented.
- [ ] Recovery path can clear all stores without reinstall.

## Sources
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../evidence/02-managedsettings-sdk-signatures.md`
- `../rundowns/12-cross-project-rundown.md`

## Confidence Notes
- Checklist items are mixed `sdk-backed` and `project-observed` best practices.
