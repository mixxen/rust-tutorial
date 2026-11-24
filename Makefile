.DEFAULT_GOAL := help
.PHONY: help run lint fmt fmt-check verify comparisons

LESSON := host/00-rust-orientation
HOST_MANIFEST := host/Cargo.toml

help:
	@printf '%s\n' 'Start at $(LESSON)/README.md' \
		'make run          Run the Lesson 00 readings example' \
		'make lint         Check the host binaries with Clippy' \
		'make fmt-check    Check Rust formatting' \
		'make fmt          Format Rust code' \
		'make verify       Check formatting, links, and runnable walkthrough examples' \
		'make comparisons  Compare the Rust, C++, and Python programs'

run:
	cargo run --manifest-path $(LESSON)/Cargo.toml --locked --offline

lint:
	cargo clippy --manifest-path $(HOST_MANIFEST) --workspace --bins --locked --offline -- -D warnings

fmt:
	cargo fmt --manifest-path $(HOST_MANIFEST) --all

fmt-check:
	cargo fmt --manifest-path $(HOST_MANIFEST) --all -- --check

verify: fmt-check lint
	@python3 scripts/check_repository.py
	@python3 scripts/check_walkthrough.py

comparisons:
	@python3 scripts/check_comparisons.py
