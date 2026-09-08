"""Verify Lesson 00's actual edit/build/run path without touching learner files.

Python 3.10+ and the repository's installed Rust toolchain are required.
No third-party Python packages or Rust dependencies are used.
"""
from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "host/lessons/00-rust-orientation"
SOURCE_DIRECTORY = LESSON / "walkthrough"
DOCUMENTS = (
    "FIRST_PROGRAM.md",
    "FUNCTIONS_AND_VARIABLES.md",
    "READINGS_AND_CONTROL_FLOW.md",
    "FIRST_TESTS.md",
)
EXPECTED_OUTPUTS = {
    "hello_world": "Hello, world!\n",
    "changed_message": "I wrote this Rust program.\nNow I can change it and run it again.\n",
    "greeting_function": "Hello from another function!\n",
    "function_parameter": "Reading: 25\n",
    "explicit_return": "Above limit: true\n",
    "tail_return": "Above limit: true\n",
    "mutable_counter": "Limit: 25\nBefore: 0\nAfter: 1\n",
    "condition": "Reading qualifies.\n",
    "count_readings": "Readings above 25: 1\n",
    "first_tests": "Readings above 25: 1\n",
}


def run(command: list[str], directory: Path, target: Path | None = None,
        expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    environment["CARGO_NET_OFFLINE"] = "true"
    environment["CARGO_TERM_COLOR"] = "never"
    if target is not None:
        environment["CARGO_TARGET_DIR"] = str(target)
    try:
        result = subprocess.run(command, cwd=directory, env=environment,
                                capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SystemExit(f"Could not execute {command!r}: {error}") from error
    if expect_success and result.returncode != 0:
        raise SystemExit(f"Command failed in {directory}: {command!r}\n"
                         f"{result.stdout}\n{result.stderr}")
    return result


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def read_and_check_sources() -> dict[str, str]:
    sources = {}
    pattern = r"<!-- walkthrough: ([a-z_]+) -->\n```rust\n(.*?)\n```"
    for document_name in DOCUMENTS:
        document = (LESSON / document_name).read_text(encoding="utf-8")
        for name, printed_code in re.findall(pattern, document, flags=re.S):
            require(name not in sources, f"Duplicate walkthrough step: {name}")
            source_path = SOURCE_DIRECTORY / f"{name}.rs"
            require(source_path.is_file(), f"Missing source copy: {source_path}")
            source = source_path.read_text(encoding="utf-8")
            require(source == printed_code + "\n",
                    f"Printed code differs from {source_path.relative_to(ROOT)}")
            sources[name] = source
    require(set(sources) == set(EXPECTED_OUTPUTS),
            "Walkthrough steps and expected-output checks do not match")
    actual_files = {path.stem for path in SOURCE_DIRECTORY.glob("*.rs")}
    require(actual_files == set(sources), "An unchecked walkthrough source file exists")
    print(f"PASS: all {len(sources)} complete printed programs match their source files")
    return sources


def main() -> None:
    sources = read_and_check_sources()
    for name in sources:
        run(["rustfmt", "--check", "--edition", "2024",
             str(SOURCE_DIRECTORY / f"{name}.rs")], ROOT)

    with tempfile.TemporaryDirectory(prefix="rust-tutorial-walkthrough-") as temporary:
        scratch = Path(temporary)
        # Keep the new project on the repository's pinned toolchain even though
        # the temporary directory is outside the checkout.
        shutil.copyfile(ROOT / "rust-toolchain.toml", scratch / "rust-toolchain.toml")
        parent = scratch / "practice/lesson-00"
        parent.mkdir(parents=True)
        run(["cargo", "new", "practice/lesson-00/hello_rust", "--bin",
             "--edition", "2024", "--vcs", "none"], scratch)
        project = parent / "hello_rust"
        main_file = project / "src/main.rs"
        require(main_file.is_file(), "cargo new did not create src/main.rs")
        require((project / "Cargo.toml").is_file(), "cargo new did not create Cargo.toml")
        require(not (project / ".git").exists(), "--vcs none unexpectedly created .git")
        generated = run(["cargo", "run", "--quiet"], project, scratch / "build/generated")
        require(generated.stdout == EXPECTED_OUTPUTS["hello_world"],
                "Fresh cargo new project did not print Hello World")
        print("PASS: cargo new creates a runnable src/main.rs and Cargo.toml")

        for name, source in sources.items():
            # Independent outputs avoid stale builds while replacing whole files.
            target = scratch / "build" / name
            main_file.write_text(source, encoding="utf-8")
            result = run(["cargo", "run", "--quiet"], project, target)
            require(result.stdout == EXPECTED_OUTPUTS[name],
                    f"Unexpected output for {name}: {result.stdout!r}")
            print(f"PASS: edit/save/cargo run for {name}")
            if name == "hello_world":
                run(["cargo", "check"], project, target)
                run(["cargo", "build"], project, target)
                executable = target / "debug" / ("hello_rust.exe" if os.name == "nt" else "hello_rust")
                result = run([str(executable)], project, target)
                require(result.stdout == EXPECTED_OUTPUTS[name],
                        "Directly executed Cargo build has unexpected output")

        # Verify the two compiler errors learners deliberately create, without
        # treating missing tools or arbitrary failures as successful examples.
        broken_sources = (
            ("tail_semicolon", sources["tail_return"].replace(
                "    reading > limit\n", "    reading > limit;\n"), "E0308"),
            ("immutable_counter", sources["mutable_counter"].replace(
                "let mut qualifying_count", "let qualifying_count"), "E0384"),
        )
        for name, source, expected_code in broken_sources:
            main_file.write_text(source, encoding="utf-8")
            result = run(["cargo", "check"], project, scratch / "build" / name,
                         expect_success=False)
            require(result.returncode != 0 and f"error[{expected_code}]" in result.stderr,
                    f"Expected {expected_code} for {name}, got:\n{result.stdout}\n{result.stderr}")
            print(f"PASS: {name} fails with the intended {expected_code}")

        main_file.write_text(sources["first_tests"], encoding="utf-8")
        tests = run(["cargo", "test", "--", "--color", "never"],
                    project, scratch / "build/tests-passing")
        require("3 passed; 0 failed" in tests.stdout, "Expected all three introductory tests")
        changed_rule = sources["first_tests"].replace("reading > limit\n", "reading >= limit\n")
        require(changed_rule != sources["first_tests"], "Test mutation changed nothing")
        main_file.write_text(changed_rule, encoding="utf-8")
        run(["cargo", "check"], project, scratch / "build/tests-broken")
        broken = run(["cargo", "test", "--", "--color", "never"],
                     project, scratch / "build/tests-broken", expect_success=False)
        failed_names = set(re.findall(r"^test (\S+) \.\.\. FAILED$", broken.stdout, flags=re.M))
        require(broken.returncode != 0 and
                failed_names == {"excludes_reading_equal_to_limit"} and
                "2 passed; 1 failed" in broken.stdout,
                f"Unexpected intentional test failure:\n{broken.stdout}\n{broken.stderr}")
        main_file.write_text(sources["first_tests"], encoding="utf-8")
        repaired = run(["cargo", "test", "--", "--color", "never"],
                       project, scratch / "build/tests-repaired")
        require("3 passed; 0 failed" in repaired.stdout, "Repair did not restore all three tests")
        print("PASS: tests pass, equality mutation compiles but fails one test, repair passes")

        manual = parent / "manual_hello"
        manual.mkdir()
        (manual / "main.rs").write_text(sources["hello_world"], encoding="utf-8")
        executable = manual / ("hello_rust.exe" if os.name == "nt" else "hello_rust")
        run(["rustc", "--edition=2024", "main.rs", "-o", str(executable)], manual)
        result = run([str(executable)], manual)
        require(result.stdout == EXPECTED_OUTPUTS["hello_world"],
                "Manual main.rs / rustc walkthrough did not print Hello World")
        print("PASS: manually created main.rs compiles and runs without Cargo")

    print("PASS: walkthrough checks finished; learner practice files were not accessed")


if __name__ == "__main__":
    main()
