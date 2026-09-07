#!/bin/bash
set -u
cd -P "$(dirname "$0")" || exit 1
./install.sh
STATUS=$?
if [ "$STATUS" -eq 0 ] && [ "$(uname -s)" = "Darwin" ] && [ -d "$HOME/Applications/Mozart.app" ]; then
  open "$HOME/Applications/Mozart.app"
fi
exit "$STATUS"
