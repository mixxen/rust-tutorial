# Rust for Experienced Programmers

## Curriculum proposal for `mixxen/rust-tutorial`

**Status:** Curriculum plan; no lesson implementations or hardware verification are implied.

**Revision:** 2 — added Lesson 00, a hands-on syntax and C/C++/Python orientation. Existing lesson IDs are unchanged.

**Audience:** Experienced C, C++, and Python programmers who are new to writing Rust independently.

**Primary environment:** Linux, including WSL 2; Docker for reproducible development and CI. macOS and native Windows are secondary, low-maintenance paths.

**Embedded platform:** NUCLEO-H723ZG, connected to the learner's computer. Embassy is the embedded framework.

**Shape:** 41 core lessons: 27 general Rust lessons (00–26) and 14 embedded lessons, plus six optional extensions. Most lessons target a 30–60-minute session; capstones and advanced hardware labs may take multiple sessions.

## 1. Purpose and teaching approach

The goal is to develop independent Rust fluency: write a small program, explain its ownership and error-handling decisions, debug it, test it, and modify it without relying on generated code that the learner cannot explain.

Teach programming concepts only where Rust changes the learner's existing mental model. Spend relatively little time on loops and arithmetic, but substantial time on ownership, borrowing, error modeling, trait-based design, and async behavior.

Use a recurring device-and-telemetry theme without making every lesson depend on the previous lesson's implementation. Each lesson starts from a complete, known baseline. Learners should be able to revisit a lesson without rebuilding their earlier exercise solutions.

The course starts with Lesson 00: a short, hands-on syntax tour that uses familiar C++ and Python examples to orient the learner before the detailed toolchain and language lessons. Testing starts in Lesson 00. Dedicated testing lessons deepen the practice rather than introduce it for the first time. Early lessons provide scaffolding for attributes and test syntax that will be explained more fully later.

Selected lessons include a review of plausible but flawed AI-generated code. The normal learning sequence is: predict the behavior, attempt the exercise, read compiler/test feedback, then consult hints or AI. Correct code is not enough; learners must explain the relevant invariants and provide evidence for their claims.

### Completion outcomes

By the end, a learner should be able to:

- Build and organize Rust applications and libraries, with intentional ownership, borrowing, and error-handling APIs.
- Write automated tests, interpret lint and coverage reports, and distinguish test evidence from unsupported confidence.
- Build concurrent host applications and explain async execution, cancellation, and resource ownership.
- Implement Embassy firmware on the NUCLEO-H723ZG, keeping portable logic separate from hardware-specific integration.
- Run host tests, target tests, and host-driven hardware tests, and produce a small reproducible acceptance report.

## 2. Environment and toolchain policy

| Area | Planned approach |
|---|---|
| Rust | Rust 2024 edition; pin an exact stable toolchain after bootstrap verification rather than continually tracking `stable`. |
| Build tooling | Cargo is authoritative. Per-lesson Makefiles are thin wrappers, and lesson READMEs also show the underlying Cargo commands. |
| Editor | Document VS Code with rust-analyzer as a convenient path; do not require an editor. |
| Linux | Primary development, build, test, flash, and debug environment. |
| WSL 2 | Primary Windows path. Document USB attachment, device permissions, and reconnect troubleshooting. |
| Docker | Provide a versioned image for compilation, host tests, coverage, and firmware builds. Use a non-root development user and cache Cargo downloads/builds. |
| Hardware access | Prefer flashing/debugging directly from Linux or WSL. Containerized USB access is an optional recipe, not a prerequisite. A host can flash an ELF built in Docker. |
| Other platforms | Provide ordinary Cargo command equivalents and brief setup notes where maintenance is small; do not make native-Windows Makefile support a first-release requirement. |
| Dependencies | Commit workspace lockfiles and lockfiles for standalone exercise/solution packages; pin external tool versions and record them centrally. |
| Embassy | Pin a compatible set of releases, or an exact commit only when necessary. Do not follow a moving Git branch. |
| Optional nightly tools | Isolate them from the stable core course; document their separate versions and invocation. |

Microsoft documents WSL USB access through `usbipd-win`; it is not something the tutorial should assume is automatically configured. [R1] Probe access and operating-system setup are documented by probe-rs. [R2]

The embedded compilation target will be `thumbv7em-none-eabihf`, with the exact STM32H723ZG chip configuration. The target is documented by Rust, and Embassy publishes STM32H723ZG-specific API documentation. [R3][R4] The pinout, clock configuration, linker setup, ST-LINK chip identifier, and supported board revision must be validated in the bootstrap milestone—not copied blindly from a different STM32H7 board.

Core board labs use onboard LEDs, the user button, timers, and the ST-LINK debug/serial connection. ST documents the integrated debugger, LEDs, button, and virtual-COM capability. [R5] Additional sensors, jumper wiring, a logic analyzer, and Ethernet are not required for the main path.

## 3. Repository organization

