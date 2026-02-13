# 04 DeviceActivity SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/DeviceActivity.framework/Modules/DeviceActivity.swiftmodule/arm64e-apple-ios.swiftinterface`
- Supplemental symbol docs: `.../DeviceActivity.swiftmodule/arm64e-apple-ios.swiftdoc`

## Canonical Signatures (SDK Extract)
- `DeviceActivityCenter.startMonitoring(_:during:events:) throws`
- `DeviceActivityCenter.stopMonitoring(_:)`
- `DeviceActivityCenter.activities`
- `DeviceActivityCenter.schedule(for:)`
- `DeviceActivityCenter.events(for:)`
- `DeviceActivitySchedule(intervalStart:intervalEnd:repeats:warningTime:)`
- `DeviceActivitySchedule.nextInterval`
- `DeviceActivityEvent(applications:categories:webDomains:threshold:)`
- `DeviceActivityEvent(... includesPastActivity:)` (iOS 17.4+)
- `DeviceActivityEvent.Name`
- `DeviceActivityMonitor` callbacks:
  - `intervalDidStart`
  - `intervalDidEnd`
  - `eventDidReachThreshold`
  - warning callbacks

## MonitoringError Enum (SDK)
- `.excessiveActivities`
- `.intervalTooLong`
- `.intervalTooShort`
- `.invalidDateComponents`
- `.unauthorized`

## Constraints from SDK Doc Strings
- Maximum monitored activities at one time: 20 (app + extensions).
- Minimum monitoring interval length: 15 minutes.
- Maximum monitoring interval length for events: one week.
- Time-zone note: schedule boundaries use device time zone at `nextInterval.start`; mid-interval zone changes can create unexpected wall-clock behavior.
- Activity names must be unique for monitored set.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
