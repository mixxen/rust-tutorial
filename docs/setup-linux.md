# Set up on Linux

Use these commands on Ubuntu 24.04 or a comparable Debian-based distribution. Setup needs internet access. After setup, you can build Lesson 00 offline. [Windows with WSL](setup-wsl.md) · [Docker](docker.md)

## 1. Install the Linux packages

Run these commands in your terminal.

```bash
sudo apt-get update
sudo apt-get install -y build-essential curl ca-certificates git python3 less
```

`build-essential` includes the linker Rust uses to produce an executable. It also includes Make and the C++ compiler used for the comparison. The repository checks use Python 3.10 or newer.

## 2. Check for rustup

`rustup` installs and selects Rust toolchains. Check whether it's already installed.

```bash
rustup --version
```

If `rustup` is already installed, go to step 3. Otherwise, download and read the installer using the first two commands. Press `q` to leave `less`, then run the last two commands.

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup-install.sh
less /tmp/rustup-install.sh
sh /tmp/rustup-install.sh -y --profile minimal --default-toolchain none
. "$HOME/.cargo/env"
```

Run the installer as your own user. The `--default-toolchain none` option leaves your global toolchain selection alone. The tutorial chooses its own Rust release through `rust-toolchain.toml`. [Official Rust installer](https://www.rust-lang.org/tools/install)

## 3. Open the tutorial and install Rust

Open your existing `main` checkout or clone a fresh copy.

```bash
git clone --branch main https://github.com/mixxen/rust-tutorial.git
cd rust-tutorial
```

If you downloaded a ZIP of `main`, extract it and open the top-level folder containing `rust-toolchain.toml` and `host/`.

From the repository root, install the Rust toolchain for this course.

```bash
rustup toolchain install 1.90.0 --profile minimal --component rustfmt --component clippy
```

- `rustup toolchain install 1.90.0` installs a specific Rust release so you use the same version as the course examples.
- `--profile minimal` installs the compiler `rustc`, Cargo, and the Rust standard library for your machine.
- `--component rustfmt` adds the formatter. `cargo fmt` uses it to format Rust source files.
- `--component clippy` adds a tool that flags common mistakes and suggests improvements. Run it with `cargo clippy`.

Rustup reads `rust-toolchain.toml` to select this release when you're in the repository. Check the active toolchain and the versions of the compiler and Cargo.

```bash
rustup show
rustc --version
cargo --version
```

`rustc --version` and `cargo --version` should both report `1.90.0`. [Tool versions](tool-versions.md)

## 4. Begin with your own Hello World

Once the tools report the expected version, start Lesson 00 or return to where you paused. [Lesson 00, part 1](../host/00-rust-orientation/01-first-program.md)

## When a command does not work

| Symptom | What to check |
|---|---|
| The shell can't find `cargo` or `rustup` | Open a new terminal or run `. "$HOME/.cargo/env"`. |
| The build can't find a linker or `cc` | Check that `build-essential` installed successfully. |
| Cargo can't find `Cargo.toml` | Change to your `hello_rust` project directory before running `cargo run`. |
| The version commands show a different release | Run `rustup show` and check for a directory override or a `RUSTUP_TOOLCHAIN` setting. |
| Rustup tries to download the compiler during an offline build | Install the toolchain first. Cargo's `--offline` flag applies to dependencies. |
| The tutorial files are missing | Check that you're in the top-level folder of your `main` checkout or ZIP. |

## macOS and native Windows

On macOS, install the system command-line build tools. On Windows, follow the WSL setup to use the same terminal commands as this guide. [Windows with WSL](setup-wsl.md)
