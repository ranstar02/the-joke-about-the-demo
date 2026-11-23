#!/usr/bin/env python3
"""The joke about the demo.

Writes one line — a joke about working beside an AI coding agent — to
/output/entry.txt. Fully deterministic: the same single joke on every run,
no randomness, no clock, no network, no environment reads.
"""

import os

JOKE = (
    # One fixed joke: the punchline turns the fix itself into the bug,
    # the exact moment every developer recognises from a live demo.
    "My AI agent fixed the demo bug in four seconds flat \u2014 then spent "
    "the rest of the demo confidently explaining why the fix was the actual bug."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE
    # The gate: UTF-8 text of 1 to 280 characters (Unicode code points),
    # and not only white space.
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert text.strip(), "joke must not be only white space"
    assert "\n" not in text, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
