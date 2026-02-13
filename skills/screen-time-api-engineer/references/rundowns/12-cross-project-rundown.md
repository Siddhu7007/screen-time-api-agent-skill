# 12 Cross-Project Rundown (Project Alpha vs Project Beta)

## Common Strengths
1. Correct framework separation: FamilyControls (select/auth), ManagedSettings (enforce), DeviceActivity (schedule), ManagedSettingsUI (custom shield UI).
2. Shared app-group state is consistently used so extensions can enforce while host app is inactive.
3. Both projects use token-native UI rendering (`Label(token)`) for app icon/title display.
4. Both include extension targets and entitlement wiring across main app + extensions.

## Key Differences

### Scheduling Strategy
- Project Alpha: multi-segment + midnight reset model with explicit named stores and fallback schedule.
- Project Beta: user schedule-derived single monitor activity plus app-level periodic reconciliation.

### Shield Semantics
- Project Alpha: strongly keyed around “unlock-after-commit” state and day rollover logic.
- Project Beta: strongly keyed around sleep window and wake/unlock offsets.

### UX Flow
- Project Alpha onboarding is linear focus-productivity flow.
- Project Beta onboarding is sleep habit flow with richer schedule validation and notification prompts.

## Shared Risks
1. Silent/weak handling of authorization revocation after first approval.
2. Limited structured diagnostics in release path.
3. Redundant writes across host and monitor extension can create unnecessary churn.

## Unified Hardened Reference Pattern
1. Always check `AuthorizationCenter.authorizationStatus` before applying shields in both app and extension code paths.
2. Normalize a single source-of-truth state machine for `authorized`, `hasSelection`, `scheduleActive`, `shieldApplied`.
3. Keep clear-all fallback available for stale restrictive states across named/default stores.
4. Add explicit user-facing recovery prompts for revoke/deny (`Settings -> Screen Time -> Apps with Screen Time Access`).
5. Add deterministic logging identifiers for monitor start/stop/apply/clear/error operations.

## Migration Guidance
- Projects can converge on a shared policy engine abstraction:
  - `PolicyInput` (auth, selection, time-state)
  - `PolicyDecision` (apply/clear + target stores)
  - `PolicyApplier` (ManagedSettingsStore writes)
- This reduces duplicate logic and race-prone branches across app and extension targets.

Last analyzed: `2026-02-08`
