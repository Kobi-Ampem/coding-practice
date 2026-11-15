"""Say what to solve today.

    python3 tools/today.py                 # today
    python3 tools/today.py --date 2026-11-18

Mon, Tue, Thu, Fri: next new problem in Python.
Wed: next new problem in C++.
Sat: re-solve every problem still waiting (see due.py).
Sun: timed HackerRank run.

"Next" is the first Blind 75 problem (tools/blind75.txt) with no solution file
in either language. Hard problems wait until HARD_FROM.
"""

import argparse
import datetime
from pathlib import Path

from due import pending

ROOT = Path(__file__).resolve().parent.parent
HARD_FROM = datetime.date(2027, 3, 1)
PLAN = {0: "py", 1: "py", 2: "cpp", 3: "py", 4: "py", 5: "resolve", 6: "hackerrank"}


def load_list() -> list[dict]:
    problems = []
    for line in (ROOT / "tools" / "blind75.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        number, difficulty, topic, title, slug = parts[:5]
        problems.append({"number": int(number), "difficulty": difficulty, "topic": topic,
                         "title": title, "slug": slug, "premium": len(parts) > 5})
    return problems


def solved_numbers() -> set[int]:
    numbers = set()
    for path in (ROOT / "leetcode").rglob("*"):
        prefix = path.name.split("_", 1)[0]
        if path.suffix in {".py", ".cpp"} and prefix.isdigit():
            numbers.add(int(prefix))
    return numbers


def next_problem(today: datetime.date) -> tuple[dict | None, int]:
    """The next problem to solve, and how many Hard ones are being held back."""
    done = solved_numbers()
    held = 0
    for problem in load_list():
        if problem["number"] in done:
            continue
        if problem["difficulty"] == "Hard" and today < HARD_FROM:
            held += 1
            continue
        return problem, held
    return None, held


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--date", type=datetime.date.fromisoformat, default=datetime.date.today())
    today = parser.parse_args().date
    task = PLAN[today.weekday()]
    waiting = pending()
    print(today.strftime("%a %d %b %Y"))

    if task == "resolve":
        print("Saturday: re-solve everything still waiting, from scratch, then fill in 'Re-solved'.")
        if not waiting:
            print("Nothing waiting. Use the slot for one extra new Python problem.")
        for date, path, problem in waiting:
            print(f"  {date}  {path.relative_to(ROOT)}  ({problem})")
        return

    if task == "hackerrank":
        print("Sunday: HackerRank timed run, 2 problems in 70 minutes, in Python.")
        print("  Interview Preparation Kit: https://www.hackerrank.com/interview/interview-preparation-kit")
        print('  python3 tools/new.py "<title>" --hackerrank')
        return

    problem, held = next_problem(today)
    if problem is None:
        print("Blind 75 finished. Move on to the rest of NeetCode 150.")
        return
    language = "C++" if task == "cpp" else "Python"
    print(f"New problem in {language}: {problem['number']}. {problem['title']} "
          f"({problem['difficulty']}, {problem['topic']})")
    print(f"  https://leetcode.com/problems/{problem['slug']}/")
    if problem["premium"]:
        print("  LeetCode Premium: solve the free version on https://neetcode.io/practice")
    print(f'  python3 tools/new.py {problem["number"]} "{problem["title"]}" '
          f'--lang {task} --difficulty {problem["difficulty"]}')
    if waiting:
        print(f"{len(waiting)} problem(s) waiting for Saturday's re-solve.")
    if held:
        print(f"{held} Hard problem(s) held back until {HARD_FROM:%d %b %Y}.")


if __name__ == "__main__":
    main()
