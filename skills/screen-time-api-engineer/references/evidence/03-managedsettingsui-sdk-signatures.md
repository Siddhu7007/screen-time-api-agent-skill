# 03 ManagedSettingsUI SDK Signatures

## Source
- SDK file: `/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.2.sdk/System/Library/Frameworks/ManagedSettingsUI.framework/Modules/ManagedSettingsUI.swiftmodule/arm64e-apple-ios.swiftinterface`

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

## Implementation Implication
- Custom shield UI is strictly data-source driven from extension context.
- Primary/secondary button behavior is defined in ManagedSettings shield action delegate, not in UI configuration alone.

## Extraction Confidence
- Classification: `sdk-backed`
- Confidence: `high`
- Last verified: `2026-02-08`