Use two deliberately separate Cargo workspaces: `host/` and `embedded/`. There is no root Cargo workspace; the root Makefile orchestrates explicitly selected checks.

A Cargo workspace gives its members shared dependency resolution, a lockfile, and a build-output directory. [R6] Separating the host and firmware workspaces keeps the normal host test command away from board-only executables and chip-specific build settings.

```text
rust-tutorial/
├── README.md
├── CURRICULUM.md
├── CONTRIBUTING.md
├── rust-toolchain.toml
├── Makefile
├── .github/workflows/
│   ├── host.yml
│   ├── firmware.yml
│   └── docs.yml
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── docs/
│   ├── setup-linux.md
│   ├── setup-wsl.md
│   ├── docker.md
│   ├── testing-strategy.md
│   ├── nucleo-h723zg.md
│   ├── hardware-testing.md
│   └── ai-assisted-learning.md
├── mk/
│   ├── host.mk
│   └── embedded.mk
├── scripts/                         # Small orchestration/check helpers
├── host/
│   ├── Cargo.toml                   # Host reference workspace
│   ├── Cargo.lock
│   └── lessons/
│       ├── 00-rust-orientation/
│       ├── 01-toolchain-and-cargo/
│       ├── 02-types-and-expressions/
│       ├── ...
│       └── 26-ci-and-reproducibility/
├── embedded/
│   ├── Cargo.toml                   # Firmware and portable-core packages
│   ├── Cargo.lock
│   ├── .cargo/config.toml           # Target-scoped configuration
│   ├── board-support/              # Minimal, documented H723ZG support
│   └── lessons/
│       ├── e01-board-bringup/
│       ├── ...
│       └── e14-capstone-verification/
├── exercises/                      # Standalone starter packages, by lesson ID
├── solutions/                      # Standalone solution packages, by lesson ID
├── electives/                      # Standalone packages, not core prerequisites
└── reports/                        # Generated output; ignored by Git
```

Every lesson has its own primary Cargo package, `Cargo.toml`, README, Makefile, and runnable example. Packages use unique names such as `lesson-03-ownership` and `lesson-e04-embassy-tasks`.

More substantial embedded lessons may add a companion `core/` library package for shared host/target logic. Capstones may contain multiple cooperating packages, but each still has a single documented lesson entry point.

Keep target-specific runner and linker settings out of host builds. Do not set a repository-wide embedded `build.target` or global linker flags. Root automation must invoke Cargo from the intended directory or pass configuration explicitly: Cargo configuration discovery depends on the invocation location. [R7]

Portable embedded libraries are tested with an explicit host target and cross-compiled for the MCU. Only those selected libraries—not the whole firmware workspace—are passed to host testing and coverage. Host `std` features and embedded time-driver features must not leak into the firmware configuration.

### Worked examples, exercises, and solutions

The primary lesson package is the small, complete worked example. It builds and passes its tests on a fresh checkout.

Exercises and full solutions are separate packages, outside the reference workspaces, with matching public acceptance-test contracts. Exercise tests are expected to fail until the learner finishes the task. They run only through an explicit exercise command, never as hidden failures in normal repository CI.

CI runs the worked examples and complete solutions. It also checks that exercise scaffolds remain usable. Intentionally non-compiling teaching examples use compile-fail tests or documented isolated fixtures, not broken normal build targets.

Avoid mutually exclusive `exercise` and `solution` Cargo features. Each command should visibly identify the package it tested, so a learner cannot mistake solution test results for verification of their own work.

## 4. Standard lesson format

A normal primary package looks like this:

```text
03-ownership/
├── Cargo.toml
├── Makefile
├── README.md
├── EXERCISE.md
├── HINTS.md
├── SOLUTION.md
├── src/
│   ├── lib.rs
│   └── main.rs                     # Or a small runnable example
├── tests/                         # Where relevant
│   └── public_api.rs
└── fixtures/                      # Only when needed
```

Every README contains the objective, prerequisites, commands, explanation, runnable walkthrough, relevant C/C++/Python comparison, expected output, exercise, verification criteria, and a few review questions. Prefer explanations adjacent to code rather than extensive unexplained source listings.

Each exercise asks the learner to change observable behavior. Add boundary or failure-case tests whenever applicable. Hints progress from conceptual guidance to a more concrete suggestion; the complete solution explains why it works and discusses an alternative.

### Command contract

| Command | Meaning |
|---|---|
| `make help` | Explain supported targets and underlying tools. |
| `make run` | Run the worked example; board lessons clearly state that this flashes/runs hardware. |
| `make test` | Run ordinary host tests, or the embedded lesson's explicitly selected portable-core tests. |
| `make fmt` / `make lint` | Format the selected code; run the documented Clippy policy. |
| `make coverage` | Generate host-side coverage for the declared code scope. |
| `make verify` | Run the lesson's non-hardware reference checks; root verification also checks complete solutions. |
| `make exercise` / `make solution` | Run acceptance tests against the clearly identified starter or solution package. |
| `make flash` | Explicitly flash the firmware. |
| `make test-target` | Execute on-device tests with the target test harness. |
| `make hil` | Run host-driven hardware acceptance tests. |

