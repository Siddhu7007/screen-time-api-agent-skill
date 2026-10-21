# 04 DeviceActivity SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/DeviceActivity.framework/Modules/DeviceActivity.swiftmodule/arm64e-apple-ios.swiftinterface` (Xcode 27.0, build 27A266a)
- Supplemental symbol docs: `.../DeviceActivity.swiftmodule/arm64e-apple-ios.swiftdoc`
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08). Changes identified from `@available` annotations in the 27.0 interface.

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

### Activity Data Fetch (iOS 26.4+)
- `DeviceActivityData.activityData(filteredBy filter: DeviceActivityFilter = .init(), using policy: DeviceActivityData.Policy = .cached) -> some AsyncSequence<DeviceActivityData, any Error>` (static)
- `DeviceActivityData.Policy`: `.cached`, `.live` (a live request may return cached data if the cache was updated recently)
- `DeviceActivityData.Error`: `.unavailable` (user not in a region that supports data access), `.unauthorized` (app not authorized to provide parental controls and access data), `.missingData` (requested data does not exist; if returned for cached data, fetching live data may resolve it)
- Requirements (SDK doc string + Apple docs): the `com.apple.developer.family-controls.app-and-website-usage` entitlement and `AuthorizationStatus.approvedWithDataAccess`. Customer installs work only on EU devices signed in with an EU Apple Account; see `01-familycontrols-sdk-signatures.md`. Always throws in iPad/iPhone apps running on visionOS or macOS.
- Apple's stated purpose: export family activity data for use in another app or platform.
- `DeviceActivityData.activitySegments` and the nested `categories`/`applications`/`webDomains` sequences are declared in `_DeviceActivity_SwiftUI` (iOS 16.0), not in `DeviceActivity`. Inference: walking those segments from the host app needs that overlay in scope (importing both `DeviceActivity` and `SwiftUI`). Verify by compiling.

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
- Re-checked in the iOS 27.0 SDK doc strings: the 20-activity, 15-minute and one-week limits are unchanged.

## Availability Notes
- iOS 26.4: `DeviceActivityData.activityData(filteredBy:using:)`, `DeviceActivityData.Policy`, `DeviceActivityData.Error`.
- Scheduling, events, `DeviceActivityCenter`, `MonitoringError` and `DeviceActivityMonitor`: no changes in iOS 26.x or 27.0.
- iOS 27.0 SDK: no new, deprecated, or renamed DeviceActivity symbols.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-10-21`
