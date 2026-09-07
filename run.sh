#!/bin/bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
if [ ! -x .venv/bin/python ]; then
  echo "Virtual environment missing. Run ./install.sh first."
  exit 1
fi
set -a
if [ -f .env ]; then . ./.env; fi
set +a
HOST="${MOZART_HOST:-0.0.0.0}"
PORT="${MOZART_PORT:-8765}"
echo ""
echo "Mozart — Autonomous Software Intelligence"
echo "Intelligence in motion."
echo "Local:     http://127.0.0.1:${PORT}"
echo "Ollama:    ${MOZART_OLLAMA_URL:-http://127.0.0.1:11434}"
echo "Workspace: ${MOZART_WORKSPACE:-./workspace}"
echo "Stop with Ctrl-C"
echo ""
exec .venv/bin/python -m uvicorn backend.main:app --host "$HOST" --port "$PORT"