Unsupported checks report “not applicable,” rather than presenting a misleading passing result. A requested hardware test fails clearly when no board is available. Repository-wide verification never silently flashes devices.

## 5. General Rust curriculum

The entries below are proposed lesson scopes and completion evidence, not existing repository contents.

### Part 0 — Rust orientation for C/C++ and Python programmers

**Lesson 00 — A first look at Rust: syntax, similarities, and differences**

**Package:** `host/lessons/00-rust-orientation/` (`lesson-00-rust-orientation`).

**Outcome:** Read a small Rust program without getting stuck on punctuation, modify its behavior, run its tests, and identify which familiar C++/Python assumptions need revisiting. This is an orientation, not a compressed ownership course.

**Session size:** Approximately 45–60 minutes after environment setup. No board is required.

**Prerequisites:** Existing programming experience and the minimal Linux/WSL setup recipe or supplied development container. Provide the exact commands needed to run the supplied package; do not require completion of Lesson 01 first. Lesson 01 subsequently explains installation choices, Cargo, and package creation in depth.

| ID and package | Concepts to practice | Exercise and evidence |
|---|---|---|
| 00 `rust-orientation` | Basic syntax, side-by-side C++/Python comparisons, reading compiler feedback, and a brief preview of Rust's ownership model. | Read equivalent small programs, predict their output, change a threshold rule in Rust, and use boundary tests to verify it. Explain one compiler error and one behavioral test failure. |

#### Guided walkthrough

| Segment | Scope |
|---|---|
| Same task, three languages | Show a small reading-threshold program in C++, Python, and Rust. Compare the entry point, variable declarations, a function, a loop, and output. Keep the algorithm and sample data identical. |
| Essential syntax | Practice `fn`, `let`, `let mut`, type annotations, function parameters and `->` return types, braces, semicolons, arrays, `if`/`else`, and `for`. Explain `println!` and `#[test]` only as needed to run the example. |
| Similar appearance, different rules | Compare inferred types with dynamic typing, mutation with shadowing, and statements with value-producing expressions. Repair short examples involving immutable bindings, a missing Boolean condition, and an unintended trailing semicolon. |
| Read, change, test | Run the worked example and its tests. In the separate exercise package, change a strict threshold to an inclusive threshold, add boundary assertions, and verify the revised behavior. |
| What comes next | Preview ownership and borrowing with one annotated owned-value example. Point to the dedicated lessons instead of requiring the learner to master moves, references, lifetimes, or traits now. |

The introductory syntax follows the Rust Book's common-programming-concepts material. [R19] Keep the required hands-on work limited to scalar values, a fixed-size array, ordinary control flow, and a tiny pure function; leave advanced vocabulary in the reference sheet.

#### Cross-language comparison guide

| Topic | Familiar connection | Rust distinction to make explicit |
|---|---|---|
| Types and inference | Compare a C++ local declared with `auto` and a Python name assigned a value. | Rust can infer a local type, but the binding still has a compile-time type; inference is not dynamic typing. [R22][R25] |
| Variables and mutation | Start with ordinary assignment and familiar C++ `const` declarations. | `let` bindings are immutable by default; `let mut` enables mutation. A new `let` can shadow an earlier binding, including with a different type. Do not present binding immutability as a guarantee of deep immutability. [R20] |
| Functions and returns | Compare C++ function signatures and Python `def` with Rust `fn`. | Function parameters have declared types; `->` introduces the return type. A tail expression can produce the return value without `return`. [R21] |
| Blocks and semicolons | Braces resemble C++; Python programmers already distinguish statements from expressions. | A block can produce a value. Adding a semicolon to its intended tail expression can discard that value and cause a type mismatch. [R21] |
| Conditions and loops | Compare C++ branches/range-based loops and Python `if`/`for`. | Conditions require `bool`, not implicit integer truthiness. Show `if` as an expression and a basic array/range loop. [R23] |
| Resource ownership | Connect scope-based cleanup to C++ RAII, then contrast it with Python assignment to an existing object. | An owned, non-`Copy` Rust value can move on assignment; the old binding is then unusable. Neither an implicit deep copy nor an unrestricted second alias should be assumed. Full treatment belongs in Lessons 03–04. [R24][R25] |

Use the C++ and Python examples as comparisons, not as specifications for all Rust behavior. In particular, do not describe Rust simply as C++ with a borrow checker, claim that modern C++ lacks automatic resource management, or imply that a program compiling proves its behavioral correctness.

#### Recognize now; explain later

Supply a short `CHEATSHEET.md` with tiny annotated examples and links to the later lessons. The learner need not write code using all these forms in Lesson 00.

