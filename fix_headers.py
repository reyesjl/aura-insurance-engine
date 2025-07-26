#!/usr/bin/env python3
"""
Script to fix malformed copyright headers in Vue files.
"""

import os
import re
from pathlib import Path

# Correct copyright header for Vue files (using HTML comments to avoid Prettier issues)
CORRECT_HEADER = """<!-- prettier-ignore -->
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

        # Pattern to match the malformed header (starts with /* * Aura and continues until */ or the actual code starts)
        # The malformed header spans multiple lines but is improperly formatted
        pattern = r"^/\* \* Aura Insurance Engine.*?(?=<template>|<script|export|import|\n\n|\*/\s*\n)"

        # Find the malformed header
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

        if match:
            # Replace the malformed header with the correct one
            new_content = content[match.end() :]

            # Clean up any leftover malformed bits at the start
            new_content = re.sub(
                r"^[^<]*?(?=<template>|<script|export|import)",
                "",
                new_content,
                flags=re.DOTALL,
            )
            new_content = CORRECT_HEADER + new_content.lstrip()

            # Write the corrected content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            return True, "Header fixed successfully"
        else:
            return False, "No malformed header found"

    except Exception as e:
        return False, f"Error: {str(e)}"


def main():
    """Main function to fix malformed headers."""
    project_root = Path(__file__).parent / "aura_frontend" / "src"

    # File patterns to check
    patterns = ["**/*.vue", "**/*.js", "**/*.ts", "**/*.html", "**/*.css"]

    fixed_files = []
    skipped_files = []
    error_files = []

    for pattern in patterns:
        for file_path in project_root.glob(pattern):
            if file_path.is_file():
                # Check if file has malformed header
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        first_line = f.readline()

                    if first_line.startswith("/* * Aura Insurance Engine"):
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
                        # Check if it already has correct header
                        if first_line.startswith("/*"):
                            skipped_files.append(
                                (
                                    str(
                                        file_path.relative_to(
                                            project_root.parent.parent
                                        )
                                    ),
                                    "Already has correct header",
                                )
                            )
                        else:
                            skipped_files.append(
                                (
                                    str(
                                        file_path.relative_to(
                                            project_root.parent.parent
                                        )
                                    ),
                                    "No header found",
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
