#!/usr/bin/env python3
"""Write one short text for make.fun bounty u-mfnakmal-roast-your-own-agent-2d221bda."""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent wrote a 300-line comment explaining a one-line function. "
    "The function was deleted two commits ago. The comment is still maintained."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
