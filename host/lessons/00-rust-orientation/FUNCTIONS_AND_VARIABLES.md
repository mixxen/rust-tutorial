# Part 2 — Functions and variables, one step at a time

[Lesson 00](README.md) · Previous: [First program](FIRST_PROGRAM.md) · Next: [Readings and control flow](READINGS_AND_CONTROL_FLOW.md)

Continue in `practice/lesson-00/hello_rust/`, with its `src/main.rs` open. If you reopened your terminal at the repository root, reach the project with:

```bash
cd practice/lesson-00/hello_rust
```

For each complete program below, **replace all of `src/main.rs`, save, and run `cargo run` from this project**. We are still using one source file. Do not put a Rust function definition into the terminal.

## 1. Define a function and call it

In Part 1, Rust started your application at `main`. You can define other functions and ask `main` to call them.

**File — replace `src/main.rs`:**

<!-- walkthrough: greeting_function -->
```rust
fn print_greeting() {
    println!("Hello from another function!");
}

fn main() {
    print_greeting();
}
```

**Terminal:**

```bash
cargo run
```

**Program output:**

```text
Hello from another function!
```

`fn print_greeting() { ... }` **defines** the function. `print_greeting();` **calls** it. Do not include `fn` at a call site. Defining a function does not run its body immediately; `main` calls it when the program runs.

We chose the name `print_greeting` to say what it does. Rust convention uses lowercase words separated by underscores for functions and variables. Ordinary functions are called without an exclamation mark; `println!` has one because it is a macro.

The order of these two definitions is not their execution order. Rust starts this application at `main`. You could place `print_greeting` below `main` without a C++-style forward declaration.

**Try it:** Call `print_greeting();` twice inside `main`. Predict the output, save, and run. Then restore the single call before continuing.

## 2. Pass an input to a function

Now give a function a reading to print. We will use an integer to avoid introducing Rust's string types yet.

**File — replace `src/main.rs`:**

<!-- walkthrough: function_parameter -->
```rust
fn print_reading(reading: i32) {
    println!("Reading: {reading}");
}

fn main() {
    print_reading(25);
}
```

Run `cargo run`. Expected output:

```text
Reading: 25
```

Read `reading: i32` as “an input named reading, whose type is i32.” An `i32` is a signed 32-bit integer, so it can represent negative as well as positive whole numbers. It is not a decimal number or text.

The **parameter** is the name and type in the definition: `reading: i32`. The **argument** is the actual value at the call: `25`. At the call site, write `print_reading(25)`, not `print_reading(reading: 25)` and not `print_reading(25: i32)`.

Inside the print string, `{reading}` means “insert the value named reading here.” Those braces are a formatting placeholder, not a Rust code block. You do not put `$` before the name. This is similar in purpose to Python's formatted strings, but the Rust spelling is different.

Compare just the signatures:

| Language | Definition |
|---|---|
| C++ | `void print_reading(int reading) { ... }` |
| Python | `def print_reading(reading): ...` |
| Rust | `fn print_reading(reading: i32) { ... }` |

Rust puts the type after the parameter name. The comparison is about the function's role, not a guarantee that C++ `int` always has Rust's `i32` range.

**Try it:** Add `print_reading(-5);` after the first call. You should see a second line, `Reading: -5`.

## 3. Return a result — start with explicit return

Printing is an action. Returning gives a value back to the caller, which can choose what to do with it. Let's ask whether a reading is strictly above a limit.

**File — replace `src/main.rs`:**

<!-- walkthrough: explicit_return -->
```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    return reading > limit;
}

fn main() {
    let reading_is_high = is_above_limit(29, 25);
    println!("Above limit: {reading_is_high}");
}
```

Run `cargo run`. Expected output:

```text
Above limit: true
```

Here is the signature without any unexplained pieces:

| Piece | Meaning |
|---|---|
| `fn` | Define a function. |
| `is_above_limit` | Its name; it asks a yes/no question. |
| `(reading: i32, limit: i32)` | Two inputs, each with an integer type; the comma separates them. |
| `-> bool` | The result has type `bool`: either `true` or `false`. The arrow describes the return type, not an operation to execute. |
| `{ ... }` | The function body. |
| `return reading > limit;` | Compare the inputs and return the Boolean answer. |

At `is_above_limit(29, 25)`, arguments match parameters by position: `reading` gets 29 and `limit` gets 25. Swapping them asks a different question.

