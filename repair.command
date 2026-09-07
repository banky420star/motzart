#!/bin/bash
set -u
SUPPORT="$HOME/Library/Application Support/Mozart"
LOG="$HOME/Library/Logs/Mozart/launcher.log"
APP="$HOME/Applications/Mozart.app"

printf 'Mozart native runtime repair\n'
printf 'This resets only the local Python renderer/runtime environment.\n'
printf 'Objectives, memory, workspace settings and project files are not deleted.\n\n'
rm -rf "$SUPPORT/venv" "$SUPPORT/.runtime-version" "$SUPPORT/.runtime-signature"
mkdir -p "$(dirname "$LOG")"
: > "$LOG"

if [ -d "$APP" ]; then
  xattr -dr com.apple.quarantine "$APP" 2>/dev/null || true
  open "$APP"
  printf 'Mozart is rebuilding its native runtime with a fresh interpreter/architecture signature.\n'
else
  printf 'Installed Mozart.app was not found at %s\n' "$APP"
  printf 'Run install.command first.\n'
fi
