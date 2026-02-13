# 15 Project Alpha Implementation Analysis

## Purpose
Document Project Alpha’s Screen Time implementation as a concrete reference and extract production-grade patterns.

## Canonical API Surface
- `AuthorizationCenter`, `FamilyActivityPicker`, token labels
- `ManagedSettingsStore` and shield APIs
- `DeviceActivityCenter.startMonitoring`
- ManagedSettingsUI shield config and action delegates

## Implementation Pattern
- Central lock manager (`ShieldController`) drives authorization, selection persistence, and shield apply/clear.
- Named + default store strategy reduces stale policy drift.
- Monitor extension reevaluates state at interval start/end/threshold and enforces policy in background.
- Onboarding requires permission and selection before final completion.
- Token label display is used in onboarding/dashboard icon stacks.

## Failure Modes
1. Silent auth request failures in picker launch path can hide denied/revoked state.
2. Host + extension can perform redundant clear/apply cycles.
3. Missing structured observability for schedule registration and monitor callback outcomes.

## Validation Checklist
- [ ] Deny/revoke UX path is explicit and testable.
- [ ] Named-store clear-all path tested for stale state elimination.
- [ ] Midnight rollover and day-state reset validated across timezone changes.
- [ ] Token icon rendering remains stable after app relaunch.

## Sources
- Template note: Replace `{{PROJECT_ALPHA_PATH}}` with your local repository root before opening project-observed files.
- `../rundowns/10-project-alpha-rundown.md`
- `{{PROJECT_ALPHA_PATH}}/ProjectAlpha/AppLocking/ProjectAlphaLockManager.swift`
- `{{PROJECT_ALPHA_PATH}}/ProjectAlphaMonitor/DeviceActivityMonitorExtension.swift`
- `{{PROJECT_ALPHA_PATH}}/ProjectAlphaShieldConfiguration/ShieldConfigurationExtension.swift`
- `{{PROJECT_ALPHA_PATH}}/ProjectAlphaShieldAction/ShieldActionExtension.swift`

## Confidence Notes
- This analysis is `project-observed` and grounded in current repository state as of `2026-02-08`.
