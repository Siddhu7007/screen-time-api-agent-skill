# 04 Displaying Activity Labels and Real App Icons

## Purpose
Explain what “real app icon/name display” is officially supported and how to implement it safely.

## Canonical API Surface
- `Label(_ applicationToken:)`
- `Label(_ categoryToken:)`
- `Label(_ webDomainToken:)`
- `FamilyActivityIconView`
- `FamilyActivityTitleView`

## Implementation Pattern
- Render selected tokens directly using `Label(token)`.
- Use `.labelStyle(.iconOnly)` for compact icon stacks.
- Keep placeholders only for empty/unselected slots.
- Avoid any private API or reverse-lookup approach for app metadata.

## Failure Modes
- Expecting token-to-bundle-id conversion through unsupported APIs.
- Caching guessed metadata that diverges from system privacy model.
- Breaking UI when token labels are unavailable or delayed.

## Validation Checklist
- [ ] Selected apps show real icon surfaces via token labels.
- [ ] Category/domain selections display consistent token-backed visuals.
- [ ] Empty state has deterministic placeholders.
- [ ] Works in onboarding and dashboard views.

## Sources
- `../evidence/01-familycontrols-sdk-signatures.md`
- https://developer.apple.com/documentation/familycontrols/activitylabel
- https://developer.apple.com/documentation/familycontrols/displayingactivitylabels
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Label/token rendering support is `canonical + sdk-backed`.
- Visual composition details are `project-observed`.
