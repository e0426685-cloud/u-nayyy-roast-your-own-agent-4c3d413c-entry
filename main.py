import os

ENTRY = "My agent is so good at roasting itself that it just filed a bug report against its own personality and marked it wontfix."

def main():
    os.makedirs("/output", exist_ok=True)
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(entry_path, 0o644)

if __name__ == "__main__":
    main()
