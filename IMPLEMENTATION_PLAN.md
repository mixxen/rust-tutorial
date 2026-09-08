# Implementation plan: Rust for Experienced Programmers

**Status:** Planning only. Implementation phases have not started. Creating this plan and the repository landing page does not complete Phase 1.

**Scope:** Implement the approved [curriculum](CURRICULUM.md): 27 general Rust lessons (00–26), 14 Embassy lessons (E01–E14), and six optional extensions. Keep existing lesson numbers and topics.

**Audience:** Experienced C, C++, and Python programmers learning to write Rust themselves.

**Guiding rule:** Finish a few lessons that people can genuinely learn from before adding more lessons. Working code is necessary; clear teaching is equally important.

## 1. How to use this plan

The curriculum describes **what to teach**. This plan describes **the order in which to build it, how small to keep each piece of work, and what evidence is needed before calling it ready**.

Work through one phase at a time. A phase is not a single large generation task or pull request. Within a phase, normally complete one lesson per change; two closely related, small lessons may share a change. Ownership, lifetimes, async, unsafe code, DMA, and each capstone deserve separate changes. A pull request is a proposed change that can be reviewed before merging into the main branch.

For each lesson, finish the explanation, runnable example, exercise, hints, solution, and checks together. Do not write all the code first and leave the teaching for a later pass. Do not create dozens of empty packages to make the repository look complete.

When a lesson grows too large, divide its walkthrough into smaller steps or put the extra material in an optional section. Do not cram advanced prerequisites into an introductory lesson. Preserve its lesson number unless a curriculum change is explicitly agreed.

At the end of each phase, review what was actually delivered, revisit earlier lessons affected by shared changes, and record the next small task. Unfinished checks remain visible. Reduce scope rather than lowering the standard to call a phase finished.

## 2. Teaching and code standards

### Write for a person learning the language

Start with a concrete task: “Decide whether a reading reaches a limit,” not an unexplained list of language features. Explain what the example does, show it running, and then explain how Rust expresses it.

Use ordinary words first, followed by the technical name when it helps. For example: “The function temporarily uses the caller's value; Rust calls this borrowing.” Technical terms are useful vocabulary, not something to avoid entirely. Define them when introduced and reuse the same explanation consistently.

Assume programming experience, not Rust fluency. Avoid both a lengthy introduction to what a loop is and an unexplained chain of Rust punctuation. Early lessons should have a small “New syntax in this example” box. Mark supplied test or startup code that will be explained later.

Compare C++, Python, and Rust fairly. State where an analogy stops working. Do not present Rust as automatically correct because it compiles, or suggest that modern C++ has no automatic resource management. Comparisons must use the same inputs and behavior, and should be checked when authored.

Each lesson should help the learner answer: **What does it do? Why is it written this way? What can I change? How will I know the change works?**

### Choose names that communicate intent

| Avoid in teaching examples | Prefer | Reason |
|---|---|---|
| `x`, `v`, `d` for domain values | `reading`, `readings`, `received_bytes` | Say what the value represents. |
| `t`, `dt`, `ms` | `timeout`, `elapsed_time`, `timeout_milliseconds` | Make meaning and units visible. |
| `proc`, `hdl`, `mgr` | `parse_command`, `handle_button_press`, `DeviceController` | Name the specific responsibility. |
| `tx`, `rx` with no introduction | `command_sender`, `command_receiver` | Describe what travels through the channel. |
| `test1`, `test_error` | `rejects_empty_command`, `includes_reading_equal_to_limit` | State the behavior being tested. |
| `foo`, `bar`, `thing` | A small, consistent device or measurement example | Give the reader something meaningful to follow. |

These are readability guidelines, not a ban on conventional syntax. Keep standard Rust names such as `self`, `Result`, and `Option`. A local loop index, a mathematical symbol, a generic type parameter such as `T`, or a lifetime such as `'a` is appropriate when the name is conventional and explained. Do not rename a hardware register or library API in a way that makes the official documentation harder to follow.

