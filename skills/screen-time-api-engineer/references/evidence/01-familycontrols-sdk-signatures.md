# 01 FamilyControls SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/FamilyControls.framework/Modules/FamilyControls.swiftmodule/arm64e-apple-ios.swiftinterface` (Xcode 27.0, build 27A266a)
- Supplemental symbol docs: `.../FamilyControls.swiftmodule/arm64e-apple-ios.swiftdoc`
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08). Changes since that baseline were found by reading `@available` annotations in the 27.0 interface; the 26.2 SDK was no longer installed for a file-level diff.

## Canonical Signatures (SDK Extract)
- `AuthorizationCenter.shared`
- `AuthorizationCenter.authorizationStatus: AuthorizationStatus`
- `AuthorizationCenter.requestAuthorization(for: FamilyControlsMember) async throws`
- `AuthorizationCenter.revokeAuthorization(completionHandler:)`
- `AuthorizationStatus`: `.notDetermined`, `.denied`, `.approved`, `.approvedWithDataAccess` (iOS 26.4+)
- `FamilyControlsMember`: `.child`, `.individual`
- `FamilyControlsError` includes `.unauthorized` (iOS 26.4+): the calling app must be authorized to provide parental controls and access data.
- `FamilyActivitySelection` includes:
  - `applicationTokens: Set<ApplicationToken>`
  - `categoryTokens: Set<ActivityCategoryToken>`
  - `webDomainTokens: Set<WebDomainToken>`
- `FamilyActivityPicker(selection:)`
- `View.familyActivityPicker(isPresented:selection:)`
- `View.familyActivityPicker(headerText:footerText:isPresented:selection:)`
- `View.familyActivityPicker(title:headerText:footerText:isPresented:selection:)` (iOS 26.2+)
- `Label(_ applicationToken: ApplicationToken)`
- `Label(_ categoryToken: ActivityCategoryToken)`
- `Label(_ webDomainToken: WebDomainToken)`

### Family Activity Data (iOS 26.4+)
- `FamilyActivityData.shared`
- `FamilyActivityData.installedApplications: [Application] { get async throws }` (each `Application` has `bundleIdentifier` and `token` populated)
- `FamilyActivityData.visitedWebDomains: [WebDomain] { get async throws }` (each `WebDomain` has `domain` and `token` populated)
- `FamilyActivityData.activityCategories: Set<ActivityCategory> { get async throws }` (each `ActivityCategory` has `localizedDisplayName` and `token` populated)

### Deprecated (unchanged since iOS 16)
- `AuthorizationCenter.requestAuthorization(completionHandler:)`: deprecated in iOS 16.0, message "Use requestAuthorization(for:) instead".

## Privacy and Token Behavior (SDK/Doc Strings)
- `FamilyActivitySelection` stores opaque values for selected applications, categories, and web domains.
- After authorization revocation, previously issued tokens are not guaranteed valid for enforcement.
- Label-based rendering is supported for token-backed title/icon display.
- Since iOS 26.4, `FamilyActivityData` returns non-tokenized values (bundle identifiers, domain names, category display names) next to their tokens. It is a separate, gated path; picker selections are still opaque.

## Data Access Requirements (Apple Docs, iOS 26.4+)
- Requires the `com.apple.developer.family-controls.app-and-website-usage` entitlement ("Family Controls App and Website Usage" capability in Xcode).
- Requires authorization status `.approvedWithDataAccess`. Apple describes it as granting everything `.approved` allows, plus `FamilyActivityData` and `DeviceActivityData.activityData(filteredBy:using:)`.
- Only one app at a time can hold `.approvedWithDataAccess` on a device. If the person grants data access to another app, your app's status reverts to `.notDetermined`.
- Region: development and testing work in any region (Apple-provided provisioning profile). Customer installs only reach `.approvedWithDataAccess` on devices located in the EU and signed in with an Apple Account whose country or region is in the EU. Elsewhere `authorizationStatus` never returns `.approvedWithDataAccess`, and `FamilyActivityData` access fails with `FamilyControlsError.unavailable`.
- In compatible iPad/iPhone apps running on visionOS or macOS, data fetches always fail (SDK doc string).
- Not found in the SDK or the doc pages checked: a separate request API for data access, or how the data-access prompt is presented. Treat the request flow as unverified until tested on device.

## Availability Notes
- FamilyControls APIs are iOS-first and unavailable on tvOS/watchOS.
- Some calls and overloads are version-gated; use `@available` checks for compatibility.
- iOS 26.2: `familyActivityPicker(title:...)`.
- iOS 26.4: `FamilyActivityData`, `AuthorizationStatus.approvedWithDataAccess`, `FamilyControlsError.unauthorized`.
- iOS 27.0 SDK: no new, deprecated, or renamed FamilyControls symbols.
- Source compatibility: with the iOS 26.4+ SDK, a `switch` over `AuthorizationStatus` that lists only `.notDetermined`, `.denied`, `.approved` and has no `default` fails to compile ("switch must be exhaustive"). The same applies to a `switch` over `FamilyControlsError` that lacks `.unauthorized`. Confirmed with `swiftc -typecheck` against the iOS 27.0 SDK (Swift 5 and Swift 6 language modes for `AuthorizationStatus`; Swift 5 for `FamilyControlsError`).

## Extraction Confidence
- Classification: `sdk-backed` (signatures, availability); `canonical` (data access requirements, from Apple docs)
- Confidence: `high`
- Last verified: `2026-10-21`
