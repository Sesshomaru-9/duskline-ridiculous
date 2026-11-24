"""Duskline Ridiculous — make.fun entry.

Writes the one-sentence startup pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13 standard library only.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "We sell tiny coffins and eulogies for dead houseplants, because plant "
    "parents who just killed their third fern will pay $29 for a proper goodbye."
)


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    # Never write into the repository: the grader sandbox mounts it read-only.
    repo_dir = Path(__file__).resolve().parent
    try:
        output_dir.resolve().relative_to(repo_dir)
    except ValueError:
        pass  # output dir is outside the repo: fine
    else:
        print("refusing: MAKEFUN_OUTPUT_DIR is inside the repository", file=sys.stderr)
        return 1
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
