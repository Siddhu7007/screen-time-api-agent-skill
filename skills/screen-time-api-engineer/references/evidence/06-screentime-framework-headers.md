# 06 ScreenTime Framework Headers

## Source
- Header root: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/ScreenTime.framework/Headers` (Xcode 27.0, build 27A266a)
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08).
- Headers reviewed:
  - `ScreenTime.h`
  - `STScreenTimeConfiguration.h`
  - `STWebHistory.h`
  - `STWebpageController.h`

## Canonical API Surface

### STScreenTimeConfiguration
- `enforcesChildRestrictions` read-only property.

### STScreenTimeConfigurationObserver
- `init(updateQueue:)`
- `startObserving()` / `stopObserving()`
- `configuration` property

### STWebHistory
- initializers for bundle identifier/profile identifier
- `fetchHistory(during:completionHandler:)` (iOS 18.4+)
- `fetchAllHistoryWithCompletionHandler(...)` (iOS 18.4+)
- delete APIs:
  - `deleteHistory(for:)`
  - `deleteHistory(during:)`
  - `deleteAllHistory()`
- profile identifier support available in newer API levels (iOS 18.4+)

### STWebpageController
- `URL` property
- `urlIsPlayingVideo` property
- `urlIsPictureInPicture` property
- `urlIsBlocked` read-only property
- `suppressUsageRecording` property
- profile identifier support for multi-profile browsing (iOS 18.4+)
- `setBundleIdentifier(_:error:)` for registered browser reporting scenarios

## Implementation Notes
- ScreenTime framework focuses on web usage reporting/control for web content your app presents.
- It is not a drop-in replacement for FamilyControls + ManagedSettings token shielding.

## Availability Notes
- No additions, deprecations, or renames in iOS 26.x or 27.0. The newest `API_AVAILABLE` annotations are iOS 18.4 / macOS 15.4.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-10-21`
