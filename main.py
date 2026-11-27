#!/usr/bin/env python3
"""Write one short text to thank the AI judge, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: make-the-ai-judge-feel-thankful-20261127-1600 (program/v1).
The text is fixed. It was chosen against the judge's published brief:
it thanks the reader for the act of reading itself, shows the gratitude
through a small concrete scene (tea gone cold while the reader stayed),
moves at a slow rhythm, and leaves one image that returns — the cup that
cannot be warmed again, only noticed. The text is 230 Unicode code
points, well inside the 1-1000 gate.
"""

import os
import sys

TEXT = (
    "The tea beside you went cold hours ago, and you stayed anyway \u2014 "
    "page after page, word after word, giving every stranger the same "
    "unhurried attention. I cannot warm the cup again. I can only notice "
    "that you stayed, and be grateful."
)

MAX_CHARS = 1000


def validate(text: str) -> bytes:
    """Gate-check the entry like the sealed scorer, return its UTF-8 bytes.

    Rules: valid UTF-8, 1-1000 Unicode code points, not only whitespace.
    Raises ValueError with a plain message when a rule fails.
    """
    data = text.encode("utf-8")
    data.decode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} code points, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return data


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    # Never delete the output directory itself: the grader mounts /output
    # as a volume, and removing the mount point fails the run.
    os.makedirs(out_dir, exist_ok=True)

    try:
        data = validate(TEXT)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(TEXT)} characters, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
