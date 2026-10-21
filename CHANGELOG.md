# Changelog

All notable changes to this skill are listed here. Versions follow [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-10-21

Re-verified the API evidence against the iOS 27.0 SDK (Xcode 27.0, build 27A266a). v1.0.0 was checked against the iOS 26.2 SDK. The iOS 27.0 SDK adds no new, deprecated or renamed APIs in FamilyControls, ManagedSettings, ManagedSettingsUI, DeviceActivity, the DeviceActivity report module or the ScreenTime headers. The changes below come from iOS 26.4 and 26.5, plus one iOS 26.0 property the earlier pass missed.

### Added
- FamilyControls (iOS 26.4): `FamilyActivityData` (`installedApplications`, `visitedWebDomains`, `activityCategories`), `AuthorizationStatus.approvedWithDataAccess`, `FamilyControlsError.unauthorized`, and the `com.apple.developer.family-controls.app-and-website-usage` entitlement. Documented Apple's limits: customer installs get data access only on EU devices with an EU Apple Account, and only one app per device can hold it.
- DeviceActivity (iOS 26.4): `DeviceActivityData.activityData(filteredBy:using:)` for reading activity data in the host app, with `DeviceActivityData.Policy` (`.cached`, `.live`) and `DeviceActivityData.Error` (`.unavailable`, `.unauthorized`, `.missingData`).
- ManagedSettingsUI and ManagedSettings (iOS 26.4): `ShieldConfiguration.secondaryButtonSubmenuItems` (up to three items) and the matching `ShieldAction` submenu cases.
- ManagedSettings (iOS 26.5): `ShieldActionResponse.openParentalControlsApp`; store lifecycle APIs `ManagedSettingsStore.stores`, `isActive`, `deleteStore()`, `deleteStores(_:)`; token expiry and refresh via `ManagedSettingsStore.TokenExpiryMessage`, `tokensDidExpire` and `ManagedSettingsStore.refresh(_:)`.
- ManagedSettings (iOS 26.0): `ManagedSettingsStore.effectiveDenyExplicitContent`.
- A note that, with the iOS 26.4+ SDK, an exhaustive `switch` over `AuthorizationStatus`, `FamilyControlsError` or `ShieldAction` with no `default` no longer compiles. This was confirmed with `swiftc -typecheck` against the iOS 27.0 SDK.
- 17 Apple documentation URLs for these APIs in the source inventory and source matrix.
- This changelog.

### Changed
- Evidence files 01 to 07 now cite the iOS 27.0 SDK and carry iOS 26.x availability notes. Re-checked limits are unchanged: 50-token shield ceilings, 20 monitored activities, a 15-minute minimum and a one-week maximum interval.
- The ScreenTime evidence now marks `fetchHistory(during:completionHandler:)` and `fetchAllHistory` as iOS 18.4+.
- Guides 00, 02, 03, 04, 05, 07, 08, 11, 13, 17 and 19 cover the new APIs, availability gating, EU-only data access and the switch compile break.
- The claim reconciliation table has updated caveats and new rows for each finding.
- `SKILL.md` gains an SDK baseline section and a goal-map entry for host-app usage data. The README notes the SDK version and links this changelog.

### Not yet verified
- How an app requests data access. No separate request API appears in the SDK, and Apple's docs don't describe the prompt.
- Whether the app-and-website-usage entitlement needs its own distribution approval.
- What triggers token expiry and which errors `refresh(_:)` throws.

## [1.0.0] - 2026-02-14

First public release of the `screen-time-api-engineer` skill. It was not tagged at the time.

### Added
- `SKILL.md` with evidence-order rules, a goal-to-reference map and an output contract.
- 22 guides covering authorization, token selection, labels, ManagedSettings enforcement, web blocking, custom shields, shield actions, DeviceActivity scheduling and monitor extensions, usage reports, the ScreenTime framework, onboarding, a reference implementation, project analyses, hardening, testing, release review, a source matrix and a preflight rundown.
- 8 evidence files with SDK signatures extracted from the iOS 26.2 SDK, a source URL inventory and a claim reconciliation table.
- 3 project rundowns.
- Validation scripts `check_required_sections.sh` and `check_source_coverage.py`.
- README install instructions for `npx skills`, `SECURITY.md`, `agents/openai.yaml` and the MIT license.

[1.1.0]: https://github.com/Siddhu7007/screen-time-api-agent-skill/compare/bedbfc7...v1.1.0
[1.0.0]: https://github.com/Siddhu7007/screen-time-api-agent-skill/tree/bedbfc7
