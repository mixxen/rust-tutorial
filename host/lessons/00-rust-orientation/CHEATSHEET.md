# Rust syntax: recognize it now, study it later

This is a map, not a list to memorize. The first table covers today's code. Everything after it is optional preview material. Lesson numbers refer to the [planned curriculum](../../../CURRICULUM.md), not to implemented packages.

## Today's vocabulary

| Form | Meaning in the example |
|---|---|
| `let limit = 25;` | Introduce a binding; its type is inferred |
| `let limit: i32 = 25;` | State a signed 32-bit type explicitly |
| `let mut qualifying_count = 0;` | Permit changing this binding |
| `fn is_above_limit(reading: i32, limit: i32) -> bool` | Name, parameters, and result type of a function |
| `reading > limit` / `reading >= limit` | Strict / inclusive comparison |
| `if condition { ... } else { ... }` | Branch on a Boolean condition |
| `for reading in readings { ... }` | Visit the readings |
| `println!("Limit: {limit}");` | Format and print using a macro |
| `#[test]` | Mark a function as a test |
| `assert!(condition)` | Fail the test if the condition is false |
| `assert_eq!(actual, expected)` | Fail the test unless the values compare equal |
| `!condition` | Boolean negation; distinct from the macro-name `!` |
| `pub`, `use`, `::` | Make an item available, bring a name into scope, and separate parts of a path |

## One ownership preview — Lessons 03–04

C++ programmers already know scope-based resource cleanup through RAII. Python programmers know that assigning an existing object to another name does not ordinarily make a deep copy. Neither analogy should be applied mechanically to Rust.

```rust
let original_label = String::from("sensor-ready");
let transferred_label = original_label;
println!("Label: {transferred_label}");
```

`String::from` creates owned text. Assigning this non-`Copy` value transfers ownership to `transferred_label`; Rust will not let you subsequently use `original_label` as though it still owned that text. This is a **move**, not an implicit deep copy. Small integer values in today's loop follow different copying rules. The details belong in the ownership lessons.

A borrowed value, written with `&`, lets another piece of code use a value without taking its ownership. `&mut` indicates exclusive mutable access under borrowing rules. Do not try to master those rules from this paragraph.

## Recognize these forms in later code

| Form | First reading | Planned lesson |
|---|---|---|
| `String`, `&str` | Owned text and a borrowed text view | 05 |
| `struct Reading { ... }` | A named group of fields | 06 |
| `enum DeviceState { ... }` | A value chosen from named alternatives, possibly carrying data | 06 |
| `match value { ... }` | Handle alternatives using patterns | 06 |
| `Option<Reading>` | A reading may be present or absent | 06 |
| `Result<Reading, ParseError>` | Success with a reading or failure with an error | 07 |
| `?` | Propagate an appropriate failure/absence in a compatible function | 07 |
| `impl Reading { ... }` | Define behavior associated with a type | 06, then 08–10 |
| `trait ReadingSource { ... }` | Describe behavior that implementations provide | 10 |
| `async fn`, `.await` | Describe suspendable work and wait without assuming a blocked thread | 22–23, then Embassy |

Angle brackets in `Option<Reading>` describe a type parameter. They are not the less-than and greater-than comparisons from the threshold function. Context matters; the dedicated lessons explain each form with a concrete task.

There is no requirement to use any of these optional features in the Lesson 00 exercise.

## Further reading

- [Rust Book: ownership](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [Rust Book: references and borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rust Book: enums and optional values](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
