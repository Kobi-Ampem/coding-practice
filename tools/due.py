"""List problems waiting for a re-solve, oldest first.

    python3 tools/due.py

A problem waits when its header says "Solved alone = N" and "Re-solved" is
still empty. Saturdays clear the whole list: rewrite each one from scratch,
then fill in "Re-solved = <date>".
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["leetcode", "hackerrank/timed"]


def header_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)} =[ \t]*(.*)$", text, re.M)
    return match.group(1).strip() if match else ""


def pending() -> list[tuple[str, Path, str]]:
    """(date, path, problem) for every problem marked N and not yet re-solved."""
    waiting = []
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).rglob("*")):
            if path.suffix not in {".py", ".cpp"}:
                continue
            text = path.read_text(encoding="utf-8")
            if header_value(text, "Solved alone").upper() == "N" and not header_value(text, "Re-solved"):
                waiting.append((header_value(text, "Date"), path, header_value(text, "Problem")))
    return sorted(waiting)


def main() -> None:
    waiting = pending()
    if not waiting:
        print("Nothing waiting for a re-solve")
    for date, path, problem in waiting:
        print(f"{date}  {path.relative_to(ROOT)}  ({problem})")


if __name__ == "__main__":
    main()
