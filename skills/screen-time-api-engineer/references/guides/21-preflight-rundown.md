# 21 Preflight Rundown

## Purpose
Provide final go/no-go preflight before implementing or shipping a Screen Time API blocking app.

## Canonical API Surface
- N/A (execution summary file)

## Implementation Pattern
Preflight sequence:
1. Verify entitlement/capability setup across all bundle IDs.
2. Verify authorization UX and deny/revoke remediation.
3. Verify token selection persistence and label rendering.
4. Verify monitor schedule registration and fallback behavior.
5. Verify extension-driven enforcement while app is terminated.
6. Verify custom shield UI/action behavior for app/category/domain.
7. Verify analytics report extension renders with sandbox constraints.
8. Verify release signing/profile parity.

## Failure Modes
- Any “works in Debug only” behavior.
- Any unsigned/mis-signed extension target.
- Any unhandled monitor error path.

## Validation Checklist
- [ ] Functional smoke pass complete.
- [ ] Edge-case matrix pass complete.
- [ ] Evidence and source matrix up to date.
- [ ] No unresolved placeholder markers in docs.
- [ ] Skill package validates and installs correctly.

## Sources
- `../evidence/07-claim-reconciliation.md`
- `../rundowns/12-cross-project-rundown.md`
- `./18-testing-matrix-device-only-edge-cases.md`
- `./19-release-and-app-review-checklist.md`

## Confidence Notes
- This preflight is a synthesized control checklist (`inference`) built on high-confidence evidence files.
