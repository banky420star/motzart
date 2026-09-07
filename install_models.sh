#!/bin/bash
set -euo pipefail
if ! command -v ollama >/dev/null 2>&1; then
  echo "Ollama is not installed or not on PATH."
  exit 1
fi
for model in qwen3:8b qwen3:4b embeddinggemma gemma3:4b; do
  echo "Ensuring $model..."
  ollama pull "$model"
done
