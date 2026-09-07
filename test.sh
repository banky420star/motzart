#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PY=.venv/bin/python
if [ ! -x "$PY" ]; then PY=python3; fi

echo "== Mozart 2.1.1 validation =="
"$PY" -m py_compile backend/*.py backend/providers/*.py backend/tools/*.py desktop.py
if command -v node >/dev/null 2>&1; then
  node --check backend/static/app.js
else
  echo "[skip] node unavailable; JavaScript parse check skipped"
fi
for script in install.sh run.sh diagnose.sh install_models.sh create_macos_app.sh install.command run.command repair.command; do
  bash -n "$script"
done
MOZART_AUTO_EXECUTE=0 "$PY" -m unittest discover -s tests -v
