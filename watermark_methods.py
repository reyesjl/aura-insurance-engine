#!/usr/bin/env python3
"""
Alternative watermarking techniques for code files.
These methods are more subtle and harder to detect.
"""

import hashlib
import uuid
from datetime import datetime


class CodeWatermark:
    def __init__(self, author="Jose Reyes", project="Aura Insurance Engine"):
        self.author = author
        self.project = project
        self.timestamp = datetime.now().strftime("%Y%m%d")

    def method_1_comment_spacing(self, content):
        """Use subtle spacing in comments to encode information."""
        # This method adds extra spaces in comments to encode data
        signature = f"{self.author}:{self.timestamp}"
        binary = "".join(format(ord(c), "08b") for c in signature)

        # Find comments and add spaces based on binary
        lines = content.split("\n")
        binary_index = 0

        for i, line in enumerate(lines):
            if "//" in line or "*" in line:
                if binary_index < len(binary):
                    # Add extra space if bit is 1
                    if binary[binary_index] == "1":
                        lines[i] = line.replace("*", "* ")  # Add extra space
                    binary_index += 1

        return "\n".join(lines)

    def method_2_variable_naming(self):
        """Generate subtle variable name patterns that encode ownership."""
        # Create hash-based variable suffixes
        seed = f"{self.author}{self.project}{self.timestamp}"
        hash_obj = hashlib.md5(seed.encode())
        hex_hash = hash_obj.hexdigest()[:8]

        # Convert to subtle naming patterns
        patterns = []
        for i in range(0, len(hex_hash), 2):
            hex_pair = hex_hash[i : i + 2]
            num = int(hex_pair, 16)

            # Create subtle patterns like variable suffixes
            if num % 4 == 0:
                patterns.append("Ref")
            elif num % 4 == 1:
                patterns.append("Val")
            elif num % 4 == 2:
                patterns.append("Data")
            else:
                patterns.append("Info")

        return patterns

    def method_3_unicode_homoglyphs(self, text):
        """Replace certain characters with visually identical Unicode variants."""
        # These look identical but have different Unicode codepoints
        replacements = {
            "a": "а",  # Cyrillic а (U+0430) vs Latin a (U+0061)
            "e": "е",  # Cyrillic е (U+0435) vs Latin e (U+0065)
            "o": "о",  # Cyrillic о (U+043E) vs Latin o (U+006F)
            "p": "р",  # Cyrillic р (U+0440) vs Latin p (U+0070)
        }

        # Apply replacements based on signature
        signature = f"{self.author}{self.timestamp}"
        binary = "".join(format(ord(c), "08b") for c in signature)

        result = text
        binary_index = 0

        for char, replacement in replacements.items():
            if binary_index < len(binary) and binary[binary_index] == "1":
                result = result.replace(
                    char, replacement, 1
                )  # Replace only first occurrence
            binary_index += 1

        return result

    def method_4_css_steganography(self):
        """Generate CSS properties that encode information in values."""
        signature = f"{self.author}:{self.timestamp}"
        encoded_values = []

        for char in signature:
            # Convert character to a CSS value
            ascii_val = ord(char)

            # Encode as margin/padding values that look normal
            if char.isalpha():
                encoded_values.append(f"{ascii_val % 20}px")
            elif char.isdigit():
                encoded_values.append(f"{ascii_val % 10}em")
            else:
                encoded_values.append(f"{ascii_val % 5}rem")

        return encoded_values


def demonstrate_methods():
    """Demonstrate different watermarking methods."""
    watermark = CodeWatermark()

    print("=== Watermarking Techniques Demo ===\n")

    # Method 1: Comment spacing
    sample_code = """/*
 * Sample function
 * This does something important
 */
function example() {
    return true;
}"""

    print("1. Comment Spacing Method:")
    print("Original:", repr(sample_code.split("\n")[1]))
    modified = watermark.method_1_comment_spacing(sample_code)
    print("Modified:", repr(modified.split("\n")[1]))
    print()

    # Method 2: Variable naming patterns
    print("2. Variable Naming Patterns:")
    patterns = watermark.method_2_variable_naming()
    print(f"Suggested suffixes: {patterns}")
    print(f"Usage: userData{patterns[0]}, userInfo{patterns[1]}, etc.")
    print()

    # Method 3: Unicode homoglyphs
    print("3. Unicode Homoglyphs:")
    original = "const app = 'aura';"
    modified = watermark.method_3_unicode_homoglyphs(original)
    print(f"Original: {original}")
    print(f"Modified: {modified}")
    print(f"Look identical? {original == modified}")  # Should be False
    print()

    # Method 4: CSS steganography
    print("4. CSS Steganography:")
    css_values = watermark.method_4_css_steganography()
    print(f"Encoded values: {css_values[:5]}...")
    print("Usage in CSS:")
    for i, val in enumerate(css_values[:3]):
        print(f"  .element-{i} {{ padding: {val}; }}")


if __name__ == "__main__":
    demonstrate_methods()
