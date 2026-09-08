# Implementation progress

## Phase 1 — Lesson 00 revised after learner feedback

**The revised Lesson 00 passed its automated Linux and Docker checks. Phase 1 remains in progress, and a learner trial of the revision is still pending.** The first version passed automated checks too, but its learner trial exposed missing instruction. Passing checks does not establish teaching readiness.

Alex downloaded and tried the first version, then reported that it assumed Rust knowledge he did not have: what Cargo is, how to create a main file, how to write Hello World, and how function syntax works. This is actual learner feedback, not a hypothetical review. No claim is made that the revised version has completed a learner trial.

| Lesson / task | Current state |
|---|---|
| 00 — opening walkthrough | Rewritten as four ordered parts: first program, functions/variables, readings/control flow, first tests/course layout |
| Reference example and acceptance exercise | Existing behavior preserved; exercise instructions rewritten with Cargo-first steps |
| New walkthrough checks | Passed: fresh `cargo new`, ten complete printed programs, direct `rustc`, specific compiler errors, test failure and repair |
| Linux and Docker entry instructions | Lead to Hello World rather than requiring Make or library knowledge first; command-line checks passed |
| WSL and VS Code interactions | Not newly tested; do not infer them from a Docker command-line result |
| 01 — Toolchain and Cargo | Not implemented; deepen the basics now introduced in 00 |
| Early H723ZG check | Still separate; no firmware build or board execution claimed |

### Scope clarification from the learner trial

Keep the approved lesson IDs and course count. Lesson 00 now includes essential Cargo/project creation and a gradual explanation of functions; these are not deferred prerequisites supplied by Lesson 01. The original short orientation duration is no longer a constraint: the four parts offer natural stopping points. `CURRICULUM.md` and `IMPLEMENTATION_PLAN.md` retain their original planning snapshot; this record and the implemented Lesson 00 describe the revised opening.

The ordinary walkthrough stays in one learner-created `src/main.rs` until after the first tests. Only then does it explain `pub`, `use`, `src/lib.rs`, and the supplied course structure. The explicit-return example precedes the final-expression shorthand. Make is a later convenience, not an unexplained first command.

## Recorded revision verification — September 8, 2026

**Implementation revision:** `28e212ddd49eba60e93fe4dd99b54a1634b60da5`.

**Evidence:** [GitHub Actions run 34283327094](https://github.com/mixxen/rust-tutorial/actions/runs/34283327094). Both the `linux` job (`102253010534`) and the `docker` job (`102253010789`) completed successfully. The Linux log and both jobs' step results were inspected. The pull-request workflow tested GitHub's proposed merge revision `15ca1c5ca34ecd05e49d08337a0e8ca5d3c392fb`, combining that implementation with the unchanged main branch. The PR has not actually been merged.

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

## Remaining limits and next step

A fresh interactive desktop installation, WSL, VS Code's container UI, macOS, native Windows, and physical hardware have not been verified here. There is no code-coverage measurement or embedded execution claim. The local-link checker does not validate external sites or Markdown heading anchors.

The revised first experience needs another learner walkthrough before expanding the teaching pattern. Lesson 01 remains the next new lesson, not work completed by this revision. The early board check remains separate and must record build results separately from observed board behavior.
