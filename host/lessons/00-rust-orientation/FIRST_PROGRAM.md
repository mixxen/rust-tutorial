# Part 1 — Cargo, files, and Hello World

[Lesson 00](README.md) · Next: [Functions and variables](FUNCTIONS_AND_VARIABLES.md)

Our first goal is small: create a Rust program yourself, understand its three lines, and change what it prints. No libraries, test framework, or embedded board yet.

## 1. What are Rust, rustc, rustup, and Cargo?

**Rust** is the language you write. A file containing Rust source code ends in `.rs`, just as a Python source file commonly ends in `.py`.

**`rustc`** is the Rust compiler. It translates Rust source into an executable program for your machine. Its role is similar to a C++ compiler such as `g++` or `clang++`.

**Cargo** is the usual command-line tool for working on Rust projects. It creates the initial files, asks `rustc` to compile them, runs your program, and runs tests. Later, it also manages the external libraries your project uses. Those libraries are called *dependencies*. Cargo coordinates the work; it is not another programming language or an editor.

**`rustup`** installs and selects versions of Rust's tools. A particular compiler release and its companion tools are often called a *toolchain*. You use rustup for setup; most of your everyday commands will start with `cargo`.

For a C++ programmer, Cargo brings several build and dependency-management tasks behind one interface. For a Python programmer, some of its jobs resemble a combination of project setup, package management, and test commands. Neither comparison is exact: Rust is compiled before its executable runs.

Keep this picture in mind:

```text
You edit and save src/main.rs
             |
             v
         cargo run
             |
             v
Cargo asks rustc to build the program when needed
             |
             v
Cargo starts the executable; it prints to your terminal
```

You do not need Make to write Rust. This repository also supplies Make shortcuts, but we will introduce them after you understand the Cargo commands they call.

## 2. Confirm that the tools are available

Complete one setup path if you have not already done so: [Linux](../../../docs/setup-linux.md), [Windows with WSL](../../../docs/setup-wsl.md), or [Docker](../../../docs/docker.md). Then return here. Setup installs the tools; this walkthrough teaches how to use them.

**Terminal — open at the tutorial repository root**, the directory containing `README.md`, `rust-toolchain.toml`, and `host/`:

```bash
pwd
ls
rustc --version
cargo --version
```

`pwd` shows your current directory; `ls` lists its contents. Both version commands should print a version, not `command not found`. This repository selects Rust **1.90.0**. It deliberately uses a recorded version rather than silently switching whenever a new version is released.

On WSL, use the Linux terminal. In Docker, run the lesson commands inside the interactive container, where the repository is mounted at `/workspace`. Do not switch between a host shell and container shell halfway through the commands without checking your directory.

## 3. Ask Cargo to create the project

**Terminal — still at the repository root:**

```bash
mkdir -p practice/lesson-00
cargo new practice/lesson-00/hello_rust --bin --edition 2024 --vcs none
cd practice/lesson-00/hello_rust
```

The first command creates the practice parent directories. The second creates a new Cargo project called `hello_rust`. The third moves your terminal into it.

The options are explicit so you can see our choices: `--bin` asks for an application you can run, `--edition 2024` selects the language edition used by this course, and `--vcs none` avoids creating another version-control repository inside your practice directory. The edition is a compatibility setting, not the compiler's version number. Cargo already defaults to an application; the option simply makes our intent clear.

**Run `cargo new` only once.** If the directory already exists from an earlier attempt, inspect it and continue with that project; do not delete it to make a command succeed.

A Cargo *package* is the project unit described by one `Cargo.toml` file. Our small project contains one runnable program. That is all the package vocabulary you need today.

## 4. Find the main file — Cargo made it for you

Your new project starts like this:

```text
hello_rust/
├── Cargo.toml
└── src/
    └── main.rs
```

`Cargo.toml` describes the package. `src` is a directory for source code. **`src/main.rs` is the source file you will edit.** Cargo uses this conventional location for the application's starting file; you do not need to list it manually in the configuration.

In your editor, expand `practice`, then `lesson-00`, then `hello_rust`, then `src`, and open `main.rs`. You can also open the `hello_rust` folder itself in the editor. If VS Code's `code` command is available, `code .` from the current terminal opens this project, but that command is optional.

Cargo has already put a minimal program in the file. Delete its contents and type the following yourself to make the structure familiar. This is the **entire file**, not code to paste below another function.

**File — `practice/lesson-00/hello_rust/src/main.rs`:**

<!-- walkthrough: hello_world -->
```rust
fn main() {
    println!("Hello, world!");
}
```

Save the file. Its name must be `main.rs`, not `main.rs.txt`. In an editor's New File dialog, this is an ordinary text file; it does not need a special Rust document type.

## 5. Understand every symbol before running it

Read `fn main() {` as “define a function named main, with no arguments, and begin its body.”

| Piece | Meaning here |
|---|---|
| `fn` | The Rust keyword for defining a function. Compare Python's `def`; C++ uses a return type before the function name. |
| `main` | The conventional starting function for this ordinary executable. |
| `()` after `main` | An empty parameter list: this function takes no inputs. |
| `{` and `}` | The beginning and end of the function body. Indentation makes it readable, but braces group the code. |
| `println!` | Rust's built-in way to format and print a line of text, including a newline at the end. |
| `!` in `println!` | Marks a macro call rather than an ordinary function call. A macro expands into code during compilation. You only need to use this one, not write macros. |
| `("Hello, world!")` | The text passed to the print operation. Double quotes delimit the string; they are not printed. |
| `;` after the print call | Finishes this statement. It is part of the Rust source, not a shell command. |

