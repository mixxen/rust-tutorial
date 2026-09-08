# Rust for Experienced Programmers

Learn to write Rust you can explain, change, debug, and test. This course assumes programming experience in C, C++, or Python, **not familiarity with Rust, Cargo, or Rust's file layout**.

## Start learning

**[Lesson 00 — Write your first Rust program](host/lessons/00-rust-orientation/README.md)** now begins at the beginning. It explains Cargo, helps you create a project and open `src/main.rs`, and walks through Hello World before introducing functions, variables, the readings example, or tests.

Read its four parts in order. Each identifies what to type in the terminal, which file to edit, and what the program should print. You work in your own practice project before touching the supplied exercise. New Rust punctuation is explained near its first use.

Start with **[Part 1 — Cargo, files, and Hello World](host/lessons/00-rust-orientation/FIRST_PROGRAM.md)**. It links to the installation path you need: [Linux](docs/setup-linux.md), [Windows with WSL](docs/setup-wsl.md), or [Docker / VS Code development container](docs/docker.md). No board is needed yet.

Already tried the first version? The opening has been substantially rewritten in response to learner feedback. Begin with Part 1 rather than jumping straight back to the threshold exercise. Your existing exercise files are not reset by the new walkthrough.

## What is available?

| Material | Status |
|---|---|
| Lesson 00: four-part walkthrough, practice steps, exercise, hints, and solution | Implemented; revised after the first learner trial |
| Linux/WSL instructions, Dockerfile, and automated host checks | Included; actual execution results are recorded in [Progress](PROGRESS.md) |
| Lesson 01 — Toolchain and Cargo | Planned; will deepen the tools first used in Lesson 00 |
| Remaining host lessons and Embassy track | Planned, not implemented |

**Phase 1 is still in progress.** Passing build checks is not the same as demonstrating that the explanation works for a new learner. The revised lesson needs a fresh learner walkthrough. No embedded build or board execution is claimed.

## After the walkthrough: repository checks

The root Make commands remain available for checking the supplied material, but they are not your introduction to Rust. After following the lesson, you can run these from the repository root:

```bash
make run
make verify
```

`make run` runs the supplied readings example, not your Hello World practice file. `make verify` checks complete examples and supplied solutions, compiles the unfinished exercise, and checks the displayed walkthrough programs in a temporary project. It does **not** mean your exercise is finished and does not edit your practice project.

Cargo is the Rust project tool; Make only gives convenient shortcuts. Each implemented lesson has a Cargo package and Makefile. The repository root is not a Cargo package. The supplied host packages are under `host/`; practice projects, exercises, and solutions are separate.

## Course and contributor documents

| Document | Purpose |
|---|---|
| [Curriculum](CURRICULUM.md) | The planned 27-lesson host track, 14-lesson embedded track, and optional extensions |
| [Implementation plan](IMPLEMENTATION_PLAN.md) | Small development phases and teaching standards |
| [Progress](PROGRESS.md) | Current implementation, learner feedback, scope clarifications, and verification evidence |
| [Contributor guide](CONTRIBUTING.md) | How to add lessons without weakening the explanations or checks |
| [Authoring instructions](AGENTS.md) | Instructions for coding assistants, including lessons learned from reader feedback |
| [Tool versions](docs/tool-versions.md) | The chosen toolchain and what is, and is not, pinned |

Feedback about an unclear explanation is as valuable as a bug report. Include the lesson, what you tried, and the point where the explanation stopped making sense. Never include secrets or private project code.
