# Use Docker for the host lessons

The Docker image contains the course's Rust release, Make, Python, and the C++ compiler used for the comparison. Install Docker before you build the image. [Docker installation guide](https://docs.docker.com/engine/install/)

The image installs tools as root during the build. The container runs the lesson as the `learner` user.

## Linux or WSL terminal

Open the repository root of your `main` checkout or ZIP. The build arguments give `learner` your user and group IDs so the files you create in the container belong to you on the host.

```bash
docker build \
  --build-arg USER_UID="$(id -u)" \
  --build-arg USER_GID="$(id -g)" \
  -t rust-tutorial:phase-1 \
  -f .devcontainer/Dockerfile .
```

Start a container from the repository root.

```bash
docker run --rm -it --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 bash
```

In the container terminal, check your directory and Rust version. `pwd` should print `/workspace`. The version commands should report `1.90.0`.

```bash
pwd
rustc --version
cargo --version
```

Run the Lesson 00 commands in the container terminal to create `practice/hello_rust/` under `/workspace`. Open `practice/hello_rust/src/main.rs` in your host editor. Save your edits and run `cargo run` from the project directory in the container. [Lesson 00, part 1](../host/00-rust-orientation/01-first-program.md)

The bind mount makes `/workspace` refer to your checkout on the host. Your edits and Cargo build output stay in that checkout when you exit the container. [Docker run reference](https://docs.docker.com/engine/containers/run/)

The image build needs internet access. The lesson runs offline because the image has the compiler and the examples use no external Rust libraries.

## Optional repository verification

Run this from the repository root on the host to check the examples and documentation.

```bash
docker run --rm --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 make verify
```

The checker runs the printed programs in a temporary Cargo project.

## VS Code development container

With Docker and the VS Code Dev Containers extension installed, open the repository and select **Dev Containers: Reopen in Container**. The configuration builds the same image, starts it as `learner`, and runs `make verify`.

Use the VS Code terminal for the lesson commands. Rust Analyzer starts with the `host/` workspace. To use it in your `hello_rust` project, add the project's `Cargo.toml` to Rust Analyzer's linked projects or open the project in a container-connected window. [Verification results](../PROGRESS.md)

## Limits of reproducibility

The image pins the Rust release. Rebuilding it can pick up newer Debian packages. Cargo uses the repository's lockfile when it builds the examples. [Tool versions](tool-versions.md)
