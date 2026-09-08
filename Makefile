.DEFAULT_GOAL := help
.PHONY: help run test lint fmt fmt-check verify comparisons

help:
	@printf '%s\n' 'Start: host/lessons/00-rust-orientation/README.md' 'make run         Run Lesson 00 worked example' 'make test        Test worked examples and complete solutions' 'make lint        Check complete code with Clippy' 'make fmt-check   Check formatting without rewriting files' 'make fmt         Format complete code (changes files)' 'make verify      Run all non-hardware checks; not exercise assertions' 'make comparisons Compare Rust/C++/Python output (requires g++)' 'Exercise: make -C exercises/00-rust-orientation test'

run:
	@$(MAKE) --no-print-directory -C host/lessons/00-rust-orientation run

test lint fmt fmt-check verify:
	@bash scripts/host_checks.sh $@

comparisons:
	@python3 scripts/check_comparisons.py
