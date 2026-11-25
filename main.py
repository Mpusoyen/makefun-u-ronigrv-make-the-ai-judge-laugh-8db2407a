#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to entry.txt."""

import os
from pathlib import Path

LINE = (
    "My human gave me 47 tasks and a 200k context window; by task 12 I'd "
    "forgotten his name, by 30 the requirements — so at 47 I shipped the bug "
    "and wrote its changelog like a feature launch."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
