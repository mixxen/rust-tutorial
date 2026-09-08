# Lesson 00 — A first look at Rust

**Goal:** Read a small Rust program, change a requirement, and use tests to check your change. You already know how to program; here we focus on how Rust expresses familiar ideas.

**Before you start:** Complete one [setup path](../../../README.md#start-learning). No board, previous Rust lesson, or AI coding tool is required. Allow roughly 45–60 minutes after setup, but stop and experiment whenever something is unclear.

The full ownership rules come later. Today, you only need a few integers, an array, a function, and a loop.

## 1. The same task in a familiar setting

A device has reported four readings: **18, 22, 25, 29**. We want to count readings **strictly above 25**. Before running anything, write down which readings qualify. Does the reading equal to 25 belong in the count?

The decision is familiar in all three languages:

**C++**

```cpp
bool is_above_limit(int reading, int limit) {
    return reading > limit;
}
```

**Python**

```python
def is_above_limit(reading: int, limit: int) -> bool:
    return reading > limit
```

**Rust** — from [`src/lib.rs`](src/lib.rs):

```rust
pub fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}
```

The comparison has not changed. Rust puts parameter types after the names, uses `fn` for a function, and puts the return type after `->`. `i32` is a signed 32-bit integer; `bool` is either `true` or `false`. The final comparison supplies the result without an explicit `return`.

`pub` makes the function available to the executable and tests outside this file's module. You do not need to design a module hierarchy yet; that small boundary is supplied. The [full C++ and Python programs](COMPARISON.md) use the same sample data and loop structure. Their types are not identical for every possible input: Python integers are not restricted to Rust's `i32` range, and C++ `int` is not universally a 32-bit type.

## 2. Run the worked example

From the **repository root**:

```bash
cd host/lessons/00-rust-orientation
make run
```

The Cargo equivalent, from that same lesson directory, is:

```bash
cargo run --locked --offline
```

`--locked` prevents Cargo from changing the selected dependency versions. `--offline` avoids dependency network access; it does not install a missing compiler. For this lesson, there are no external Rust crates to download.

The program's output is:

```text
Readings above 25: 1
```

Only 29 qualifies. Cargo and Make also print build or command information; those lines are not part of the program's output.

## 3. Read the program without guessing at punctuation

Here is [`src/main.rs`](src/main.rs), the executable's starting point:

```rust
use lesson_00_rust_orientation::is_above_limit;

fn main() {
    let readings = [18, 22, 25, 29];
    let limit = 25;
    let mut qualifying_count = 0;

    for reading in readings {
        if is_above_limit(reading, limit) {
            qualifying_count += 1;
        }
    }

    println!("Readings above {limit}: {qualifying_count}");
}
```

Read it from top to bottom. The `use` line makes the library function's name available here. Cargo's package name contains hyphens, while the Rust library path uses underscores. `::` separates parts of a Rust path. These are supplied package connections; Lesson 01 will explain the tools and files more fully.

`main` is where this executable starts. `readings` is a fixed-size array of four integers. `for reading in readings` visits each reading, and the `if` body runs only when the function returns `true`. `println!` writes a line to the terminal, inserting the two named values in the string. The `!` marks a **macro**, a form of code expansion; using this supplied output macro does not require learning to write macros today.

### New syntax in this example

| Rust | Read it as |
|---|---|
| `fn main()` | Define the executable's starting function |
| `let limit = 25;` | Bind the name `limit` to an inferred integer value |
| `let mut qualifying_count = 0;` | This binding may be changed later |
| `reading: i32` | This parameter must have the declared integer type |
| `-> bool` | The function returns a Boolean |
| `{ ... }` | A block of code, not Python indentation-based grouping |
| `reading > limit` at the end of the function | Use this expression's value as the function result |
| `println!(...)` | Format and print a line using the supplied macro |

An **expression** produces a value. You already use them in other languages: `reading > limit` produces a Boolean. Rust also allows a whole block or an `if`/`else` to produce a value. A **binding** is the association between a name and its value; for these simple numbers, you can initially think of it as a variable declaration.

## 4. Three familiar-looking things with different rules

### A. Type inference is not dynamic typing

Rust infers the types of `readings` and `limit` from their use. The function's `i32` parameters constrain those values. You can also write `let limit: i32 = 25;` explicitly.

This resembles C++ `auto` more than Python's ordinary assignment: Rust still checks the type at compile time. An assignment of text into this same integer binding does not become valid because you left out the annotation. Python type hints, by themselves, do not impose this kind of runtime enforcement.

### B. Mutability is a deliberate choice

We change `qualifying_count`, so it uses `let mut`. We do not change `limit`, so it uses plain `let`. Removing `mut` from the counter makes the later increment invalid.

Rust also permits **shadowing**: a new `let` can introduce another binding with the same name. That is not the same operation as assigning a new value to an existing mutable binding. For example:

```rust
let limit = 25;
let limit = limit + 5;
```

The second line creates a new binding whose value is 30. This is sometimes useful, but choosing distinct names is often clearer when the values mean different things. Also, an immutable binding is not a promise that every value reachable through it can never change; later lessons explain controlled interior mutation.

### C. A semicolon can discard a result

Our function finishes with `reading > limit`, without a semicolon. Adding a semicolon makes that final comparison a statement whose result is discarded. The function body then provides `()`, called the **unit value**, rather than its promised `bool`.

Do not memorize this as “Rust never uses return.” An explicit `return reading > limit;` is valid too. The tail-expression form is simply the direct form used here.

One more difference: a Rust `if` condition must be a Boolean. `if reading` is not valid merely because the number is nonzero. Write the intended question, such as `if reading != 0`. C++ and Python permit broader truth tests; Rust asks you to make this one explicit.

## 5. Learn from a compiler error without breaking your package

Three deliberately invalid standalone files live in [`fixtures/compiler-errors/`](fixtures/compiler-errors/). They are outside Cargo's normal source targets. Each has a repaired partner.

From this lesson directory, inspect one error using a temporary output location:

```bash
scratch_directory=$(mktemp -d)
rustc --edition=2024 fixtures/compiler-errors/immutable_binding.rs -o "$scratch_directory/example"
```

This command is **expected to fail**. Look for `E0384` and the message about assigning to an immutable variable. Read the highlighted source line before looking for a fix. A missing `rustc` is a setup problem, not this intended demonstration.

Now build and run the repair:

```bash
rustc --edition=2024 fixtures/compiler-errors/immutable_binding_fixed.rs -o "$scratch_directory/example"
"$scratch_directory/example"
rm -r "$scratch_directory"
```

Expected output:

```text
Before: 0
After: 1
```

Try the integer-condition and tail-semicolon examples the same way. Both have a type mismatch (`E0308`), but for different reasons. The file names ending in `_fixed.rs` contain the repairs. To automatically check all three failures and their repairs:

```bash
make errors
```

This author-provided check requires the intended error code, then compiles and runs the repair. It does not treat every nonzero exit as success. These isolated files are not invitations to suppress warnings in working code.

## 6. Run a test and read what it proves

Back in the lesson directory:

```bash
make test
```

Equivalent:

```bash
cargo test --locked --offline
```

The library contains tests like this:

```rust
#[test]
fn excludes_reading_equal_to_limit() {
    assert!(!is_above_limit(25, 25));
}
```

`#[test]` tells the test runner to execute this function. `assert!` fails if its argument is false. The `!` before a Boolean expression means **not**; it is separate from the `!` in the macro name `assert!`. Here, the assertion checks that equality does **not** qualify under the original rule.

The tests sit in a supplied `#[cfg(test)] mod tests` block. This says “include this module for testing.” Its `use super::is_above_limit` line brings in the function from the parent module. You can use that structure now; test organization gets a full lesson later.

There is also a supplied executable-output test in [`tests/program_output.rs`](tests/program_output.rs). It checks the printed count. Process-launching details are not required for this lesson.

A passing test establishes the behavior of the checked cases. It does not prove every possible property of the program. In particular, the compiler cannot tell whether your customer asked for “above” or “at or above.” That is the next exercise.

## 7. Change the requirement yourself

Open **[EXERCISE.md](EXERCISE.md)**. The exercise changes the rule to include equality. You will work in a separate package, preserve the working example, and add your own boundary tests.

The intended sequence is: predict, edit, test, and explain. Try that before asking an AI tool to solve it. The [hints](HINTS.md) and [explained solution](SOLUTION.md) are available when needed.

The [syntax reference](CHEATSHEET.md) also previews symbols you may have seen in generated Rust. Most of those are **not** required in this lesson.

## 8. Check your understanding

Before leaving, explain these in your own words:

1. Why does `qualifying_count` need `mut`, but `limit` does not?
2. Why is `let limit = 25;` not evidence that Rust uses Python-style dynamic typing?
3. What changes when a semicolon is added to the function's last expression?
4. How can a program compile successfully and still fail the exercise tests?

Then write a small `is_below_limit` function from memory in your exercise's own test file or scratch program. Test the equal case before running it. Explaining that boundary is more valuable than typing the syntax quickly.

**Next:** Lesson 01 will unpack Cargo and create a package from scratch. It is still planned in this first batch; see [Progress](../../../PROGRESS.md). You do not need to complete any advanced material to finish this lesson.

## References and further reading

These sources support the language and tool behavior discussed above; they are optional reading, not prerequisites.

- [Rust Book: variables and mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [Rust Book: functions, expressions, and return values](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [Rust Book: control flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [Cargo: running tests](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [Python: typing and runtime enforcement](https://docs.python.org/3/library/typing.html)
