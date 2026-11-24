# Contributing a lesson

Work on one complete lesson at a time. Check its scope and the current progress before you start. [Curriculum](CURRICULUM.md) · [Implementation plan](IMPLEMENTATION_PLAN.md) · [Progress](PROGRESS.md)

## Teaching standard

Explain what a program does before discussing its abstractions. Define new terms near their first use. Prefer `reading`, `received_bytes`, and `command_receiver` over unexplained abbreviations. Keep standard Rust and hardware API names recognizable. A short conventional name is fine when its meaning has been explained.

Lesson 00 is an example-only orientation. When a later lesson includes an exercise, write its tests, hints, and explained solution together. Give each lesson an independent starting point. For cross-language comparisons, use matching inputs and behavior. Use `COMPARISON.md` when readers benefit from seeing the complete programs together.

Use the lesson checklist to plan the material and add files as needed. [Lesson template](docs/lesson-template.md) · [Instructions for coding assistants](AGENTS.md)

## Check a proposed change

From the repository root after [setup](docs/setup-linux.md):

```bash
make verify
make comparisons
git diff --check
```

`make verify` runs formatting, Clippy, and local Markdown link checks. It checks the printed Rust programs against their source copies and runs them in a temporary Cargo project. `make comparisons` requires `g++` and checks the readings program's output in all three languages.

Use `make fmt` when you intend to format the supplied Rust sources. Verification runs the formatting check in read-only mode.

## Evidence and scope

Use a small branch and pull request. Record commands actually run, their environment, and results; label unavailable checks. Keep learner feedback separate from author review. Never fabricate compiler output, coverage numbers, or board observations.

The automated checks run on GitHub-hosted Linux machines with read-only repository permissions, no secrets, and no board access. Do not move public pull-request execution onto a persistent workstation with a connected board. Firmware work needs a separate review of its execution environment.

Update [Progress](PROGRESS.md), navigation, and the tool-version note when applicable. Preserve existing lesson numbers and keep the next small task visible. Coverage and embedded testing remain later lessons, not hidden prerequisites for the orientation.
