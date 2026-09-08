# Lesson 00 exercise — your work

Read the [exercise instructions](../../host/lessons/00-rust-orientation/EXERCISE.md) first. Edit `src/lib.rs` here, not the worked example or the solution.

From this directory:

```bash
make test
```

Equivalent:

```bash
cargo test --locked --offline
```

The initial strict comparison fails four of the six acceptance tests. Change the behavior to meet the stated requirement, leave `tests/acceptance.rs` intact, and add your own tests in `tests/your_cases.rs`.

Use `make verify` here to check your exercise's formatting, lints, and tests. This is a standalone package with its own lockfile. Its library is named `threshold_rule` so the exercise and solution can use the same acceptance tests; the package being tested is `lesson-00-exercise`.

[Hints](../../host/lessons/00-rust-orientation/HINTS.md) are separate from the [explained solution](../../host/lessons/00-rust-orientation/SOLUTION.md).
