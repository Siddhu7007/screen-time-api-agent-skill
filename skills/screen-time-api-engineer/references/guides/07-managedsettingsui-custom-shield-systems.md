# 07 ManagedSettingsUI Custom Shield Systems

## Purpose
Standardize custom shield UI implementation for blocked apps/categories/web domains.

## Canonical API Surface
- `ShieldConfigurationDataSource`
- `ShieldConfiguration`
- Shield configuration extension point for UI rendering

## Implementation Pattern
- Implement all four configuration override variants.
- Build shared shield theme helper to avoid drift.
- Populate title/subtitle/button labels from shared state (app group values), not network.
- Keep style deterministic and performant; shield extensions are latency sensitive.

## Failure Modes
- Implementing only one override path (app) and forgetting category/web paths.
- Using unavailable assets without fallback symbols.
- Depending on host app runtime state rather than persisted app-group state.

## Validation Checklist
- [ ] App, category, domain, domain-in-category all return valid configuration.
- [ ] Primary button label + style are always set.
- [ ] Fallback icon path works if custom asset missing.
- [ ] Visual state reflects lock/unlock status from app-group data.

## Sources
- `../evidence/03-managedsettingsui-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettingsui
- https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationextension
- https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Extension interface contract is `canonical + sdk-backed`.
- Visual design recommendations are `project-observed`.
