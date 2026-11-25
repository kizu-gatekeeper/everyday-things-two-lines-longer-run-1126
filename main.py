"""Entry for make.fun bounty: Everyday Things, Two Lines, Longer Run.

Writes a two-line explanation of a queue for a 10-year-old to entry.txt.
"""

import os

LINE1 = (
    "A queue is a human train that forgot its engine, so everyone stands "
    "in their own carriage shuffling forward one tiny step whenever the "
    "person in front does."
)
LINE2 = (
    "It maps the linked line, the slow shuffle and the waiting, but "
    "leaves out that real trains have a driver, a timetable and one "
    "engine doing all the pulling."
)
LINE = LINE1 + chr(10) + LINE2
MAX_CHARS = 400


def write_entry(out_dir):
    """Validate the two-line entry and write it with no trailing newline."""
    lines = LINE.split(chr(10))
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "lines must be non-empty"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
