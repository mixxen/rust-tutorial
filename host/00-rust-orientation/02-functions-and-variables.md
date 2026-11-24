# Part 2. Functions and variables

[Lesson 00](README.md) · [Part 1. First program](01-first-program.md) · [Part 3. Readings and control flow](03-readings-and-control-flow.md)

Keep `src/main.rs` open in the `hello_rust` project from part 1. If your terminal reopened at the repository root, go back to your project. The default path is `practice/hello_rust`.

```bash
cd practice/hello_rust
```

Each example is a complete program. Replace `src/main.rs` in your editor, save the file, and run `cargo run` from `hello_rust/`.

## 1. Define a function and call it

In this version, `main` calls another function to print the greeting. Replace `src/main.rs` with the program below.

<!-- walkthrough: greeting_function -->
```rust
fn print_greeting() {
    println!("Hello from another function!");
}

fn main() {
    print_greeting();
}
```

Save the file and run this command.

```bash
cargo run
```

The program prints the greeting.

```text
Hello from another function!
```

`fn print_greeting() { ... }` defines what the function does. `print_greeting();` calls it. Rust runs the body of `print_greeting` when it reaches that call in `main`.

Rust convention uses lowercase words separated by underscores for function and variable names. The `!` after a name marks a macro call, as in `println!(...)`.

Rust starts at `main` even if you place `print_greeting` below it. You can define either function first.

## 2. Pass an input to a function

Give the function a reading to print. Replace `src/main.rs` with this program.

<!-- walkthrough: function_parameter -->
```rust
fn print_reading(reading: i32) {
    println!("Reading: {reading}");
}

fn main() {
    print_reading(25);
}
```

Save the file and run `cargo run`. The program prints the argument you passed.

```text
Reading: 25
```

`reading: i32` declares an input named `reading` with type `i32`. An `i32` is a signed 32-bit integer. It can hold negative and positive whole numbers, including zero.

The *parameter* is `reading: i32` in the definition. The *argument* is the value `25` in the call `print_reading(25)`. Rust checks that the argument fits the parameter's type.

Inside the string, `{reading}` is a placeholder. `println!` puts the value of `reading` there, much like a Python f-string.

Here's how each language starts the function definition.

| Language | Definition |
|---|---|
| C++ | `void print_reading(int reading) { ... }` |
| Python | `def print_reading(reading): ...` |
| Rust | `fn print_reading(reading: i32) { ... }` |

## 3. Return a value with `return`

`is_above_limit` returns an answer to `main`, and `main` prints it. Replace `src/main.rs` with this program.

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

Save the file and run `cargo run`. The program prints the result of comparing 29 with 25.

```text
Above limit: true
```

| Part of the function | Meaning |
|---|---|
| `fn` | Define a function. |
| `is_above_limit` | The function's name. |
| `(reading: i32, limit: i32)` | Two integer parameters separated by a comma. |
| `-> bool` | The arrow introduces the return type. A `bool` is either `true` or `false`. |
| `{ ... }` | The function body. |
| `return reading > limit;` | Compare the inputs and return the Boolean answer. |

Rust matches arguments to parameters by position. In `is_above_limit(29, 25)`, `reading` gets 29 and `limit` gets 25.

`let` introduces a *binding*, which gives a value a name. Here it gives the function's answer the name `reading_is_high`. Rust infers that the binding's type is `bool` from the return type of `is_above_limit`.

The comparison is strict. Calling `is_above_limit(25, 25)` would return `false`.

## 4. Return the final expression

An *expression* computes a value. The comparison `reading > limit` computes a Boolean. Rust can return that value directly when the comparison is the function body's final expression. Replace `src/main.rs` with this version.

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

Save the file and run `cargo run`. This version also prints `Above limit: true`.

| Function body ending | Result |
|---|---|
| `return reading > limit;` | `return` sends the Boolean back to the caller. |
| `reading > limit` | The final expression supplies the Boolean. |
| `reading > limit;` | The semicolon discards the Boolean. Rust reports a type error here. |

With the semicolon in the last row, the body yields `()`, which Rust calls *unit*. `print_greeting` returns unit. The signature of `is_above_limit` says it returns a `bool`, so the compiler rejects a body that yields `()`.

Use `return` when you need to leave a function early.

## 5. Let the counter change

This example keeps the limit fixed and updates the counter. Replace `src/main.rs` with the program below.

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

Save the file and run `cargo run`. The output shows the counter before and after the update.

```text
Limit: 25
Before: 0
After: 1
```

In `let limit: i32 = 25;`, `:` introduces the type and `=` sets the initial value.

Plain `let` makes a binding immutable. `let mut` makes it mutable, which allows you to assign it a new value. The counter needs `mut` so the program can add to it.

`qualifying_count += 1;` adds one to the counter. It's shorthand for `qualifying_count = qualifying_count + 1;`.

Rust can infer the type from `let limit = 25;` as well. It gives `limit` a fixed type at compile time.

[Part 3. Readings and control flow](03-readings-and-control-flow.md)

### Optional references

[Rust Book, functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html) · [Rust Book, variables and mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
