#!/usr/bin/env python3
"""
Script to add invisible watermarks to code files using zero-width characters.
Creates a unique signature that proves authorship without affecting code functionality.
"""

import os
import base64
from pathlib import Path

# Zero-width characters for encoding
ZERO_WIDTH_SPACE = "\u200b"  # U+200B
ZERO_WIDTH_NON_JOINER = "\u200c"  # U+200C
ZERO_WIDTH_JOINER = "\u200d"  # U+200D
WORD_JOINER = "\u2060"  # U+2060


def text_to_zero_width(text):
    """Convert text to zero-width character encoding."""
    # Convert text to binary
    binary = "".join(format(ord(char), "08b") for char in text)

    # Map binary to zero-width characters
    # 00 = ZERO_WIDTH_SPACE
    # 01 = ZERO_WIDTH_NON_JOINER
    # 10 = ZERO_WIDTH_JOINER
    # 11 = WORD_JOINER
    result = ""
    for i in range(0, len(binary), 2):
        pair = binary[i : i + 2].ljust(2, "0")  # Pad if needed

        if pair == "00":
            result += ZERO_WIDTH_SPACE
        elif pair == "01":
            result += ZERO_WIDTH_NON_JOINER
        elif pair == "10":
            result += ZERO_WIDTH_JOINER
        elif pair == "11":
            result += WORD_JOINER

    return result


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


def add_watermark_to_file(file_path, watermark_text):
    """Add zero-width watermark to a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Encode watermark
        watermark = text_to_zero_width(watermark_text)

        # Different insertion strategies based on file type
        file_ext = file_path.suffix.lower()

        if file_ext == ".vue":
            # Insert after the copyright comment
            if "<!--" in content and "-->" in content:
                comment_end = content.find("-->") + 3
                new_content = content[:comment_end] + watermark + content[comment_end:]
            else:
                # Insert at the beginning
                new_content = watermark + content

        elif file_ext in [".js", ".ts"]:
            # Insert after the copyright comment or at the beginning
            if "/*" in content and "*/" in content:
                comment_end = content.find("*/") + 2
                new_content = content[:comment_end] + watermark + content[comment_end:]
            else:
                new_content = watermark + content

        elif file_ext == ".py":
            # Insert after docstring or imports
            if '"""' in content:
                # Find the end of the first docstring
                first_quotes = content.find('"""')
                if first_quotes != -1:
                    second_quotes = content.find('"""', first_quotes + 3)
                    if second_quotes != -1:
                        insert_pos = second_quotes + 3
                        new_content = (
                            content[:insert_pos]
                            + "\n"
                            + watermark
                            + content[insert_pos:]
                        )
                    else:
                        new_content = watermark + content
                else:
                    new_content = watermark + content
            else:
                new_content = watermark + content
        else:
            # For other files, insert at the beginning
            new_content = watermark + content

        # Write the watermarked content
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        return True, "Watermark added successfully"

    except Exception as e:
        return False, f"Error: {str(e)}"


def create_signature():
    """Create a unique signature for this codebase."""
    import datetime

    # Create a unique signature
    signature_data = {
        "author": "Jose Reyes (@reyesjl)",
        "project": "Aura Insurance Engine",
        "timestamp": datetime.datetime.now().isoformat(),
        "repo": "https://github.com/reyesjl/aura-insurance-engine",
    }

    signature_text = (
        f"AURA:{signature_data['author']}:{signature_data['timestamp'][:10]}"
    )
    return signature_text


def main():
    """Main function to add watermarks to selected files."""
    project_root = Path(__file__).parent

    # Create signature
    signature = create_signature()
    print(f"Using signature: {signature}")
    print(f"Encoded as: {repr(text_to_zero_width(signature))}")

    # Files to watermark (choose stable files that won't change much)
    watermark_files = [
        "aura_frontend/src/types/User.ts",
        "aura_frontend/src/types/ApplicationSession.ts",
        "aura_frontend/src/types/Question.ts",
        "aura_frontend/src/components/FootBar.vue",
        "aura_backend/core/models.py",
        "README.md",
    ]

    watermarked = []
    errors = []

    for file_path in watermark_files:
        full_path = project_root / file_path
        if full_path.exists():
            success, message = add_watermark_to_file(full_path, signature)
            if success:
                watermarked.append(file_path)
                print(f"✓ Watermarked: {file_path}")
            else:
                errors.append((file_path, message))
                print(f"✗ Error: {file_path}: {message}")
        else:
            print(f"! File not found: {file_path}")

    print(f"\n=== Summary ===")
    print(f"Files watermarked: {len(watermarked)}")
    print(f"Errors: {len(errors)}")

    # Show how to decode
    print(f"\n=== Verification ===")
    print("To verify watermark, use:")
    print("python3 verify_watermark.py <filename>")


if __name__ == "__main__":
    main()
