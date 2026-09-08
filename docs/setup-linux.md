# Set up on Linux

This is the primary host-learning path. The package commands below target Ubuntu 24.04 or a comparable Debian-based distribution. A Rust **toolchain** is the compiler plus related tools; `rustup` installs and selects it. You need internet access for initial installation, but Lesson 00 has no third-party Rust dependencies and its checks run offline afterward.

For Windows, start with [WSL setup](setup-wsl.md). For an isolated development environment, use [Docker](docker.md). No board or embedded tools are needed yet.

## 1. Install the operating-system tools

In a terminal:

```bash
sudo apt-get update
sudo apt-get install -y build-essential curl ca-certificates git python3
```

`build-essential` includes Make, a C/C++ toolchain, and the system support needed for linking. The C++ compiler is only needed to execute the optional three-language comparison check, not to follow the Rust walkthrough. Python 3.10 or newer runs the small repository checks; no Python packages need installing.

## 2. Install rustup, unless you already have it

Check first:

```bash
rustup --version
```

If the command is missing, use the official installer. These commands download the script so you can inspect it before executing it:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs -o /tmp/rustup-install.sh
less /tmp/rustup-install.sh
sh /tmp/rustup-install.sh -y --profile minimal --default-toolchain none
. "$HOME/.cargo/env"
```

Press `q` to leave `less`. The installer comes from the [official Rust installation service](https://www.rust-lang.org/tools/install). Do not run the installer with `sudo`.

We do not change an existing global Rust default. The repository's `rust-toolchain.toml` chooses its own release. See [rustup's toolchain selection rules](https://rust-lang.github.io/rustup/overrides.html) when an existing override selects a different version.

## 3. Open your checkout and install its selected tools

Clone the repository if you do not already have it:

```bash
git clone https://github.com/mixxen/rust-tutorial.git
cd rust-tutorial
```

If you are reviewing an implementation pull request, switch to its branch before continuing. You should see `rust-toolchain.toml` and the `host/` directory in this checkout.

From the repository root:

```bash
rustup toolchain install 1.90.0 --profile minimal --component rustfmt --component clippy
rustup show
rustc --version
cargo --version
```

The installation command requests the compiler and the formatter/linter used by the repository. `rustup show` then displays the active choice. The expected Rust release for this batch is **1.90.0**, not whichever release happens to be newest. [Tool versions](tool-versions.md) explains this choice. Installing a named toolchain does not replace an existing global default.

## 4. Run the first program and the checks

Still in the repository root:

```bash
make run
make verify
```

The program prints `Readings above 25: 1`. The verification command checks complete code and compiles the exercise scaffold without running its unfinished assertions. Build and test output will contain additional lines; exact compiler timings are not part of the lesson.

Now open **[Lesson 00](../host/lessons/00-rust-orientation/README.md)**. You have finished setup; the lesson explains the code you are running.

## When a command does not work

| Symptom | What to check |
|---|---|
| `cargo` or `rustup` is not found | Open a new terminal, or run `. "$HOME/.cargo/env"`. Do not install a second Rust distribution just to repair `PATH`. |
| A linker or `cc` is missing | Check that `build-essential` installed successfully. |
| `could not find Cargo.toml` at the repository root | Use `make run`, or change into the lesson directory before using Cargo. The root intentionally is not a Cargo workspace. |
| Another Rust version appears | Run `rustup show`; inspect existing directory or `RUSTUP_TOOLCHAIN` overrides before changing them. |
| Rust tries to download tools despite `--offline` | Cargo's offline flag controls dependency access. The rustup toolchain must already be installed. |
| `make exercise` fails | Exercise assertion failures are initially expected. Missing tools or compilation errors are different problems. Read the named failing test. |

## macOS and native Windows

These are secondary paths, not verified platforms for this batch. The lesson shows direct Cargo commands that do not require Make. macOS needs its normal command-line build tools; native Windows needs a compatible Rust linker toolchain. For a documented Windows path, use WSL rather than adapting every shell command. Do not interpret these notes as evidence of testing on either platform.
