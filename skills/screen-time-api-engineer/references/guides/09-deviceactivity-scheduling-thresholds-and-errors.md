# 09 DeviceActivity Scheduling Thresholds and Errors

## Purpose
Define schedule/event modeling with explicit limits and error handling requirements.

## Canonical API Surface
- `DeviceActivityCenter.startMonitoring(_:during:events:)`
- `DeviceActivitySchedule`
- `DeviceActivityEvent`
- `DeviceActivityCenter.MonitoringError`

## Implementation Pattern
1. Build schedule windows from deterministic date components.
2. Use named `DeviceActivityName` constants to avoid collisions.
3. Include threshold events only when required.
4. Handle `MonitoringError` with user-visible and telemetry-visible paths.
5. Use fallback schedule when detailed monitor setup fails.

## MonitoringError Handling Matrix
- `.excessiveActivities`: reduce monitor count and consolidate schedules.
- `.intervalTooShort`: enforce minimum 15-minute intervals.
- `.intervalTooLong`: enforce one-week cap for event monitoring intervals.
- `.invalidDateComponents`: validate schedule components before registration.
- `.unauthorized`: request/recover FamilyControls authorization.

## Failure Modes
- Attempting >20 simultaneous monitored activities.
- Non-unique activity names.
- Too granular intervals causing runtime throws.
- Ignoring timezone behavior at interval boundaries.

## Validation Checklist
- [ ] Interval bounds validated pre-registration.
- [ ] Activity names are unique.
- [ ] Start-monitoring exceptions are surfaced and logged.
- [ ] Fallback schedule path tested.
- [ ] Time-zone change scenario tested.

## Sources
- `../evidence/04-deviceactivity-sdk-signatures.md`
- https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/startmonitoring(_:during:events:)
- https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror
- https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/monitoringerror/intervaltooshort
- https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule
- https://developer.apple.com/documentation/deviceactivity/deviceactivityevent

## Confidence Notes
- Limits and errors are `sdk-backed` and reinforced by canonical doc pages.
