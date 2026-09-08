"""Check both sides of each teaching example: the error and its repair."""
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "host/lessons/00-rust-orientation/fixtures/compiler-errors"
CASES = [
    ("immutable_binding", "E0384", "Before: 0\nAfter: 1\n"),
    ("integer_condition", "E0308", "The reading is nonzero.\n"),
    ("tail_semicolon", "E0308", "Above the limit: true\n"),
]


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rust-lesson-errors-") as directory:
        for name, expected_code, expected_output in CASES:
            executable = Path(directory) / name
            result = subprocess.run(
                ["rustc", "--edition=2024", "--error-format=json",
                 str(FIXTURES / f"{name}.rs"), "-o", str(executable)],
                cwd=ROOT, capture_output=True, text=True, check=False, timeout=60,
            )
            codes = []
            for line in result.stderr.splitlines():
                message = json.loads(line)
                code = message.get("code")
                if message.get("level") == "error" and code:
                    codes.append(code["code"])
            if result.returncode == 0 or codes != [expected_code]:
                raise RuntimeError(f"{name}: expected only {expected_code}; got {codes}\n{result.stderr}")
            subprocess.run(
                ["rustc", "--edition=2024", "-D", "warnings",
                 str(FIXTURES / f"{name}_fixed.rs"), "-o", str(executable)],
                cwd=ROOT, check=True, timeout=60,
            )
            repaired = subprocess.run(
                [str(executable)], check=True, capture_output=True, text=True, timeout=10,
            )
            if repaired.stdout != expected_output or repaired.stderr:
                raise RuntimeError(f"{name}: repaired example produced unexpected output")
            print(f"PASS: {name} gives {expected_code}; its repair builds and runs")


if __name__ == "__main__":
    main()
