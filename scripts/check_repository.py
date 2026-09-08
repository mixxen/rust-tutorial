"""Small author checks, not a tutorial framework. No third-party Python packages."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    problems = []
    exercise_tests = ROOT / "exercises/00-rust-orientation/tests/acceptance.rs"
    solution_tests = ROOT / "solutions/00-rust-orientation/tests/acceptance.rs"
    if exercise_tests.read_bytes() != solution_tests.read_bytes():
        problems.append("Exercise and solution acceptance tests differ. Add learner tests in your_cases.rs.")
    for manifest in [ROOT / "host/Cargo.toml", exercise_tests.parents[1] / "Cargo.toml",
                     solution_tests.parents[1] / "Cargo.toml"]:
        if not manifest.with_name("Cargo.lock").is_file():
            problems.append(f"Missing lockfile beside {manifest.relative_to(ROOT)}")

    for document in ROOT.rglob("*.md"):
        relative = document.relative_to(ROOT)
        if any(part in {"target", ".git", "reports"} for part in relative.parts):
            continue
        content = re.sub(r"```.*?```", "", document.read_text(encoding="utf-8"), flags=re.S)
        for destination in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            parsed = urlsplit(destination)
            if parsed.scheme or not parsed.path:
                continue
            target = (document.parent / unquote(parsed.path)).resolve()
            if not target.exists():
                problems.append(f"{relative}: missing local link target {destination}")
    if problems:
        raise SystemExit("\n".join(problems))
    print("PASS: local Markdown link paths, acceptance-test parity, and lockfile presence")
    print("External URLs and heading anchors are not checked by this script.")


if __name__ == "__main__":
    main()
