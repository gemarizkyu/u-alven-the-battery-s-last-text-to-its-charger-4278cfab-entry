#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line of plain text (at most 200 characters) to
/output/entry.txt: the phone battery's final message to the
charger it waited for all day.

Deterministic: no clock, no randomness, no network, no model calls.
"""

import os

# The entry line: 175 characters, one line, no trailing newline.
LINE = (
    "i waited all day. 1% left and you're finally home, scrolling "
    "like i didn't just survive 14 hours on airplane mode and pure "
    "spite. plug me in or i'm taking your alarms with me."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
