# 10 Project Alpha Rundown

## Scope
- Template note: Replace `{{PROJECT_ALPHA_PATH}}` with your local repository root before following file references.
- Codebase: `{{PROJECT_ALPHA_PATH}}`
- Focus: FamilyControls, ManagedSettings, ManagedSettingsUI, DeviceActivity, onboarding permission UX, icon/token display.

## Target and Entitlement Topology
- Main app and all Screen Time extensions include:
  - `com.apple.developer.family-controls`
  - App Group: `group.com.example.projectalpha.shared`
- Entitlements files:
  - `{{PROJECT_ALPHA_PATH}}/ProjectAlpha/ProjectAlpha.entitlements`
  - `{{PROJECT_ALPHA_PATH}}/ProjectAlpha/ProjectAlphaMonitor.entitlements`
  - `{{PROJECT_ALPHA_PATH}}/ProjectAlpha/ProjectAlphaShieldConfiguration.entitlements`
  - `{{PROJECT_ALPHA_PATH}}/ProjectAlpha/ProjectAlphaShieldAction.entitlements`

## Architecture Map
- Main coordinator: `ShieldController` (`ProjectAlphaLockManager.swift`).
- Shared state transport: app-group `UserDefaults` keys in `ProjectAlphaShared.swift`.
- Scheduler: `DeviceActivityScheduler` with multiple named activities.
- Monitor extension: `DeviceActivityMonitorExtension` applies/clears shields from background callbacks.
- UI extension: `ShieldConfigurationExtension` and `ShieldActionExtension`.

## Permission and Picker UX
- Authorization request path:
  - `requestAuthorization(for: .individual)` in `ProjectAlphaLockManager.swift:55-56`.
- Picker presentation:
  - `.familyActivityPicker(isPresented:selection:)` in `AppSelectionView.swift:69`.
- Onboarding triggers auth request with fallback `try?` logic at `OnboardingView.swift:164`.

## Enforcement Behavior
- Foreground/manual shield apply: `applyDoomscrollShield()` at `ProjectAlphaLockManager.swift:91`.
- Full clear path: `removeDoomscrollShield()` at `ProjectAlphaLockManager.swift:131` and `clearAllSettings()` at lines `136`, `140`.
- Multi-store strategy:
  - named stores + default store to avoid stale restrictive state.

## Scheduling and Monitor Behavior
- Scheduler starts three recurring monitors (`segment1`, `segment2`, `midnightReset`) and fallback daily monitor.
- Start-monitoring lines:
  - `DeviceActivityScheduler.swift:55-57`, fallback at `65`.
- Monitor extension evaluates day rollover and commit/unlock state before applying or clearing shields.

## Shield UI/Action
- Custom terminal-themed shield in:
  - `{{PROJECT_ALPHA_PATH}}/ProjectAlphaShieldConfiguration/ShieldConfigurationExtension.swift`
- Shield action behavior:
  - `.close` response for primary actions in `{{PROJECT_ALPHA_PATH}}/ProjectAlphaShieldAction/ShieldActionExtension.swift`

## Real App Icon Strategy
- Project Alpha renders token labels directly:
  - `OnboardingView.swift:525`, `548` using `Label(token)`.
  - `ContentView.swift:825`, `833` using `Label(token)`.
- This is the correct Apple-supported token display pattern for icon/name materialization.

## Observed Risks
1. Silent auth failure path in `AppSelectionView.requestPicker()` (`try? await ...` at `AppSelectionView.swift:98`) can hide deny/revoke states.
2. Aggressive repeated clear/apply across monitor + main app can cause redundant writes.
3. Missing explicit user-facing recovery guidance when authorization gets revoked after onboarding.

## Reusable Hardened Patterns
- Multi-store + default-store clearing for deterministic state reset.
- Shared defaults key contract across app and extensions.
- Onboarding gating before picker open.
- Token label rendering instead of attempting private app metadata lookups.

Last analyzed: `2026-02-08`
