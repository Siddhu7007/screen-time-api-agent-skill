# 02 Authorization Setup

## Purpose
Provide a complete entitlement and authorization setup path for iOS 16+ Screen Time apps, including distribution approval workflow.

## Canonical API Surface
- Entitlement key: `com.apple.developer.family-controls`.
- Authorization API: `AuthorizationCenter.shared.requestAuthorization(for:)`.
- Status API: `AuthorizationCenter.authorizationStatus`.
- Member type: `FamilyControlsMember` (`individual`, `child`).

## Implementation Pattern
1. Register capability for **every relevant bundle ID**:
   - main app
   - DeviceActivity monitor extension
   - shield configuration extension
   - shield action extension
   - report extension (if used)
2. Add matching app group to every participating target.
3. Add `NSFamilyControlsUsageDescription` in app target info settings.
4. On first launch/onboarding, request authorization.
5. Re-check authorization at each enforcement boundary (app + extension).

## Entitlement Distribution Workflow
1. Request Family Controls distribution capability through Apple managed capability request flow.
2. Use official request endpoint:
   [Family Controls distribution request](https://developer.apple.com/contact/request/family-controls-distribution)
3. Wait for approval before production distribution.
4. Regenerate provisioning profiles after approval.
5. Validate Debug and Release both contain capability and correct entitlement file mapping.

## Waiting-Period Reality
- Observed in field reports and forum discussions: approval turnaround varies widely.
- Practical planning assumption:
  - best case: a few days
  - common case: multiple days to multiple weeks
- Treat capability approval as a critical release dependency and start early.

## Failure Modes
- Capability enabled only for app target, not extensions.
- Debug works, Release fails due to missing capability/profile refresh.
- Authorization denied/revoked but UI lacks recovery instructions.

## Validation Checklist
- [ ] Entitlement present in all required target entitlement files.
- [ ] `CODE_SIGN_ENTITLEMENTS` points to intended file for each build configuration.
- [ ] Usage description key is present in app build settings.
- [ ] App correctly handles `.notDetermined`, `.denied`, `.approved`.
- [ ] User-facing remediation path shown for deny/revoke.

## Sources
- https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.family-controls
- https://developer.apple.com/documentation/familycontrols/requesting-the-family-controls-entitlement
- https://developer.apple.com/documentation/xcode/configuring-family-controls
- https://developer.apple.com/contact/request/family-controls-distribution
- https://developer.apple.com/help/account/capabilities/capability-requests/
- `../evidence/01-familycontrols-sdk-signatures.md`
- `../evidence/07-claim-reconciliation.md`

## Confidence Notes
- Entitlement mechanics and authorization states are `canonical + sdk-backed`.
- Approval lead-time expectation is `field-note` and should be treated as risk planning guidance.
