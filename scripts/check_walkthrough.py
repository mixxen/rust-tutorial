"""Run the printed Lesson 00 programs in a fresh Cargo project."""
from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "host/00-rust-orientation"
DOCUMENTS = (
    "01-first-program.md",
    "02-functions-and-variables.md",
    "03-readings-and-control-flow.md",
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
}


def run(command: list[str], directory: Path, target: Path) -> str:
    environment = os.environ.copy()
    environment["CARGO_NET_OFFLINE"] = "true"
    environment["CARGO_TARGET_DIR"] = str(target)
    try:
        result = subprocess.run(command, cwd=directory, env=environment,
                                capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SystemExit(f"Could not execute {command!r}: {error}") from error
    if result.returncode != 0:
        raise SystemExit(f"Command failed in {directory}: {command!r}\n"
                         f"{result.stdout}\n{result.stderr}")
    return result.stdout


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
            source_path = LESSON / "examples" / f"{name}.rs"
            if name == "count_readings":
                source_path = LESSON / "src/main.rs"
            source = source_path.read_text(encoding="utf-8")
            require(source == printed_code + "\n",
                    f"Printed code differs from {source_path.relative_to(ROOT)}")
            sources[name] = source
    require(sources.keys() == EXPECTED_OUTPUTS.keys(),
            "Walkthrough steps and expected-output checks do not match")
    actual_examples = {path.stem for path in (LESSON / "examples").glob("*.rs")}
    require(actual_examples == sources.keys() - {"count_readings"},
            "Cargo examples and walkthrough steps do not match")
    print(f"PASS: all {len(sources)} complete printed programs match their source files")
    return sources


def main() -> None:
    sources = read_and_check_sources()
    with tempfile.TemporaryDirectory(prefix="rust-tutorial-walkthrough-") as temporary:
        scratch = Path(temporary)
        shutil.copyfile(ROOT / "rust-toolchain.toml", scratch / "rust-toolchain.toml")
        (scratch / "practice").mkdir()
        generated_target = scratch / "build/generated"
        run(["cargo", "new", "practice/hello_rust", "--edition", "2024", "--vcs", "none"],
            scratch, generated_target)
        project = scratch / "practice/hello_rust"
        main_file = project / "src/main.rs"
        require(main_file.is_file() and (project / "Cargo.toml").is_file(),
                "cargo new did not create src/main.rs and Cargo.toml")
        require(not (project / ".git").exists(), "--vcs none unexpectedly created .git")
        generated = run(["cargo", "run", "--quiet"], project, generated_target)
        require(generated == EXPECTED_OUTPUTS["hello_world"],
                "Fresh cargo new project did not print Hello World")
        print("PASS: cargo new creates a runnable src/main.rs and Cargo.toml")

        run(["cargo", "check"], project, generated_target)
        run(["cargo", "build"], project, generated_target)
        executable = generated_target / "debug" / ("hello_rust.exe" if os.name == "nt" else "hello_rust")
        require(run([str(executable)], project, generated_target) == generated,
                "Directly executed Cargo build has unexpected output")
        print("PASS: cargo check, cargo build, and direct execution")

        for name, source in sources.items():
            # Separate build directories prevent Cargo from reusing an earlier program.
            target = scratch / "build" / name
            main_file.write_text(source, encoding="utf-8")
            output = run(["cargo", "run", "--quiet"], project, target)
            expected = EXPECTED_OUTPUTS[name]
            require(output == expected, f"{name}: expected {expected!r}, got {output!r}")
            print(f"PASS: edit/save/cargo run for {name}")


if __name__ == "__main__":
    main()
