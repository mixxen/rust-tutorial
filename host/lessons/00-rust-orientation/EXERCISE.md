# Exercise — Include the boundary

[Lesson 00](README.md) · Before this exercise: [Part 4 — First tests](FIRST_TESTS.md)

The original worked example asks whether a reading is **strictly above** a limit. A new requirement says: **a reading qualifies when it is at or above the supplied limit**.

For `[18, 22, 25, 29]` and a limit of 25, the new count must be **2**, not 1. Predict the result for a reading of -5 and a limit of -5 as well.

## 1. Open the exercise project

Leave your practice program and the supplied example intact. The exercise has its own Cargo package and source file.

If you finished Part 4 in `host/lessons/00-rust-orientation`, return to the repository root:

```bash
cd ../../..
```

**From the repository root**, enter the exercise:

```bash
cd exercises/00-rust-orientation
cargo test
```

These tests initially fail **four equality-sensitive checks**. That is the expected starting point. A missing compiler, a missing file, or a compilation error is not the intended failure.

In your editor, open `exercises/00-rust-orientation/src/lib.rs`. This is a library, so it does not have a `main` function. Cargo's test runner calls its function from the tests. The file already contains `pub fn is_at_or_above_limit(...)`: the name matches the new requirement, but its implementation still uses the old rule.

Correct the comparison. Save the file and run `cargo test` again **from the exercise directory**. Do not rename the function or change the supplied acceptance tests to make an incorrect implementation pass.

## 2. Add tests of your own

In your editor, create a new file named **`your_cases.rs` inside this exercise's `tests` directory**, beside `acceptance.rs`. Its full repository path is `exercises/00-rust-orientation/tests/your_cases.rs`.

Start with this entire file:

```rust
use threshold_rule::is_at_or_above_limit;

#[test]
fn excludes_a_cold_reading_below_the_limit() {
    assert!(!is_at_or_above_limit(-12, -10));
}
```

The `use` line imports the function from the exercise library, named `threshold_rule` in this package's `Cargo.toml`. The `::` separates the library name from the function name. That is the same idea introduced at the end of Part 4, not another language feature you need to guess.

Save, and add your own equal and above cases using -10 as the limit. Keep the supplied `acceptance.rs` unchanged; your new file is where your additional cases belong. Cargo discovers `.rs` test files in `tests/` automatically.

Run `cargo test` after your edits. Use names that communicate behavior, not `test1`. A passing test of the supplied solution is not a passing test of your work.

## 3. Check the result and explain it

| Requirement | Evidence |
|---|---|
| Below the limit does not qualify | Passing below-boundary assertions |
| Equality qualifies | A passing equality assertion, including your own case |
| Above the limit qualifies | Passing above-boundary assertions |
| The supplied limit is actually used | The non-25-limit test passes |
| Negative readings follow the same rule | The supplied negative test and your new cases pass |
| Two sample readings now qualify | The supplied count assertion passes |
| You understand the change | Explain why the new rule differs from the original without reading the solution |

From the exercise directory, an optional final quality check is:

```bash
make verify
```

This checks **your exercise**, including formatting, linting, and its assertions. Use `make fmt` here to fix formatting when requested; it rewrites formatting, not the intended behavior. The underlying tests still run with `cargo test`.

The reference and solution are separate packages. Both the exercise and solution use the library name `threshold_rule` so they can share identical acceptance-test requirements, but their Cargo package names are different. Read the command output to see which one you tested.

You can also run `make exercise` from the **lesson directory** as a shortcut for testing this exercise. You do not need that shortcut to finish the work above.

Need help? Read the [gradual hints](HINTS.md), then the [explained solution](SOLUTION.md) when you are ready. The purpose is to make a change you can explain, not just obtain green test results.
