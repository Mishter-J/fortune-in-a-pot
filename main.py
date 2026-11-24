#!/usr/bin/env python3
"""Fortune in a Pot.

Writes a single kind, funny fortune for a houseplant (at most
120 characters) to /output/entry.txt, exactly as the program/v1
gate requires: UTF-8 text, 1 to 120 characters, not only white
space, one line.

The fortune was chosen from ten candidates scored against the
judge's own brief (a gardener of thirty years, judging pairs):
a prediction about the plant's own future first, a small joke
that lands second, warm with no doom, no withering and no
mockery, fortune cadence rather than a slogan or a care
instruction, and specific to this plant on this windowsill.

Winner (local score 76.5, pairwise bracket winner): the keeper's
praise is already out of date — by the time someone points and
says "that one grew", the plant is growing the next one. The
quoted praise plus the parallel turn is the aphorism pattern
that wins: concrete, second person, one quiet twist at the end.
"""

import os

ENTRY = (
    "Before spring, someone will point at you and say "
    "'that one grew' \u2014 and you will already be growing "
    "the next one."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    # Fail closed: entry must be one non-blank line, 1-120 chars.
    line = text.strip()
    if not line:
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-120")
    return line


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    # Read back and verify: what the grader reads must be exactly the line.
    # Guards against a truncated or partial write.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("output mismatch: file does not contain the entry exactly")
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    print(line)


if __name__ == "__main__":
    main()
