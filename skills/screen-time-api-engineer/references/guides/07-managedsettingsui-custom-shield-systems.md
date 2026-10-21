# 07 ManagedSettingsUI Custom Shield Systems

## Purpose
Standardize custom shield UI implementation for blocked apps/categories/web domains.

## Canonical API Surface
- `ShieldConfigurationDataSource`
- `ShieldConfiguration`
- Shield configuration extension point for UI rendering
- `ShieldConfiguration.secondaryButtonSubmenuItems: [String]?` (iOS 26.4+), set through the initializer that takes `secondaryButtonSubmenuItems:`

## Implementation Pattern
- Implement all four configuration override variants.
- Build shared shield theme helper to avoid drift.
- Populate title/subtitle/button labels from shared state (app group values), not network.
- Keep style deterministic and performant; shield extensions are latency sensitive.
- On iOS 26.4+, optionally pass up to three `secondaryButtonSubmenuItems`. Define the item list once and share it with the shield action extension so item order and handler mapping can't drift. The system adds a Cancel item.

## Failure Modes
- Implementing only one override path (app) and forgetting category/web paths.
- Using unavailable assets without fallback symbols.
- Depending on host app runtime state rather than persisted app-group state.
- Submenu labels (configuration extension) and their handlers (action extension) drifting apart.
- Passing more than three submenu items. Apple documents up to three, and `ShieldAction` has only three submenu cases.

## Validation Checklist
- [ ] App, category, domain, domain-in-category all return valid configuration.
- [ ] Primary button label + style are always set.
- [ ] Fallback icon path works if custom asset missing.
- [ ] Visual state reflects lock/unlock status from app-group data.
- [ ] Submenu items are gated with `if #available(iOS 26.4, *)`, and older versions fall back to the plain secondary button.

## Sources
- `../evidence/03-managedsettingsui-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettingsui
- https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationextension
- https://developer.apple.com/documentation/managedsettingsui/shieldconfigurationdatasource
- https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/secondarybuttonsubmenuitems
- `../rundowns/10-project-alpha-rundown.md`
- `../rundowns/11-project-beta-rundown.md`

## Confidence Notes
- Extension interface contract is `canonical + sdk-backed`.
- Visual design recommendations are `project-observed`.
- Submenu behavior (up to three items, nil/empty falls back, system Cancel) is `canonical + sdk-backed` (iOS 26.4+).
