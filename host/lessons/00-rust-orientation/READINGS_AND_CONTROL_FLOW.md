# Part 3 — Build the readings example

[Lesson 00](README.md) · Previous: [Functions and variables](FUNCTIONS_AND_VARIABLES.md) · Next: [First tests](FIRST_TESTS.md)

Continue editing `practice/lesson-00/hello_rust/src/main.rs`. Run all commands in this part from `practice/lesson-00/hello_rust/`. If your terminal starts at the repository root, first run `cd practice/lesson-00/hello_rust`.

We will now use the function you understand to make a decision, then repeat that decision for several readings. We are still using one source file and no external libraries.

## 1. Use a Boolean result in an if statement

**File — replace all of `src/main.rs`:**

<!-- walkthrough: condition -->
```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

fn main() {
    let reading = 29;
    let limit = 25;

    if is_above_limit(reading, limit) {
        println!("Reading qualifies.");
    } else {
        println!("Reading does not qualify.");
    }
}
```

Save and run `cargo run`. Expected output:

```text
Reading qualifies.
```

The function returns `true`, so Rust executes the first block. If it returned `false`, Rust would execute the `else` block instead. Both blocks are surrounded by braces. There is no Python-style colon after the condition, and unlike conventional C++ syntax you do not need parentheses around it.

The condition must be a `bool`. Rust does not treat an arbitrary integer as a truth value: `if reading` is not a substitute for writing the question you mean. To ask whether a number is nonzero, write `if reading != 0`.

**Try it:** Change `reading` to 25, save, and rerun. Equality does not qualify under a strictly-above rule, so the other message should appear. Then try 22. You have checked an above, equal, and below case without changing the function.

## 2. Use an array and a loop

A device has supplied four readings: 18, 22, 25, and 29. With a limit of 25, how many readings are strictly above the limit? Predict the answer before running the next program.

**File — replace all of `src/main.rs`:**

<!-- walkthrough: count_readings -->
```rust
fn is_above_limit(reading: i32, limit: i32) -> bool {
    reading > limit
}

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

Save and run `cargo run`. Expected output:

```text
Readings above 25: 1
```

`[18, 22, 25, 29]` creates an **array**: four values of one element type, with a fixed length. The square brackets here are array syntax, not a function call. These integers are used with the function's `i32` parameters, so Rust can infer their type.

`for reading in readings` visits each array element. The plural name `readings` refers to the collection; the singular name `reading` refers to the current value. There is no loop index to maintain in this example.

The outer pair of braces belongs to the loop. The inner pair belongs to the condition. `qualifying_count` uses `mut` because it is updated. Neither the array binding nor the limit needs to be reassigned.

Trace the program without looking at the output:

| Current reading | Is it greater than 25? | Count after this iteration |
|---|---|---|
| 18 | No | 0 |
| 22 | No | 0 |
| 25 | No: equal is not greater | 0 |
| 29 | Yes | 1 |

The final `println!` inserts the named values into the text. It runs after the loop, not once for every reading. Notice which closing brace ends the `if`, which ends the `for`, and which ends `main`.

**Try it:** Replace the array with `[25, 26, 27, 28]`. Predict the new count, save, and run. The answer should be 3, not 4. Restore `[18, 22, 25, 29]` afterward so the next part starts from the documented example.

## 3. Connect this to C++ and Python

The algorithm is unchanged: start a count at zero, visit each reading, compare it, and increment when it qualifies. The important differences here are the spelling and the rules for local variables and function signatures.

| Familiar concept | Rust in this program |
|---|---|
| Define a function | `fn is_above_limit(...) -> bool { ... }` |
| Declare an integer input | `reading: i32`, with the type after the name |
| Declare a local | `let limit = 25;` |
| Declare a local that changes | `let mut qualifying_count = 0;` |
| Loop over values | `for reading in readings { ... }` |
| Branch on a comparison | `if is_above_limit(reading, limit) { ... }` |
| Print formatted text | `println!("Readings above {limit}: {qualifying_count}");` |

The [full C++ and Python versions](COMPARISON.md) perform the same task. Reading them is optional; you do not need a C++ compiler installed to complete the Rust lesson. Their numeric types are not equivalent for every possible input: Python's integers are not limited to `i32`, and C++ `int` is not universally a 32-bit type.

Two familiar assumptions to leave behind: omitting a type annotation does not make a Rust variable dynamically typed, and an integer is not automatically a Boolean condition. We will explore ownership differences later rather than trying to learn them all here.

## 4. Keep the small program understandable

At this point, all of the actual behavior is visible in one file. The decision lives in a named function; the loop lives in `main`. We have not needed an object hierarchy, shared helper framework, iterator chain, or async task.

A larger project may organize functions in several files. That is a separate concern from understanding a function call. We will make that transition at the end of the next part, after you have also written a test in this same file.

**Checkpoint:** Explain why the count is 1, why it needs `mut`, and what would change if the requirement included equality. Make one prediction about a different array and verify it before continuing.

**Next: [Part 4 — Your first tests and the course files](FIRST_TESTS.md).**

### Optional references

[Rust Book: data types and arrays](https://doc.rust-lang.org/book/ch03-02-data-types.html) and [control flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html) explain the language rules used here. The loop trace and sample outputs above are specific to this lesson's inputs.
