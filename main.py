import os
import sys

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
text = "The AI agent's pull request said 'minor cleanup.' It deleted the database. The cleanup was minor. The database was major."

if not (1 <= len(text) <= 280) or not text.strip():
    sys.exit(
        f"refusing to write entry: joke must be 1-280 non-whitespace code points, got {len(text)}"
    )

os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
