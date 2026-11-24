# Part 1. Cargo, files, and Hello World

[Lesson 00](README.md) · [Part 2. Functions and variables](02-functions-and-variables.md)

Create a Rust program, read its three lines, and change what it prints.

## 1. The Rust tools

Rust source files end in `.rs`. The compiler, `rustc`, turns that code into a program your machine can run. It plays the same role as `g++` or `clang++` in C++.

Cargo creates a project's initial files, calls `rustc`, and runs the compiled program. It also manages the libraries your project uses, called *dependencies*.

`rustup` installs and selects versions of Rust's tools. A compiler release and its companion tools are called a *toolchain*. You'll use `rustup` during setup and `cargo` when you work on the program.

## 2. Confirm that the tools are available

If you need to install the tools, follow the setup guide for your environment, then return here. [Linux](../../docs/setup-linux.md) · [Windows with WSL](../../docs/setup-wsl.md) · [Docker](../../docs/docker.md)

Open a terminal in the repository root, the folder containing `README.md`, `rust-toolchain.toml`, and `host/`. Use the Ubuntu terminal on WSL or the container terminal in Docker. In Docker, the repository is at `/workspace`.

```bash
pwd
ls
rustc --version
cargo --version
```

`pwd` shows where you are. `ls` lists the files and folders there. Both version commands should report `1.90.0`.

## 3. Ask Cargo to create the project

If you already have a `hello_rust` project, including one at `practice/lesson-00/hello_rust`, open it and continue to step 4. To create the project, run these commands from the repository root.

```bash
mkdir -p practice
cargo new practice/hello_rust --edition 2024 --vcs none
cd practice/hello_rust
```

`mkdir -p` creates `practice/` if needed. `cargo new` creates a project called `hello_rust`. `cd` moves your terminal into that project.

`--edition 2024` selects the Rust language edition used by this course. The edition sets language compatibility rules. `--vcs none` tells Cargo to skip creating a separate Git repository inside `practice`.

A Cargo *package* is a project described by one `Cargo.toml` file. This package contains one runnable program.

## 4. Open `src/main.rs`

Cargo creates this layout.

```text
hello_rust/
├── Cargo.toml
└── src/
    └── main.rs
```

`Cargo.toml` describes the package. `src/` holds the source code. Cargo looks for the program's starting file at `src/main.rs`.

Open your `hello_rust` folder in the editor and select `src/main.rs`. In VS Code, `code .` from the project directory opens that folder if the `code` command is available.

Cargo filled in a short program. Replace the entire contents of `src/main.rs` with the code below and save the file.

<!-- walkthrough: hello_world -->
```rust
fn main() {
    println!("Hello, world!");
}
```

If your editor asks for a file type, choose plain text and name the file `main.rs`.

## 5. Read the program

The first line defines a function named `main` with an empty parameter list. Its body starts at the opening brace.

| Piece | Meaning here |
|---|---|
| `fn` | Defines a function, much like `def` in Python. |
| `main` | The function Rust calls to start the program. |
| `()` after `main` | An empty parameter list. This function takes no inputs. |
| `{` and `}` | Mark where the function body starts and ends. |
| `println!` | Rust's built-in way to format and print a line of text, including a newline at the end. |
| `!` in `println!` | Marks a macro call. A macro expands into code when Rust compiles the program. |
| `("Hello, world!")` | Passes the text between the quotes to `println!`. |
| `;` after the print call | Ends the statement. |

The exclamation mark after `world` sits inside the quotes, so it appears in the output.

## 6. Build and run it

In your terminal, run this from `hello_rust/`, where `Cargo.toml` lives.

```bash
cargo run
```

Cargo builds and starts the program. It prints the line below.

```text
Hello, world!
```

Cargo prints its own progress lines, such as `Compiling` and `Running`. It finds `src/main.rs` from the project layout, so `cargo run` needs no filename.

After the first build, look for `Cargo.lock` and `target/`. `Cargo.lock` records the package versions Cargo selected. `target/` holds build output, including the executable. You'll keep editing the source in `src/`.

## 7. Change what the program prints

Replace all of `src/main.rs` with this version.

<!-- walkthrough: changed_message -->
```rust
fn main() {
    println!("I wrote this Rust program.");
    println!("Now I can change it and run it again.");
}
```

Save the file and run `cargo run` again from `hello_rust/`. The program now prints two lines.

```text
I wrote this Rust program.
Now I can change it and run it again.
```

## 8. Check, build, and run

Run these commands from `hello_rust/`.

```bash
cargo check
cargo build
cargo run
```

`cargo check` checks the code for compilation errors and skips producing the executable. `cargo build` creates the executable. `cargo run` builds it when needed and starts it.

On Linux, WSL, or in the container, you can also start the executable directly from `hello_rust/`.

```bash
./target/debug/hello_rust
```

`./` starts the path in your current directory. Cargo puts the default development build in `target/debug/`. Running the executable directly starts the last build. After an edit, use `cargo run` to build and run the new version.

Open `Cargo.toml` in the editor.

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2024"

[dependencies]
```

The `[package]` section gives the project its name, version, and Rust edition. The empty `[dependencies]` section says that the project uses no external libraries. Cargo may add comments to this file.

## When something goes wrong

| Symptom | First thing to check |
|---|---|
| `cargo: command not found` | Return to the setup guide for this terminal. |
| Cargo cannot find `Cargo.toml` | Run `pwd` and `ls`. You should be in your `hello_rust` directory, where `Cargo.toml` lives. |
| `cargo new` says the destination exists | Open the existing `hello_rust` project. |
| An error mentions `main` defined more than once | A complete example was probably appended instead of replacing the previous file. Keep one `fn main`. |
| An error points at a quote, bracket, or line number | Compare `src/main.rs` with the full example. |
| The printed text does not change | Save `src/main.rs` and run `cargo run` again from `hello_rust/`. |

Leave your terminal in `hello_rust/`. [Part 2. Functions and variables](02-functions-and-variables.md)

### Optional references

[Rust Book, Hello World](https://doc.rust-lang.org/book/ch01-02-hello-world.html) · [Rust Book, Hello Cargo](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html) · [Cargo project creation](https://doc.rust-lang.org/cargo/commands/cargo-new.html)
