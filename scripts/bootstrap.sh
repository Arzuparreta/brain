#!/usr/bin/env bash
# Deprecated name — use ./scripts/setup.sh
exec "$(cd "$(dirname "$0")" && pwd)/setup.sh" "$@"