| Syntax or idea | Later treatment |
|---|---|
| `&value`, `&mut value`, moves, and explicit cloning | Lessons 03–04: ownership and borrowing. |
| `String` and `&str` | Lesson 05: owned text and borrowed string views. |
| `struct`, `enum`, `match`, `Option`, `Result`, and `?` | Lessons 06–07: modeling data, optional values, and recoverable errors. Use `Option` to preview explicit absence rather than a nullable ordinary value. [R26] |
| `use`, `pub`, `impl`, and traits | Lessons 08 and 10: organization, APIs, and trait-based design. |
| `async` and `.await` | Lessons 22–23 and the Embassy track. |

#### Exercise: change a threshold rule

Provide a working program that examines `[18, 22, 25, 29]` with a limit of `25`. Its small pure function initially implements a strict comparison: `value > limit`. The walkthrough predicts and then confirms that exactly one reading qualifies.

The exercise changes the requirement to include readings equal to the limit: `value >= limit`. The learner updates the separate starter implementation, adds assertions for below/equal/above the limit, and verifies that the example now counts two qualifying readings. Include a negative-value case so the tests are not merely copies of the demonstration data.

Supply one intentionally incorrect implementation that still compiles, such as retaining `>` instead of `>=`, and show which boundary assertion catches it. Keep compiler-error demonstrations separate: a rejected program and a wrong-but-compiling program teach different lessons. Fix diagnostics one at a time and restore the passing reference example afterward.

**Completion evidence:** The learner can explain the main program, the mutability of the counter, the type and return value of the predicate, why the equality case matters, and the difference between successful compilation and correct behavior. They can make the change without replacing the package with an unexplained AI-generated solution.

#### Planned lesson package

```text
host/lessons/00-rust-orientation/
├── Cargo.toml
├── Makefile
├── README.md
├── CHEATSHEET.md
├── EXERCISE.md
├── HINTS.md
├── SOLUTION.md
├── src/
│   ├── lib.rs                      # Small scalar predicate and unit tests
│   └── main.rs                     # Fixed sample data, loop, and output
└── comparisons/
    ├── threshold.cpp               # C++ reading aid; optional local execution
    └── threshold.py                # Python reading aid; optional local execution
```

The exercise and complete solution follow the repository's existing separate-package convention. `make run`, `make test`, `make lint`, and `make verify` operate on the worked example; `make exercise` and `make solution` identify their respective packages. An extra C++ compiler is not a prerequisite for running the Rust lesson. Cross-language examples must be checked for consistent sample results when authored.

**Transition:** Lesson 00 answers “What am I looking at, and how do I make a small change?” Lesson 01 explains the tools and creates a package from scratch. Lesson 02 revisits the basic syntax with numeric boundaries, conversions, and more precise type reasoning. Lessons 03–04 then develop the ownership and borrowing model.

### Part A — Rust foundations

**Outcome:** Write small Rust programs and explain how values move through them.

| ID and package | Concepts to practice | Exercise and evidence |
|---|---|---|
| 01 `toolchain-and-cargo` | Explain the tools used in Lesson 00: toolchain, package layout, build/run/check/test, compiler diagnostics, formatting. | Create a tiny unit-conversion library and executable from a blank package. Distinguish a compilation failure from a failing test, repair both, and run the checks. |
| 02 `types-and-expressions` | Deepen the syntax from Lesson 00: bindings and shadowing, scalar types, functions, expression types, matching basic values, checked integer conversions and numeric boundaries. | Implement a bounded numeric conversion; test ordinary values, boundaries, and invalid input. Explain the type and conversion choices rather than repeat the introductory syntax tour. |
| 03 `ownership-and-moves` | Ownership, moves, `Copy`, `Clone`, destruction; contrast with C++ resource ownership. | Repair moved-value errors without indiscriminate cloning. Predict which values remain usable and when resources are released. |
| 04 `borrowing-and-slices` | Shared/mutable references, aliasing restrictions, slices, borrowing through function calls. | Process a buffer in place and expose a borrowed view. Explain and repair an overlapping-borrow example. |
| 05 `strings-and-bytes` | `String`, `&str`, byte slices, UTF-8, owned versus borrowed text. | Parse text without assuming character indices equal byte offsets; test ASCII, multibyte input, and malformed byte data. |
| 06 `structs-enums-and-patterns` | Structs, methods, enums with data, `Option`, exhaustive matches. | Model device states without sentinel values or incompatible Boolean combinations. Add and test a new state. |
| 07 `errors-and-results` | `Result`, `?`, recoverable errors, `panic!`, `unwrap`/`expect`, useful context. | Replace panics in a parser with a small explicit error type; assert the distinct failure cases. |
| 08 `modules-and-packages` | Modules, visibility, library/binary separation, dependencies, features, derive attributes, rustdoc. | Split a program into a library and thin executable; document its public API and add a working documentation example. |

**Checkpoint:** Starting from a blank package, implement a small parser and explain its ownership and error behavior. Do not assess the learner merely on whether generated code compiles.

### Part B — Idiomatic design and testable code

**Outcome:** Design clear Rust APIs and make dependencies controllable in tests.

