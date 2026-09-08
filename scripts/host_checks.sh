#!/usr/bin/env bash
# Author/repository checks. Learners can use Cargo directly in each package.
set -euo pipefail
cd "$(dirname "$0")/.."
mode="${1:-verify}"
case "$mode" in
    test|lint|fmt|fmt-check|verify) ;;
    *) printf 'Unknown check: %s\n' "$mode" >&2; exit 2 ;;
esac

for manifest in host/Cargo.toml solutions/00-rust-orientation/Cargo.toml; do
    printf '\nComplete code: %s (%s)\n' "$manifest" "$mode"
    if [[ "$mode" == fmt ]]; then
        cargo fmt --manifest-path "$manifest" --all
    fi
    if [[ "$mode" == fmt-check || "$mode" == verify ]]; then
        cargo fmt --manifest-path "$manifest" --all -- --check
    fi
    if [[ "$mode" == lint || "$mode" == verify ]]; then
        cargo clippy --manifest-path "$manifest" --all-targets --locked --offline -- -D warnings
    fi
    if [[ "$mode" == test || "$mode" == verify ]]; then
        cargo test --manifest-path "$manifest" --locked --offline
    fi
done

if [[ "$mode" == verify ]]; then
    printf '\nEXERCISE: compile only; your exercise assertions are not run here.\n'
    cargo check --manifest-path exercises/00-rust-orientation/Cargo.toml --all-targets --locked --offline
    python3 scripts/check_repository.py
    python3 scripts/check_expected_errors.py
fi
