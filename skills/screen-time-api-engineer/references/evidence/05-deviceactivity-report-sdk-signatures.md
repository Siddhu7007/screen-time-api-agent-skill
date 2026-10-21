# 05 DeviceActivity Report SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Modules/_DeviceActivity_SwiftUI.swiftmodule/arm64e-apple-ios.swiftinterface` (Xcode 27.0, build 27A266a)
- Supplemental symbol docs: `.../_DeviceActivity_SwiftUI.swiftmodule/arm64e-apple-ios.swiftdoc`
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08).

## Canonical Signatures (SDK Extract)
- `DeviceActivityReport(context:filter:)` SwiftUI view.
- `DeviceActivityReport.Context` raw string wrapper.
- `DeviceActivityReportExtension` protocol with `@DeviceActivityReportBuilder body`.
- `DeviceActivityReportScene` protocol with:
  - `context`
  - `makeConfiguration(representing:) async`
  - `content(configuration)`
- `DeviceActivityResults<Element>: AsyncSequence`
- Async iteration via `makeAsyncIterator()`.

## Report Extension Environment
- Extension point identifier documented in symbol docs: `com.apple.deviceactivityui.report-extension`.
- Report extension sandbox constraints documented in symbol docs:
  - no network requests
  - sensitive content cannot be moved outside extension address space
- The sandbox wording is unchanged in the iOS 27.0 SDK doc strings.

## Privacy/Authorization Dependency
- Usage data availability depends on Family Controls authorization state.
- Since iOS 26.4 there is a second, gated way to read activity data outside the report extension: `DeviceActivityData.activityData(filteredBy:using:)` in the host app. It needs the app-and-website-usage entitlement and `.approvedWithDataAccess`, and works for customers only in the EU. See `04-deviceactivity-sdk-signatures.md`. The report extension remains the general-purpose path.

## Availability Notes
- No additions, deprecations, or renames in iOS 26.x or 27.0. The newest annotations in this module are iOS 18.0 (`AsyncSequence`/`AsyncIteratorProtocol` `Failure` typealiases) and iOS 17.4 (`DeviceActivityReportBuilder` overloads for 11–20 scenes).

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-10-21`
