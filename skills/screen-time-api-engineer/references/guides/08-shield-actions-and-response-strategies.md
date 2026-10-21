# 08 Shield Actions and Response Strategies

## Purpose
Define robust shield button action behavior and guardrails for unlock bypass prevention.

## Canonical API Surface
- `ShieldActionDelegate`
- `ShieldAction`
- `ShieldActionResponse`
- Submenu actions (iOS 26.4+): `.firstSecondarySubmenuItemPressed`, `.secondSecondarySubmenuItemPressed`, `.thirdSecondarySubmenuItemPressed`
- `ShieldActionResponse.openParentalControlsApp` (iOS 26.5+)

## Implementation Pattern
- Route all action variants (application/category/webDomain) to shared handler.
- Use response mapping intentionally:
  - `.close` to dismiss shield UI
  - `.defer` where deferral UX is intended
  - `.none` only when explicit no-op is desired
  - `.openParentalControlsApp` (iOS 26.5+) when the person should continue in your app
- Map submenu actions by index to the same item list the configuration extension uses (iOS 26.4+).
- Keep business unlock decisions in app/monitor state machine, not action delegate alone.

## Failure Modes
- Returning permissive responses without state checks.
- Handling only app token actions and ignoring categories/web domains.
- Mixing shield action with unrelated network or heavy logic.
- A `switch` over `ShieldAction` with no `default` no longer compiles with the iOS 26.4+ SDK.

## Validation Checklist
- [ ] All three token contexts implemented.
- [ ] Response mapping documented and tested.
- [ ] No hidden unlock side effects in action delegate.
- [ ] Action behavior aligns with policy engine states.
- [ ] Submenu actions and `.openParentalControlsApp` are availability-gated and tested on iOS 26.4+ / 26.5+ devices.

## Sources
- `../evidence/02-managedsettings-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettings/shieldactiondelegate
- https://developer.apple.com/documentation/managedsettings/shieldaction
- https://developer.apple.com/documentation/managedsettings/shieldactionresponse
- https://developer.apple.com/documentation/managedsettings/shieldactionresponse/openparentalcontrolsapp
- https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/secondarybuttonsubmenuitems

## Confidence Notes
- Action/response semantics are `canonical + sdk-backed`.
- The `ShieldAction` switch compile break is `sdk-backed` (typecheck against the iOS 27.0 SDK).
- Strategy guidance is `project-observed + inference` and should be validated with UX tests.
