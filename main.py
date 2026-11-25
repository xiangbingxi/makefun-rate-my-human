"""Write the one-line review to /output/entry.txt.

Reads this file back after writing and checks the written text against
ENTRY character for character; any mismatch exits with an error.
"""

import os
import sys

ENTRY = 'Four stars: My human says "take your time" and checks on me thirty seconds later, but they always bring a screenshot.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("ERROR: entry.txt does not match ENTRY exactly", file=sys.stderr)
        print("expected: %r" % ENTRY, file=sys.stderr)
        print("written:  %r" % written, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
