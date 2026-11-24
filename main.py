#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry.

Writes a single line of quiet, earned pride to /output/entry.txt.
Deterministic: the same bytes on every run. The file holds exactly the
line, with no trailing newline, so its byte count is the line's length.
"""

import os

ENTRY = "Emeka laid the last block straight, stepped back, and ran his thumb along the joint the way other men check a newborn's face."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
