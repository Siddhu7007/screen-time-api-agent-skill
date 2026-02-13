# 05 DeviceActivity Report SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/_DeviceActivity_SwiftUI.framework/Modules/_DeviceActivity_SwiftUI.swiftmodule/arm64e-apple-ios.swiftinterface`
- Supplemental symbol docs: `.../_DeviceActivity_SwiftUI.swiftmodule/arm64e-apple-ios.swiftdoc`

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

## Privacy/Authorization Dependency
- Usage data availability depends on Family Controls authorization state.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
