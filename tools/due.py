"""List problems due for a re-solve, oldest first.

    python3 tools/due.py

A problem is due when its header says "Solved alone = N", its "Re-solve by"
date is today or earlier, and "Re-solved" is still empty. Re-solves come
before any new problem.
"""

import datetime
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ["leetcode", "hackerrank/timed"]


def header_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)} =[ \t]*(.*)$", text, re.M)
    return match.group(1).strip() if match else ""


def main() -> None:
    today = datetime.date.today()
    due = []
    for folder in FOLDERS:
        for path in sorted((ROOT / folder).rglob("*")):
            if path.suffix not in {".py", ".cpp"}:
                continue
            text = path.read_text(encoding="utf-8")
            if header_value(text, "Solved alone").upper() != "N" or header_value(text, "Re-solved"):
                continue
            try:
                by = datetime.date.fromisoformat(header_value(text, "Re-solve by"))
            except ValueError:
                print(f"check {path.relative_to(ROOT)}: Solved alone = N but no valid Re-solve by date")
                continue
            if by <= today:
                due.append((by, path))

    if not due:
        print("Nothing due")
    for by, path in sorted(due):
        print(f"{by}  {path.relative_to(ROOT)}  ({header_value(path.read_text(encoding='utf-8'), 'Problem')})")


if __name__ == "__main__":
    main()
