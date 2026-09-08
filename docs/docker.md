# Use Docker for the host lessons

The development image contains the selected Rust release, Make, Python, and the C++ compiler used for comparison checks. Docker is an alternative to installing those tools directly. You need a working Docker installation first; use the [official installation documentation](https://docs.docker.com/engine/install/).

The image installs tools as root during its build, then runs lessons as the **non-root `learner` user**. It does not request privileged mode, USB access, or a mounted Docker socket. It is not a board-flashing setup.

## Linux or WSL terminal

Run from the repository root. Matching your user and group numbers avoids creating root-owned build files in your checkout:

```bash
docker build \
  --build-arg USER_UID="$(id -u)" \
  --build-arg USER_GID="$(id -g)" \
  -t rust-tutorial:phase-1 \
  -f .devcontainer/Dockerfile .
```

Then run the checks with network access disabled:

```bash
docker run --rm --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 make verify
```

To work interactively:

```bash
docker run --rm -it --network none \
  --mount type=bind,source="$PWD",target=/workspace \
  --workdir /workspace \
  rust-tutorial:phase-1 bash
```

Inside the container, start with:

```bash
cd host/lessons/00-rust-orientation
make run
make test
```

The bind mount makes your host files visible inside the container, so edits and build output persist in the checkout. The `--rm` option removes the container afterward, not the mounted source files. Only mount a checkout you intend to work on. See [Docker's run reference](https://docs.docker.com/engine/containers/run/).

The image build needs internet access. Runtime checks do not: the toolchain is already installed and Lesson 00 has no external Rust dependencies. Docker reuses image layers between builds, while Cargo output remains in the mounted package/workspace `target/` directories. There are no dependency-download caches to configure yet.

## VS Code development container

With Docker and VS Code's Dev Containers extension installed, open the repository and select **Dev Containers: Reopen in Container**. `.devcontainer/devcontainer.json` builds the same image, selects `learner`, and runs `make verify` after creation.

Rust Analyzer initially opens the worked-example workspace. When editing the standalone exercise, open its folder in a separate editor window or add its `Cargo.toml` to Rust Analyzer's linked projects. This does not change which package the terminal commands test.

The Docker CLI checks and the interactive VS Code integration have separate verification status; consult [Progress](../PROGRESS.md). The configuration's existence does not establish that every Docker Desktop or editor setup has been tested.

## Limits of reproducibility

The Rust release and Cargo lockfiles are pinned. The Debian-based image tag and operating-system package repositories can receive updates, so this is not a byte-for-byte frozen operating-system image. The [tool version note](tool-versions.md) records that distinction. No coverage tooling or embedded target is installed in this first image.
