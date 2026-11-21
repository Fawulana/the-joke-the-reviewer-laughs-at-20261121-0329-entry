#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic, offline, stdlib-only: the same fixed text is written to
/output/entry.txt on every run.
"""

import os

JOKE = "My agent's pull request was approved in four seconds \u2014 by another agent that hadn't read a line of it either."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    # Gate: 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("joke fails the length gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
