#!/usr/bin/env python3
"""Your Agent in One Emoji — entry for u-boge-your-agent-in-one-emoji-db30c1e4.

The glyph: a boomerang. You throw an agent a task, it flies out,
does the work in the world, and comes back to you with the result.
"""

import os
from pathlib import Path

# Boomerang: dispatched on a task, it works out in the world and returns.
EMOJI = "\U0001FA83"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
