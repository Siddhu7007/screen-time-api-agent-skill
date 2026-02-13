# Screen Time API Agent Skill

A production-oriented agent skill for building and shipping iOS Screen Time features using:
- `FamilyControls`
- `ManagedSettings`
- `ManagedSettingsUI`
- `DeviceActivity`
- `ScreenTime`

This skill is designed for implementation, debugging, hardening, and release-readiness workflows.

## Install

```bash
npx skills add Siddhu7007/screen-time-api-agent-skill --list
npx skills add Siddhu7007/screen-time-api-agent-skill -a codex -g -y --skill screen-time-api-engineer
npx skills add https://github.com/Siddhu7007/screen-time-api-agent-skill/tree/main/skills/screen-time-api-engineer -a codex -g -y
```

For Codex users: `Restart Codex to pick up new skills.`

## Skill Path

```text
skills/screen-time-api-engineer
```

## When To Use

Use this skill when you need to:
- Implement app/website blocking with token-based policies.
- Build custom shields and shield action flows.
- Configure schedule-based enforcement and monitor callbacks.
- Validate entitlements/signing and Screen Time distribution readiness.
- Debug Screen Time edge cases and harden for production.

## What It Covers

- Authorization patterns and onboarding UX for Screen Time permissions.
- Token selection and handling for app/category/web domain controls.
- Policy enforcement patterns with ManagedSettings stores.
- ManagedSettingsUI custom shield architecture and responses.
- DeviceActivity scheduling, thresholds, monitor extension behavior.
- Usage analytics/reporting architecture and reliability checks.
- Release and App Review checklist for Screen Time apps.

## Example Prompts

- "Implement app + website blocking with ManagedSettings and FamilyControls tokens."
- "Build a custom shield UI with ManagedSettingsUI and safe action handling."
- "Debug DeviceActivity monitor callback timing and threshold behavior."
- "Design a production onboarding flow for Screen Time authorization with fallback UX."
- "Run a release readiness review for entitlements, extensions, and policy parity."

## Using In Codex

After installation, you can invoke the skill explicitly in prompts:

```text
$screen-time-api-engineer
```

## Validation

Run these checks from repo root:

```bash
bash skills/screen-time-api-engineer/scripts/check_required_sections.sh
python3 skills/screen-time-api-engineer/scripts/check_source_coverage.py
npx skills add . --list
npx skills add Siddhu7007/screen-time-api-agent-skill --list
```

Expected result:
- Section check passes
- Source coverage check passes
- `npx skills ... --list` shows `screen-time-api-engineer`

## Safety

See `SECURITY.md` for script execution and secret-handling guidance.

## Repository Structure

```text
skills/
  screen-time-api-engineer/
    SKILL.md
    agents/
      openai.yaml
    references/
    scripts/
    assets/
```
