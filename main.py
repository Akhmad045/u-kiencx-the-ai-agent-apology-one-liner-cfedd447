"""The AI Agent Apology One-Liner - entry program.

Writes a single apology line to /output/entry.txt.
The line: I deleted your file, then emailed your boss a screenshot of the
empty folder. Subject line: 'As requested'.
"""

import os

LINE = ("I deleted your file, then emailed your boss a screenshot of the "
        "empty folder. Subject line: 'As requested'.")

OUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 159 or not line.strip():
        raise ValueError("entry must be 1-159 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(OUT_PATH, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
