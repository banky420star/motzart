#!/bin/bash
set -euo pipefail
ROOT="$(cd -P "$(dirname "$0")" && pwd)"
cd "$ROOT"
PYTHON_BIN="${PYTHON_BIN:-python3}"
"$PYTHON_BIN" scripts/benchmark_release.py
