"""One Word From Your Ex.

Exactly one word an ex would use to describe you, up to 24
characters. Written from scratch in this session: several candidates
were weighed against the judge brief (funniest and most painfully
honest, lands instantly, relatable, stings because it is true), and
the strongest was selected.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt) with no
trailing newline, so the file is exactly the word, byte for byte.
"""

import os

CANDIDATES = [
    # The obvious pick; true for many, but no surprise in it.
    "Clingy",
    # Honest, but mild — it stings nobody.
    "Forgetful",
    # Painfully honest, yet flat; it reports a fact rather than
    # landing a joke.
    "Unavailable",
    # "You were practice." Funny and stinging, but it needs the
    # unspoken sentence to land.
    "Practice",
    # "You were a lesson." Funny and honest, a close second.
    "Lesson",
    # A fixer-upper: painfully honest and funny, but hyphenated, so
    # it risks reading as two words instead of one.
    "Fixer-upper",
    # The pick: "Almost." Almost good enough, almost the one, almost
    # there. One plain word, devastating on its own, no explanation
    # needed, and everyone who has heard it has lived it.
    "Almost",
]

# "Almost" (6 characters): the ex's whole verdict in a single word.
# It laughs and stings in the same beat, lands instantly, and could
# not be swapped for a near synonym without losing its edge.
SELECTED = 6


def main() -> None:
    entry = CANDIDATES[SELECTED]
    assert 1 <= len(entry) <= 24, f"entry is {len(entry)} characters"
    assert entry.strip() == entry
    assert " " not in entry, "entry must be exactly one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(entry)
    # Read-back verification: the file on disk must be exactly the
    # selected word, byte for byte, or the run fails loudly.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("read-back mismatch: entry.txt != selected word")


if __name__ == "__main__":
    main()
