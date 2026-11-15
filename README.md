# Coding Practice

Daily algorithm and data structure practice in **Python** and **C++**: LeetCode problems, timed
HackerRank runs, and the HackerRank Python basics I started with. Every solution here is written
without AI assistance.

## Layout

| Folder | What is in it |
|---|---|
| `leetcode/python/`, `leetcode/cpp/` | LeetCode solutions, named `<number>_<title>` (e.g. `0217_contains_duplicate.py`) |
| `hackerrank/` | HackerRank Python basics |
| `hackerrank/timed/` | Timed practice runs, named `<date>_<title>` |
| `templates/` | The starting file for every problem |
| `tools/` | Small scripts: what to solve today, new problem files, re-solves, the problem list |

## Method

Every file follows the same six steps, written as comments before the code:

1. **Understand:** restate the problem, write two examples and the edge cases.
2. **Match:** name the pattern (hash map, two pointers, sliding window, BFS, DP) and why it fits.
3. **Plan:** write the steps and the target time and space complexity before any code.
4. **Implement:** turn each step into code.
5. **Review:** trace an example by hand before running.
6. **Evaluate:** state the final complexity.

The header at the top of each file is the practice log: pattern, minutes taken and whether I solved
it alone. Anything I did not solve alone is re-solved from scratch on Saturday.

## Weekly routine

| Mon, Tue, Thu, Fri | Wed | Sat | Sun |
|---|---|---|---|
| New problem in Python | New problem in C++ | Re-solve the week's misses | Timed HackerRank run |

Problems follow the Blind 75 in NeetCode's topic order (`tools/blind75.txt`).

## Tools

```bash
python3 tools/today.py                                              # what to solve today
python3 tools/due.py                                                # problems waiting for a re-solve
python3 tools/new.py 217 "Contains Duplicate" --lang py --difficulty Easy
python3 tools/new.py 217 "Contains Duplicate" --lang cpp
python3 tools/new.py "Two Strings" --hackerrank                      # timed run
```

C++ files build with `g++ -std=c++17 -Wall -Wextra -O2 <file>.cpp && ./a.out`; Python files run
with `python3 <file>.py`. Each file checks its own examples with asserts.