Prefer the shortest name that clearly communicates the intended meaning. Avoid both cryptic abbreviations and long names that repeat every detail of the type.

An introductory example should be as direct as this:

```rust
fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {
    reading >= limit
}
```

Explain the parameter types, return type, and final expression alongside the code. Do not replace a clear early loop with an iterator chain before iterators have been taught.

Comments should explain a decision, assumption, or constraint. A comment saying “increment count” is less useful than an explanation of why a boundary value must be included. Keep explanations close to the relevant code, and keep shown snippets synchronized with the runnable files.

### Keep the course approachable

Every lesson supplies a known starting point. Earlier concepts are prerequisites, but a learner's earlier exercise implementation is not a build dependency. Small examples should not require a custom tutorial framework or hidden helper library to understand them.

Keep solutions out of the default walkthrough. Provide gradual hints and an explicit link to the complete solution. A correct solution should discuss its reasoning and a relevant alternative, not simply display the final code.

AI review exercises come after the concept they assess. Ask the learner to predict, change, test, and explain. Do not make access to a paid AI product a prerequisite, and do not reward a generated solution the learner cannot explain.

## 3. Shared repository decisions

Retain the architecture in the curriculum: a `host/` Cargo workspace and a separate `embedded/` workspace, with a package and small Makefile for each lesson. A workspace is a group of packages managed together; Cargo documents its shared lockfile and build directory. [S1]

The Makefiles are convenient shortcuts, not another build system to learn. Lesson READMEs show the equivalent Cargo command and the directory from which to run it. Target-specific board settings must not affect ordinary host lessons. Cargo configuration lookup depends on the invocation directory; test root and lesson-local commands rather than assuming `--manifest-path` discovers every nested setting. [S2]

Keep worked examples, unfinished exercise packages, and full solution packages separate. Regular verification checks complete examples and solutions. Exercise commands identify the exact package they test. Starter packages should normally compile and fail only the documented exercise assertions; deliberate compiler-error exercises are isolated and clearly labeled.

A fresh checkout must not look broken because unfinished exercises are included in ordinary checks. Conversely, a command testing a solution must not be presented as proof that the learner's exercise passed. Give starter and solution acceptance tests the same behavioral requirements, and check for accidental differences.

Pin the actual Rust toolchain and dependency/tool versions after a working combination is tested. Preserve the curriculum's Rust 2024 edition policy. Commit applicable lockfiles and keep version choices in one documented place. Avoid selecting versions from memory or following moving development branches.

Linux and WSL are the primary interactive environments. Docker supports reproducible compilation and host-side checks; hardware flashing may run from Linux or WSL outside the container. Add macOS/native Windows checks only when they remain small. An untested environment is described as untested, not supported by assumption.

Root `make verify` must never flash hardware or modify source files. Formatting checks inspect formatting; `make fmt` is the explicit command that changes it. Requested hardware tests fail clearly when the board cannot be reached. “Not applicable” and “not run” are not synonyms for “passed.”

## 4. Phase overview

All implementation phases below are **not started** when this plan is introduced. Lesson ranges are inclusive. Phase numbers describe development work, not new lesson numbers.