Notice the two exclamation marks on the output line. The one in `println!` is Rust syntax. The one **inside the quotes**, after `world`, is just a character to print.

You do not need a C++-style `#include` to use `println!` in this ordinary Rust program. There is no `pub`, `use`, or separate library file in your program yet.

## 6. Build and run it

**Terminal — in `practice/lesson-00/hello_rust`:**

```bash
cargo run
```

Cargo builds the executable and starts it. **Your program's output** is:

```text
Hello, world!
```

Cargo also prints progress lines such as `Compiling`, `Finished`, and `Running`. Those are tool messages, not text from your program. Paths and timings in those lines vary by machine.

Do not type `cargo run main.rs` or `python main.rs`. Cargo finds `src/main.rs` through the project layout. The command runs from the directory containing this project's `Cargo.toml`.

After the first build, the project also has `Cargo.lock` and `target/`. The lockfile records selected package versions. `target/` holds generated build output, including the executable. Edit files in `src/`, not files in `target/`.

## 7. Make a change and see it happen

Replace the **whole contents** of `src/main.rs` with:

<!-- walkthrough: changed_message -->
```rust
fn main() {
    println!("I wrote this Rust program.");
    println!("Now I can change it and run it again.");
}
```

Save, then run `cargo run` again from the same terminal directory. Expected program output:

```text
I wrote this Rust program.
Now I can change it and run it again.
```

Now write your own message inside the first pair of quotes and rerun it. If you still see the old message, first check that you saved the correct `src/main.rs` and that your terminal is in **this** project, not the course's worked example.

Your basic working cycle is **edit → save → run → inspect**. Cargo handles rebuilding changed code; you do not rerun `cargo new` for every change.

## 8. What do the other basic Cargo commands do?

Try these in the same project:

```bash
cargo check
cargo build
cargo run
```

`cargo check` checks the code without producing the final executable. It is useful while editing. `cargo build` creates the executable but does not start it. `cargo run` builds as needed and starts it. None of these commands edits your source code.

On the Linux/WSL/container path, you can also run the program built by `cargo build` directly:

```bash
./target/debug/hello_rust
```

`./` means “from this directory.” `debug` is the ordinary development-build directory. If you edit the source and run this executable directly **without rebuilding**, you will still run the old executable. That is one reason to use `cargo run` while learning.

Open `Cargo.toml` once to see what it describes:

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2024"

[dependencies]
```

These are configuration settings, not Rust statements. The package has a name, its own version, and a language edition. The empty dependencies section means we have not requested external libraries. Cargo may add comments or other harmless defaults; do not replace your file just to make it visually identical.

## Optional: create a main file without Cargo

This answers a useful question: is `main.rs` a special file that only Cargo can create? **No.** You can create it yourself and ask the compiler to build it. This detour is optional; our normal path continues to use Cargo.

Starting from `practice/lesson-00/hello_rust`, create a neighboring directory:

```bash
cd ..
mkdir manual_hello
cd manual_hello
```

In your editor, create a new text file named `main.rs` in `practice/lesson-00/manual_hello/`. Type and save this entire file:

```rust
fn main() {
    println!("Hello, world!");
}
```

**Terminal — in `practice/lesson-00/manual_hello`:**

```bash
rustc --edition=2024 main.rs -o hello_rust
./hello_rust
```

The first command compiles your file into an executable named `hello_rust`; `-o` names that output. The second runs it and prints `Hello, world!`. There is no `Cargo.toml` here because we are invoking the compiler directly.

Return to your Cargo project before the next part:

```bash
cd ../hello_rust
```

## When something goes wrong

| Symptom | First thing to check |
|---|---|
| `cargo: command not found` | Return to setup; the tool is not available in this terminal. |
| Cargo cannot find `Cargo.toml` | Run `pwd` and `ls`. For this part, your directory should end in `practice/lesson-00/hello_rust`. |
| `cargo new` says the destination exists | Open the existing project and continue; do not recreate or overwrite it. |
| An error mentions `main` defined more than once | A complete example was probably appended instead of replacing the previous file. Keep one `fn main`. |
| An error points at a quote, bracket, or line number | Compare the file with the small complete example. The message is about source code, not package setup. |
| The printed text does not change | Save the file, check which project you are in, and use `cargo run` instead of an old executable. |

**Checkpoint:** Without looking at the table, explain what Cargo does, where your main file is, and what `fn main()` means. Change one printed line and run it again. That is enough for this part.

**Next: [Part 2 — Functions and variables](FUNCTIONS_AND_VARIABLES.md). Leave your terminal in the `hello_rust` project.**

### Optional references

[Rust Book: Hello World](https://doc.rust-lang.org/book/ch01-02-hello-world.html), [Hello Cargo](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html), and [Cargo's project-creation command](https://doc.rust-lang.org/cargo/commands/cargo-new.html) document the tools and conventions used here. They are references, not required reading before this walkthrough.