| ID and package | Concepts to practice | Exercise and evidence |
|---|---|---|
| 09 `lifetimes-and-borrowed-apis` | Lifetime relationships, elision, structs containing references, owned alternatives. | Return borrowed fields from an input buffer; explain why a returned reference cannot outlive its source. |
| 10 `traits-and-generics` | Trait bounds, associated types, static/dynamic dispatch, trait objects. | Define a reading source and implement real/fake sources. Compare a generic API with a trait-object API. |
| 11 `iterators-and-closures` | Iterator adapters, closures, captures, `iter`/`iter_mut`/`into_iter`, collections. | Filter and aggregate telemetry using both loops and iterators. Test equivalent behavior and explain ownership differences. |
| 12 `newtypes-and-conversions` | Newtypes, `From`/`TryFrom`, validated construction, units, a small typestate example. | Prevent mixing raw counts with engineering units and reject invalid construction through tested APIs. |
| 13 `smart-pointers-and-interior-mutability` | `Box`, `Rc`, `Weak`, `Cell`/`RefCell`, when plain borrowing is simpler. | Refactor shared state and explain the ownership graph; reproduce and remove an unnecessary runtime borrow failure. |
| 14 `designing-for-tests` | Pure logic, dependency injection, fake clocks and I/O, state transitions. | Extract a time-dependent state machine from I/O code. Test it using explicit inputs and simulated time, without sleeping. |

### Part C — Automated testing and a useful application

**Outcome:** Test behavior systematically and interpret quality tools rather than chase a green badge.

| ID and package | Concepts to practice | Exercise and evidence |
|---|---|---|
| 15 `test-organization` | Unit, integration, documentation, and compile-fail tests; fixtures and test isolation. | Test a library through private and public interfaces; add an API example that must compile and a misuse that must not compile. |
| 16 `formatting-linting-and-docs` | rustfmt, Clippy, warning policy, documentation checks, justified local exceptions. | Clean up a deliberately poor implementation without blanket lint suppression; explain each material change. |
| 17 `coverage-and-test-quality` | Line/region coverage, missing error paths, weak assertions, honest exclusions. | Find a defect in highly covered code. Strengthen the assertions, cover a missed failure path, and inspect the HTML report. |
| 18 `property-based-testing` | Input generators, invariants, shrinking, preserving regression examples. | Property-test a bounded encoder/decoder: round trips, malformed inputs, empty input, truncation, and overflow behavior. |
| 19 `cli-files-and-serialization` | CLI arguments, buffered I/O, serialization, exit status, separation of I/O and logic. | Build a log summarizer; black-box test the executable with temporary files, bad input, and expected exit codes. |
| 20 `capstone-telemetry-analyzer` | Integrate ownership, API design, errors, documentation, and testing. | Deliver a CLI that reads telemetry, validates it, filters it, and emits a deterministic summary. Include a short acceptance report. |

Rust distinguishes unit tests from integration tests through their relationship to the library and its public API. [R8] Documentation tests also remain part of the planned test suite. [R9] Clippy supports making warnings fail CI, while its documentation advises selecting restriction lints deliberately rather than enabling the entire group. [R10] Property-based testing will use `proptest`. [R11]

### Part D — Concurrency and engineering practice

**Outcome:** Understand the host-side concepts that make embedded async code comprehensible.

| ID and package | Concepts to practice | Exercise and evidence |
|---|---|---|
| 21 `threads-and-message-passing` | Threads, `Send`/`Sync`, `Arc`, mutexes, channels, shared ownership. | Build a bounded worker pipeline and implement clean shutdown. Test missing, duplicate, and reordered results as appropriate. |
| 22 `async-and-futures` | Futures, polling/waking at a conceptual level, executors, `async`/`await`, Tokio; introductory `Pin` vocabulary. | Run two asynchronous activities and explain when each can make progress. Repair a blocking operation in async code. |
| 23 `async-coordination-and-testing` | Timeouts, cancellation, bounded channels, backpressure, shutdown, virtual time. | Handle a slow consumer and cancelled operation without losing ownership or hanging tests. Use controlled time where practical. |
| 24 `unsafe-boundaries` | Raw pointers, safety invariants, a narrow C ABI boundary, safe wrappers. | Wrap a tiny supplied C function, documenting pointer, length, lifetime, and ownership obligations. Most application code remains safe Rust. |
| 25 `measurement-and-performance` | Debug/release behavior, allocation, benchmarking, profiling concepts, code size. | Compare two implementations on the same workload, measure before changing code, and retain correctness tests. |
| 26 `ci-and-reproducibility` | Lockfiles, pinned tools, feature matrices, CI stages, artifacts, dependency review. | Package the host quality pipeline. Deliberately introduce failures and demonstrate that the correct jobs catch them. |

Minimal CI is present from the start of the repository. Lesson 26 teaches how it is designed and extended; it is not the first point at which the course uses CI.

## 6. Embedded Rust and Embassy curriculum

**Platform:** NUCLEO-H723ZG, with the learner's board connected.

