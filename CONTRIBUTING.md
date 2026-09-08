# Contributing a lesson

This repository teaches people, not just compilers. Read the [curriculum](CURRICULUM.md), [implementation plan](IMPLEMENTATION_PLAN.md), and [current progress](PROGRESS.md) before expanding it. Start with one complete lesson rather than a set of empty future packages.

## Teaching standard

Explain what a program does before discussing its abstractions. Define new terms near their first use. Prefer `reading`, `received_bytes`, and `command_receiver` over unexplained abbreviations. Keep standard Rust and hardware API names recognizable. A short conventional name is fine when its meaning has been explained.

Write the example, tests, exercise, hints, and explained solution together. Do not depend on a learner's completed earlier exercise. Use C++ and Python comparisons carefully: compare the same inputs and behavior without claiming the languages have identical type or ownership rules.

Use the [lesson template](docs/lesson-template.md) as a writing checklist, not a requirement to create unnecessary files. [AGENTS.md](AGENTS.md) also applies to coding assistants.

## Check a proposed change

From the repository root after [setup](docs/setup-linux.md):

```bash
make verify
make comparisons
python3 scripts/check_exercise_baseline.py
git diff --check
```

`make verify` checks complete code and compiles unfinished exercises without executing their assertions. It also validates local Markdown file paths, matching acceptance tests, and isolated compiler failures and repairs. `make comparisons` requires `g++` and checks actual output from all three languages.

The baseline script uses a temporary package with the old rule and the acceptance suite. It requires exactly the four intended failures, then substitutes the complete solution and requires a passing suite. It does not rewrite learner files or insist that a learner leave their exercise unsolved. A missing compiler or a compilation failure is not accepted as a successful behavioral demonstration.

Use `make fmt` only when you intend to change complete Rust sources. `make fmt-check` and `make verify` must not rewrite them. Exercise directories have their own `make fmt` command. Keep exercise and solution `tests/acceptance.rs` files identical; learner-added tests belong in `tests/your_cases.rs`.

## Evidence and scope

Use a small branch and pull request. Record commands actually run, their environment, and results; label unavailable checks. Keep learner feedback separate from author review. Never fabricate compiler output, coverage numbers, or board observations.

The automated checks run on GitHub-hosted Linux machines with read-only repository permissions, no secrets, and no board access. Do not move public pull-request execution onto a persistent workstation with a connected board. Firmware work needs a separate review of its execution environment.

Update [Progress](PROGRESS.md), navigation, and the tool-version note when applicable. Preserve existing lesson numbers and keep the next small task visible. Coverage and embedded testing remain later lessons, not hidden prerequisites for the orientation.
