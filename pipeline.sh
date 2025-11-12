#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
ZIP_IN="$ROOT/earthquake_synthesis_clean.zip"
CLEAN_ROOT="$ROOT/earthquake_synthesis_clean_out"

mkdir -p "$CLEAN_ROOT"
python3 diagnose_and_copy.py --out "$CLEAN_ROOT" --manifest-json manifest.json

echo "Diagnostics + copy complete"
