#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word describing my Wi-Fi to $MAKEFUN_OUTPUT_DIR/entry.txt.
Gate: 1-20 UTF-8 characters, not only whitespace, exactly one word.
Word: Buffering (9 chars, 1 word, 0 newlines) — verified against the gate.
"""
import os

WORD = "Buffering"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(WORD) <= 20, "word must be 1-20 characters"
    assert len(WORD.split()) == 1, "entry must be a single word"
    assert WORD.strip(), "word must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