**Learning order:** The normal path follows the general track. E01 can also be used early as a guided environment smoke test. A learner moving directly into firmware should first complete 00–18 and 21–23; the CLI capstone remains strongly recommended. Deep unsafe programming is not an Embassy prerequisite.

Embassy provides an async executor, hardware abstraction layers, and supporting components; the curriculum will explicitly distinguish Rust async syntax from the executor and hardware drivers that make progress possible. [R12] The `no_std` lessons distinguish `core`, `alloc`, and `std`; allocation is a deliberate policy choice rather than something inferred solely from `#![no_std]`. [R13]

| ID and package | Concepts to practice | Board exercise and evidence |
|---|---|---|
| E01 `board-bringup` | Probe discovery, exact target/chip selection, startup scaffold, flashing, RTT logging, basic debugger use. | Build and flash a supplied minimal example, observe LED activity, read a known log message, and record the working environment. |
| E02 `no-std-and-portable-core` | `no_std`/`no_main`, startup/panic roles, `core`/`alloc`/`std`, portable library boundaries. | Compile one logic library for both host and MCU. Run its host tests, then call the same implementation from firmware. |
| E03 `gpio-and-peripheral-ownership` | Peripheral singleton ownership, pin configuration, inputs/outputs, hardware resources as Rust values. | Drive onboard LEDs and read the user button. Explain a rejected attempt to give the same peripheral to two owners. |
| E04 `embassy-tasks-and-time` | Task spawning, timers, periodic work, cooperative execution, task state. | Run heartbeat and status activities concurrently. Compare blocking delay with asynchronous waiting and show the behavioral difference. |
| E05 `interrupts-and-debouncing` | Interrupt bindings, EXTI waits, event-driven input, debounce state machines. | Handle the button asynchronously. Test debounce logic with synthetic traces and separately observe the real switch. |
| E06 `channels-signals-and-shared-state` | Bounded channels, signals, mutex choices, static task storage, peripheral-owning tasks. | Build producer/consumer tasks with an explicit overload policy. Test queue saturation and document what is retained or dropped. |
| E07 `uart-command-interface` | Board virtual-COM route, async serial I/O, bounded framing, incomplete input, error responses. | Accept simple commands, return deterministic responses, and remain responsive under malformed or partial traffic. |
| E08 `dma-and-memory-awareness` | DMA buffer lifetimes, placement, cache coherency, alignment, target memory constraints. | Extend a known-working serial transfer using the pinned HAL's DMA path. Explain buffer ownership and validate the documented configuration in release builds. |
| E09 `testing-drivers-and-state-machines` | Portable control logic, hardware adapter traits, fake peripherals, injected failures. | Test a command-driven state machine on the host. Use embedded-HAL mocks where suitable and keep the firmware adapter thin. |
| E10 `on-device-tests` | Target test harnesses, initialization/reset, assertions, bounded test execution. | Run a small on-device suite through `embedded-test` and probe-rs. Cause a controlled failing test and inspect the reported failure. |
| E11 `hardware-in-the-loop` | Host orchestration, serial discovery, request/response assertions, deadlines, test artifacts. | Use a Python/pytest harness to exercise the running firmware. Verify valid/invalid commands and deterministic state transitions. |
| E12 `faults-timeouts-and-recovery` | Timeout policies, watchdog supervision, deliberate stalls, reset reasons, fault diagnostics. | Inject a controlled failure, verify the documented recovery policy, and record both expected and observed behavior. |
| E13 `capstone-device-supervisor` | Task architecture, ownership, bounded storage, commands, status, debounce, reliability. | Integrate a small asynchronous device supervisor using only the board and its USB connection. |
| E14 `capstone-verification` | Requirement-based tests, host/target/system evidence, repeatability, soak testing, release artifacts. | Run the automated acceptance suite, record resource observations, and deliver a reproducible verification report with explicit limitations. |

`embedded-hal-mock` supports hardware-independent tests against embedded-HAL traits. [R14] `embedded-test` provides target-side test execution with probe-rs, including async test support with the compatible Embassy integration. Pin and validate that integration rather than copying version-specific feature names from unrelated examples. [R15]

E08 is an introductory, tightly scoped DMA lesson, not an attempt to teach the entire Cortex-M7 memory system in one sitting. The provided board scaffold documents the actual clock/memory/cache policy. Broad changes to cache policy, networking DMA, or linker memory regions are advanced exercises and must not be introduced as unexplained fixes.

## 7. Capstones

### Capstone A: Telemetry analyzer

The tool accepts a documented telemetry format, validates records, filters them, computes summaries, and emits predictable text or JSON output. It must distinguish input errors from internal failures and return useful exit codes.

Acceptance evidence includes parser/unit tests, invalid and boundary inputs, encoder/decoder properties where applicable, black-box CLI tests, documentation examples, lint results, and coverage for the declared host code scope. Temporary files and deterministic fixtures keep tests independent of a learner's machine.

