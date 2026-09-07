#!/bin/bash
set -u
cd -P "$(dirname "$0")" || exit 1
if [ "$(uname -s)" = "Darwin" ]; then
  if [ -d "$HOME/Applications/Mozart.app" ]; then
    open "$HOME/Applications/Mozart.app"
  elif [ -d "Mozart.app" ]; then
    open "Mozart.app"
  else
    ./run.sh
  fi
else
  ./run.sh
fi
