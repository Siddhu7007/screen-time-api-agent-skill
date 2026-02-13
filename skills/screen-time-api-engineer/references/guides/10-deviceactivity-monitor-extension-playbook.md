# 10 DeviceActivity Monitor Extension Playbook

## Purpose
Provide a production-safe pattern for monitor extension callbacks that enforce and clear policies reliably.

## Canonical API Surface
- `DeviceActivityMonitor` callbacks:
  - `intervalDidStart`
  - `intervalDidEnd`
  - `eventDidReachThreshold`
  - warning callbacks
- `ManagedSettingsStore` policy writes from extension process

## Implementation Pattern
1. In every callback, load app-group state snapshot.
2. Re-evaluate enforcement decision from shared state only.
3. Apply or clear shields atomically for intended store set.
4. Persist resulting state marker for host UI diagnostics.
5. Keep extension work bounded and deterministic.

## Failure Modes
- Extension reads stale/missing app-group keys.
- Callback applies policies without auth or selection sanity checks.
- Clearing only some stores and leaving residual restrictions.
- Complex branching that diverges from host app state machine.

## Validation Checklist
- [ ] App-group keys used by extension are versioned and documented.
- [ ] Extension handles missing selection payload safely.
- [ ] Apply and clear paths are idempotent.
- [ ] Day rollover and unlock windows are tested over midnight boundary.

## Sources
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`
- https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor

## Confidence Notes
- Callback contract is `canonical + sdk-backed`.
- Operational playbook is `project-observed`.
