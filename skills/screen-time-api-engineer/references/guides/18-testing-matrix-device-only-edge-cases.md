# 18 Testing Matrix Device Only Edge Cases

## Purpose
Define a comprehensive QA matrix for real-device validation of Screen Time features.

## Canonical API Surface
- FamilyControls auth/picker behavior
- DeviceActivity monitor behavior
- ManagedSettings policy application
- ManagedSettingsUI custom shield rendering
- DeviceActivity report extension behavior

## Implementation Pattern
Test at three layers:
1. Functional (permission, picker, apply/clear)
2. Lifecycle (background/terminated/relaunch/reboot)
3. Temporal (timezone shift, DST, midnight rollover, long-running schedules)

## Failure Modes
- Simulator-only confidence for features that require real Screen Time environment.
- Not testing revocation after initial approval.
- Ignoring extension-only edge conditions.

## Validation Checklist
- [ ] Authorization states: notDetermined/denied/approved.
- [ ] Picker updates app/category/domain selections correctly.
- [ ] Monitor applies and clears when app is terminated.
- [ ] Revocation in Settings reflected on next enforcement attempt.
- [ ] Timezone change during active interval tested.
- [ ] Interval too short/too many activities error paths tested.
- [ ] Shield UI/action renders for app, category, and web domain contexts.
- [ ] Usage report loads with no network dependency.

## Sources
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../evidence/05-deviceactivity-report-sdk-signatures.md`
- https://developer.apple.com/videos/play/wwdc2021/10123/
- https://developer.apple.com/videos/play/wwdc2022/110336/

## Confidence Notes
- Matrix is `inference` built from canonical constraints plus project behavior.
