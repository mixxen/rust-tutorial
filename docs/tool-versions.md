# Tool versions for the first host batch

| Tool / input | Selection |
|---|---|
| Rust, Cargo, rustfmt, Clippy | Rust **1.90.0**, declared in `rust-toolchain.toml`; rustfmt and Clippy use components from that release |
| Language edition | Rust **2024** in each package manifest |
| Rust dependencies | No third-party crates in Lesson 00; all three applicable lockfiles are committed |
| Python | Standard library only; Python 3.10 or newer |
| C++ comparison | C++17, compiled with warnings enabled and treated as errors |
| Linux CI | GitHub-hosted `ubuntu-24.04`; no self-hosted runner |
| Docker image base | `rust:1.90.0-bookworm`; not an immutable digest pin |
| GitHub checkout action | v7.0.1 at `3d3c42e5aac5ba805825da76410c181273ba90b1`; checkout credentials are not persisted |

Rust 1.90.0 is an explicitly selected stable baseline, **not a claim about the latest release**. Its availability is documented by the [Rust release announcement](https://blog.rust-lang.org/2025/09/18/Rust-1.90.0/). The first batch needs no newer language feature. Check [Progress](../PROGRESS.md) for actual validation results; the pin is not evidence by itself.

The toolchain is selected from the repository root or a child directory. An explicit rustup override can take precedence; [rustup documents the selection order](https://rust-lang.github.io/rustup/overrides.html). Install the selected release explicitly before inspecting it with `rustup show`; current rustup warns against relying on automatic installation by that inspection command. CI reads the release from the file and records the actual compiler version.

The Dockerfile repeats the Rust version because Docker needs to select its base image before it can read a checkout. When changing the pin, update that file and the human-readable setup recipe, rerun Linux and Docker checks, and inspect compiler-error demonstrations for changed diagnostics. Keep `.lock` files in Git and reject unintended changes during normal verification.

Operating-system packages, Python patch releases, the runner image, and editor extensions are not frozen. We record actual tools in CI logs and do not call this a completely immutable environment. No nightly toolchain, code coverage tool, or Embassy release has been selected for this batch.
