# Rust for Experienced Programmers

A planned, hands-on Rust course for programmers familiar with C, C++, and Python, followed by embedded development with Embassy on the NUCLEO-H723ZG.

The goal is to write Rust you can explain, change, debug, and test—not simply recognize syntax in generated code.

## Current status

**Planning stage. No runnable lessons are available yet.** The curriculum and implementation plan are documented; implementation phases have not started. No successful board execution is implied.

## Start here

| Document | Purpose |
|---|---|
| [Curriculum](CURRICULUM.md) | What the course will teach: 27 general Rust lessons, 14 embedded lessons, and six optional extensions. |
| [Implementation plan](IMPLEMENTATION_PLAN.md) | Small development phases, teaching standards, verification requirements, and the first implementation task. |
| [Authoring instructions](AGENTS.md) | A short guide for coding assistants; contributors can use the same standards. |

## What the course is designed to offer

Each lesson will have its own Cargo package and Makefile, a runnable worked example, an exercise, gradual hints, an explained solution, and appropriate tests. Examples will use deliberate names and introduce technical vocabulary when it is needed.

The opening lesson compares a small task in C++, Python, and Rust. Testing begins there and develops into automated unit and integration tests, linting, coverage, and testing on real hardware.

Linux, including WSL, is the primary environment. Docker is planned for reproducible builds and host-side checks. The embedded track assumes a connected NUCLEO-H723ZG; extra sensors are not required for the core course. macOS and native Windows are secondary paths where support stays simple.

## First implementation step

Build the minimum working setup and complete Lesson 00 before expanding the lesson template. See [Phase 1](IMPLEMENTATION_PLAN.md#phase-1--make-the-first-experience-work) and the [first implementation request](IMPLEMENTATION_PLAN.md#9-first-implementation-request).

Lessons will be linked here as they become available. Build results, board execution, and learner feedback will be reported separately.
