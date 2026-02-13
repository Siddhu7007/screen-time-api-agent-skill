#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
GUIDES_DIR="$BASE_DIR/references/guides"

required=(
  "## Purpose"
  "## Canonical API Surface"
  "## Implementation Pattern"
  "## Failure Modes"
  "## Validation Checklist"
  "## Sources"
  "## Confidence Notes"
)

failed=0
for f in "$GUIDES_DIR"/*.md; do
  for h in "${required[@]}"; do
    if ! grep -Fq "$h" "$f"; then
      echo "MISSING: $(basename "$f") -> $h"
      failed=1
    fi
  done
done

if [ "$failed" -ne 0 ]; then
  echo "Section check failed"
  exit 1
fi

echo "Section check passed"