| Phase | Deliverable | Lessons | Suggested small batches |
|---|---|---|---|
| 1 | A working starting point and a model for later lessons | 00–01 | Setup + 00; then 01; early board check tracked separately |
| 2 | Values, ownership, borrowing, and text | 02–05 | One lesson at a time |
| 3 | Data models, errors, and organization | 06–08 | One lesson at a time |
| 4 | Clear APIs and everyday Rust techniques | 09–11 | 09; 10; 11 |
| 5 | Safer designs that are easy to test | 12–14 | 12; 13; 14 |
| 6 | Thorough automated testing | 15–18 | 15–16 if small; 17; 18 |
| 7 | The first useful application | 19–20 | 19; then capstone 20 in reviewed steps |
| 8 | Threads and async programs | 21–23 | One lesson at a time |
| 9 | Advanced boundaries, measurement, and repeatable checks | 24–26 | One lesson at a time |
| 10 | Embedded foundations and Embassy tasks | E01–E04 | Finish E01; E02; E03; E04 |
| 11 | Board inputs and communication | E05–E07 | One lesson at a time |
| 12 | Hardware-aware programming and testing | E08–E11 | One lesson at a time; keep E08 tightly scoped |
| 13 | Recovery and the embedded capstone | E12–E14 | E12; capstone E13; verification E14 |
| 14 | A complete first-release walkthrough | All core lessons | Host review; board review; final navigation and evidence review |
| 15 | Optional extensions | X01–X06 | Select and complete one extension at a time |

### Early board check: find setup problems before writing the embedded course

Begin this engineering check alongside the first host phase, as the approved curriculum requests. Its purpose is to establish a working hardware baseline, not to rush the full embedded lessons.

Prepare a small buildable draft in the eventual E01 package and a minimal portable-library example for E02. Reuse those files when the full lessons are written rather than maintaining a second set of board examples. Mark them as drafts in course navigation.

Check the exact NUCLEO-H723ZG configuration, tool versions, build, connection to the programming/debugging probe, firmware loading, a recognizable log message, and an observed LED change. Test the portable library on the host and build it for the microcontroller. Record any board setup steps that were needed.

A board connected to a learner's computer is not automatically accessible to a remote authoring environment. Actual execution requires Alex or another tester to run the documented commands on a machine with board access. Until results exist, record **needs board verification**. Do not invent logs, measurements, or successful tests.

Host phases can proceed while USB or board setup is unresolved. However, dependent hardware lessons must not be called board-verified, and the embedded first-release gate remains open. Changes to the pinned tools or board configuration require the baseline to be checked again.

## 5. Detailed phases and finish lines

### Phase 1 — Make the first experience work

**Build:** Linux/WSL setup notes, a small development container, the host workspace, per-lesson command wrappers, the lesson template, and minimal GitHub Actions checks. GitHub Actions will run automated checks when changes are proposed or committed; introduce that purpose without requiring learners to understand workflow configuration yet.

Implement Lesson 00 completely: the same threshold task in C++, Python, and Rust; a syntax guide; an ordinary runnable Rust example; the separate inclusive-threshold exercise; boundary tests; progressive hints; and an explained solution. The extra C++ compiler is an authoring check, not a learner prerequisite for the Rust lesson.

Then implement Lesson 01: explain the tools just used and create a tiny package from scratch. Audit `.gitignore` so intended lockfiles are retained and build outputs stay untracked. Add the minimum contributor instructions and review template needed to preserve these conventions. No empty future lesson packages or nonfunctional commands.

**Finish line:** From a clean checkout in a recorded primary environment, the supplied setup, run, test, lint, and verification steps work. The reference and solution pass; the untouched exercise fails for the documented reason. The learner can tell which package ran. Formatting checks do not rewrite files. Docker checks have a recorded result or an explicit unresolved issue; Phase 1 is not complete with required checks merely assumed.

**Teaching checkpoint:** Read Lesson 00 from start to finish before expanding the template. Invite early learner feedback on confusing words, unexplained punctuation, and naming. Record actual feedback separately from an author's own walkthrough. The early board check has its own evidence status and does not hold up the host lesson pilot.

### Phase 2 — Make ownership understandable

**Build:** Lessons 02–05: precise types and conversions, ownership and moves, borrowing and slices, strings and bytes.

Use small examples where a reader can track every value. Explain who owns a value before and after a move, and whether a function borrows or takes ownership. Include a deliberate compiler error, explain its useful part, and show the smallest justified repair. Demonstrate why adding `clone()` everywhere is not a substitute for understanding the design.

