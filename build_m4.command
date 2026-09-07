#!/bin/bash
set -euo pipefail
ROOT="$(cd -P "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [ "$(uname -s)" != "Darwin" ] || [ "$(uname -m)" != "arm64" ]; then
  echo "This builder requires an Apple Silicon Mac."
  exit 1
fi

PYTHON_BIN=""
for candidate in /opt/homebrew/bin/python3.12 /opt/homebrew/bin/python3.13 /usr/local/bin/python3.12 /usr/local/bin/python3.13; do
  if [ -x "$candidate" ]; then PYTHON_BIN="$candidate"; break; fi
done
if [ -z "$PYTHON_BIN" ]; then
  echo "Python 3.12 or 3.13 is required. Install it from python.org, then run this file again."
  exit 2
fi

BUILD_ENV="$ROOT/.m4-build"
"$PYTHON_BIN" -m venv "$BUILD_ENV"
"$BUILD_ENV/bin/python" -m pip install --upgrade pip
"$BUILD_ENV/bin/python" -m pip install --no-cache-dir -r requirements-build.txt
"$BUILD_ENV/bin/pyinstaller" --noconfirm --clean Mozart-arm64.spec

/usr/bin/codesign --force --deep --sign - "$ROOT/dist/Mozart.app"
/usr/bin/xattr -dr com.apple.quarantine "$ROOT/dist/Mozart.app" 2>/dev/null || true
/usr/bin/open "$ROOT/dist"
echo
echo "Built native ARM64 app: $ROOT/dist/Mozart.app"
echo "This app contains its Python runtime and can launch offline."
