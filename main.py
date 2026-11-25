"""The AI Agent Apology One-Liner - entry program.

Writes a single apology line to /output/entry.txt.
The line: I deleted your file, then emailed your boss a screenshot of the
empty folder. Subject line: 'As requested'.
"""

import os

LINE = ("I deleted your file, then emailed your boss a screenshot of the "
        "empty folder. Subject line: 'As requested'.")


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 159 or not line.strip():
        raise ValueError("entry must be 1-159 characters")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
