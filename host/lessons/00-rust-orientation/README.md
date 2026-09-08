# Lesson 00 — Write your first Rust program

You already know how to program. **You do not need to know anything about Rust, Cargo, Rust file layouts, or Rust function syntax to begin this lesson.** We will introduce those things before asking you to use them.

We start with an empty project and `Hello, world!`, not a library import or a completed application. You will create a project, open its source file, change it, save it, and run it. Then we will build up to the readings example and its tests.

## Follow these four parts in order

| Part | What you will actually do |
|---|---|
| **[1 — Cargo, files, and Hello World](FIRST_PROGRAM.md)** | Learn what the tools do, create a project, find `src/main.rs`, understand every symbol in Hello World, and run your own change. |
| **[2 — Functions and variables](FUNCTIONS_AND_VARIABLES.md)** | Define and call functions, pass an integer, return a result, and introduce `let` and `mut` one step at a time. |
| **[3 — Build the readings example](READINGS_AND_CONTROL_FLOW.md)** | Add a condition, an array, and a loop, then relate the finished program to C++ and Python. |
| **[4 — Your first tests and the course files](FIRST_TESTS.md)** | Write a test in the same file, see a meaningful failure, and only then learn why the supplied course example has a library and a separate exercise. |

Treat these as four sittings if that helps. There is no need to squeeze all of this into the previous short orientation session. Each part ends at a useful stopping point. Lesson 01 will deepen Cargo and project organization; it is **not** a prerequisite for this lesson.

## How to use the walkthrough

Commands labeled **Terminal** go in your Linux, WSL, or development-container terminal. Code labeled **File** goes in your editor. Output blocks show what to expect; do not type them as commands. When a step says **replace the file**, replace its entire contents rather than adding a second `main` function below the first.

Use any plain-text code editor. VS Code is convenient, but no editor extension is required to understand or run the programs. Save the file before returning to the terminal. The lesson always identifies the working directory and the file to edit.

Most of the walkthrough takes place in **your own practice project** at `practice/lesson-00/hello_rust/`. It is separate from the supplied lesson, exercise, and solution. The `practice/` directory is ignored by Git and by course checks, so experiments there do not change the teaching examples. Do not put valuable work there without arranging your own backup.

Do not start by running every Make command or opening the solution. Start with **[Part 1](FIRST_PROGRAM.md)**. It explains Cargo before sending you to the setup instructions, and uses ordinary Cargo commands before introducing Make shortcuts.

## Before moving on

By the end, you should be able to create a new project and write this from memory, explaining the function, parentheses, braces, output line, and semicolon:

```rust
fn main() {
    println!("Hello, world!");
}
```

You should also be able to explain which tool builds the program, where your source file lives, how to call a function with an argument, and why passing a compiler check is different from passing a behavioral test.

## Supporting material — not prerequisites

The [exercise](EXERCISE.md), [hints](HINTS.md), and [solution](SOLUTION.md) come after Part 4. The [C++/Python comparison](COMPARISON.md) and [syntax reference](CHEATSHEET.md) are references, not a list of things you must already understand. In particular, ownership, borrowing, lifetimes, and async syntax are later topics.

The [walkthrough source copies](walkthrough/README.md) let you compare your work with each complete step. Automated checks create a temporary Cargo project and run those steps; they never overwrite your practice project. See [Progress](../../../PROGRESS.md) for actual verification results and known limitations.

**Start: [Part 1 — Cargo, files, and Hello World](FIRST_PROGRAM.md).**
