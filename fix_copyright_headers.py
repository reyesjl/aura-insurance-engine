#!/usr/bin/env python3
"""
Script to fix malformed copyright headers in Vue and other files.
Uses HTML comments for Vue files to avoid Prettier formatting issues.
"""

import os
import re
from pathlib import Path

# Correct copyright header for Vue files (using HTML comments to avoid Prettier issues)
VUE_HEADER = """<!-- prettier-ignore -->
<!--
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
-->

"""

# Correct copyright header for JS/TS files
JS_HEADER = """/*
 * Aura Insurance Engine – Proprietary Software
 *
 * Copyright © 2025 Jose Reyes (GitHub: @reyesjl). All rights reserved.
 *
 * This software was developed solely by Jose Reyes – full-stack engineer and designer.
 * It is a modern insurance submission platform built to streamline the intake
 * and processing of insurance applications.
 *
 * This code is proprietary and confidential. Unauthorized use, reproduction,
 * distribution, or modification is strictly prohibited.
 *
 * Project repository: https://github.com/reyesjl/aura-insurance-engine
 * DeepWiki: https://app.devin.ai/wiki/reyesjl/aura-insurance-engine
 */

"""


def fix_malformed_header(file_path):
    """Fix malformed copyright header in a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Choose the appropriate header based on file extension
        file_ext = file_path.suffix.lower()
        if file_ext in [".vue", ".html"]:
            header = VUE_HEADER
        else:
            header = JS_HEADER

        # Multiple patterns to match different types of malformed or existing headers
        patterns = [
            r"^/\* \* Aura Insurance Engine.*?(?=<template>|<script|export|import|\n\n)",  # Malformed JS-style
            r"^<!-- prettier-ignore -->\s*<!--.*?Aura Insurance Engine.*?-->\s*",  # Existing HTML comment
            r"^/\*\s*\n \* Aura Insurance Engine.*?\*/\s*\n",  # Existing JS comment
        ]

        content_without_header = content
        header_found = False

        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
            if match:
                # Remove the existing header
                content_without_header = content[match.end() :]
                header_found = True
                break

        # Also check for the specific malformed pattern we're seeing
        if not header_found and (
            content.startswith("/* * Aura")
            or content.startswith("<!-- prettier-ignore -->")
        ):
            # Find where the actual content starts
            if file_ext == ".vue":
                content_start = content.find("<template>")
                if content_start == -1:
                    content_start = content.find("<script>")
                if content_start > 0:
                    content_without_header = content[content_start:]
                    header_found = True
            else:
                # For JS/TS files, find import/export statements
                for start_pattern in [
                    "import ",
                    "export ",
                    "const ",
                    "let ",
                    "var ",
                    "function ",
                    "class ",
                ]:
                    pos = content.find(start_pattern)
                    if pos > 0:
                        content_without_header = content[pos:]
                        header_found = True
                        break

        if header_found:
            # Clean up any leftover malformed bits at the start
            content_without_header = content_without_header.lstrip()
            new_content = header + content_without_header

            # Write the corrected content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            return True, "Header fixed successfully"
        else:
            return False, "No header found to fix"

    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Main function to fix malformed headers."""
    project_root = Path(__file__).parent / "aura_frontend" / "src"

    # File patterns to check
    patterns = ["**/*.vue", "**/*.js", "**/*.ts", "**/*.html"]

    fixed_files = []
    skipped_files = []
    error_files = []

    for pattern in patterns:
        for file_path in project_root.glob(pattern):
            if file_path.is_file():
                # Check if file has malformed header or needs fixing
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Check if it needs fixing
                    needs_fixing = (
                        content.startswith("/* * Aura Insurance Engine")
                        or (
                            content.startswith("<!-- prettier-ignore -->")
                            and "Aura Insurance Engine" in content[:500]
                        )
                        or (
                            content.startswith("/*")
                            and "Aura Insurance Engine" in content[:500]
                        )
                    )

                    if needs_fixing:
                        success, message = fix_malformed_header(file_path)

                        if success:
                            fixed_files.append(
                                str(file_path.relative_to(project_root.parent.parent))
                            )
                            print(
                                f"✓ Fixed: {file_path.relative_to(project_root.parent.parent)}"
                            )
                        else:
                            error_files.append(
                                (
                                    str(
                                        file_path.relative_to(
                                            project_root.parent.parent
                                        )
                                    ),
                                    message,
                                )
                            )
                            print(
                                f"✗ Error: {file_path.relative_to(project_root.parent.parent)}: {message}"
                            )
                    else:
                        skipped_files.append(
                            (
                                str(file_path.relative_to(project_root.parent.parent)),
                                "No header to fix",
                            )
                        )

                except Exception as e:
                    error_files.append(
                        (
                            str(file_path.relative_to(project_root.parent.parent)),
                            f"Read error: {str(e)}",
                        )
                    )

    # Print summary
    print(f"\n=== Summary ===")
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Files skipped: {len(skipped_files)}")
    print(f"Files with errors: {len(error_files)}")

    if error_files:
        print(f"\nErrors:")
        for file_path, error in error_files:
            print(f"  {file_path}: {error}")


if __name__ == "__main__":
    main()
