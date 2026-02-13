# 01 FamilyControls SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/FamilyControls.framework/Modules/FamilyControls.swiftmodule/arm64e-apple-ios.swiftinterface`
- Supplemental symbol docs: `.../FamilyControls.swiftmodule/arm64e-apple-ios.swiftdoc`

## Canonical Signatures (SDK Extract)
- `AuthorizationCenter.shared`
- `AuthorizationCenter.authorizationStatus: AuthorizationStatus`
- `AuthorizationCenter.requestAuthorization(for: FamilyControlsMember) async throws`
- `AuthorizationCenter.revokeAuthorization(completionHandler:)`
- `AuthorizationStatus`: `.notDetermined`, `.denied`, `.approved`
- `FamilyControlsMember`: `.child`, `.individual`
- `FamilyActivitySelection` includes:
  - `applicationTokens: Set<ApplicationToken>`
  - `categoryTokens: Set<ActivityCategoryToken>`
  - `webDomainTokens: Set<WebDomainToken>`
- `FamilyActivityPicker(selection:)`
- `View.familyActivityPicker(isPresented:selection:)`
- `View.familyActivityPicker(headerText:footerText:isPresented:selection:)`
- `View.familyActivityPicker(title:headerText:footerText:isPresented:selection:)` (available in iOS 26.2 SDK)
- `Label(_ applicationToken: ApplicationToken)`
- `Label(_ categoryToken: ActivityCategoryToken)`
- `Label(_ webDomainToken: WebDomainToken)`

## Privacy and Token Behavior (SDK/Doc Strings)
- `FamilyActivitySelection` stores opaque values for selected applications, categories, and web domains.
- After authorization revocation, previously issued tokens are not guaranteed valid for enforcement.
- Label-based rendering is supported for token-backed title/icon display.

## Availability Notes
- FamilyControls APIs are iOS-first and unavailable on tvOS/watchOS.
- Some calls and overloads are version-gated; use `@available` checks for compatibility.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
