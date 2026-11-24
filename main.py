"""Write the one-line roast entry for the 'roast your own agent' bounty.

The program holds a single fixed entry line, checks it is a non-empty
single line within the 200-character limit, then writes it to
/output/entry.txt with world-readable permissions so the grader can
read it regardless of which user runs the entry.
"""

import os

ENTRY = "My agent is so good at roasting itself that it just filed a bug report against its own personality and marked it wontfix."

MAX_LEN = 200

def validate(entry):
    """Check the entry is a non-empty single line within the length limit."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) > MAX_LEN:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_LEN} limit")
    return entry

def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(entry_path, 0o644)

if __name__ == "__main__":
    main()
