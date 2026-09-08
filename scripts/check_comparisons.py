"""Author check: all three implementations must produce the specified output."""
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "host/lessons/00-rust-orientation"
EXPECTED = "Readings above 25: 1\n"


def check_output(name: str, command: list[str]) -> None:
    result = subprocess.run(
        command, cwd=LESSON, check=True, capture_output=True, text=True, timeout=120,
    )
    if result.stdout != EXPECTED:
        raise RuntimeError(f"{name}: expected {EXPECTED!r}, got {result.stdout!r}")
    print(f"PASS: {name} prints {EXPECTED.strip()!r}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rust-lesson-comparisons-") as directory:
        executable = Path(directory) / "threshold"
        subprocess.run(
            ["g++", "-std=c++17", "-Wall", "-Wextra", "-Werror", "-pedantic",
             str(LESSON / "comparisons/threshold.cpp"), "-o", str(executable)],
            check=True, timeout=60,
        )
        check_output("C++", [str(executable)])
        check_output("Python", [sys.executable, str(LESSON / "comparisons/threshold.py")])
        check_output("Rust", ["cargo", "run", "--quiet", "--locked", "--offline"])


if __name__ == "__main__":
    main()
