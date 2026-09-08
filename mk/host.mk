# Included from a lesson directory; Cargo remains the build system.
.DEFAULT_GOAL := help
.PHONY: help run test lint fmt fmt-check verify exercise solution errors comparisons

help:
	@printf '%s\n' 'WORKED EXAMPLE: $(PACKAGE)' 'make run / test / lint / fmt / fmt-check / verify' 'make exercise   Test YOUR separate exercise (initial failures expected)' 'make solution   Test the supplied complete solution, not your work' 'make errors     Verify the isolated compiler-error demonstrations' 'make comparisons  Compare Rust/C++/Python output (requires g++)'

run:
	@printf '%s\n' 'Running WORKED EXAMPLE: $(PACKAGE)'
	cargo run --locked --offline

test:
	@printf '%s\n' 'Testing WORKED EXAMPLE: $(PACKAGE)'
	cargo test --locked --offline

lint:
	cargo clippy --all-targets --locked --offline -- -D warnings

fmt:
	cargo fmt -p $(PACKAGE)

fmt-check:
	cargo fmt -p $(PACKAGE) -- --check

verify: fmt-check lint test

exercise:
	@$(MAKE) --no-print-directory -C "$(ROOT)/exercises/$(LESSON_ID)" test

solution:
	@$(MAKE) --no-print-directory -C "$(ROOT)/solutions/$(LESSON_ID)" test

errors:
	@python3 "$(ROOT)/scripts/check_expected_errors.py"

comparisons:
	@python3 "$(ROOT)/scripts/check_comparisons.py"