`let reading_is_high = ...;` introduces a variable and gives it the function's answer. Here, `let` is roughly “declare this local name.” Rust also calls this introducing a *binding*: associating a name with a value. We do not need to write its type because Rust can infer `bool` from the function's return type.

C++ might express the declaration as `bool reading_is_high = is_above_limit(29, 25);`; Python might use `reading_is_high = is_above_limit(29, 25)`. Rust uses `let` for the declaration and still checks the type before running the program.

**Try it:** Change the first argument from 29 to 25. Does equality count as strictly above? Predict `false`, then verify it. Restore 29 before the next step.

## 4. Rust's other return spelling: a final expression

The explicit `return` form is valid Rust. You will also see functions return the value of their final expression, without writing `return`. An **expression** computes a value; `reading > limit` computes a Boolean.

Replace the whole file with this version, which produces the same output:

<!-- walkthrough: tail_return -->
```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let reading_is_high = is_above_limit(29, 25);
    println!("Above limit: {reading_is_high}");
}
```

Run `cargo run` and confirm `Above limit: true` again.

The missing semicolon on `reading > limit` is intentional. In this position, the expression's value becomes the function result. The caller sees the same answer as it did with `return reading > limit;`.

For this example, these are the important distinctions:

| Function body ending | Result |
|---|---|
| `return reading > limit;` | Explicitly return the comparison's value. Valid. |
| `reading > limit` | Use the final expression's value as the result. Valid. |
| `reading > limit;` | Discard the comparison's value. With no other return, this body does not provide its promised Boolean. Invalid here. |

A body that falls through without a result provides Rust's empty result, written `()` and called *unit*. That was fine for `print_greeting`, but it does not match `-> bool`.

**Try one compiler error:** Add the semicolon after `reading > limit`, save, and run `cargo check`. This is expected to fail. Look for the function's `-> bool` and the message about expected `bool` versus `()`. The line numbers and exact wording may vary. Remove the semicolon, save, and run `cargo check` again; it should succeed.

You do not need to avoid the `return` keyword. Explicit returns are useful, especially for leaving a function early. We introduced that familiar spelling first, then the common final-expression form so neither is mysterious.

## 5. Declare variables, then choose which may change

Let's isolate `let` and `mut` in a small complete program before combining them with a loop.

**File — replace `src/main.rs`:**

<!-- walkthrough: mutable_counter -->
```rust
fn main() {
    let limit: i32 = 25;
    let mut qualifying_count: i32 = 0;

    println!("Limit: {limit}");
    println!("Before: {qualifying_count}");

    qualifying_count += 1;

    println!("After: {qualifying_count}");
}
```

Run `cargo run`. Expected output:

```text
Limit: 25
Before: 0
After: 1
```

The declarations put a name on the left of `:` and its type on the right. `=` supplies the initial value. `let limit: i32 = 25;` declares an integer named `limit` and initializes it to 25.

Plain `let` does not permit assigning a new value to the same binding later. `mut` means **mutable**: this variable can be updated. We update the counter, so it needs `mut`. We never update `limit`, so it does not.

`qualifying_count += 1;` adds one to the existing counter. It does not create another variable. You could spell the same operation as `qualifying_count = qualifying_count + 1;`.

The type annotations make the lesson explicit; for these values Rust can infer them, so `let limit = 25;` is also a common spelling. Type inference does not turn Rust into a dynamically typed language. Leaving out `: i32` does not allow the same integer variable to accept arbitrary text later.

**Try it:** Remove `mut`, save, and run `cargo check`. You should get an error about assigning to an immutable variable. Put `mut` back and confirm that the program runs again. This is different from Python, where ordinary assignment does not require a separate mutability declaration.

A later lesson explains shadowing with another `let`. Do not use shadowing to avoid understanding why this counter needs to change.

## Checkpoint

Create a second small function named `is_below_limit` in your practice file. It should take a reading and a limit and return a Boolean. Call it from `main` and print its answer. Start with explicit `return` if that feels clearer; then try the final-expression spelling.

Before running it, explain where the parameter types go, where the return type goes, and what equality should do. You have now practiced defining a function, calling it, using its result, and interpreting two compiler errors.

**Next: [Part 3 — Build the readings example](READINGS_AND_CONTROL_FLOW.md).** We will replace the practice file again, so leaving your checkpoint function there is fine.

### Optional references

[Rust Book: functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html) and [variables and mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html) document the syntax used here. The explicit-return step is intentionally a bridge from familiar C++/Python syntax, not a claim that it is always Rust's preferred style.
