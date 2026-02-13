# 02 ManagedSettings SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/ManagedSettings.framework/Modules/ManagedSettings.swiftmodule/arm64e-apple-ios.swiftinterface`
- Supplemental symbol docs: `.../ManagedSettings.swiftmodule/arm64e-apple-ios.swiftdoc`

## Canonical Signatures (SDK Extract)

### Core Store
- `ManagedSettingsStore()`
- `ManagedSettingsStore(named: ManagedSettingsStore.Name)`
- `ManagedSettingsStore.clearAllSettings()`
- `ManagedSettingsStore.Name.default`

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
- `ShieldActionResponse`: `.none`, `.close`, `.defer`
- `ShieldActionDelegate.handle(action:for:completionHandler:)` for application/category/web domain tokens

## Practical Limits from SDK Doc Strings
- Shielding limits include 50-token ceilings across several APIs:
  - Up to 50 application tokens shielded at once.
  - Up to 50 web domain tokens shielded at once.
  - Up to 50 category tokens with up to 50 exceptions (depending on policy).
  - Web content filter policies include 50-domain related constraints for blocked/except sets.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
