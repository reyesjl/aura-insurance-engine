#!/usr/bin/env python3
"""
Script to verify and decode watermarks from files.
"""

import sys
from pathlib import Path

# Zero-width characters for decoding
ZERO_WIDTH_SPACE = "\u200b"  # U+200B
ZERO_WIDTH_NON_JOINER = "\u200c"  # U+200C
ZERO_WIDTH_JOINER = "\u200d"  # U+200D
WORD_JOINER = "\u2060"  # U+2060


def zero_width_to_text(zero_width_string):
    """Decode zero-width characters back to text."""
    # Map zero-width characters back to binary
    binary = ""
    for char in zero_width_string:
        if char == ZERO_WIDTH_SPACE:
            binary += "00"
        elif char == ZERO_WIDTH_NON_JOINER:
            binary += "01"
        elif char == ZERO_WIDTH_JOINER:
            binary += "10"
        elif char == WORD_JOINER:
            binary += "11"

    # Convert binary back to text
    result = ""
    for i in range(0, len(binary), 8):
        byte = binary[i : i + 8]
        if len(byte) == 8:
            result += chr(int(byte, 2))

    return result


def find_watermarks(file_path):
    """Find and decode watermarks in a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract zero-width characters
        zero_width_chars = ""
        for char in content:
            if char in [
                ZERO_WIDTH_SPACE,
                ZERO_WIDTH_NON_JOINER,
                ZERO_WIDTH_JOINER,
                WORD_JOINER,
            ]:
                zero_width_chars += char

        if zero_width_chars:
            decoded = zero_width_to_text(zero_width_chars)
            return True, decoded, len(zero_width_chars)
        else:
            return False, "No watermark found", 0

    except Exception as e:
        return False, f"Error reading file: {str(e)}", 0


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 verify_watermark.py <filename>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    found, result, char_count = find_watermarks(file_path)

    if found:
        print(f"✓ Watermark found in {file_path}")
        print(f"  Decoded text: {result}")
        print(f"  Character count: {char_count}")
    else:
        print(f"✗ {result}")


if __name__ == "__main__":
    main()
