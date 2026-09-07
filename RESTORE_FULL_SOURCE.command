#!/bin/bash
set -euo pipefail
ROOT="$(cd -P "$(dirname "$0")" && pwd)"
ARCHIVE="$ROOT/source/Mozart-2.1.1-Living-Swarm-source.tar.gz"
if [ ! -f "$ARCHIVE" ]; then
  echo "Missing source archive: $ARCHIVE"
  exit 1
fi
printf 'Restoring the complete Mozart 2.1.1 frontend/backend source into %s\n' "$ROOT"
tar -xzf "$ARCHIVE" -C "$ROOT"
printf 'Source restored. Run ./test.sh, ./install.command, or ./build_m4.command next.\n'
