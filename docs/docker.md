# Use Docker for the host lessons

The development image contains the selected Rust release, Make, Python, and the C++ compiler used for comparison checks. Docker is an alternative to installing those tools directly. You need a working Docker installation first; see the [official installation documentation](https://docs.docker.com/engine/install/).

The image installs tools as root during its build, then runs lessons as the **non-root `learner` user**. It does not request privileged mode, USB access, or a mounted Docker socket. It is not a board-flashing setup.

## Linux or WSL terminal

Run from the repository root, where `.devcontainer/Dockerfile` lives. Matching your user and group numbers avoids creating root-owned build files in the checkout:

```bash
docker build \
  --build-arg USER_UID="$(id -u)" \
  --build-arg USER_GID="$(id -g)" \
  -t rust-tutorial:phase-1 \
  -f .devcontainer/Dockerfile .
```

Start an interactive terminal in the image:

```bash
docker run --rm -it --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 bash
```

Inside this terminal, the tutorial repository is `/workspace`. Check the tools:

```bash
pwd
rustc --version
cargo --version
```

Now follow **[Lesson 00, Part 1](../host/lessons/00-rust-orientation/FIRST_PROGRAM.md)**. Run its terminal commands inside this container. They create `practice/lesson-00/hello_rust` under `/workspace`, not inside the supplied lesson package.

The bind mount connects your host checkout to `/workspace`, so you can use a host editor to open `practice/lesson-00/hello_rust/src/main.rs` and run it from the container terminal. No editor command inside the container is required. Save on the host before running `cargo run` in the container's project directory.

Your source and practice edits persist in the mounted checkout. `--rm` removes the container when you exit, not the mounted files. Only mount a checkout you intend to work on. See [Docker's run reference](https://docs.docker.com/engine/containers/run/).

The image build needs internet access. Runtime checks do not: the compiler is already installed and this lesson has no external Rust dependencies. Docker reuses image layers, while Cargo build output remains in the mounted project/workspace `target/` directories.

## Optional repository verification

After the walkthrough introduces tests and Make, you can run the course checks without opening an interactive shell. Run this from the repository root **on the host**, not inside the container:

```bash
docker run --rm --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 make verify
```

This checks supplied course code and creates a temporary project for the printed walkthrough steps. It does not reset or grade your practice project.

## VS Code development container

With Docker and VS Code's Dev Containers extension installed, open the repository and select **Dev Containers: Reopen in Container**. `.devcontainer/devcontainer.json` builds the same image, selects `learner`, and runs `make verify` after creation. That setup check is not a task you must understand before Hello World.

Use the terminal in the reopened container for the walkthrough. Rust Analyzer initially opens the supplied host workspace. Your independent practice project and exercise are not members of that workspace. Add their `Cargo.toml` paths to Rust Analyzer's linked projects when you need editor assistance, or open the project folder in a suitable container-connected window. Editor assistance is optional: it does not determine what Cargo compiles from the terminal.

The Docker CLI checks and the interactive VS Code setup have separate verification status. Consult [Progress](../PROGRESS.md); passing command-line checks does not establish that every editor or Docker Desktop setup has been tested.

## Limits of reproducibility

The Rust release and supplied Cargo lockfiles are pinned. The Debian-based image tag and operating-system package repositories can receive updates, so the operating-system image is not frozen byte for byte. The [tool version note](tool-versions.md) records that distinction. No coverage tooling or embedded target is installed in this first image.
