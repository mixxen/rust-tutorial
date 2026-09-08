# Set up on Linux

This guide installs the tools. **[Lesson 00, Part 1](../host/lessons/00-rust-orientation/FIRST_PROGRAM.md)** explains what they do and then teaches how to create and run your first program. You do not need to understand Cargo before reading the lesson's introduction.

Briefly: `rustc` compiles Rust, Cargo manages building and running a project, and `rustup` installs and selects their versions. A compiler release and its related tools are called a toolchain.

The commands below target Ubuntu 24.04 or a comparable Debian-based distribution. Initial installation needs internet access; Lesson 00 itself has no external Rust dependencies. For Windows, use [WSL setup](setup-wsl.md). For an isolated environment, use [Docker](docker.md). No board or embedded tools are needed yet.

## 1. Install the operating-system tools

In a terminal:

```bash
sudo apt-get update
sudo apt-get install -y build-essential curl ca-certificates git python3 less
```

`build-essential` supplies Make, a C/C++ toolchain, and the system support needed for linking. The C++ compiler is used only by the optional three-language comparison check, not the Rust walkthrough. Python 3.10 or newer runs the repository checks; no Python packages need installing.

## 2. Install rustup, unless you already have it

Check first:

```bash
rustup --version
```

If that command is missing, download the official installer so you can inspect it before running it:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup-install.sh
less /tmp/rustup-install.sh
sh /tmp/rustup-install.sh -y --profile minimal --default-toolchain none
. "$HOME/.cargo/env"
```

Press `q` to leave `less`. The installer comes from the [official Rust installation service](https://www.rust-lang.org/tools/install). Do not run it with `sudo`.

This installation does not select a new global Rust default. The repository's `rust-toolchain.toml` chooses its own release. [Rustup's selection rules](https://rust-lang.github.io/rustup/overrides.html) explain existing environment or directory overrides that may affect it.

## 3. Open the tutorial and install its selected tools

Use your existing checkout or extracted download. For a new Git checkout of the implementation branch:

```bash
git clone --branch phase-1/orientation https://github.com/mixxen/rust-tutorial.git
cd rust-tutorial
```

The implementation is currently proposed in pull request #1. A checkout of `main` alone does not yet contain the lesson. For a ZIP download, extract the `phase-1/orientation` branch and open its extracted top-level folder instead. The folder name can differ from `rust-tutorial`; look for `rust-toolchain.toml` and `host/` inside it.

From that repository root:

```bash
rustup toolchain install 1.90.0 --profile minimal --component rustfmt --component clippy
rustup show
rustc --version
cargo --version
```

The installation command requests the compiler plus formatting and lint tools. `rustup show` reports the active selection. The expected Rust release is **1.90.0**, not whatever happens to be newest. [Tool versions](tool-versions.md) explains this choice. Installing a named toolchain does not replace an existing global default.

## 4. Begin with your own Hello World

Setup is complete when the version commands succeed in this directory. Return to **[Lesson 00, Part 1](../host/lessons/00-rust-orientation/FIRST_PROGRAM.md)**, at “Ask Cargo to create the project.” It explains the file creation, editor steps, and run command.

You do not need to run `make verify` or understand the repository's library layout before writing Hello World. Those are introduced after the first program and tests.

## When a command does not work

| Symptom | What to check |
|---|---|
| `cargo` or `rustup` is not found | Open a new terminal, or run `. "$HOME/.cargo/env"`. Do not install a second Rust distribution just to repair the command search path. |
| A linker or `cc` is missing | Check that `build-essential` installed successfully. |
| Cargo cannot find `Cargo.toml` at the repository root | The root is not a Cargo project. The walkthrough creates your own project and tells you when to enter it. |
| Another Rust version appears | Run `rustup show`; inspect existing directory or `RUSTUP_TOOLCHAIN` overrides before changing them. |
| A tool download is attempted during an offline command | Cargo's offline option controls dependencies, not installation of a missing compiler. Install the toolchain first. |
| The expected lesson files are missing | Check the branch or ZIP download; the implementation has not yet been merged into `main`. |

## macOS and native Windows

These remain secondary, unverified paths for this batch. Ordinary Cargo commands are similar, but the shell and linker setup may differ. macOS needs its usual command-line build tools; native Windows needs a compatible Rust linker toolchain. Use the documented WSL path on Windows instead of assuming every Linux shell command works in PowerShell.