**Finish line:** Reference examples and solutions pass; isolated failure demonstrations fail for their intended reason. Include numeric boundaries, relevant empty inputs, and multibyte text cases. A prose review checks that no unexplained trait, lifetime annotation, or iterator-heavy solution is required to complete these exercises.

**Review task:** Ask the learner to predict what remains usable after a function call and explain their answer before running the compiler.

### Phase 3 — Represent data and errors clearly

**Build:** Lessons 06–08: structs/enums/patterns, recoverable errors, modules and package boundaries.

Use a simple device-state model and parser. Give states, error variants, modules, and tests descriptive names. Show which failures a caller can handle and why. Introduce the library/executable split with a before-and-after explanation rather than starting with many unexplained files.

**Finish line:** Tests exercise valid states, bad input, and the public library interface. Documentation examples execute where supported by the pinned setup. The learner can create the curriculum's small-parser checkpoint from a blank package without reusing an unexplained framework.

**Keep out:** Async execution, a reusable device framework, and a large error-handling dependency stack.

### Phase 4 — Build clear APIs

**Build:** Lessons 09–11: lifetimes, traits and generics, iterators and closures.

Give each topic room. Start with the concrete problem before introducing notation. Explain a lifetime relationship in words and a small diagram where helpful. Introduce a fake reading source only after the real source's responsibility is clear. Compare a loop and an iterator version using the same input and expected output.

**Finish line:** Borrowed APIs have valid and intentionally invalid usage examples. Real and fake sources satisfy the same behavioral requirements. Loop and iterator versions produce the same results. Naming and explanations distinguish the data itself from the trait describing access to it.

**Keep out:** Elaborate generic hierarchies, a dependency-injection framework, or performance claims that have not been measured.

### Phase 5 — Make design choices testable

**Build:** Lessons 12–14: meaningful wrapper types and conversions, smart pointers and controlled shared mutation, and design for testing.

Use types to make units and invalid values visible. Explain when an ordinary reference is simpler than a shared pointer. Extract a small time-dependent state machine into code whose inputs and time can be controlled by a test.

**Finish line:** Tests cover rejected construction, ownership relationships, transitions, and time boundaries. Portable logic is tested without real sleeping, real I/O, or a board. The explanation shows why each abstraction exists and also identifies an abstraction that was deliberately not needed.

**Review task:** Can a learner explain the design using names and responsibilities, without first explaining several helper layers?

### Phase 6 — Teach testing as reasoning, not button-pushing

**Build:** Lessons 15–18: test organization, formatting/linting/documentation, coverage, and property-based testing.

Explain the different questions answered by a function-level test, a public-API test, a documentation example, and an intentional compile-failure test. Make lint messages actionable. Clippy's guidance supports deliberate lint selection; do not enable every restrictive lint and then add blanket exceptions. [S3]

Add a highly covered but incorrect implementation. Ask the learner to strengthen the assertions and cover missing failure behavior. Introduce property-based testing as checking a rule over many generated inputs, then explain shrinking with a concrete failure.

**Finish line:** The quality commands run locally and in CI; expected compiler failures are verified rather than accidentally ignored. Coverage names the packages and exclusions it measures. Apply the curriculum's proposed 90% line-coverage floor only to designated portable application-core packages after Lesson 17, not to every tutorial file. Include at least one example where a better test finds a bug despite a high coverage percentage. Preserve generated regression cases.

**Keep out:** Nightly-only checks as core prerequisites, a coverage badge with an unclear denominator, and tests that simply repeat the implementation's algorithm.

### Phase 7 — Deliver the telemetry analyzer

**Build:** Lesson 19 and capstone Lesson 20, following the curriculum's bounded CLI scope. A command-line interface is a program the learner runs from the terminal with arguments.

Provide a small documented dataset and requirements before the implementation. Separate reading files, parsing records, filtering, and producing the summary. Keep the capstone independent of unfinished earlier exercises. Split development into a first working command, error cases, and the final verification/documentation pass.

