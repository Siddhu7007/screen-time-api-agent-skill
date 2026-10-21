# 07 Claim Reconciliation

This file reconciles claims across canonical docs, SDK extraction, project implementations, and field notes.

| Claim | Classification | Evidence | Caveat |
|---|---|---|---|
| Family activity selections are opaque tokens. | canonical + sdk-backed | FamilyControls doc strings + `FamilyActivitySelection` signatures. | Still true for picker selections. Since iOS 26.4, `FamilyActivityData` can return bundle IDs and domains, but only under `.approvedWithDataAccess` (EU customer devices). |
| You can render real app/category/domain labels from tokens. | canonical + sdk-backed | `Label(_ applicationToken:)` and related in FamilyControls interface. | Display fidelity depends on system-provided metadata. |
| ManagedSettings shield/app/web token limits include 50 ceilings. | sdk-backed | ManagedSettings `.swiftdoc` limit statements (re-checked in iOS 27.0 SDK). | Limits are per API/policy context; enforce defensive validation. |
| `DeviceActivityCenter` supports at most 20 monitored activities. | sdk-backed | DeviceActivity `.swiftdoc` for `excessiveActivities` (re-checked in iOS 27.0 SDK). | Subject to platform/runtime evolution; re-check SDK each release. |
| Minimum interval is 15 minutes and max interval is one week. | sdk-backed | DeviceActivity `.swiftdoc` monitoring error docs (re-checked in iOS 27.0 SDK). | Validate behavior on your deployment iOS floor. |
| DeviceActivity report extensions run in privacy sandbox with no network. | sdk-backed | `_DeviceActivity_SwiftUI.swiftdoc` extension notes (unchanged in iOS 27.0 SDK). | Keep rendering logic local and deterministic. iOS 26.4 adds a separate host-app fetch path under data access; it does not relax the extension sandbox. |
| Authorization revocation can invalidate previously obtained tokens. | canonical + sdk-backed | FamilyControls symbol docs note revocation implications. | Always re-check authorization before applying shields. |
| Host apps can read app/website usage data directly on iOS 26.4+. | canonical + sdk-backed | `FamilyActivityData`, `DeviceActivityData.activityData(filteredBy:using:)`, `AuthorizationStatus.approvedWithDataAccess` docs. | Needs the `com.apple.developer.family-controls.app-and-website-usage` entitlement. Customer installs: EU devices with an EU Apple Account only. One app per device holds it; others revert to `.notDetermined`. |
| `.approvedWithDataAccess` grants everything `.approved` does. | canonical | `AuthorizationStatus.approvedWithDataAccess` doc page. | Code that checks `status == .approved` treats a data-access app as unauthorized. Check for both cases. |
| Adding enum cases in iOS 26.4 breaks exhaustive switches. | sdk-backed | `swiftc -typecheck` against iOS 27.0 SDK: `AuthorizationStatus`, `FamilyControlsError` and `ShieldAction` switches without `default` fail with "switch must be exhaustive" (Swift 5 and 6 modes). | `@unknown default` turns the error into a warning; handle the new cases explicitly. |
| Shield secondary button supports a submenu of up to three items (iOS 26.4+). | canonical + sdk-backed | `ShieldConfiguration.secondaryButtonSubmenuItems` doc page + `ShieldAction` submenu cases. | Nil/empty array keeps the old `.secondaryButtonPressed` behavior. System adds Cancel. |
| ManagedSettings tokens can expire and be refreshed (iOS 26.5+). | sdk-backed | `ManagedSettingsStore.TokenExpiryMessage`, `tokensDidExpire`, `refresh(_:)` overloads. | Expiry triggers, cadence, and `refresh` error cases are not documented. Treat as unknown until tested on device. |
| Apps can enumerate, deactivate, and delete their own stores (iOS 26.5+). | sdk-backed | `ManagedSettingsStore.stores`, `isActive`, `deleteStore()`, `deleteStores(_:)`. | Docs do not say how `deleteStore()` differs from `clearAllSettings()` beyond the names. |
| iOS 27.0 SDK adds no Screen Time API changes. | sdk-backed | No `iOS 27` availability or new deprecation annotations in FamilyControls, ManagedSettings, ManagedSettingsUI, DeviceActivity, `_DeviceActivity_SwiftUI`, or ScreenTime headers (Xcode 27.0, 27A266a). | Point releases (27.x) may add APIs; re-check each SDK. |
| Project Alpha uses multi-store shielding and day rollover with shared defaults. | project-observed | Project Alpha monitor/lock manager code. | Pattern is valid; still verify race conditions and redundant clear calls. |
| Project Beta uses schedule-driven monitor + immediate manager fallback logic. | project-observed | Project Beta app manager + monitor extension code. | Consider explicit auth checks in monitor callbacks. |
| Medium/field posts reflect practical extension pitfalls and iteration patterns. | field-note | Julius + Letvar posts. | Treat as advisory unless corroborated by canonical/SDK evidence. |

## Reconciliation Rule Applied
- Final guides default to canonical and SDK-backed claims.
- `project-observed` and `field-note` claims are explicitly labeled.
- `inference` claims are only used with caveats and validation checklist items.

Last verified: `2026-10-21` (rows carried over from the iOS 26.2 SDK pass were last verified `2026-02-08` unless marked re-checked)
