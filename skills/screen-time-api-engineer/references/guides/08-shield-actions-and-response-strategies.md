# 08 Shield Actions and Response Strategies

## Purpose
Define robust shield button action behavior and guardrails for unlock bypass prevention.

## Canonical API Surface
- `ShieldActionDelegate`
- `ShieldAction`
- `ShieldActionResponse`

## Implementation Pattern
- Route all action variants (application/category/webDomain) to shared handler.
- Use response mapping intentionally:
  - `.close` to dismiss shield UI
  - `.defer` where deferral UX is intended
  - `.none` only when explicit no-op is desired
- Keep business unlock decisions in app/monitor state machine, not action delegate alone.

## Failure Modes
- Returning permissive responses without state checks.
- Handling only app token actions and ignoring categories/web domains.
- Mixing shield action with unrelated network or heavy logic.

## Validation Checklist
- [ ] All three token contexts implemented.
- [ ] Response mapping documented and tested.
- [ ] No hidden unlock side effects in action delegate.
- [ ] Action behavior aligns with policy engine states.

## Sources
- `../evidence/02-managedsettings-sdk-signatures.md`
- https://developer.apple.com/documentation/managedsettings/shieldactiondelegate
- https://developer.apple.com/documentation/managedsettings/shieldaction
- https://developer.apple.com/documentation/managedsettings/shieldactionresponse

## Confidence Notes
- Action/response semantics are `canonical + sdk-backed`.
- Strategy guidance is `project-observed + inference` and should be validated with UX tests.