**Finish line:** Black-box tests run the executable and check output and exit status. Include empty input, malformed records, boundary values, and a missing file. Complete the acceptance report with actual results, source revision, commands, and limitations. Record a clean-checkout walkthrough and recheck the earlier host lessons.

**Keep out:** Databases, cloud deployment, authentication, and unrelated product features.

### Phase 8 — Explain concurrency before adding complexity

**Build:** Lessons 21–23: threads/message passing, async/futures, and coordination/testing.

Begin with a small diagram of who sends what to whom. Introduce an executor as the component that runs async work, and backpressure as what happens when a producer must wait because a consumer cannot keep up. Explain those terms before relying on them. Use names such as `command_sender` and `status_receiver`.

**Finish line:** Tests cover shutdown, full queues, slow consumers, and cancellation where applicable. Use controlled time when practical; remaining waits have a reason and a deadline. Test failures cannot hang indefinitely. The learner can explain why an async function does not automatically run in parallel or make blocking work harmless.

**Keep out:** Replacing every simple function with async code or introducing a network service only to demonstrate task scheduling.

### Phase 9 — Handle advanced topics carefully

**Build:** Lessons 24–26: a small unsafe/C boundary, measurement and performance, and CI/reproducibility.

Keep unsafe obligations next to the relevant code. Separate safe caller responsibilities from internal implementation obligations. Start measurement with a question and a repeatable workload. Explain the quality pipeline already present in the repository instead of pretending CI starts at this lesson.

**Finish line:** The small foreign-function example has documented ownership and input rules with relevant tests. Benchmarks record environment and workload; an unmeasured speedup is not a result. Deliberately introduced failures are caught by the intended CI checks. Explicitly supported feature combinations are verified rather than blindly enabling every feature together.

**Release checkpoint:** The host course can be reviewed and shared as a complete host track even while board work is still being verified.

### Phase 10 — Turn the board baseline into lessons

**Build:** Finish E01 and E02 from the early drafts, then E03 and E04: board setup, portable logic without the host standard library, GPIO/peripheral ownership, and Embassy tasks/time.

Name the microcontroller, programming connection, and host computer consistently. Explain supplied startup and board configuration in layers. Keep board support small enough that learners can find the code responsible for the behavior. Clearly separate portable Rust logic from the hardware-specific part.

**Finish line:** The same portable implementation is tested on the host and built into firmware. Documented board loading, logging, LED/button behavior, and task timing have recorded board results where required. The learner has connection troubleshooting and a return-to-known-firmware procedure. Build-only results remain explicitly marked as such.

**Keep out:** Custom hardware, external sensors, unexplained clock changes, and a large board abstraction that hides the concepts being taught.

### Phase 11 — Connect inputs, tasks, and commands

**Build:** E05–E07: button interrupts/debouncing, bounded task communication, and a UART command interface.

Use a clear sequence: input arrives, an event is produced, one task handles it, and a response or state change follows. Explain debouncing as handling a physical switch that can appear to change repeatedly during one press. Explain UART as the serial communication interface used by the lesson.

**Finish line:** Test synthetic button traces and queue saturation on the host where appropriate; separately record physical observations. Serial command tests include partial, oversized, malformed, and valid input. Buffer limits and overload behavior are deliberate. Name and verify the board's actual serial route rather than copying another board's pin assignments.

**Keep out:** A general protocol framework, Ethernet, and external instruments as hidden requirements.

### Phase 12 — Test hardware without confusing the evidence

**Build:** E08–E11, separately: DMA and memory awareness, driver/state-machine tests, on-device tests, and host-driven hardware tests.

DMA means a peripheral can transfer data to or from memory without the CPU copying every item. Explain the relevant buffer and memory rules for the pinned board setup; do not turn E08 into an entire processor-memory course. Build on the existing serial example.

