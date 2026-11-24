# Tool versions for the first host batch

| Tool / input | Selection |
|---|---|
| Rust, Cargo, rustfmt, Clippy | Rust **1.90.0**, declared in `rust-toolchain.toml`; rustfmt and Clippy use components from that release |
| Language edition | Rust **2024** in each package manifest |
| Host lockfile | `host/Cargo.lock` covers the host workspace. Lesson 00 uses only the standard library. |
| Python | Standard library only; Python 3.10 or newer |
| C++ comparison | C++17, compiled with warnings enabled and treated as errors |
| Linux CI | GitHub-hosted `ubuntu-24.04`; no self-hosted runner |
| Docker image base | `rust:1.90.0-bookworm`; not an immutable digest pin |
| GitHub checkout action | v7.0.1 at `3d3c42e5aac5ba805825da76410c181273ba90b1`; checkout credentials are not persisted |

Lesson 00 uses Rust 1.90.0 as its stable baseline. [Rust release announcement](https://blog.rust-lang.org/2025/09/18/Rust-1.90.0/) · [Verification results](../PROGRESS.md)

Rustup selects the toolchain from `rust-toolchain.toml` when you work in the repository. An explicit override can take precedence. CI reads the version from that file and logs the compiler version it runs. [Rustup selection order](https://rust-lang.github.io/rustup/overrides.html)

The Dockerfile repeats the Rust version in its base image tag. When changing the pin, update `rust-toolchain.toml`, the Dockerfile, and the Linux setup guide. Run the Linux and Docker checks and review any printed diagnostics affected by the change.

OS packages, Python patch releases, the runner image, and editor extensions can change independently of the Rust pin. The Linux CI job logs its tool versions.
