# 02 ManagedSettings SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/ManagedSettings.framework/Modules/ManagedSettings.swiftmodule/arm64e-apple-ios.swiftinterface` (Xcode 27.0, build 27A266a)
- Supplemental symbol docs: `.../ManagedSettings.swiftmodule/arm64e-apple-ios.swiftdoc`
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08). Changes identified from `@available` annotations in the 27.0 interface.

## Canonical Signatures (SDK Extract)

### Core Store
- `ManagedSettingsStore()`
- `ManagedSettingsStore(named: ManagedSettingsStore.Name)`
- `ManagedSettingsStore.clearAllSettings()`
- `ManagedSettingsStore.Name.default`

### Store Lifecycle (iOS 26.5+)
- `store.isActive: Bool { get set }`: an inactive store is not included in the effective settings calculation. Defaults to `true`.
- `store.deleteStore()`: deletes this store.
- `ManagedSettingsStore.deleteStores(_ storeNames: Set<ManagedSettingsStore.Name>)`: deletes the given stores configured by your app, if they exist.
- `ManagedSettingsStore.stores: Set<ManagedSettingsStore.Name>`: names of all stores configured by your app.

### Token Expiry and Refresh (iOS 26.5+)
- `ManagedSettingsStore.refresh(_ tokens: inout [ApplicationToken]) throws`
- `ManagedSettingsStore.refresh(_ tokens: inout [ActivityCategoryToken]) throws`
- `ManagedSettingsStore.refresh(_ tokens: inout [WebDomainToken]) throws`
- `ManagedSettingsStore.TokenExpiryMessage`: a `NotificationCenter.AsyncMessage` (`Subject == ManagedSettingsStore`) posted when ManagedSettingsStore tokens expire. Doc string: use it to refresh expired tokens in your database.
- `NotificationCenter.MessageIdentifier.tokensDidExpire`: identifier for observing `TokenExpiryMessage`.
- Not documented in the SDK or doc pages checked: when or why tokens expire, and which errors `refresh` throws.

### Effective Settings (read-only)
- `store.effectiveMaximumMovieRating: Int`, `store.effectiveMaximumTVShowRating: Int` (existing)
- `store.effectiveDenyExplicitContent: Bool` (iOS 26.0+, `@Published`): the deny-explicit-content constraint active on the device.

### Shield Settings
- `store.shield.applications: Set<ApplicationToken>?`
- `store.shield.applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?`
- `store.shield.webDomains: Set<WebDomainToken>?`
- `store.shield.webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?`

### Activity Category Policies
- `ShieldSettings.ActivityCategoryPolicy.none`
- `ShieldSettings.ActivityCategoryPolicy.specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>> = [])`
- `ShieldSettings.ActivityCategoryPolicy.all(except: Set<Token<Activity>> = [])`

### Web Content / Blocking
- `ApplicationSettings.blockedApplications`
- `WebContentSettings.blockedByFilter`
- `WebContentSettings.FilterPolicy` and associated cases (SDK-defined)

### Shield Actions
- `ShieldAction`: `.primaryButtonPressed`, `.secondaryButtonPressed`
- `ShieldAction` submenu cases (iOS 26.4+): `.firstSecondarySubmenuItemPressed`, `.secondSecondarySubmenuItemPressed`, `.thirdSecondarySubmenuItemPressed`
- `ShieldActionResponse`: `.none`, `.close`, `.defer`
- `ShieldActionResponse.openParentalControlsApp` (iOS 26.5+): the system opens your parental controls app, the one responsible for shielding the app or web browser.
- `ShieldActionDelegate.handle(action:for:completionHandler:)` for application/category/web domain tokens

## Practical Limits from SDK Doc Strings
- Shielding limits include 50-token ceilings across several APIs:
  - Up to 50 application tokens shielded at once.
  - Up to 50 web domain tokens shielded at once.
  - Up to 50 category tokens with up to 50 exceptions (depending on policy).
  - Web content filter policies include 50-domain related constraints for blocked/except sets.
- Re-checked in the iOS 27.0 SDK doc strings: the 50 limits are unchanged.

## Availability Notes
- iOS 26.0: `effectiveDenyExplicitContent`.
- iOS 26.4: `ShieldAction` submenu cases.
- iOS 26.5: store lifecycle APIs, token refresh/expiry APIs, `ShieldActionResponse.openParentalControlsApp`.
- The iOS SDK interface also annotates `ManagedSettingsStore`, `ManagedSettingsStore.Name` and `init()` with `tvOS 26.0`. Only the iOS SDK was inspected; the tvOS SDK was not.
- iOS 27.0 SDK: no new, deprecated, or renamed ManagedSettings symbols.
- Source compatibility: with the iOS 26.4+ SDK, a `switch` over `ShieldAction` covering only the primary/secondary cases with no `default` fails to compile. Confirmed with `swiftc -typecheck` against the iOS 27.0 SDK.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-10-21`