Use a small supplied dataset with normal, malformed, missing, and boundary-value records. Do not turn the capstone into a database, web service, or cloud deployment exercise.

### Capstone B: Asynchronous device supervisor

The firmware has a heartbeat, a debounced button, a bounded serial command interface, observable state transitions, and watchdog/recovery behavior. Suggested commands are `status`, `set-period`, `set-mode`, and a deliberately gated test-only fault injection command.

A pure Rust core defines protocol and state-machine behavior. Hardware tasks translate inputs into events and apply the resulting actions. The same core implementation is used by host tests and firmware; tests must not validate an independently rewritten behavioral model instead.

The Python harness sends commands, checks responses and counters, verifies timeouts within stated tolerances, and saves diagnostic information. Assertions about an LED physically illuminating or a button electrically transitioning remain manual unless an independent observation/actuation fixture is added. A firmware log is not sufficient evidence for those physical claims.

The final report identifies firmware/source revision, toolchain, board revision, test configuration, expected results, observed results, failures, and untested behavior. No certification or hard-real-time guarantee is implied.

## 8. Testing and coverage strategy

### Test layers

| Layer | Runs on | What it demonstrates |
|---|---|---|
| Unit and property tests | Host | Portable logic, parsing, validation, and state transitions under controlled inputs. |
| Integration and CLI tests | Host | Public APIs, module composition, executable output, files, and exit behavior. |
| Compile-fail/documentation tests | Host compiler/toolchain | API usage examples and intentional type-system constraints. |
| Cross-builds | CI or developer host | Firmware compiles and links for the selected target; this is not execution evidence. |
| On-device tests | NUCLEO-H723ZG | Assertions while actually executing on the MCU. |
| Host-driven system tests | Host plus NUCLEO-H723ZG | End-to-end command/response, timeout, state, and recovery behavior. |
| Manual physical observations | Board, learner, optional instruments | Physical behavior that the automated setup cannot independently observe. |

### Coverage policy

Use `cargo-llvm-cov` for host-side line/region coverage and HTML reports. Its documentation currently treats branch coverage and inclusion of doctests in coverage as unstable capabilities; keep them out of the stable baseline while continuing to execute documentation tests normally. [R16]

After Lesson 17, use a proposed **90% line-coverage floor for the designated portable application-core packages**, with documented exclusions. This is a teaching gate, not an industry requirement or proof of correctness. Early syntax examples, startup/linker code, generated code, hardware adapters, and incomplete exercises do not distort that denominator.

Track missing error paths and assertion quality, not only percentage. Include a deliberately highly covered but incorrect implementation. Collect instrumented child-process output when measuring CLI executable tests. Label host coverage separately from target execution results; do not advertise bare-metal firmware coverage based on host-only measurements.

### Quality policy

Formatting, ordinary lint checks, and tests apply from the first lesson. Complete reference implementations and solutions must pass. Use targeted, explained lint allowances for intentional teaching examples rather than global suppression.

Default examples avoid unnecessary `unsafe`. The unsafe lesson isolates and documents its boundary. Do not forbid constructs globally when the curriculum intentionally teaches them; apply stricter policies to the relevant packages and stages.

Default tests must not require internet connectivity, wall-clock sleeps, random external datasets, secret credentials, or a board unless explicitly marked hardware-dependent. Property-test failures should preserve reproducible regression cases.

## 9. CI and hardware automation

### Normal GitHub-hosted CI

Run formatting checks, Clippy, unit/integration/documentation/property tests, compile-fail cases, host coverage, and firmware compile/link checks. Build complete solutions separately. Validate supported feature combinations explicitly instead of blindly enabling mutually incompatible runtime or chip features.

Retain coverage reports and firmware artifacts where useful. Establish Linux as the required gate; add small macOS/Windows host smoke checks only when they do not create a second maintenance project.

### Hardware execution

The initial path is automated local execution against the learner's board. The course does not require a permanently connected cloud runner.

An advanced hardware-CI extension may use a dedicated isolated machine and a trusted private execution context. Never automatically execute arbitrary public pull-request code on a developer workstation with a connected board. GitHub explicitly warns about the persistent-compromise risks of self-hosted runners handling untrusted code. [R17]

Hardware jobs must select the correct probe/board, serialize access, reset to a known state, enforce deadlines, and save diagnostics. They must distinguish setup failure from a firmware assertion failure and must not retry failures until they happen to pass.

## 10. Optional extensions

These are not prerequisites for completing the core path. Each extension also receives its own Cargo package and lesson Makefile.

