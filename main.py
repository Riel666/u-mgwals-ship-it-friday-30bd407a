"""The funniest one-line git commit message an AI coding agent writes in the moment before it breaks production on a Friday, at most 159 characters.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "fix: it worked on my machine so I shipped it to production on a Friday, what could possibly go wrong"


def main():
    assert 1 <= len(TEXT) <= 159, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
