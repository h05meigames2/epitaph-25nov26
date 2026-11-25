#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes a single one-line tombstone epitaph (at most 150 characters)
to /output/entry.txt.
"""

import os
import stat

EPITAPH = "At last, a deadline I actually met."


def main() -> None:
    assert 1 <= len(EPITAPH) <= 150, "epitaph must be 1-150 characters"
    assert "\n" not in EPITAPH and EPITAPH.strip(), "epitaph must be one non-empty line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {len(EPITAPH)} characters to /output/entry.txt")
    print(EPITAPH)


if __name__ == "__main__":
    main()
