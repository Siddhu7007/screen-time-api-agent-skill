# 11 Project Beta Rundown

## Scope
- Template note: Replace `{{PROJECT_BETA_PATH}}` with your local repository root before following file references.
- Codebase: `{{PROJECT_BETA_PATH}}`
- Focus: same Screen Time API surface as Project Alpha, with schedule-heavy onboarding.

## Target and Entitlement Topology
- Main app, monitor extension, and shield extension share:
  - `com.apple.developer.family-controls`
  - App Group: `group.com.example.projectbeta.shared`
- Core files:
  - `{{PROJECT_BETA_PATH}}/ProjectBeta/ProjectBeta.entitlements`
  - `{{PROJECT_BETA_PATH}}/ProjectBetaMonitor/ProjectBetaMonitor.entitlements`
  - `{{PROJECT_BETA_PATH}}/ProjectBetaShield/ProjectBetaShield.entitlements`

## Architecture Map
- Coordinator: `AppBlockingManager` (authorization, selection, immediate shielding, schedule setup).
- Schedule model: `ScheduleSettings.swift` + `DeviceActivitySchedule` generation.
- Monitor extension applies and clears shields on interval boundaries.
- Shield extension provides themed UI and action handling.

## Permission and Picker UX
- Authorization request:
  - `requestAuthorization(for: .individual)` in `AppBlockingManager.swift:35-37`.
- Picker path:
  - `.familyActivityPicker(...)` in `AppSelectionView.swift:235`.
- Onboarding gating with `hasGrantedPermission` + `hasSelectedApps` before allowing progression.

## Enforcement Behavior
- Immediate apply path: `activateBlocking()` in `AppBlockingManager.swift:81`.
- Immediate clear path: `deactivateBlocking()` in `AppBlockingManager.swift:95`.
- Monitor fallback ensures interval-based enforcement when app is inactive.

## Schedule and Monitor Behavior
- `DeviceActivitySchedule` generation in `AppBlockingManager.swift:186`.
- Monitor registration in `AppBlockingManager.swift:199`.
- Runtime state reconciliation in `checkAndActivateIfInBlockingPeriod()`.

## Shield UI/Action
- Shield configuration uses day/night-aware copy and style in:
  - `{{PROJECT_BETA_PATH}}/ProjectBetaShield/ShieldConfiguration.swift`
- Shield action delegates in:
  - `{{PROJECT_BETA_PATH}}/ProjectBetaShield/ShieldAction.swift`

## Real App Icon Strategy
- Project Beta dashboard uses `Label(token)` for selected app icons:
  - `MainView.swift:319`.
- This is aligned with FamilyControls token rendering and supports real icon/name display where system data is available.

## Observed Risks
1. Potential race between periodic app-level check and monitor extension callbacks when toggling active blocking state.
2. Monitor extension currently does not explicitly surface authorization-revoked state to the user.
3. Error paths rely heavily on console prints; insufficient structured telemetry for diagnosing release issues.

## Reusable Hardened Patterns
- Persist `FamilyActivitySelection` as plist in app group defaults for extension read consistency.
- Validate selection limits in onboarding UI.
- Keep schedule values mirrored to app group for extension/widget consistency.

Last analyzed: `2026-02-08`