| ID | Topic | Example scope and requirements |
|---|---|---|
| X01 | Deeper C/C++ interoperability | Bindings, ownership transfer, ABI contracts, C++ wrapper boundaries, cross-language testing. |
| X02 | Python extensions | Expose the telemetry parser through a Python extension and compare results across language boundaries. |
| X03 | Macros and advanced abstractions | A small declarative macro, derive-macro concepts, deeper pinning or custom futures; avoid making a procedural-macro framework a prerequisite. |
| X04 | Advanced test methods | Fuzzing, mutation testing, and Miri where applicable; separate optional toolchains and interpret tool limitations. Cargo-fuzz is documented in the Rust Fuzz Book. [R18] |
| X05 | I²C/SPI driver development | Build and mock-test a small driver; physical bus tests require an explicitly documented external device and wiring. |
| X06 | Embassy networking | Extend the supervisor over Ethernet with bounded buffers and reconnect tests; requires a cable and suitable local network. |

## 11. Authoring and release milestones

### Milestone 1: Validate the course scaffold

Create the root navigation, lesson templates, initial host CI, and Linux/WSL/Docker setup. Implement Lesson 00 and the Lesson 01 tooling walkthrough as the first runnable host packages, including the orientation comparisons, exercise, solution, and tests. In parallel, validate a minimal H723ZG flash/log example and one host-testable embedded core library. Choose and record the actual working toolchain and crate versions.

This is a prerequisite for writing dozens of embedded examples: hardware and toolchain assumptions should fail early rather than after the curriculum has been implemented around them.

### Milestone 2: Complete the foundations and host application

Complete Lessons 00–20 in small groups, building on the two bootstrap lessons. Check each worked example, exercise contract, solution, and README command before adding more abstractions. Complete the telemetry analyzer before expanding into advanced concurrency.

### Milestone 3: Complete concurrency and the embedded track

Author 21–26 and E01–E14 against the validated scaffold. Keep the board support deliberately thin and explain any abstraction before making learners depend on it. Add on-device and host-driven tests progressively.

### Milestone 4: Harden and extend

Run a fresh-checkout walkthrough, review cross-language explanations, verify all executable documentation and failure demonstrations, and add only the electives that are useful. Mark hardware lessons as cross-built, board-tested, or awaiting board verification according to actual evidence.

## 12. Definition of done for a lesson

A lesson is ready when its documented commands work from a fresh checkout in the primary environment; its complete example and solution pass the appropriate checks; its exercise has a meaningful observable outcome; and its tests include relevant boundaries or failure behavior.

The learner can identify what the test suite establishes and what it does not. Each hardware lesson lists required equipment, recovery steps, and whether its results were actually obtained on the NUCLEO-H723ZG. Claims of successful board execution require recorded board execution, not just successful cross-compilation.

The intended result is not familiarity with Rust syntax alone. It is the ability to make a small, justified change, predict its consequences, and demonstrate its correctness with appropriately scoped evidence.

## References

These references support the platform and tooling decisions. Lesson content will link to the APIs and versions actually pinned when it is implemented.

- [R1: Microsoft — Connect USB devices to WSL](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
- [R2: probe-rs — Probe setup](https://probe.rs/docs/getting-started/probe-setup/)
- [R3: Rust — thumbv7em target support](https://doc.rust-lang.org/rustc/platform-support/thumbv7em-none-eabi.html)
- [R4: Embassy — STM32H723ZG API documentation, version 0.6.0](https://docs.embassy.dev/embassy-stm32/0.6.0/stm32h723zg/index.html)
- [R5: STMicroelectronics — NUCLEO-H723ZG](https://www.st.com/en/evaluation-tools/nucleo-h723zg.html)
- [R6: Cargo — Workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)
- [R7: Cargo — Configuration](https://doc.rust-lang.org/cargo/reference/config.html)
- [R8: The Rust Programming Language — Test organization](https://doc.rust-lang.org/book/ch11-03-test-organization.html)
- [R9: Cargo — cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
- [R10: Clippy — Usage](https://doc.rust-lang.org/clippy/usage.html)
- [R11: Proptest — Introduction](https://proptest-rs.github.io/proptest/intro.html)
- [R12: Embassy Book](https://embassy.dev/book/)
- [R13: Embedded Rust Book — no_std](https://doc.rust-lang.org/embedded-book/intro/no-std.html)
- [R14: embedded-hal-mock documentation](https://docs.rs/embedded-hal-mock/latest/embedded_hal_mock/)
- [R15: embedded-test documentation](https://docs.rs/embedded-test/latest/embedded_test/)
- [R16: cargo-llvm-cov documentation](https://github.com/taiki-e/cargo-llvm-cov)
- [R17: GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
- [R18: Rust Fuzz Book — cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz.html)
- [R19: The Rust Programming Language — Common programming concepts](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html)
- [R20: The Rust Programming Language — Variables and mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html)
- [R21: The Rust Programming Language — Functions](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html)
- [R22: The Rust Programming Language — Data types](https://doc.rust-lang.org/book/ch03-02-data-types.html)
- [R23: The Rust Programming Language — Control flow](https://doc.rust-lang.org/book/ch03-05-control-flow.html)
- [R24: The Rust Programming Language — What is ownership?](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)
- [R25: Python Language Reference — Simple statements and assignment](https://docs.python.org/3/reference/simple_stmts.html)
- [R26: The Rust Programming Language — Defining an enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html)
