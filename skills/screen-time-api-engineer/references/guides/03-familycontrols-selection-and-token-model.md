# 03 FamilyControls Selection and Token Model

## Purpose
Define correct token lifecycle and picker usage patterns for selecting apps, categories, and web domains.

## Canonical API Surface
- `FamilyActivitySelection`
- `FamilyActivityPicker`
- `View.familyActivityPicker(...)`
- `ApplicationToken`, `ActivityCategoryToken`, `WebDomainToken`
- `Label(_ applicationToken:)`, `Label(_ categoryToken:)`, `Label(_ webDomainToken:)`

## Implementation Pattern
1. Request authorization.
2. Present system picker with bound `FamilyActivitySelection`.
3. Persist encoded selection in app-group defaults.
4. Use tokens for ManagedSettings policy assignment.
5. Use token labels in UI for icon/title rendering.

## Failure Modes
- Trying to create tokens from bundle IDs manually.
- Assuming token set remains valid after authorization revocation.
- Storing only display names instead of token payload.
- Forgetting to include web domain tokens where website blocking is required.

## Validation Checklist
- [ ] Picker opens only when authorization is approved.
- [ ] Selection includes app/category/domain dimensions.
- [ ] Persisted selection decodes in both app and extension process.
- [ ] Token labels render correctly in dashboard/onboarding summary.

## Sources
- `../evidence/01-familycontrols-sdk-signatures.md`
- https://developer.apple.com/documentation/familycontrols/familyactivitypicker
- https://developer.apple.com/documentation/familycontrols/familyactivityselection
- https://developer.apple.com/documentation/familycontrols/displayingactivitylabels
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Opaque token behavior is `canonical + sdk-backed`.
- UI summary styles are `project-observed`.
