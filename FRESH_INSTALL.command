#!/bin/bash
set -euo pipefail
ROOT="$(cd -P "$(dirname "$0")" && pwd)"
STAMP="$(date +%Y%m%d-%H%M%S)"
TRASH="$HOME/.Trash"
mkdir -p "$TRASH"

echo "MOZART 2.1.1 — LIVING SWARM BUILD"
echo "================================"
echo "This replaces the old Mozart app bundle but preserves your user projects and Application Support data."
echo

for old in "$HOME/Applications/Mozart.app" "/Applications/Mozart.app"; do
  if [ -e "$old" ]; then
    if [ -w "$(dirname "$old")" ]; then
      target="$TRASH/Mozart-old-$STAMP.app"
      echo "Moving old app bundle to Trash: $old"
      mv "$old" "$target"
    else
      echo "Old app found at $old but this user cannot move it. The new user-level app will still be installed."
    fi
  fi
done

cd "$ROOT"
exec ./install.sh
