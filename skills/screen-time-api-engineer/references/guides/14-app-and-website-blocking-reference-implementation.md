# 14 App and Website Blocking Reference Implementation

## Purpose
Provide an end-to-end implementation recipe for combined app/category/domain blocking with custom shields and scheduled enforcement.

## Canonical API Surface
- FamilyControls selection APIs
- ManagedSettings shield and filter APIs
- DeviceActivity scheduling APIs
- ManagedSettingsUI shield configuration/action APIs

## Implementation Pattern
1. Authorize with FamilyControls.
2. Collect `applicationTokens`, `categoryTokens`, `webDomainTokens`.
3. Persist selection to app-group defaults.
4. Apply policies via ManagedSettings store(s):
   - apps -> `shield.applications`
   - categories -> `shield.applicationCategories`
   - sites -> `shield.webDomains`
5. Register DeviceActivity schedule for auto apply/clear lifecycle.
6. Implement custom shield config/action extensions.
7. Add manual clear-all recovery action in app settings.

## Failure Modes
- Partial policy updates (app only, no web reset).
- Schedule registration errors ignored silently.
- Shield extensions compiled but not embedded/configured correctly.

## Validation Checklist
- [ ] Full triplet selection (apps/categories/domains) supported.
- [ ] Enforcement persists when app is terminated.
- [ ] Unlock windows clear restrictions completely.
- [ ] Recovery action clears all stores.

## Sources
- `../evidence/01-familycontrols-sdk-signatures.md`
- `../evidence/02-managedsettings-sdk-signatures.md`
- `../evidence/03-managedsettingsui-sdk-signatures.md`
- `../evidence/04-deviceactivity-sdk-signatures.md`
- `../rundowns/12-cross-project-rundown.md`

## Confidence Notes
- API wiring is `canonical + sdk-backed`.
- This file is a synthesized reference pattern (`inference`) validated against both project rundowns.
