# 03 FamilyControls Selection and Token Model

## Purpose
Define correct token lifecycle and picker usage patterns for selecting apps, categories, and web domains.

## Canonical API Surface
- `FamilyActivitySelection`
- `FamilyActivityPicker`
- `View.familyActivityPicker(...)`, including `familyActivityPicker(title:headerText:footerText:isPresented:selection:)` (iOS 26.2+)
- `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`
- `Label(_ applicationToken:)`, `Label(_ categoryToken:)`, `Label(_ webDomainToken:)`
- Token refresh (iOS 26.5+): `ManagedSettingsStore.refresh(_:)` for application, category and web domain token arrays; `ManagedSettingsStore.TokenExpiryMessage` via `NotificationCenter.MessageIdentifier.tokensDidExpire`
- `FamilyActivityData` (iOS 26.4+, data access only)

## Implementation Pattern
1. Request authorization.
2. Present system picker with bound `FamilyActivitySelection`.
3. Persist encoded selection in app-group defaults.
4. Use tokens for ManagedSettings policy assignment.
5. Use token labels in UI for icon/title rendering.
6. On iOS 26.5+, observe `tokensDidExpire`, run `ManagedSettingsStore.refresh(_:)` on persisted token arrays, and save the refreshed tokens.
7. On iOS 26.2+, use the `title:` picker overload when you need a custom picker title.

## Failure Modes
- Trying to create tokens from bundle IDs manually.
- Assuming token set remains valid after authorization revocation.
- Storing only display names instead of token payload.
- Forgetting to include web domain tokens where website blocking is required.
- Assuming persisted tokens never expire. iOS 26.5 added an expiry message and a refresh API.
- Treating `FamilyActivityData` as a replacement for the picker. It needs a separate entitlement and only works for customers in the EU.

## Validation Checklist
- [ ] Picker opens only when authorization is approved.
- [ ] Selection includes app/category/domain dimensions.
- [ ] Persisted selection decodes in both app and extension process.
- [ ] Token labels render correctly in dashboard/onboarding summary.
- [ ] On iOS 26.5+, refreshed tokens are written back to app-group storage and shields using them are re-applied (inference: docs don't say whether active shields update on their own).

## Sources
- `../evidence/01-familycontrols-sdk-signatures.md`
- https://developer.apple.com/documentation/familycontrols/familyactivitypicker
- https://developer.apple.com/documentation/familycontrols/familyactivityselection
- https://developer.apple.com/documentation/familycontrols/displayingactivitylabels
- https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:)
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/tokenexpirymessage
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/refresh(_:)-65mti
- https://developer.apple.com/documentation/familycontrols/familyactivitydata
- `../evidence/02-managedsettings-sdk-signatures.md`
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Opaque token behavior is `canonical + sdk-backed`.
- Token expiry/refresh APIs are `sdk-backed` (iOS 26.5+). What triggers expiry and which errors `refresh` throws are not documented.
- UI summary styles are `project-observed`.
