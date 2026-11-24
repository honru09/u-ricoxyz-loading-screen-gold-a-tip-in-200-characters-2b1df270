#!/usr/bin/env python3
"""Loading Screen Gold entry: one sharp, funny loading-screen tip.

Writes the single tip to /output/entry.txt (creating /output if needed).
Python standard library only; no network access.
"""

import os

TIP = (
    "Loading\u2026 Your AI agent just rewrote the function you spent an hour "
    "perfecting \u2014 in four seconds, while you read this tip. Breathe. "
    "The tests will decide which of you was right."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
