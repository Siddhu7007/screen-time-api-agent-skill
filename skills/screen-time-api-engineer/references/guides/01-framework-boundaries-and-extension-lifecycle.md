# 01 Framework Boundaries and Extension Lifecycle

## Purpose
Prevent architectural bugs caused by placing logic in the wrong process or extension type.

## Canonical API Surface
- Device Activity monitor extension point: `com.apple.deviceactivity.monitor-extension`.
- Shield configuration extension point: `com.apple.ManagedSettingsUI.shield-configuration-service`.
- Shield action extension point: `com.apple.ManagedSettings.shield-action-service`.
- Device Activity report extension point: `com.apple.deviceactivityui.report-extension`.

## Implementation Pattern
- Host app:
  - authorization requests
  - picker presentation
  - settings/state mutation
- Monitor extension:
  - schedule callbacks and policy application/clearing when app is inactive
- Shield configuration extension:
  - visual shield configuration only
- Shield action extension:
  - button response routing (`close`, `defer`, `none`)
- Report extension:
  - transform report data into SwiftUI output only

## Failure Modes
- Assuming host app is alive when monitor callback fires.
- Putting network-dependent logic in report extension.
- Forgetting to embed extensions or configure principal class correctly.
- Divergent app group IDs across targets.

## Validation Checklist
- [ ] All extension `Info.plist` files use correct extension identifiers and principal classes.
- [ ] Extension targets have family-controls + app-group capabilities.
- [ ] Host app and extension read/write same app-group keys.
- [ ] Report extension works with no outbound network.

## Sources
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Extension boundaries and identifiers are `canonical + sdk-backed`.
- Process choreography recommendations are `project-observed` and hardened patterns.
