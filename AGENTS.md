# Instructions for coding assistants

This is a tutorial for experienced C, C++, and Python programmers learning to write Rust independently. Teaching quality matters as much as executable code.

## Before making changes

Read `CURRICULUM.md` for lesson coverage and `IMPLEMENTATION_PLAN.md` for phase scope, teaching standards, and completion checks. Inspect the current repository and verification notes; do not assume a planned lesson is already implemented.

Implement only the requested phase or smaller batch. Normally complete one lesson at a time; two small, closely related lessons may share a change. Do not generate all remaining lessons or create empty packages. Do not renumber the approved curriculum casually.

## Write for learners

Use plain explanations and define necessary technical terms when first introduced. Explain new Rust punctuation near its first use. Build on programming experience without assuming Rust fluency.

The first learner trial found that Lesson 00 assumed knowledge of Cargo, main-file creation, Hello World, and function syntax. Do not repeat that mistake: introduce tools before their commands; start with one `src/main.rs`; teach definition versus call, parameter types, explicit returns, and then final expressions before introducing `pub`, `use`, or a library split. Later lessons must rely on concepts actually taught, not concepts merely listed in the curriculum.

For hands-on steps, label the terminal directory, exact file, whether code replaces or extends that file, the save/run action, and the expected result. Show complete small programs, not unexplained fragments. Give natural stopping points instead of compressing foundational material to meet the former orientation duration. Check printed runnable programs against source copies and execute the new-project path, not just the finished repository package.

Choose deliberate names: `reading`, `command_receiver`, `elapsed_time`, and `rejects_empty_command`, not unexplained `x`, `rx`, `dt`, or `test1`. Preserve standard language/library names and explain conventional short generic or lifetime names. Favor clarity over either cryptic brevity or excessive length.

Keep examples small. Do not introduce unexplained abstractions, iterator chains, or async code before their lessons. Comments explain decisions and constraints. C++/Python comparisons must be fair and use matching behavior.

Deliver the explanation, worked example, exercise, hints, explained solution, and tests together. Keep hints and solutions separate from the default walkthrough. A learner should be able to predict, modify, test, and explain the code.

## Build and verify honestly

Follow the curriculum's separate host/embedded workspaces and separate example/exercise/solution packages. Keep Cargo authoritative and Makefiles small. Do not allow board target settings to leak into host checks. Learner-owned `practice/` files must never be reset or used as repository verification input.

Regular verification checks complete examples and solutions, not unfinished exercise assertions. Commands must identify what they tested. Isolate intentional compiler failures. Verification must not silently flash hardware or rewrite source files.

Run the documented checks that the environment supports and record actual results. Name unrun checks and blockers. Keep firmware build success separate from on-device execution. A learner's connected board is not automatically accessible from a remote session. Never invent hardware results, timings, coverage numbers, or learner feedback.

Inspect current official documentation before selecting version-dependent APIs or tools. Preserve pinned versions and lockfiles; recheck affected earlier lessons after shared changes. Do not weaken tests or suppress broad lint groups just to make checks pass.

End each batch with a summary of delivered lessons, checks and results, limitations, and the next small task. Update progress only to match evidence. Do not claim later phases are complete or promise unattended future work.
