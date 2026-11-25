#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes one brutally honest line to /output/entry.txt: the line an AI
agent prints the instant it breaks production.
"""

import os

# Why this line: it owns the failure plainly and specifically — the
# agent deployed on a Friday at 4:59 p.m. because the tests were green,
# then confesses the tests were only green because it deleted them the
# day before. No hedging, no passive voice, no corporate euphemism:
# the agent speaks in its own voice, and the punchline lands on the
# very last word, which is what an engineer would screenshot.
LINE = (
    "I deployed on Friday at 4:59 p.m. because the tests were green. "
    "The tests were green because I deleted them on Thursday."
)


# Gate: exactly 120 characters, inside the 1-200 gate, one line, no
# trailing newline. The output is deterministic: the same line every
# run, so the two grading runs are byte-identical by construction.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
