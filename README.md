# Rust for Experienced Programmers

Learn to write Rust you can explain, change, debug, and test. This course assumes you already program in C, C++, or Python; it does not assume you have written Rust before.

The examples use ordinary names and small tasks. When a new symbol or term appears, the lesson explains it. The later embedded track will use Embassy on the NUCLEO-H723ZG.

## Start learning

**[Lesson 00 — A first look at Rust](host/lessons/00-rust-orientation/README.md)** is the first implemented lesson. It compares one small task across languages, introduces the syntax, and gives you a change to make and test yourself.

First choose a setup path: **[Linux](docs/setup-linux.md)**, **[Windows with WSL](docs/setup-wsl.md)**, or **[Docker / VS Code development container](docs/docker.md)**. No board is needed for Lesson 00.

With the setup complete, run these commands from the repository root:

```bash
make run
make verify
```

The program prints:

```text
Readings above 25: 1
```

`make verify` checks the working examples and supplied solutions. It does **not** claim your exercise is finished. Your exercise has its own command, introduced in the lesson.

## What is available?

| Material | Status |
|---|---|
| Lesson 00, exercise, hints, solution, and syntax reference | Implemented in the first Phase 1 batch |
| Linux/WSL instructions, Dockerfile, and automated host checks | Included; observed results are recorded in [Progress](PROGRESS.md) |
| Lesson 01 — Toolchain and Cargo | Next Phase 1 batch; not implemented yet |
| Remaining host lessons and Embassy track | Planned, not implemented |

**Phase 1 is in progress, not complete.** We are establishing one complete learning experience before expanding the course. No board execution or learner completion is claimed. [Progress and verification notes](PROGRESS.md) distinguish implemented files from checks actually run.

## How lessons work

Read the worked example, predict its behavior, run it, and then tackle the separate exercise. Hints offer gradual help. The complete solution explains the reasoning and an alternative. Tests help you check a change; they do not replace understanding it.

Each implemented lesson has a Cargo package and Makefile. Cargo does the Rust work; Make just provides convenient shortcuts. The lesson shows both forms. There is no root Cargo package: ordinary host examples live in `host/`, while exercises and solutions are separate packages.

## Course and contributor documents

| Document | Purpose |
|---|---|
| [Curriculum](CURRICULUM.md) | The full 27-lesson host track, 14-lesson embedded track, and optional extensions |
| [Implementation plan](IMPLEMENTATION_PLAN.md) | Approved development phases and teaching standards |
| [Progress](PROGRESS.md) | Current delivery and verification status; the planning documents retain their original planning snapshot |
| [Contributor guide](CONTRIBUTING.md) | How to add a lesson without losing clarity or weakening checks |
| [Tool versions](docs/tool-versions.md) | The selected toolchain and what is, and is not, pinned |

Feedback about an unclear explanation is as valuable as a bug report. Include the lesson, the command or paragraph, what you expected, and where you became stuck. Never include secrets or private project code.
