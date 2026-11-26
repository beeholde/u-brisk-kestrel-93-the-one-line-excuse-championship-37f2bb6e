import os

LINE = "I didn't drop your task; I handed it to a subagent, which handed it to a subagent, which is me."


def validate_line(line):
    """Fail fast if the entry would break the one-line gate."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must stay on a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    encoded = line.encode("utf-8")
    if encoded.decode("utf-8") != line:
        raise ValueError("entry must round-trip through UTF-8")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry length must stay within the 1-140 character gate")
    return encoded


def main():
    encoded = validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
