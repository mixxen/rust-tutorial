# Implementation progress

## Phase 1. Lesson 00

Lesson 00 has a three-part walkthrough and runnable examples. The learner edits one `src/main.rs` from the first Hello World program through the readings example. [Lesson overview](host/00-rust-orientation/README.md)

New practice projects use `practice/hello_rust/`. Learners who started at `practice/lesson-00/hello_rust/` can keep using that project.

The comparison page brings the three complete readings programs together. [C++, Python, and Rust comparison](host/00-rust-orientation/COMPARISON.md)

### Verification on November 23, 2026

Verified the Lesson 00 changes and documentation using a fresh copy of the staged files and the pinned Rust 1.90.0 toolchain. The follow-up is based on `c9c7bf5`.

| Environment | Observed results |
|---|---|
| Ubuntu 22.04.3 | `make verify` passed formatting, Clippy, Markdown links, and the fresh Cargo project walkthrough. All nine printed programs matched their source copies and ran with the expected output. |
| Ubuntu 22.04.3 | `make comparisons` and `make run` printed `Readings above 25: 1`. From the lesson directory, `cargo run` printed the same count, `cargo run --example hello_world` printed `Hello, world!`, and `cargo check --examples --locked --offline` passed. |
| Docker development image | Image build passed. A non-root container with runtime networking disabled passed `make verify`, `make comparisons`, and `make run` using a read-only source mount. |
| Documentation and CI review | All 17 Markdown files were reviewed. The local links passed, the 37 external links resolved, and all comparison snippets and complete listings matched their sources. `actionlint` accepted the host workflow. |

The latest review feedback was that Lesson 00 looks good. A fresh learner walkthrough and interactive WSL and VS Code setup still need a run. Firmware and board checks are tracked separately. Lesson 01 is the next implementation batch and will introduce Cargo tests.

## Historical revision — Lesson 00 after the first learner trial

This earlier four-part revision passed automated Linux and Docker checks. The first version had passed automated checks too, and the first learner trial still found gaps in the instructions.

Alex tried the first version and reported gaps in the explanations of Cargo, source files, Hello World, and function syntax.

| Lesson or task | State at that revision |
|---|---|
| 00 — opening walkthrough | Rewritten as four ordered parts: first program, functions/variables, readings/control flow, first tests/course layout |
| Reference example and acceptance exercise | Existing behavior preserved; exercise instructions rewritten with Cargo-first steps |
| New walkthrough checks | Passed: fresh `cargo new`, ten complete printed programs, direct `rustc`, specific compiler errors, test failure and repair |
| Linux and Docker entry instructions | Lead to Hello World rather than requiring Make or library knowledge first; command-line checks passed |
| WSL and VS Code interactions | Not newly tested; do not infer them from a Docker command-line result |
| 01 — Toolchain and Cargo | Not implemented; deepen the basics now introduced in 00 |
| Early H723ZG check | Still separate; no firmware build or board execution claimed |

### Scope clarification from the learner trial

This revision brought project creation and function syntax into Lesson 00 and split the material into four parts. The lesson numbers and course count stayed the same.

The ordinary walkthrough stays in one learner-created `src/main.rs` until after the first tests. Only then does it explain `pub`, `use`, `src/lib.rs`, and the supplied course structure. The explicit-return example precedes the final-expression shorthand. Make is a later convenience, not an unexplained first command.

## Recorded revision verification — September 8, 2026

**Implementation revision:** `28e212ddd49eba60e93fe4dd99b54a1634b60da5`.

**Evidence:** Both the `linux` job (`102253010534`) and the `docker` job (`102253010789`) completed successfully. The Linux log and both jobs' step results were inspected. The pull-request workflow tested GitHub's proposed merge revision `15ca1c5ca34ecd05e49d08337a0e8ca5d3c392fb`, which combined that implementation with `main` as it existed at the time. [GitHub Actions run 34283327094](https://github.com/mixxen/rust-tutorial/actions/runs/34283327094)

This record is a subsequent documentation-only update; the evidence names the exact implementation it verifies.

| Check | Observed result |
|---|---|
| Printed programs | All ten complete Rust listings matched their checked source copies |
| New project | `cargo new` created `Cargo.toml` and `src/main.rs`; generated Hello World ran |
| Edit/save/run path | All ten replacement programs ran with the declared output |
| Basic tool commands | `cargo check`, `cargo build`, and direct execution of the built Hello World succeeded |
| Manually created file | A separate `main.rs` compiled with `rustc` and printed Hello World |
| Intended syntax/type errors | The added tail semicolon produced E0308; removing counter mutability produced E0384 |
| First tests | Three passed; changing the rule to include equality still compiled but failed exactly the equality test; repair restored all three |
| Existing reference and solution | Five reference tests and six solution acceptance tests passed |
| Existing quality checks | Formatting, Clippy, three-language comparison, isolated compiler examples, and exercise baseline/repair checks passed |
| Repository checks | Local link paths, acceptance-test parity, lockfile presence, and no tracked-file modifications passed |

The Docker image ran checks as a non-root user with runtime networking disabled. Initial image/toolchain installation used network access. The walkthrough checker creates its own temporary project and independent build directories; it does not read, write, or reset a learner's `practice/` project. Git ignores that directory, and repository Markdown checks exclude it.

The authoring sandbox itself has neither Rust nor Docker available and could not resolve GitHub for a local clone. Execution evidence comes from the GitHub-hosted jobs, not claimed local execution. Fresh interactive installation and editor behavior remain distinct from the successful command-line results.

## Historical verification — initial implementation

**Tested implementation commit:** `db2afb082b907e999267873dfd15f1982f82f9c5`.

**Evidence:** [GitHub Actions run 34274526377](https://github.com/mixxen/rust-tutorial/actions/runs/34274526377), completed successfully. Both the `linux` and `docker` jobs passed. A subsequent documentation update at `f4a3879262aef088244b87d0b661444a7fd040d4` also passed [run 34274757606](https://github.com/mixxen/rust-tutorial/actions/runs/34274757606).

The Linux job used a fresh GitHub-hosted Ubuntu 24.04 checkout and installed the pinned Rust toolchain. Docker built the development image and ran as a non-root user with `--network none`; build-time downloads were allowed.

| Initial check | Observed result |
|---|---|
| Reference tests | Four library tests and one executable-output test passed |
| Complete solution | Six acceptance tests passed |
| Formatting and Clippy | Passed for the complete reference and solution code |
| Exercise scaffolding | Compiled without requiring unfinished assertions to pass |
| Isolated compiler errors | Three intended error codes confirmed; three repairs built and ran |
| C++ / Python / Rust comparison | All three printed `Readings above 25: 1` |
| Temporary exercise baseline | Four intended equality-sensitive failures; the solution passed the identical six-test suite |
| Documentation / repository checks | Local link paths, acceptance-test parity, and lockfile presence passed |
| Lesson-local commands | `run`, `verify`, and `solution` passed |
| Tracked-file changes after verification | None in either job |

An initial run found stale-build reuse in the author-only exercise checker when copied sources preserved timestamps. Writing replacement source and using independent build directories fixed it. No acceptance assertions were weakened. The new walkthrough checker follows the same independent-output approach.
