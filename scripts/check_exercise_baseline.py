"""Author check on a temporary copy; never rejects or rewrites a learner's solution.

The old strict rule must fail exactly the four equality-sensitive acceptance
checks. The complete solution must pass that identical suite. Compilation errors
and missing tooling are failures of this check, not successful demonstrations.
"""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FAILURES = {
    "includes_reading_equal_to_limit", "uses_the_supplied_limit",
    "compares_negative_readings", "counts_two_qualifying_readings_in_the_sample",
}
BASELINE = "pub fn is_at_or_above_limit(reading: i32, limit: i32) -> bool {\n    reading > limit\n}\n"


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="rust-lesson-baseline-") as directory:
        temporary_root = Path(directory)
        practice = temporary_root / "practice"
        practice.mkdir()
        for name in ["Cargo.toml", "Cargo.lock"]:
            shutil.copy2(ROOT / "exercises/00-rust-orientation" / name, practice / name)
        shutil.copy2(ROOT / "rust-toolchain.toml", practice / "rust-toolchain.toml")
        (practice / "src").mkdir()
        (practice / "tests").mkdir()
        shutil.copy2(ROOT / "exercises/00-rust-orientation/tests/acceptance.rs",
                     practice / "tests/acceptance.rs")
        (practice / "src/lib.rs").write_text(BASELINE, encoding="utf-8")
        command = ["cargo", "test", "--locked", "--offline", "--test", "acceptance"]
        baseline_command = command + ["--target-dir", str(temporary_root / "baseline-build"),
                                      "--", "--color", "never"]
        result = subprocess.run(baseline_command, cwd=practice, capture_output=True,
                                text=True, check=False, timeout=120)
        failures = set(re.findall(r"^test (\w+) \.\.\. FAILED$", result.stdout, flags=re.M))
        if result.returncode != 101 or failures != EXPECTED_FAILURES:
            raise RuntimeError(f"Unexpected baseline result:\n{result.stdout}\n{result.stderr}")
        print("PASS: untouched strict-rule baseline fails exactly the four intended checks", flush=True)

        # Independent output directories prevent an old timestamp or build cache
        # from making the second check accidentally execute the first program.
        solution_source = ROOT / "solutions/00-rust-orientation/src/lib.rs"
        (practice / "src/lib.rs").write_text(solution_source.read_text(encoding="utf-8"), encoding="utf-8")
        solution_command = command + ["--target-dir", str(temporary_root / "solution-build"),
                                      "--", "--color", "never"]
        subprocess.run(solution_command, cwd=practice, check=True, timeout=120)
        print("PASS: supplied solution passes the identical six-check acceptance suite")


if __name__ == "__main__":
    main()
