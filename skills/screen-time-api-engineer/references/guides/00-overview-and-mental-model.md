# 00 Overview and Mental Model

## Purpose
Define the end-to-end Screen Time API architecture for building iOS 16+ app/website blocking and usage analytics apps without mixing framework responsibilities.

## Canonical API Surface
- `FamilyControls`: authorization + selection (`AuthorizationCenter`, `FamilyActivityPicker`, `FamilyActivitySelection`).
- `ManagedSettings`: enforcement (`ManagedSettingsStore`, `ShieldSettings`, web content filtering, app blocking knobs).
- `ManagedSettingsUI`: custom shield display and action extension points.
- `DeviceActivity`: schedule/event monitoring and background enforcement callbacks.
- `_DeviceActivity_SwiftUI`: report rendering pipeline for usage analytics.
- `ScreenTime` framework: web usage reporting/control for web content your app presents.

## Implementation Pattern
1. Request Family Controls authorization.
2. Collect token selection through system picker.
3. Persist selection in app-group storage for app + extensions.
4. Apply/clear policies through ManagedSettings stores.
5. Use DeviceActivity to schedule enforcement while app is inactive.
6. Provide custom shield UX through ManagedSettingsUI extensions.
7. Render usage reports with report extension and context-based filtering.

## Failure Modes
- Treating tokens as bundle IDs or stable app metadata.
- Applying shields without checking authorization status.
- Omitting app-group sharing across targets.
- Attempting network calls in report extension sandbox.
- Using schedule intervals below supported minimums.

## Validation Checklist
- [ ] Main app + all extensions share family-controls entitlement and same app group.
- [ ] Selection persistence works across process boundaries.
- [ ] Monitor callbacks apply/clear policies as expected when app is terminated.
- [ ] Token-based labels render in UI.
- [ ] Report extension renders without network dependencies.

## Sources
- `../evidence/01-familycontrols-sdk-signatures.md`
- `../evidence/02-managedsettings-sdk-signatures.md`
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- `../evidence/06-screentime-framework-headers.md`

## Confidence Notes
- Framework role separation is `canonical + sdk-backed`.
- The exact product UX ordering is an implementation choice (`inference`, validated by project rundowns).
