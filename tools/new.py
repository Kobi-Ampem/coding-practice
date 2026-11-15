"""Create a new problem file from the templates.

    python3 tools/new.py 217 "Contains Duplicate" --lang py --difficulty Easy
    python3 tools/new.py 217 "Contains Duplicate" --lang cpp
    python3 tools/new.py "Two Strings" --hackerrank          # Sunday timed run

The file gets the header and the six-step skeleton, never solution code.
"""

import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXT = {"py": "py", "cpp": "cpp"}


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("problem", nargs="+", help="LeetCode number and title, or a HackerRank title")
    parser.add_argument("--lang", choices=EXT, default="py")
    parser.add_argument("--difficulty", default="")
    parser.add_argument("--hackerrank", action="store_true", help="timed HackerRank run")
    args = parser.parse_args()

    today = datetime.date.today().isoformat()
    number = ""
    words = args.problem
    if not args.hackerrank:
        if not words[0].isdigit() or len(words) < 2:
            parser.error("LeetCode problems need a number and a title")
        number, words = words[0], words[1:]
    title = " ".join(words)
    slug = slugify(title)

    if args.hackerrank:
        path = ROOT / "hackerrank" / "timed" / f"{today}_{slug.replace('-', '_')}.{EXT[args.lang]}"
        fields = {"platform": "HackerRank", "number": "", "link": ""}
    else:
        language_dir = "python" if args.lang == "py" else "cpp"
        path = ROOT / "leetcode" / language_dir / f"{int(number):04d}_{slug.replace('-', '_')}.{EXT[args.lang]}"
        fields = {"platform": "LeetCode", "number": f"{number}. ",
                  "link": f"https://leetcode.com/problems/{slug}/"}

    if path.exists():
        sys.exit(f"{path.relative_to(ROOT)} already exists; not overwriting")

    fields.update(title=title, difficulty=args.difficulty, date=today, filename=path.name)
    text = (ROOT / "templates" / f"problem.{EXT[args.lang]}").read_text(encoding="utf-8")
    for key, value in fields.items():
        text = text.replace("{" + key + "}", value)

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
