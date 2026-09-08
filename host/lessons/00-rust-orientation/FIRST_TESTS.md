# Part 4 — Your first tests and the course files

[Lesson 00](README.md) · Previous: [Readings and control flow](READINGS_AND_CONTROL_FLOW.md) · Next: [Exercise](EXERCISE.md)

Continue in `practice/lesson-00/hello_rust/`, editing `src/main.rs`. Up to now, you have changed inputs and looked at printed output. A test lets the computer repeat a check and report a failure when the result is wrong.

## 1. Write tests in the same main file

There is no need to create a separate library just to write your first test. Here is the **entire file**, including the program from Part 3 and three tests below it.

**File — replace `src/main.rs`:**

<!-- walkthrough: first_tests -->
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

#[test]
fn includes_reading_above_limit() {
    assert!(is_above_limit(29, 25));
}

#[test]
fn excludes_reading_equal_to_limit() {
    assert!(!is_above_limit(25, 25));
}

#[test]
fn excludes_reading_below_limit() {
    assert!(!is_above_limit(22, 25));
}
```

Save the file. The program still prints `Readings above 25: 1` when you use `cargo run`.

Now run the tests instead:

```bash
cargo test
```

Cargo builds a test executable and runs the functions marked `#[test]`. You should see `running 3 tests` and a summary containing `3 passed; 0 failed`. The test order and timings can vary. You do not call these functions yourself from `main`, and an ordinary `cargo run` does not run them for you.

## 2. Read a test without treating its syntax as magic

`#[test]` is an **attribute**: an instruction attached to the function below it. Here it marks that function as a test. The `#` is not a comment character as it would be in Python. Rust line comments start with `//`.

`fn includes_reading_above_limit()` is an ordinary no-argument function declaration. We choose a name that describes the expected behavior, so a failure report tells us what stopped working.

`assert!(condition)` checks that its argument is `true`. If the condition is false, the test fails. In the first test, the condition is the answer from `is_above_limit(29, 25)`.

In the other tests, `!is_above_limit(...)` means **not** that answer. For example, if the function correctly returns `false` for equality, applying `!` produces `true`, and `assert!` passes.

These exclamation marks have different jobs. The `!` in the name `assert!` marks a macro call, like `println!`. The `!` placed before a Boolean expression negates it. We explain both because visually similar punctuation is not a substitute for understanding it.

A successful compiler check tells us that the program obeys the checked language rules. It does not tell us that the customer's intended comparison was `>` rather than `>=`. The tests express that behavioral requirement for selected inputs.

## 3. See a meaningful failure, then repair it

Temporarily change **only the comparison inside `is_above_limit`** from `reading > limit` to `reading >= limit`. Keep all three tests unchanged.

Save and run:

```bash
cargo check
cargo test
```

The compiler check succeeds: `>=` is perfectly valid Rust. The equality test fails: you should see `excludes_reading_equal_to_limit ... FAILED` and a summary with two passed and one failed. This is an intentional **behavioral bug** relative to the current strictly-above requirement, not a broken Rust installation.

Restore `reading > limit`, save, and rerun `cargo test`. All three tests should pass again. Do not remove the equality assertion to hide the failure.

**Try it:** Add a fourth test with negative inputs, using a descriptive name. Decide what `is_above_limit(-5, -5)` should return before writing the assertion. You already have all the syntax needed.

## 4. Now understand the supplied course example

Your own practice project has served its purpose: you created it, wrote functions in its main file, and tested them. The repository also has a supplied, working example so every learner has a reliable reference.

**Terminal — from `practice/lesson-00/hello_rust`, return to the repository root:**

```bash
cd ../../..
```

You should now see the repository's `README.md`, `rust-toolchain.toml`, and `host/` directory when you run `ls`. Enter the supplied lesson:

```bash
cd host/lessons/00-rust-orientation
cargo run
cargo test
```

The output is still `Readings above 25: 1`. This is the supplied example, **not your practice file**. Its tests include four library tests and an executable-output test, so its test count differs from your three-test practice program.

The relevant files are:

```text
00-rust-orientation/
├── Cargo.toml
├── src/
│   ├── main.rs
│   └── lib.rs
└── tests/
    └── program_output.rs
```

`src/main.rs` is the application entry point, just as before. `src/lib.rs` holds the reusable comparison function. It does not need a `main`: a library supplies code for other code to call, rather than being an executable on its own. `tests/program_output.rs` contains a supplied test that starts the executable and checks its printed result. You do not need to write process-launching code in this lesson.

Open [`src/lib.rs`](src/lib.rs). Its comparison function starts with `pub fn`. **`pub` means public**: it makes that function accessible to code outside its defining module, such as this package's executable.

Open [`src/main.rs`](src/main.rs). Its first line is:

```rust
use lesson_00_rust_orientation::is_above_limit;
```

Read that as “make the library's `is_above_limit` function available by this short name.” `::` separates parts of the path. The library name uses underscores in Rust code, while the Cargo package name uses hyphens. After the import, `main` can call the function in exactly the way your single-file program did.

The library's tests are grouped in `#[cfg(test)] mod tests { ... }`. `mod` groups code into a named module, and `#[cfg(test)]` includes that group for testing. Inside it, `use super::is_above_limit` refers to the function in the parent module. You have already written the underlying tests without that grouping; detailed module design comes later.

The lesson belongs to the `host/` **workspace**, a group of packages managed together. That is why its shared lockfile and build directory are under `host/`. Your practice package is separate and has its own. Neither arrangement is something you needed to design before Hello World.

## 5. What are the Make commands for?

A Makefile gives convenient names to shell commands. In this lesson directory, `make run` is a shortcut for running the supplied Cargo program, and `make test` runs its tests. Make is not required by Rust.

The repository often adds `--locked --offline` to Cargo commands. `--locked` prevents a build from changing the selected dependency versions; `--offline` avoids dependency-network access. Those checks are useful for supplied packages with committed lockfiles. We did not put them in front of the first `cargo new`/`cargo run` experience, where Cargo needs to create a new project's lockfile.

`make verify` also checks formatting and runs **Clippy**, Rust's lint tool for finding suspicious or unnecessarily awkward code. Formatting standardizes layout; linting is not a replacement for tests. The dedicated testing lessons will explain those tools more deeply.

**Important:** Root `make verify` checks complete course code and supplied solutions; it only compiles unfinished exercises. It does not claim that your exercise is finished. Inside an exercise package, its own `make verify` also runs that exercise's assertions. Always check your directory and the package name printed by the command.

## 6. Apply a new requirement in your own exercise

You are ready for **[EXERCISE.md](EXERCISE.md)**. A new requirement deliberately changes the rule to include equality. That exercise has its own source file and requirements; leave the strictly-above reference example intact.

You can also revisit the isolated compiler-error demonstrations from this lesson directory with `make errors`. The [fixture files](fixtures/compiler-errors/) are outside normal build targets; their repaired partners end in `_fixed.rs`. That is optional review, not another prerequisite before the exercise.

**Completion checkpoint:** Create a project, write Hello World, define a function with parameters and a return value, and test it without copying an unexplained library import. Then complete the inclusive-boundary exercise and explain the difference between valid Rust and correct behavior.

**Next: [Exercise — Include the boundary](EXERCISE.md).** Lesson 01 remains a later, separate implementation batch; it will build on this first practical use of Cargo rather than supply missing prerequisites.

### Optional references

[Rust Book: writing tests](https://doc.rust-lang.org/book/ch11-01-writing-tests.html), [packages and crates](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html), and [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html) document the distinctions introduced here.
