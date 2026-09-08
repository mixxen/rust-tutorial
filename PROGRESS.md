# Implementation progress

## Phase 1 — first batch: setup and Lesson 00

**State: in progress.** Lesson 00 and the initial setup are implemented. Lesson 01 has not started. This file is the live status record; the curriculum and implementation plan contain their original planning snapshot.

| Lesson / task | Writing and implementation | Host checks | Firmware build | Board execution |
|---|---|---|---|---|
| 00 — Rust orientation | Implemented; awaiting review | Pending recorded CI run | Not applicable | Not applicable |
| Linux/WSL setup and Docker configuration | Implemented | Pending recorded CI run; WSL interaction not tested | Not applicable | Not applicable |
| 01 — Toolchain and Cargo | Planned | Not run | Not applicable | Not applicable |
| Early H723ZG check | Deferred to a separate small batch | Not run | Not run | Needs board access and verification |

## Verification record for this change

The authoring environment has no Rust compiler or Docker installation and cannot download the toolchain. No Rust or Docker execution is claimed from that environment. The repository includes GitHub-hosted Linux and Docker checks so executable results can be recorded separately. Those checks use no secrets and never access or flash a board.

The checks cover reference and solution tests, Clippy, formatting without rewriting sources, compiler-error demonstrations and repairs, matching C++/Python/Rust output, exercise acceptance behavior in a temporary copy, and local Markdown link paths. They do not measure coverage, test WSL USB access, or validate a physical board.

This record must be updated with an actual workflow run and results before calling the Linux or Docker path verified. Merely adding a workflow is not a successful CI run.

## Teaching review

The walkthrough introduces punctuation beside its first use, uses names such as `reading` and `qualifying_count`, and keeps hints separate from the solution. A fresh-reader review and Alex's actual learning feedback are still pending; an author's review is not a learner trial.

## Next small tasks

Finish verification of this first batch and address any failures. Then implement Lesson 01: explain the tools just used and create a small package from scratch. The early board check remains separate and must record build results separately from observed board behavior.
