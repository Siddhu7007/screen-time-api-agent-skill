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
- Store lifecycle (iOS 26.5+): `ManagedSettingsStore.stores`, `isActive`, `deleteStore()`, `deleteStores(_:)`
- `ManagedSettingsStore.effectiveDenyExplicitContent` (iOS 26.0+, read-only)

## Implementation Pattern
1. Start by clearing target shield fields (or store) to avoid stale policy residue.
2. Apply tokens only when non-empty.
3. Use named stores for segment or feature scoping.
4. Keep explicit global reset path over all active store names + default store. On iOS 26.5+, `ManagedSettingsStore.stores` lists the stores your app configured; keep your own name list for earlier versions.
5. Persist enforcement state flags for UX diagnostics.
6. On iOS 26.5+, set `isActive = false` to leave a store out of the effective settings without deleting it, and use `deleteStore()` or `deleteStores(_:)` to remove stores you no longer need.

## Failure Modes
- Leaving restrictive settings in old stores after policy update.
- Applying categories without intended exceptions.
- Misusing default store and named stores simultaneously without precedence plan.
- Failing to clear web domain policies when app policies are removed.
- Leaving a store at `isActive = false` by mistake. The store still exists but is excluded from the effective settings, which looks like a shielding bug.

## Validation Checklist
- [ ] Policy apply path sets only expected fields.
- [ ] Reset path clears every relevant store.
- [ ] Store naming strategy is documented and deterministic.
- [ ] Policy composition tested with apps + categories + web domains together.
- [ ] On iOS 26.5+, `ManagedSettingsStore.stores` matches the documented store inventory.

## Sources
- `../evidence/02-managedsettings-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettings
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/clearallsettings()
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/isactive
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/stores
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/deletestore()
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/deletestores(_:)
- https://developer.apple.com/documentation/managedsettings/managedsettingsstore/effectivedenyexplicitcontent
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- API behavior is `canonical + sdk-backed`.
- Store orchestration recommendations are `project-observed` hardened practice.
- Store lifecycle APIs are `sdk-backed` (iOS 26.5+). The docs don't explain how `deleteStore()` differs from `clearAllSettings()`.
