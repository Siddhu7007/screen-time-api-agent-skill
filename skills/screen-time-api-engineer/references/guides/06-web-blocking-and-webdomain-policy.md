# 06 Web Blocking and WebDomain Policy

## Purpose
Define the correct strategy for website blocking across ManagedSettings and token-based selection.

## Canonical API Surface
- `WebDomainToken`
- `ShieldSettings.webDomains`
- `ShieldSettings.webDomainCategories`
- `WebContentSettings`
- `WebContentSettings.FilterPolicy`
- `WebContentSettings.blockedByFilter`

## Implementation Pattern
- User-driven domain selection via FamilyActivityPicker -> `webDomainTokens`.
- Apply selected domain tokens through `store.shield.webDomains`.
- For broader content policy, use `WebContentSettings` filter policy with explicit exceptions.
- Keep domain and app policy transitions synchronized in apply/clear paths.

## Failure Modes
- Applying web filtering without mirrored reset logic.
- Treating domain strings as token equivalents.
- Overblocking due to missing exception handling in category policy.

## Validation Checklist
- [ ] Domain tokens persist and decode across app/extension.
- [ ] Domain shields apply during active schedule windows.
- [ ] Domain shields clear on unlock state.
- [ ] Filter policies with exception sets are tested with realistic websites.

## Sources
- `../evidence/02-managedsettings-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettings/webdomain
- https://developer.apple.com/documentation/managedsettings/webdomaintoken
- https://developer.apple.com/documentation/managedsettings/webcontentsettings
- https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy
- https://developer.apple.com/documentation/managedsettings/webcontentsettings/blockedbyfilter-swift.property

## Confidence Notes
- Token-based web shielding and filter policy APIs are `canonical + sdk-backed`.
- Policy composition order remains an implementation decision (`inference`) and must be tested.
