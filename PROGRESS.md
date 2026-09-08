# Implementation progress

## Phase 1 — Lesson 00 revised after learner feedback

**Lesson 00 has been rewritten; verification of this revision is pending. Phase 1 remains in progress.** The previous version passed automated Linux/Docker checks, but the first learner trial exposed missing instruction. Passing checks did not establish teaching readiness.

Alex downloaded and tried the first version, then reported that it assumed Rust knowledge he did not have: what Cargo is, how to create a main file, how to write Hello World, and how function syntax works. This is actual learner feedback, not a hypothetical review. No claim is made that the revised version has completed a learner trial.

| Lesson / task | Current state |
|---|---|
| 00 — opening walkthrough | Rewritten as four ordered parts: first program, functions/variables, readings/control flow, first tests/course layout |
| Reference example and acceptance exercise | Existing behavior preserved; exercise instructions rewritten with Cargo-first steps |
| New walkthrough checks | Added: fresh `cargo new`, ten complete printed programs, direct `rustc`, intentional compiler errors, test failure and repair; awaiting execution evidence |
| Linux and Docker entry instructions | Now lead to Hello World rather than requiring Make or library knowledge first |
| WSL and VS Code interactions | Not newly tested; do not infer them from a Docker command-line result |
| 01 — Toolchain and Cargo | Not implemented; deepen the basics now introduced in 00 |
| Early H723ZG check | Still separate; no firmware build or board execution claimed |

### Scope clarification from the learner trial

Keep the approved lesson IDs and course count. Lesson 00 now includes essential Cargo/project creation and a gradual explanation of functions; these are not deferred prerequisites supplied by Lesson 01. The original short orientation duration is no longer a constraint: the four parts offer natural stopping points. `CURRICULUM.md` and `IMPLEMENTATION_PLAN.md` retain their original planning snapshot; this record and the implemented Lesson 00 describe the revised opening.

The ordinary walkthrough stays in one learner-created `src/main.rs` until after the first tests. Only then does it explain `pub`, `use`, `src/lib.rs`, and the supplied course structure. The explicit-return example precedes the final-expression shorthand. Make is a later convenience, not an unexplained first command.

### Revision verification plan

`make verify` now includes `scripts/check_walkthrough.py`. The checker compares displayed complete programs with their source copies, creates a temporary Cargo project with the pinned toolchain, builds/runs every step, checks the direct compiler path, and verifies specific failures and repairs. It never accesses the learner's `practice/` project. Git ignores that directory, and repository Markdown checks exclude it.

Actual results must be recorded after the new GitHub-hosted Linux and Docker jobs complete. The authoring sandbox has neither Rust nor Docker available and cannot resolve the GitHub host for a local clone. No local Rust or Docker execution is claimed.

## Historical verification — initial implementation

**Tested implementation commit:** `db2afb082b907e999267873dfd15f1982f82f9c5`.

**Evidence:** [GitHub Actions run 34274526377](https://github.com/mixxen/rust-tutorial/actions/runs/34274526377), completed successfully. Both the `linux` and `docker` jobs passed. A subsequent documentation update at `f4a3879262aef088244b87d0b661444a7fd040d4` also passed [run 34274757606](https://github.com/mixxen/rust-tutorial/actions/runs/34274757606). These are historical results, not verification of the new walkthrough.

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
