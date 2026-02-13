# 05 ManagedSettings Enforcement Patterns

## Purpose
Provide enforcement-safe policy patterns for app/category/domain shielding and reset behavior.

## Canonical API Surface
- `ManagedSettingsStore`
- `ManagedSettingsStore.clearAllSettings()`
- `ShieldSettings.applications`
- `ShieldSettings.applicationCategories`
- `ShieldSettings.webDomains`
- `ShieldSettings.webDomainCategories`
- `ShieldSettings.ActivityCategoryPolicy.{none,specific,all}`

## Implementation Pattern
1. Start by clearing target shield fields (or store) to avoid stale policy residue.
2. Apply tokens only when non-empty.
3. Use named stores for segment or feature scoping.
4. Keep explicit global reset path over all active store names + default store.
5. Persist enforcement state flags for UX diagnostics.

## Failure Modes
- Leaving restrictive settings in old stores after policy update.
- Applying categories without intended exceptions.
- Misusing default store and named stores simultaneously without precedence plan.
- Failing to clear web domain policies when app policies are removed.

## Validation Checklist
- [ ] Policy apply path sets only expected fields.
- [ ] Reset path clears every relevant store.
- [ ] Store naming strategy is documented and deterministic.
- [ ] Policy composition tested with apps + categories + web domains together.

## Sources
- `../evidence/02-managedsettings-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettings
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/clearallsettings()
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- API behavior is `canonical + sdk-backed`.
- Store orchestration recommendations are `project-observed` hardened practice.
