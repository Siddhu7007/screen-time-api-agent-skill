# 12 ScreenTime Framework Web Usage Reporting

## Purpose
Clarify how `ScreenTime.framework` complements (not replaces) FamilyControls/ManagedSettings for web usage scenarios.

## Canonical API Surface
- `STScreenTimeConfiguration`
- `STScreenTimeConfigurationObserver`
- `STWebpageController`
- `STWebHistory`

## Implementation Pattern
- In apps with embedded/custom browser flows:
  - Use `STWebpageController` to report URL and playback/PiP state.
  - Observe child restriction state via `STScreenTimeConfigurationObserver`.
  - Use `STWebHistory` APIs for scoped history fetch/delete where applicable.
- Continue to use FamilyControls + ManagedSettings for system token-based blocking workflows.

## Failure Modes
- Assuming `STWebpageController` alone can enforce system-wide token shielding.
- Ignoring newer API availability for profile identifier workflows.
- Forgetting to reset video/PiP state before URL transitions.

## Validation Checklist
- [ ] Web usage reporting hooks update URL + playback flags correctly.
- [ ] History APIs tested with bundle/profile combinations.
- [ ] Child restriction observer updates host browser policy in real time.

## Sources
- `../evidence/06-screentime-framework-headers.md`
- https://developer.apple.com/documentation/screentime
- https://developer.apple.com/documentation/screentime/stwebpagecontroller
- https://developer.apple.com/documentation/screentime/stwebhistory
- https://developer.apple.com/documentation/screentime/stscreentimeconfigurationobserver

## Confidence Notes
- Framework surface and role constraints are `sdk-backed` from headers.
- Integration strategy with token-based APIs is `inference + canonical alignment`.