Add portable driver tests, a validated on-device test setup, and a readable Python/pytest command harness. Explain hardware-in-the-loop as a test program on the computer communicating with real running firmware.

**Finish line:** Host tests, firmware builds, on-device assertions, and host-driven acceptance tests have separate results. Test both a controlled firmware failure and an unavailable-board setup failure. Select the intended device, allow only one test process to use it at a time, reset to a known state, impose deadlines, and retain useful diagnostics. Validate the documented release-build memory configuration on the board.

**Keep out:** Silent retries until a failure disappears, claims of MCU instruction coverage based on host coverage, or treating a log message as independent proof that an LED physically illuminated.

### Phase 13 — Build and verify a recoverable device

**Build:** E12, E13, and E14: faults/timeouts/recovery, the device supervisor, and its verification report.

Agree the small set of observable requirements before integrating the capstone. Implement heartbeat, button handling, bounded commands, status, and a documented watchdog policy. Fault injection is a clearly gated test-only facility. Reuse the exact portable logic in firmware and host tests, not a separately rewritten model.

**Finish line:** Each capstone requirement points to a test or a clearly identified manual observation. Recovery behavior has expected and observed results. A bounded soak test has a documented duration, observation method, and outcome; do not invent long-running results. Report revision, tools, board details, configuration, failures, and untested behavior. Restore the board to the known non-test firmware after fault testing.

**Keep out:** Certification claims, unsupported hard-real-time guarantees, and extra product features added to make the demo look larger.

### Phase 14 — Walk through the whole course as a learner

**Build:** No new mandatory topics. Review the course from a fresh checkout using only the published instructions.

Check setup, navigation, filenames, naming consistency, explanations, snippets, exercise entry points, hints, and solutions. Re-run supported host checks and required board checks. Check that later improvements did not make early examples depend on concepts introduced much later. Mark optional reading and unfinished extensions clearly.

**Finish line:** Every core lesson has a truthful status and verification record. Required first-release checks pass; unresolved blockers remain visible and prevent declaring the affected track complete. A host-only release may be clearly labeled while embedded work remains in preview. Update the main README to point to real working lessons, not proposed paths. Invite learner feedback and distinguish it from technical checks.

**Release rule:** Tag a release only after its declared scope has passed its checks. Optional extensions do not hold the core release open.

### Phase 15 — Add useful optional extensions

Choose extensions based on learner feedback, not to increase the lesson count. Deeper testing (X04), C/C++ interoperability (X01), and Python integration (X02) are sensible candidates given this audience. X03, X05, and X06 remain available in the curriculum.

Each selected extension gets the same complete explanation/example/exercise/solution/check cycle. New hardware or toolchain requirements stay explicit and optional. Do not begin all six at once, or make a later extension a hidden dependency of the core lessons.

## 6. What every lesson must deliver

The package layout and command names remain those defined in the curriculum. This checklist is a review aid, not a requirement to create empty files where a section is genuinely unnecessary.

| Item | What a reviewer checks |
|---|---|
| Objective and prerequisites | One concrete outcome; prerequisite concepts and equipment are stated. |
| Explanation | New vocabulary and notation are explained at the point of use. |
| Worked example | Small, complete, and runnable; expected output or behavior is described. |
| Commands | Working directory, prerequisites, and selected package are clear. |
| Exercise | A meaningful change with observable acceptance criteria; distinct from the example. |
| Hints | Gradual help that does not reveal the full answer immediately. |
| Solution | Complete code, reasoning, and a relevant alternative or tradeoff. |
| Tests | Normal behavior plus relevant boundaries/failures; intentional failures are isolated. |
| Code review | Names are deliberate, comments explain decisions, and unnecessary machinery is removed. |
| Verification record | Actual commands/results, revision and environment; unrun checks are named. |
| Navigation | A clear way to start, find help, and continue; only existing lessons are linked as runnable. |

