# 16 Project Beta Implementation Analysis

## Purpose
Document Project Beta’s Screen Time implementation and extract reusable patterns for schedule-driven blocking products.

## Canonical API Surface
- FamilyControls authorization + picker APIs
- ManagedSettings shield APIs
- DeviceActivity schedule and monitor APIs
- ManagedSettingsUI shield configuration/action APIs

## Implementation Pattern
- `AppBlockingManager` centralizes authorization, selection persistence, schedule registration, and local state reconciliation.
- Onboarding heavily validates schedule constraints and selection prerequisites before completion.
- Monitor extension applies/clears persisted token set at interval boundaries.
- Custom shield theme adjusts copy/styling with schedule context from app-group state.
- Dashboard uses token labels for real app icon rendering.

## Failure Modes
1. Potential race between app-level periodic state checks and extension callback enforcement.
2. Extension lacks explicit user-visible remediation for auth revocation scenarios.
3. Runtime errors mostly logged to console; production telemetry path is limited.

## Validation Checklist
- [ ] Start/stop monitor behavior validated for bedtime-waketime crossover.
- [ ] Selection decode path tested after app restart and extension invocation.
- [ ] Revoke authorization mid-cycle and verify shield behavior + UI handling.
- [ ] Report any schedule registration errors beyond console output.

## Sources
- `../rundowns/11-project-beta-rundown.md`
- `/path/to/project-beta/ProjectBeta/AppBlockingManager.swift`
- `/path/to/project-beta/ProjectBetaMonitor/DeviceActivityMonitor.swift`
- `/path/to/project-beta/ProjectBetaShield/ShieldConfiguration.swift`
- `/path/to/project-beta/ProjectBetaShield/ShieldAction.swift`

## Confidence Notes
- This analysis is `project-observed` and grounded in current repository state as of `2026-02-08`.
