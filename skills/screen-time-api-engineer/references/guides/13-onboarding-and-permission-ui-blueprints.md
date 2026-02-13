# 13 Onboarding and Permission UI Blueprints

## Purpose
Define a resilient onboarding sequence for Screen Time authorization, app selection, and schedule setup.

## Canonical API Surface
- `AuthorizationCenter.authorizationStatus`
- `requestAuthorization(for:)`
- `FamilyActivityPicker`

## Implementation Pattern
1. Explain why permission is needed before prompting.
2. Request authorization with clear state feedback.
3. Gate picker until authorization is approved.
4. Require at least one selected token set before completion.
5. Add explicit deny/revoke remediation steps.
6. Persist onboarding-complete only after policy prerequisites are met.

## Failure Modes
- Silent authorization errors (`try?` with no UX fallback).
- Allowing onboarding completion without valid selection.
- Not handling post-approval revocation.

## Validation Checklist
- [ ] UI differentiates `.notDetermined` vs `.denied` states.
- [ ] Picker opens only when authorized.
- [ ] Selection summary updates immediately after picker change.
- [ ] Recovery copy includes Settings navigation path.

## Sources
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`
- `../evidence/01-familycontrols-sdk-signatures.md`
- https://developer.apple.com/documentation/familycontrols/authorizationcenter
- https://developer.apple.com/documentation/familycontrols/familyactivitypicker

## Confidence Notes
- Permission state model is `canonical + sdk-backed`.
- Onboarding flow sequence is `project-observed` blueprint guidance.