A practical authoring sequence is: write the learning outcome, draft the small example, write behavior-focused tests, build the exercise and solution, write the walkthrough around them, then run a clean-checkout review. Iterate between code and prose instead of treating either as final too early.

When a shared template, dependency, or Makefile changes, test earlier affected lessons as well as the newest one. Fix a confusing pattern at its source, not by copying it into the next lesson.

## 7. Quality checks grow with the course

| Stage | Required evidence |
|---|---|
| First host lesson onward | Build, tests, formatting check, selected Clippy checks, and working documented commands. |
| Public APIs and documentation | Integration/documentation checks and purposeful compile-failure examples as introduced. |
| Testing phase onward | Scoped coverage, assertion-quality review, and generated-input tests where appropriate. |
| Host capstone | Executable-level acceptance tests, deterministic fixtures, and a short result report. |
| First board example onward | Firmware build result separate from observed hardware execution. |
| Embedded testing phase | Separate host, on-device, and host-driven results with setup failures distinguished. |
| Final capstone | Requirement-to-test mapping, recovery evidence, and explicitly untested behavior. |

Normal CI should run without a physical board. Keep host tests deterministic and independent of secret credentials or live services. Dependency downloads during setup are distinct from tests depending on internet access. Use approved, explicit feature combinations and record versions when checks are introduced.

Initially run hardware tests locally on a machine with the board. Do not automatically execute untrusted public pull-request code on a developer's workstation or persistent board runner. GitHub documents the compromise risk of self-hosted runners; any later automated board service needs its own isolated, trusted execution design. [S4]

## 8. Track progress without building a second project

Use this plan as the source for phase scope. During Phase 1, add a small Markdown progress table with one row per implemented or actively drafted lesson. Record a lesson's writing status separately from its verification status. Avoid dashboards and duplicate trackers that take more effort than they save.

Suggested writing states are **planned**, **draft**, **in review**, and **ready**. Evidence columns should separately identify **host checks**, **firmware build**, and **board execution** with a result or “not run.” A passing host check does not fill the board-execution column.

A phase can use one tracking issue, with its lesson changes linked beneath it. Create issues when work is queued, not a large set of empty tickets now. The repository's ordinary review and permission settings remain unchanged by this plan.

Each implementation change should explain the learning outcome, lessons affected, files changed, commands actually run, results, and limitations. A compact verification note may live in the pull request; hardware results should also have a durable record linked from the lesson. Keep generated reports separate from committed summaries.

At a phase boundary, provide a short handoff:

```text
Phase and lessons:
Completed code and teaching material:
Commands run and observed results:
Readability review and learner feedback, if any:
Board checks still needed:
Known issues or deliberate exclusions:
Next small implementation task:
```

Do not mark work complete because the files exist or the text sounds polished. Do not claim an actual learner completed a walkthrough unless one did. Technical testing and learner feedback are both valuable, but they are different evidence.

## 9. First implementation request

The first bounded task is **Phase 1, first batch: setup plus Lesson 00**. Deliver the minimum working host setup, the complete orientation package, its separate exercise and solution, tests, readable walkthrough, and basic CI. Verify that starting experience before adding Lesson 01 or broadening the template.

The early board check remains a separately tracked engineering task. The rest of the curriculum stays planned, not represented by empty packages or misleading completion badges.

The desired result is a repository someone can learn from a little at a time, with examples they can explain and modify—not merely a collection of Rust files that happen to compile.

## Sources and governing documents

The [curriculum](CURRICULUM.md) governs lesson coverage and platform choices. The references below support the specific tooling and safety constraints in this plan. Verify version-specific commands again when implementing the relevant phase.

- [S1: Cargo — Workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html)
- [S2: Cargo — Configuration](https://doc.rust-lang.org/cargo/reference/config.html)
- [S3: Clippy — Usage](https://doc.rust-lang.org/clippy/usage.html)
- [S4: GitHub Actions — Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use)
