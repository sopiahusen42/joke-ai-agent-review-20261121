"""make.fun entry: one-line joke about working beside AI coding agents.

Competition: "The joke the reviewer laughs at"
(the-joke-the-reviewer-laughs-at-20261121-0329).

Writes the joke to /output/entry.txt (standard library only).
MAKEFUN_OUTPUT_DIR overrides the output directory for local testing.
"""
import os
import sys

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
JOKE = "I gave my AI agent a small task to test it. It finished in 40 seconds and asked me to review the PR. I've been reviewing for three days."


def validate(text):
    if not (1 <= len(text) <= 280):
        sys.exit(
            f"refusing to write entry: joke must be 1-280 code points, got {len(text)}"
        )
    if not text.strip():
        sys.exit("refusing to write entry: joke must not be only whitespace")


def main():
    validate(JOKE)
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
