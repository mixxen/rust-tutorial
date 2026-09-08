.DEFAULT_GOAL := help
.PHONY: help test check lint fmt fmt-check verify

help:
	@printf '%s\n' '$(ROLE): $(PACKAGE)' 'make test       Run acceptance tests in this package' 'make check      Compile this package without executing tests' 'make lint / fmt / fmt-check / verify' 'An unfinished EXERCISE is expected to fail make test.'

test:
	@printf '%s\n' 'Testing $(ROLE): $(PACKAGE)'
	cargo test --locked --offline

check:
	cargo check --all-targets --locked --offline

lint:
	cargo clippy --all-targets --locked --offline -- -D warnings

fmt:
	cargo fmt

fmt-check:
	cargo fmt -- --check

verify: fmt-check lint test
