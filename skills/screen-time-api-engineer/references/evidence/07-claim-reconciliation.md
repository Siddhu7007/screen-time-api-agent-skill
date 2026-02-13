# 07 Claim Reconciliation

This file reconciles claims across canonical docs, SDK extraction, project implementations, and field notes.

| Claim | Classification | Evidence | Caveat |
|---|---|---|---|
| Family activity selections are opaque tokens. | canonical + sdk-backed | FamilyControls doc strings + `FamilyActivitySelection` signatures. | None. |
| You can render real app/category/domain labels from tokens. | canonical + sdk-backed | `Label(_ applicationToken:)` and related in FamilyControls interface. | Display fidelity depends on system-provided metadata. |
| ManagedSettings shield/app/web token limits include 50 ceilings. | sdk-backed | ManagedSettings `.swiftdoc` limit statements. | Limits are per API/policy context; enforce defensive validation. |
| `DeviceActivityCenter` supports at most 20 monitored activities. | sdk-backed | DeviceActivity `.swiftdoc` for `excessiveActivities`. | Subject to platform/runtime evolution; re-check SDK each release. |
| Minimum interval is 15 minutes and max interval is one week. | sdk-backed | DeviceActivity `.swiftdoc` monitoring error docs. | Validate behavior on your deployment iOS floor. |
| DeviceActivity report extensions run in privacy sandbox with no network. | sdk-backed | `_DeviceActivity_SwiftUI.swiftdoc` extension notes. | Keep rendering logic local and deterministic. |
| Authorization revocation can invalidate previously obtained tokens. | canonical + sdk-backed | FamilyControls symbol docs note revocation implications. | Always re-check authorization before applying shields. |
| Project Alpha uses multi-store shielding and day rollover with shared defaults. | project-observed | Project Alpha monitor/lock manager code. | Pattern is valid; still verify race conditions and redundant clear calls. |
| Project Beta uses schedule-driven monitor + immediate manager fallback logic. | project-observed | Project Beta app manager + monitor extension code. | Consider explicit auth checks in monitor callbacks. |
| Medium/field posts reflect practical extension pitfalls and iteration patterns. | field-note | Julius + Letvar posts. | Treat as advisory unless corroborated by canonical/SDK evidence. |

## Reconciliation Rule Applied
- Final guides default to canonical and SDK-backed claims.
- `project-observed` and `field-note` claims are explicitly labeled.
- `inference` claims are only used with caveats and validation checklist items.

Last verified: `2026-02-08`
