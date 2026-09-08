# Exercise — Include the boundary

The original worked example answers “Is this reading strictly above the limit?” A new requirement says: **A reading qualifies when it is at or above the supplied limit.**

For `[18, 22, 25, 29]` and a limit of `25`, the new count must be **2**, not 1. Predict the answer for a reading of `-5` and a limit of `-5` as well.

## Work in the exercise, not the example

From the Lesson 00 directory:

```bash
make exercise
```

This prints the selected exercise package and runs its tests. It initially fails four equality-sensitive tests. That is the expected starting point, not a broken installation. A compiler error, missing tool, or lockfile error is not the expected failure.

The Cargo equivalent, from the **repository root**, is:

```bash
cargo test --manifest-path exercises/00-rust-orientation/Cargo.toml --locked --offline
```

Edit [`exercises/00-rust-orientation/src/lib.rs`](../../../exercises/00-rust-orientation/src/lib.rs). The function is already named `is_at_or_above_limit`, but its implementation still follows the old requirement. Correct the implementation; do not change the function signature or weaken the supplied acceptance tests.

The two standalone packages both expose a library named `threshold_rule`, allowing them to use identical acceptance-test files. Their package names and printed command labels remain different. A passing solution test is not a passing test of your exercise.

## Add your own tests

Create `tests/your_cases.rs` **inside the exercise package**, beside `tests/acceptance.rs`. Start with this ordinary passing example and add your own below/equal/above cases using a different limit:

```rust
use threshold_rule::is_at_or_above_limit;

#[test]
fn excludes_a_cold_reading_below_the_limit() {
    assert!(!is_at_or_above_limit(-12, -10));
}
```

Use names that describe the behavior, not `test1`. Add at least one equality assertion. Leave `tests/acceptance.rs` unchanged: it represents the supplied requirements. Your new test file is automatically discovered by Cargo.

Run `make exercise` again from the lesson directory, or `make test` from the exercise directory. Run it after **your** edit, not merely after opening the solution.

## Completion checklist

| Requirement | Evidence |
|---|---|
| Below the limit does not qualify | A passing assertion with a below-boundary input |
| Equality qualifies | A passing assertion with equal input and limit |
| Above the limit qualifies | A passing assertion with an above-boundary input |
| The actual parameter is used | The supplied non-25-limit test passes |
| Negative values follow the same ordering | The supplied negative-reading test and your added case pass |
| The sample now has two qualifying readings | The supplied sample-count assertion passes |
| You can explain the fix | Describe the behavioral difference without reading the solution |

From the exercise directory, finish with:

```bash
make verify
```

Here `make verify` checks **your exercise**, including its assertions. By contrast, root `make verify` checks the course's complete code and only compiles the exercise. The location matters, and each test command prints which package it selected.

Need a nudge? Open [HINTS.md](HINTS.md). The [solution discussion](SOLUTION.md) is separate so you can choose when to reveal it.
