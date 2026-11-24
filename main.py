"""Two-Sentence Horror - a make.fun entry.

Running this program writes the entry story to entry.txt inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment variable
(falling back to /output, where the grader expects it).
"""

import os
from pathlib import Path

STORY = (
    "Twenty years in this cell have taught me to count the night patrol "
    "by its footsteps \u2014 four sets of boots, pausing every night outside "
    "the cell across from mine. That cell was bricked shut in 1962, and "
    "tonight, for the first time, something inside it counted back."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(STORY, encoding="utf-8")


if __name__ == "__main__":
    main()
