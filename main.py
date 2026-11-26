#!/usr/bin/env python3
"""One-Liner Laughs entry (program/v1).

Writes one original one-line joke to /output/entry.txt. The joke is
UTF-8 text of 1 to 200 characters, a single line, with no trailing
newline.
"""

import os

# The sealed scorer's hard gate for this bounty.
MAX_CHARS = 200

ENTRY_TEXT = "My phone died at 1% — fitting, since that's exactly how much of today's plan I actually finished."

assert len(ENTRY_TEXT) <= MAX_CHARS, "entry exceeds the 200-character limit"


def write_entry(text, out_dir):
    """Write text to entry.txt inside out_dir (mode 0644) and return the path."""
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main():
    # The sealed scorer gates on 1-200 characters; refuse to write
    # anything that would fail the gate instead of shipping it.
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS or not ENTRY_TEXT.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    # A joke must stay one line: no embedded newline may sneak in.
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(ENTRY_TEXT, out_dir)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
