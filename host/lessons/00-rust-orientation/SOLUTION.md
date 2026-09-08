# Solution — Include the boundary

Attempt the [exercise](EXERCISE.md) before using this page as a reference.

The complete implementation lives in [`solutions/00-rust-orientation/src/lib.rs`](../../../solutions/00-rust-orientation/src/lib.rs):

```rust
pub fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {
    reading >= limit
}
```

`>=` includes equality. The comparison still uses both parameters, so the function works with another limit and with negative readings. It produces a Boolean directly, matching `-> bool`.

The strict rule's answer changes only for equal values:

| Relationship | Old rule | New rule |
|---|---|---|
| Reading below limit | false | false |
| Reading equal to limit | false | true |
| Reading above limit | true | true |

For `[18, 22, 25, 29]` at 25, both 25 and 29 now qualify. No loop change is needed; the decision function was the appropriate place to express the changed requirement.

## Another valid form

This explicit-return form is also valid Rust:

```rust
pub fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {
    return reading >= limit;
}
```

We use the first form because it is a direct tail expression. Do not confuse the semicolon after an explicit `return` with adding a semicolon to a bare final comparison. Clippy can suggest the simpler expression form; Lesson 16 will discuss lint choices in detail.

## Verify the supplied answer, then your own work

From the lesson directory:

```bash
make solution
make exercise
```

The first command tests the supplied answer. The second tests your separate exercise and may still fail if you have not changed it. You need the second command to pass after your own edit, along with the additional cases you wrote.

The complete solution uses the same six supplied acceptance tests as the exercise. Those cases show the intended distinctions; they are not a proof of all possible program behavior.

## Why this small exercise matters

The original program was valid Rust and its original tests passed. A changed requirement made different tests necessary. The compiler did not know which rule the customer wanted. Being precise about that boundary—and using a meaningful function name and test name—made the change small and understandable.

Return to the [lesson](README.md#8-check-your-understanding) and explain the result without looking at this code.
