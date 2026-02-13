# 06 ScreenTime Framework Headers

## Source
- Header root: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/ScreenTime.framework/Headers`
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
- `fetchHistory(during:completionHandler:)`
- `fetchAllHistoryWithCompletionHandler(...)`
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

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
