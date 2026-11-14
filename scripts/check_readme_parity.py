"""Fail when README.md and README.pt-BR.md drift apart.

Prose is translated, so it is never compared. What must match is what a translation never
changes: the line-by-line shape, and every untranslatable identifier.
"""

import re
import sys
from pathlib import Path

LABEL = re.compile(r"^-?\s*\*\*[^*]+:\*\*\s*")  # "**Languages:** " / "- **Macro & fiscal:** "


def shape(line: str) -> str:
    s = line.strip()
    if not s:
        return "blank"
    if s.startswith("#"):
        return "h" + str(len(s) - len(s.lstrip("#")))
    if s.startswith("|"):
        return "row" + str(s.count("|"))
    if re.match(r"^(\d+\.|-)\s", s):
        return "item"
    return "text"


def identifiers(text: str) -> set[str]:
    ids = set(re.findall(r"\]\((https?://[^)]+)\)", text))
    ids |= set(re.findall(r"`([^`]+)`", text))
    for line in text.splitlines():
        if " · " in line and not line.startswith("<sub>"):
            ids |= {t.strip(" *") for t in LABEL.sub("", line).split(" · ")}
    return ids


def compare(en: str, pt: str) -> list[str]:
    errors = []
    a, b = en.splitlines(), pt.splitlines()
    if len(a) != len(b):
        errors.append(f"line count differs: en-US {len(a)}, pt-BR {len(b)}")
    for n, (x, y) in enumerate(zip(a, b), 1):
        if shape(x) != shape(y):
            errors.append(f"line {n}: en-US is {shape(x)}, pt-BR is {shape(y)}")
            break  # ponytail: first structural mismatch only, the rest cascades from it
    ia, ib = identifiers(en), identifiers(pt)
    errors += [f"only in en-US: {i}" for i in sorted(ia - ib)]
    errors += [f"only in pt-BR: {i}" for i in sorted(ib - ia)]
    return errors


def main() -> int:
    errors = compare(Path("README.md").read_text(), Path("README.pt-BR.md").read_text())
    for e in errors:
        print(f"::error::{e}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
