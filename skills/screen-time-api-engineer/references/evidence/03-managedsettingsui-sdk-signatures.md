# 03 ManagedSettingsUI SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.sdk/System/Library/Frameworks/ManagedSettingsUI.framework/Modules/ManagedSettingsUI.swiftmodule/arm64e-apple-ios.swiftinterface` (Xcode 27.0, build 27A266a)
- Previous baseline: `iPhoneOS26.2.sdk` (verified 2026-02-08).

## Canonical Signatures (SDK Extract)
- `ShieldConfigurationDataSource` override points:
  - `configuration(shielding application: Application)`
  - `configuration(shielding application: Application, in category: ActivityCategory)`
  - `configuration(shielding webDomain: WebDomain)`
  - `configuration(shielding webDomain: WebDomain, in category: ActivityCategory)`
- `ShieldConfiguration` properties:
  - `backgroundBlurStyle`
  - `backgroundColor`
  - `icon`
  - `title`
  - `subtitle`
  - `primaryButtonLabel`
  - `primaryButtonBackgroundColor`
  - `secondaryButtonLabel`
  - `secondaryButtonSubmenuItems: [String]?` (iOS 26.4+)
- `ShieldConfiguration.init(backgroundBlurStyle:backgroundColor:icon:title:subtitle:primaryButtonLabel:primaryButtonBackgroundColor:secondaryButtonLabel:secondaryButtonSubmenuItems:)` (iOS 26.4+). The older initializer without `secondaryButtonSubmenuItems` remains.

## Secondary Button Submenu (Apple Docs, iOS 26.4+)
- When `secondaryButtonSubmenuItems` is set, tapping the secondary button shows a submenu. Apple's docs say to add up to three items.
- Item taps arrive in the shield action extension as `ShieldAction.firstSecondarySubmenuItemPressed`, `.secondSecondarySubmenuItemPressed`, `.thirdSecondarySubmenuItemPressed`.
- `nil` or an empty array means no submenu; the secondary button sends `.secondaryButtonPressed` as before.
- The system adds a Cancel button to dismiss the menu.

## Implementation Implication
- Custom shield UI is strictly data-source driven from extension context.
- Primary/secondary button behavior is defined in ManagedSettings shield action delegate, not in UI configuration alone.
- Submenu item labels live in the configuration extension, but their meaning lives in the action extension. Keep both mapped from one shared definition.

## Availability Notes
- iOS 26.4: `secondaryButtonSubmenuItems` and its initializer.
- iOS 27.0 SDK: no new, deprecated, or renamed ManagedSettingsUI symbols.

## Extraction Confidence
- Classification: `sdk-backed` (signatures); `canonical` (submenu behavior, from Apple docs)
- Confidence: `high`
- Last verified: `2026-10-21`
