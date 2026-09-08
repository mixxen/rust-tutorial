# Implementation progress

## Phase 1 — first batch: setup and Lesson 00

**First batch implemented; automated Linux and Docker checks passed. Phase 1 remains in progress.** Lesson 01 has not started. This file is the live status record; the curriculum and implementation plan retain their original planning snapshot.

| Lesson / task | Writing and implementation | Host checks | Firmware build | Board execution |
|---|---|---|---|---|
| 00 — Rust orientation | Implemented; ready for learner review | Passed on GitHub-hosted Linux and in Docker | Not applicable | Not applicable |
| Linux setup and Docker configuration | Implemented | Checkout/toolchain checks and Docker CLI run passed; fresh desktop installation not observed | Not applicable | Not applicable |
| WSL guide and VS Code development-container configuration | Implemented | Interactive WSL and editor setup not tested | Not applicable | Not applicable |
| 01 — Toolchain and Cargo | Planned | Not run | Not applicable | Not applicable |
| Early H723ZG check | Deferred to a separate small batch | Not run | Not run | Needs board access and verification |

## Recorded verification — September 8, 2026

**Tested implementation commit:** `db2afb082b907e999267873dfd15f1982f82f9c5`.

**Evidence:** [GitHub Actions run 34274526377](https://github.com/mixxen/rust-tutorial/actions/runs/34274526377), completed successfully. Both the `linux` and `docker` jobs passed. The author inspected their step results rather than inferring success from the presence of a workflow. This evidence refers to the named implementation revision; this subsequent record update changes documentation and a help description only.

The Linux job used a fresh checkout on a GitHub-hosted Ubuntu 24.04 runner and explicitly installed the pinned Rust toolchain. The Docker job built `.devcontainer/Dockerfile` and ran the checks as a non-root user with `--network none`. Build-time downloads were allowed; runtime dependency access was not needed.

| Check | Observed result |
|---|---|
| Reference tests | Four library tests and one executable-output test passed |
| Complete solution | All six acceptance tests passed |
| Formatting and Clippy | Passed for the complete reference and solution code |
| Exercise scaffolding | Compiled without requiring the learner's unfinished assertions to pass |
| Deliberate compiler errors | All three produced their intended error code; all three repaired examples built and ran with the specified output |
| C++ / Python / Rust comparison | All three printed `Readings above 25: 1` |
| Temporary exercise baseline | Exactly the four intended equality-sensitive tests failed; substituting the complete solution passed the identical six-test suite |
| Documentation / repository checks | Local Markdown link paths, acceptance-test parity, and lockfile presence passed |
| Lesson-local commands | `run`, `verify`, and `solution` passed from the lesson directory |
| Tracked-file changes after verification | None, in either CI job |

An initial run found a bug in the author-only exercise checker: copying the solution while preserving an old file timestamp allowed Cargo to reuse the intentionally failing build. The fix writes the replacement source and uses separate build directories for the baseline and solution. The acceptance assertions were not weakened. The recorded successful run includes that fix.

The authoring sandbox itself has no Rust compiler or Docker and could not download the toolchain. The execution evidence above comes from the actual GitHub-hosted runs, not from claimed local execution.

## What this does not establish

Interactive WSL installation, a fresh desktop Rust installation, VS Code's development-container UI, macOS, native Windows, and physical-board access have not been tested in this batch. The Docker CLI result does not stand in for those interactions. No coverage measurement, firmware build, or board execution is claimed. External website availability and Markdown heading anchors are not checked by the local-link script.

## Teaching review

The walkthrough explains punctuation beside its first use, uses names such as `reading` and `qualifying_count`, keeps the C++/Python task consistent, and separates hints from the answer. Author review is complete for this batch. Alex's actual learning feedback and a fresh-reader walkthrough are still pending; they are not implied by passing automated tests.

## Next small task

Implement Lesson 01: explain the tools just used and create a small package from scratch. Preserve the Lesson 00 example and its command behavior. The early board check remains separate and must record firmware build results separately from observed board behavior.
