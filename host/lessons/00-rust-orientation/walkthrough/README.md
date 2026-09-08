# Complete source copies for the Lesson 00 walkthrough

These are reference copies of the small programs shown in the four [lesson parts](../README.md). They are not separate lessons or packages. A learner creates one Cargo project under `practice/lesson-00/hello_rust/` and gradually replaces its `src/main.rs` as instructed.

Read the explanation before opening the source copies. All required programs are also printed in full in the walkthrough; no step depends on a hidden helper or an import from this directory.

| File | Purpose |
|---|---|
| `hello_world.rs` | The first three-line program |
| `changed_message.rs` | Save a change and observe new output |
| `greeting_function.rs` | Define and call a no-argument function |
| `function_parameter.rs` | Pass an integer to a function |
| `explicit_return.rs` | Introduce returning a Boolean using familiar explicit syntax |
| `tail_return.rs` | Express the same result as a final expression |
| `mutable_counter.rs` | Separate variable declarations from updates |
| `condition.rs` | Use a Boolean result to select a branch |
| `count_readings.rs` | Combine an array, loop, and comparison |
| `first_tests.rs` | Test the function in the same source file |

For authors, `python3 scripts/check_walkthrough.py` from the repository root checks that these files match the complete programs printed in the lesson. It creates a fresh temporary Cargo project, builds and runs all ten steps, checks the direct-compiler Hello World path, and verifies the deliberate compiler/test failures and their repairs. It does not read, write, or reset a learner's `practice/` directory.

The explicit-return program is valid Rust used to teach a familiar spelling before the final-expression form. Source copies receive formatting and compiler/runtime checks; they are not extra automatic Cargo targets, and the explicit-return teaching step is not rewritten merely to satisfy a style suggestion. The regular lesson and solution keep their existing Clippy checks.
