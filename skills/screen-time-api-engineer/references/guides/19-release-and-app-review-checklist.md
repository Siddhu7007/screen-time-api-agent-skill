# 19 Release and App Review Checklist

## Purpose
Provide a release-safe checklist for TestFlight/App Store deployment of Screen Time apps.

## Canonical API Surface
- Family Controls entitlement
- Target capability configuration
- Provisioning profile and signing consistency

## Implementation Pattern
1. Verify capability and entitlements on all required targets.
2. Regenerate and re-download provisioning profiles after entitlement approval.
3. Validate Debug and Release config parity for capability wiring.
4. Confirm usage description keys and user-facing permission rationale copy.
5. Execute real-device end-to-end smoke before TestFlight submission.

## Failure Modes
- Release profile missing entitlement while Debug succeeds.
- Extension target signing mismatch.
- Missing usage description or incorrect capability scope.

## Validation Checklist
- [ ] All target bundle IDs approved for family-controls distribution use.
- [ ] `CODE_SIGN_ENTITLEMENTS` correct in Debug + Release.
- [ ] App groups identical across app and extension targets.
- [ ] Entitlement approval dependency tracked in release timeline.
- [ ] Real-device smoke run performed on production provisioning profile.

## Sources
- https://developer.apple.com/documentation/xcode/configuring-family-controls
- https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement
- https://developer.apple.com/contact/request/family-controls-distribution
- `../evidence/07-claim-reconciliation.md`

## Confidence Notes
- Checklist is `canonical + field-note`; approval timelines vary by account/process load.
